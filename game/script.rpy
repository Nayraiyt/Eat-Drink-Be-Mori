#Main Charecters
define aze = Character("Aze", color="#6f1069")
define cece = Character("Cece", color="#393323")
define puzzle = Character("Puzzle", color="#37333a")
define meep = Character("Meep", color="#1a6391")

#BG Charecters
define narrator = Character(None)

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

label start:
    jump title_ch1
label title_ch1:
    jump ch1_pg1
label ch1_pg1:
    #Starting Scene
    scene bg bedroom night
    show aze default at pos_2

    aze "Good news. And bad news. And somewhat neutral news. It's always a mix of the three. "
    aze "Never is something wholly good, but neither is it something wholly bad. I suppose that is what has happened in my family."
    aze "I was able to track down my old neighbour, Charms, and they knew of what happened to my family. My parent..."
    menu:
        "What happened?":
            jump ch1_pg1_1
        "How about you write it down? We'll start a log.":
            jump ch1_pg1_2

    label ch1_pg1_1:
        # --> What happened?
        scene bg bedroom night
        show aze default at pos_2

        aze "My parent had starved themself in grief. Charrus could hear them pacing to and fro."
        aze "All the way until he died that is."
        aze "However, it gives me heart that my sibling is well off They have found a partner, Charrus even attended their wedding, and if they are happy then I am happy finally. finally, I have my proof!"
        aze "Charrus said that he was high on foliate, but they have enough cybertions to have recording functionality."
        aze "As soon as I got my hands on that, it was clear as day that Meep and Purple plotted to have one of my accounts laden with illicit information."
        aze "tomorrow. tomorrow we plan."
        aze "And for now we rest."

        #The next Morning 
        scene bg bedroom day with fade
        narrator "The Next morning"
        show aze default at pos_2
        aze "I think we should start a log. then we wouldn't need those nightly check-ins."
        jump ch1_pg2

    label ch1_pg1_2:
        #--> How about you write it down? we'll start a log. (Affinity+)
        scene bg bedroom day
        show aze default at pos_2
    
        aze "that's a great idea."
        aze "Add what you did too and then both of us can retire to bed. No need for nightly check-ins"

        #The next Morning 
        scene bg bedroom day with fade
        narrator "The Next morning"
        jump ch1_pg2

label ch1_pg2:
    #The Next Morning
    scene bg bedroom day
    show aze default at pos_2

    aze "As for now, focus your research on whomever you'd like. I want to know how to hurt them the worst. That, or help me with the money."
    
    $ options = []
    menu ch1_pg2_hub:
        set options
        "Help with gathering money":
            call ch1_pg2_1
        "Investigate why Aze was Imprisoned":
            call ch1_pg2_2
        "Investigate Meep":
            call ch1_pg2_3
        "Investigate Purple":
            call ch1_pg2_4
        "Investigate Cecilia":
            call ch1_pg2_5
    
    jump ch1_night

    label ch1_pg2_1:
        #--> Help with gathering money
        scene bg bedroom day
        show aze default at pos_2

        aze "I'm...."
        aze "I'm glad. that you're helping, that is"
        aze "I'm selling code-based products."
        aze "And leaking a good amount of stuff developed in the private sector two decades ago-so vastly outdated."
        aze "But with the two of us I'm sure we'll be able to make twice the money in half the time."
        menu:
            "I still have my life's savings.":
                aze "Your accounts- they have a not tiny fortune."
                aze "And I may use it..."
            " I can help with whatever you need... but not coding or cybertionies or anything like that.":
                aze "at least your honest about your abilities."
                aze "I'll find work suited for you."
        jump ch1_pg2_hub
        
    label ch1_pg2_2:
        #-->Investigate why Aze was Imprisoned
        pause
        jump ch1_pg2_hub
    label ch1_pg2_3:
        #-->Investigate Meep
        pause
        jump ch1_pg2_hub
    label ch1_pg2_4:
        #-->Investigate Purple
        pause
        jump ch1_pg2_hub
    label ch1_pg2_5:
        #-->Investigate Cecilia
        pause
        jump ch1_pg2_hub

label ch1_night:
    scene bg bedroom night
    narrator "The Next Night"
    menu:
        "Read the log":
            jump ch1_night_1
        "Leave a note for Aze":
            jump ch1_night_2
    
    label ch1_night_1:
        #-->Read the log
        return
    label ch1_night_2:
        #-->Leave a note for Aze
        return


label interlude:
    jump title_ch2
label title_ch2:
    jump ch2
label end:
    jump test

label test:
    scene bg test
    python:
        for index,pos in enumerate (positions):
            renpy.show("aze default", at_list=[pos])
            renpy.say("aze","Position: " + str(index+1))
    return

