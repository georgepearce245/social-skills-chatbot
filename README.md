## My undergraduate final year project: "An AI Chatbot To Help Autistic Children Develop Their Social Skills"

### Feel free to look through my final report for a more detailed walkthrough of the project, or continue reading here for a very brief summary.

The project consists of two main components, a chatbot built using Rasa Open Source, and a Django web application through which the user would interact with the chatbot. 

The web app is a simple, messenger-style application which will send user messages to the chatbot and display the chatbot's response.

The chatbot would be intended for use with a very young autistic user, with extremely limited competency of neurotypical social skills. It is therefore capable of having very basic 'small talk' and determining the user's level of ability for several very fundamental 'social skills'. The chatbot keeps track of these scores as the conversation progresses, and tailors the conversation somewhat to try to help the child improve them. This tailoring could take the form of prompts, examples, or suggested 'games' or educational material.

A basic example conversation:
![](https://github.com/georgepearce245/social-skills-chatbot/conversation.png)
