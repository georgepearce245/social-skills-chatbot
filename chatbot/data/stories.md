
## interaction EP1_1
* interaction
  - action_interaction
  - slot{"EP1_1": 5}
  
## no interaction EP1_1
* no_interaction
  - action_no_interaction
  - slot{"EP1_1": 0}

## slow interaction EP1_1
* slow_interaction
  - action_slow_interaction
  - slot{"EP1_1": 3}
  
## intitiation EP1_2
* initiation
  - action_initiation
  - slot{"EP1_2": 5}
  
## no intitiation EP1_2
* no_initiation
  - action_no_initiation
  - slot{"EP1_2": 0}
  - action_utter_greet

## ask what is my name
* ask_whatismyname
  - action_answer_whatismyname
  
## ask what is possible
* ask_whatispossible
  - action_answer_whatispossible
  
## ask what is your name
* ask_whatisyourname
  - action_answer_whatisyourname
  
## ask who am I
* ask_whoami
  - action_answer_whoami
  
## bot challenge
* bot_challenge
  - action_answer_bot_challenge
  
## explain
* explain
  - action_answer_explain

## thank
* thank
  - utter_youre_welcome

## say goodbye
* goodbye
  - action_goodbye
  
## good to meet you
* goodtomeetyou
  - action_utter_goodtomeetyou
  
## good to see you
* goodtoseeyou
  - utter_goodtoseeyou
  
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  
## greet + name
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou

## greet + name + ask_name
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
* ask_whatisyourname
  - action_answer_whatisyourname
  
## greet + name + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
* ask_howdoing
  - action_answer_howdoing
  
## greet + name + ask_howdoing
* greet
  - action_utter_greet
* ask_howdoing
  - action_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  
## greet + name + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
* ask_howdoing
  - action_answer_howdoing
  
## greet + name + howdoing + happy
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  
## greet + name + howdoing + happy
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
* ask_whatisyourname
  - action_answer_whatisyourname
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## greet + name + howdoing + sad 1
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* affirm
  - action_user_affirm
  
## greet + name + howdoing + sad 2
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* deny
  - action_user_deny
  
## greet + name + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet  
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
* ask_howdoing
  - action_answer_howdoing

  
## greet + name + howdoing + sad 1 + ask_howdoing
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* affirm
  - action_user_affirm
* ask_howdoing
  - action_answer_howdoing
  
## greet + name + howdoing + sad 2 + ask_howdoing
* greet
  - action_utter_greet
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* deny
  - action_user_deny
* ask_howdoing
  - action_answer_howdoing
  
## greet + howdoing + happy
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## greet + howdoing + happy + ask_howdoing
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
* ask_howdoing
  - action_answer_howdoing
  
## greet + howdoing + happy
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## ask where from  
* ask_wherefrom
  - action_answer_wherefrom
* ask_whereisthat
  - action_answer_whereisthat
  
## ask where from + react_positive + wherefrom
* ask_wherefrom
  - action_answer_wherefrom
* ask_whereisthat
  - action_answer_whereisthat
* react_positive
  - action_user_react_positive
  - utter_ask_wherefrom
  
## greet + ask_howdoing + happy
* greet+ask_howdoing
  - action_utter_greet
  - action_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
    - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## greet + ask_howdoing + sad
* greet+ask_howdoing
  - action_utter_greet
  - action_answer_howdoing
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* deny
  - action_user_deny
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## greet + ask_howdoing + happy
* greet+ask_howdoing
  - action_utter_greet
  - action_answer_howdoing
  - utter_ask_howdoing
* mood_great
  - action_user_mood_great
    - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## greet + ask_howdoing + sad
* greet+ask_howdoing
  - action_utter_greet
  - action_answer_howdoing
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* deny
  - action_user_deny
  - action_ask_whatisyourname
* inform{"name": "adam"}
  - slot{"name": "adam"}
  - action_user_inform
  - action_utter_goodtomeetyou
  - utter_ask_wherefrom
* inform{"location": "Kenilworth"}
  - slot{"location": "Kenilworth"}
  - action_user_inform
  - action_user_mood_great
  
## sad path 1
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* affirm
  - action_user_affirm  
  
## sad path 1 + ask_howdoing
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* affirm
  - action_user_affirm
* ask_howdoing
  - action_answer_howdoing

## sad path 1 + ask_name
* greet
  - action_utter_greet
  - utter_ask_howdoing
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* affirm
  - action_user_affirm
* ask_whatisyourname
  - action_answer_whatisyourname

## sad path 2
* greet
  - action_utter_greet
* mood_unhappy
  - action_user_mood_unhappy
  - utter_did_that_help
* deny
  - action_user_deny

## interactive_story_1
* greet
    - action_utter_greet
    - utter_ask_howdoing
* ask_howdoing
    - action_answer_howdoing
* ask_whatisyourname
    - action_answer_whatisyourname
    - action_ask_whatisyourname
* inform{"PERSON": "George", "name": "George"}
    - slot{"name": "George"}
    - action_user_inform
    - action_utter_goodtomeetyou
    - utter_ask_wherefrom
* inform{"GPE": "Redditch", "ORG": "Worcestershire", "location": "Redditch, Worcestershire"}
    - slot{"location": "Redditch, Worcestershire"}
    - action_user_inform
    - action_user_mood_great
* ask_wherefrom
    - action_answer_wherefrom
* ask_whereisthat
    - action_answer_whereisthat
* affirm
    - action_user_affirm
* goodtoseeyou{"DATE": "today", "PERSON": "John"}
    - utter_goodtoseeyou
* goodbye
    - action_goodbye
* goodbye

## interactive_story_1
* greet
    - action_utter_greet
    - slot{"EP2_1": 4.0}
    - action_ask_whatisyourname
* inform{"name": "George"}
    - slot{"name": "George"}
    - action_user_inform
    - slot{"EP3_3": 3.0}
    - action_utter_goodtomeetyou
    - utter_ask_howdoing
* ask_howdoing
    - action_answer_howdoing
    - slot{"EP3_1": 2.5}
    - slot{"EP3_3": 3.5}
* goodbye
    - action_goodbye
    - slot{"EP3_1": 2.5}
    - slot{"EP3_3": 3.5}
    - slot{"EP2_2": 5.0}
