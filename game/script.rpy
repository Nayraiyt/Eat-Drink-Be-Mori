#Main Charecters
define aze = Character("Aze", color="#6f1069")
define cece = Character("Cece", color="#393323")
define puzzle = Character("Puzzle", color="#37333a")
define meep = Character("Meep", color="#1a6391")

#BG Charecters

#positions (Left to Right, like setting positions :D)
define pos_default_y = 1100

define pos_1 = Position(xpos=200,  ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_2 = Position(xpos=360,  ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_3 = Position(xpos=560,  ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_4 = Position(xpos=760,  ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_5 = Position(xpos=960,  ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_6 = Position(xpos=1160, ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_7 = Position(xpos=1360, ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_8 = Position(xpos=1560, ypos=pos_default_y, xanchor='center', yanchor='bottom')
define pos_9 = Position(xpos=1700, ypos=pos_default_y, xanchor='center', yanchor='bottom')

define positions = [pos_1,pos_2,pos_3,pos_4,pos_5,pos_6,pos_7,pos_8,pos_9]

define counter_interlude = [0,0,0,0,0,0]
define counter_ending = [0,0,0,0,0,0]

label intro:
    jump title_ch1
label title_ch1:
    jump ch1
label ch1:
    jump interlude
label interlude:
    jump title_ch2
label title_ch2:
    jump ch2
label end:
    jump start

label start:
    scene bg test
    python:
        for index,pos in enumerate (positions):
            renpy.show("aze default", at_list=[pos])
            renpy.say("aze","Position: " + str(index+1))
    return

