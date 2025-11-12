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

label start:

    scene bg TestBack
    show aze default at pos_1
    aze "1"
    show aze default at pos_2
    aze "2"
    show aze default at pos_3
    aze "3"
    show aze default at pos_4
    aze "4"
    show aze default at pos_5
    aze "5"
    show aze default at pos_6
    aze "6"
    show aze default at pos_7
    aze "7"
    show aze default at pos_8
    aze "8"
    show aze default at pos_9
    aze "9"
    jump test

label test
    scene bg TestBack
    for pos in positions:
        show aze default at pos
        pause
    return