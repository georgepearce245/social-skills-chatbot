$(document).ready(function() {
    scrollToBottom();

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
    }


    // Post the Chatbot's reply in the chatbox
    function postChatbotMessage(message) {
        if (message.length < 1) {
            // TODO no response - error

        } else {
            for (i = 0; i < message.length; i++){
                if (message[i].hasOwnProperty("text")) {
                    var chatbotMessage = '<li class="card chatbot-message">Chatbot: ' + message[i].text + '</li>';
                    $(chatbotMessage).appendTo('#messagebox').fadeIn(5000);
                }
            }
            scrollToBottom();
        }
    }


    // Scroll to the bottom of the page
    function scrollToBottom() {
        $(document).scrollTop($(document).height());
    }
});
