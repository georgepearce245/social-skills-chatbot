
## ask what is my name
* ask_whatismyname
  - action_utter_user_name
  
## ask what is possible
* ask_whatispossible
  - utter_answer_whatispossible
  
## ask what is your name
* ask_whatisyourname
  - utter_answer_whatisyourname
  
## ask who am I
* ask_whoami
  - utter_answer_whoami
  
## bot challenge
* bot_challenge
  - utter_chatbot

## thank
* thank
  - utter_youre_welcome

## say goodbye
* goodbye
  - utter_goodbye
  
## good to meet you
* goodtomeetyou
  - action_utter_goodtomeetyou
  
## good to see you
* goodtoseeyou
  - utter_goodtoseeyou
  
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  
## greet + name
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou

## greet + name + ask_name
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
* ask_whatisyourname
  - utter_answer_whatisyourname
  
## greet + name + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
* ask_howdoing
  - utter_answer_howdoing
  
## greet + name + ask_howdoing
* greet
  - action_utter_greet
* ask_howdoing
  - utter_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - utter_happy
  
## greet + name + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - utter_happy
* ask_howdoing
  - utter_answer_howdoing
  
## greet + name + howdoing + happy
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - utter_happy
  
## greet + name + howdoing + happy
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
* ask_whatisyourname
  - utter_answer_whatisyourname
  - utter_ask_howdoing
* mood_great
  - utter_happy
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## greet + name + howdoing + sad 1
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
  
## greet + name + howdoing + sad 2
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry_no_help
  
## greet + name + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - utter_happy
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
* ask_howdoing
  - utter_answer_howdoing

  
## greet + name + howdoing + sad 1 + ask_howdoing
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* ask_howdoing
  - utter_answer_howdoing
  
## greet + name + howdoing + sad 2 + ask_howdoing
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry_no_help
* ask_howdoing
  - utter_answer_howdoing
  
## greet + howdoing + happy
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - utter_happy
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## greet + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - utter_happy
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
* ask_howdoing
  - utter_answer_howdoing
  
## greet + howdoing + happy
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - utter_happy
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## ask where from  
* ask_wherefrom
  - utter_answer_wherefrom
* ask_whereisthat
  - utter_answer_whereisthat
  
## ask where from + react_positive + wherefrom
* ask_wherefrom
  - utter_answer_wherefrom
* ask_whereisthat
  - utter_answer_whereisthat
* react_positive
  - utter_ask_wherefrom
  
## greet + ask_howdoing + happy
* greet+ask_howdoing
  - action_utter_greet
  - utter_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - utter_happy
    - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## greet + ask_howdoing + sad
* greet+ask_howdoing
  - action_utter_greet
  - utter_answer_howdoing
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry_no_help
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## greet + ask_howdoing + happy
* greet+ask_howdoing
  - action_utter_greet
  - utter_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - utter_happy
    - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## greet + ask_howdoing + sad
* greet+ask_howdoing
  - action_utter_greet
  - utter_answer_howdoing
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry_no_help
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - utter_happy
  
## sad path 1
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy  
  
## sad path 1 + ask_howdoing
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* ask_howdoing
  - utter_answer_howdoing

## sad path 1 + ask_name
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy
* ask_whatisyourname
  - utter_answer_whatisyourname

## sad path 2
* greet
  - action_utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_sorry_no_help