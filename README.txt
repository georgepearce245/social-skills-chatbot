The project is split into two parts within the project directory.
The chatbot/ directory contains the Rasa chatbot. The djangoproject/ directory contains the Django web application

The chatbot training data can be found in the chatbot/data/ directory
The chatbot testing results can be found in the chatbot/results/ directory

The web application html can be found in the djangoproject/webapp/templates/webapp/ directory
The web application css can be found in the djangoproject/webapp/static/css/ directory
The web application javascript can be found in the djangoproject/webapp/static/js/ directory


The project requires:
Python: 3.8.5
Django: 3.1
Rasa: 1.8.0

Python can be downloaded here: https://www.python.org/downloads/release/python-385/
Django can be downloaded here: https://www.djangoproject.com/download/
Installation instructions for Rasa can be found here: https://rasa.com/docs/rasa/1.8.0/user-guide/installation/


To run the chatbot, three terminal windows must be open simultaneously.

In the first terminal, navigate to the chatbot/ directory and run the following command:
rasa run -m models --enable-api --cors "*" --debug

The --debug flag will allow you to see what's going on behind-the-scenes, but could be omitted if you like

This command runs the Rasa server and takes several seconds.
When in DEBUG mode, the line following line will indicate that the server is ready to go:
DEBUG    rasa.core.nlg.generator  - Instantiated NLG to 'TemplatedNaturalLanguageGenerator'.

When the Rasa server is running, open a second terminal, navigate to the chatbot/ directory and enter:
rasa run actions

This command will start the actions server and should take a second or two.

Finally, open a third terminal, navigate to the djangoproject/ directory and run:
python3 manage.py runserver

The chatbot will then be up and running at http://127.0.0.1:8000/webapp/
