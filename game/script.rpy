#######################
#        Main         #
#######################

define a = Character("Adelaine")

define m = Character("Miruna")

define n = Character("Very Snarky Narrator")

image a = Placeholder("girl", True, False, "Adelaine Placeholder")

transform scale(ratio):
    zoom ratio

# The game starts here.

label start:

    scene black

    n "What was that{space=0.1}? 2 spaceships crashing into eachother{space=0.1}??"

    scene bg explosion final at truecenter, scale(4)

    n "What a coincidence{space=0.1}!!!"


label a_one:
    # This is going to be a's first scene + story. 
    
    show a at left, scale(0.5)

    a "What the heck{space=0.1}?? Where am I{space=0.1}??"


label flowers:
    scene bg forest two at truecenter

    # TMP, need a shocked sprite for M
    show m talk at left, scale(0.5)
    pause 0.5
    m "Woah{space=0.1}!! what are these{space=0.1}??"

