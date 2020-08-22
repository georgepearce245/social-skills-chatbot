$(document).ready(function() {
    scrollToBottom();

    var initiated = false
    var no_initiation = setTimeout(function() {
        sendToRasa('/no_initiation');
        initiated = true;}, 15000);
    $('.input').keypress(function() {
        if (!initiated) {
            clearTimeout(no_initiation);
            sendToRasa(('/initiation'));
            initiated = true;
        }
    })

    // On user input 'send' clicked
    $('.send').click(function() {
       var message = $('.input').val();

       if (message == "" || message.trim() == "") {
           return false;
       } else {
           $('.input').val('');
           var userMessage = '<li class="card user-message">You: ' + message + '</li>';
           $(userMessage).appendTo('#messagebox');
           scrollToBottom();
           sendToRasa(message.trim());
       }

    });


    // Activate click function when the user presses enter
    $('.input').keypress(function(e) {
       var key = e.which;
       if (key == 13) {
           $('.send').click();
           return false;
       }
    });


    // Send input to Rasa, receive chatbot response and post that in the chat
    function sendToRasa(message) {
        setTimeout(function() {
            console.log("User Message: ", message);
            $.ajax({
                url: 'http://localhost:5005/webhooks/rest/webhook',
                type: 'POST',
                data: JSON.stringify({
                    "message": message,
                    "sender": "user"
                }),
                success: function(message, status) {
                    postChatbotMessage(message);
                    console.log('Rasa Response: ' + message + '\n Status: ' + status);
                },
                error: function(errorMessage) {
                    postChatbotMessage("");
                    console.log('Error: ' + errorMessage);
                }
            });
        }, 500);
    }


    // Post the Chatbot's reply in the chatbox
    function postChatbotMessage(message) {
        if (message.length < 1) {
            // TODO no response - error

        } else {
            for (i = 0; i < message.length; i++){
                if (message[i].hasOwnProperty("text")) {
                    var chatbotMessage = '<li class="card chatbot-message">' + message[i].text + '</li>';
                    $(chatbotMessage).appendTo('#messagebox').hide().fadeIn(100);
                }
            }
            scrollToBottom();
            var slow_interaction = setTimeout(function() {sendToRasa('/slow_interaction')}, 12000);
            var no_interaction = setTimeout(function() {sendToRasa('/no_interaction')}, 30000);
            var interacted = false;
            $('.input').keypress(function() {
                if (!interacted) {
                    clearTimeout(slow_interaction);
                    clearTimeout(no_interaction);
                    sendToRasa(('/interaction'));
                    interacted = true;
                }
            })
        }
    }


    // Scroll to the bottom of the page
    function scrollToBottom() {
        $(document).scrollTop($(document).height());
    }
});
