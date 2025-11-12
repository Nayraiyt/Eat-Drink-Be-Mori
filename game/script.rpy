

#Main Charectors Go Here
define char_aze = Character("Aze", color="#6f1069")
define char_cece = Character("Cece", color="#393323")
define char_puzzle = Character("Puzzle", color="#37333a")
define char_meep = Character("Meep", color="#1a6391")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aze happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
