# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Adelaine")

define m = Character("Miruna")

define n = Character("Very Snarky Narrator")

transform scale(ratio):
    zoom ratio

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene black
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    n "What was that? 2 spaceships crashing into eachother??"

    scene bg explosion final at truecenter, scale(4)

    n "What a coincidence!!!"

label evilalienyuri:
    
