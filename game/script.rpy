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

label act_one:
    scene bg forest four at truecenter, scale(0.45)

    show a at left, scale(0.5)

    a "Hello, Planet Earth! I am here to take you all over!"

    a "Where are all my loyal subjects ?"

    show m1talk at left, scale(0.5)

    m "Oh hello! It seems our spaceships have had a … crashing into each other. It seems."

    a "You should be very sorry for doing that to my dearest ship. Hmph."

    show m pose1 talk at left, scale(0.5)

    pause 1

    show m pose1 smile at left, scale(0.5)

    m "My dearest apologies."

# label flowers:
#     scene bg forest two at truecenter

#     # TMP, need a shocked sprite for M
#     show m pose1 talk at left, scale(0.5)
#     pause 0.5
#     m "Woah{space=0.1}!! what are these{space=0.1}??"