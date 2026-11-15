#######################
#        Main         #
#######################

define a = Character("Adelaine")
define m = Character("Miruna")
define n = Character("Very Snarky Narrator")

image a = Placeholder("girl", True, False, "Adelaine Placeholder")


transform scale(ratio):
    zoom ratio

label start:

    scene black

    n "What was that{space=0.1}? 2 spaceships crashing into eachother{space=0.1}??"

    scene bg explosion at truecenter, scale(4)

    n "What a coincidence{space=0.1}!!!"

    jump act_one