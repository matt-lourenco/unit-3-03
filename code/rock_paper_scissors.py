# Created by: Matthew Lourenco
# Created on: 4 Oct 2016
# This is a program that lets you play rock paper scissors with the computer

import ui
import random

box = ['rock_button', 'paper_button', 'scissors_button']
box2 = ['rock.', 'paper.', 'scissors.']

def rock_paper_scissors_touch_up_inside(sender):
    #choose random number
    rand_chosen = random.randint(0, 2)
    print(rand_chosen)
    
    if sender.name == 'rock_button' and box[rand_chosen] == 'scissors_button':
        view['reply_label'].text = 'You won! The computer chose ' + box2[rand_chosen]
    
    elif sender.name == 'paper_button' and box[rand_chosen] == 'rock_button':
        view['reply_label'].text = 'You won! The computer chose ' + box2[rand_chosen]
    
    elif sender.name == 'scissors_button' and box[rand_chosen] == 'paper_button':
        view['reply_label'].text = 'You won! The computer chose ' + box2[rand_chosen]
    
    elif sender.name  == box[rand_chosen]:
        view['reply_label'].text = 'Tie! You chose the same one as the computer. The computer chose ' + box2[rand_chosen]
    
    else:
        view['reply_label'].text = 'You lost. The computer chose ' + box2[rand_chosen]

view = ui.load_view()
view.present('full_screen')
