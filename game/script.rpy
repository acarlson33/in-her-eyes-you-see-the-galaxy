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
    scene bg forest four at truecenter, scale(0.48)

    show a at left, scale(0.5)

    a "Hello, Planet Earth! I am here to take you all over!"

    a "Where are all my loyal subjects ?"

    show a pose2 shout at left, scale(0.5)

    a "Hey! You!"

    show m pose1 talk at left, scale(0.5)
    show a pose1 frown at left, scale(0.5)

    m "Oh, hello!"

    m "It seems our spaceships have had a … crashing into each other. It seems."

    show a pose2 talk at left, scale(0.5)

    a "So ths is your fault, huh?!"

    show a pose1 talk at left, scale(0.5)

    a "You should be very sorry for doing that to my dearest ship. Hmph."

    show m pose1 talk at left, scale(0.5)

    pause 1

    show m pose1 smile at left, scale(0.5)

    m "My dearest apologies."

    show a pose1 blush at left, scale(0.5)

    a "You should be."

    show a pose2 shout at left, scale(0.5)

    a "Our plans better not intersect, or you will rue the day you have messed with me!"

    show a pose1 frown at left, scale(0.5)

    show m pose2 confused at left, scale(0.5)

    m "Plans?"

    show a pose1 talk at left, scale(0.5)

    a "Yeah. Plans."

    show a pose2 shout at left, scale(0.5)

    a "AKA, what you are currently ruining right now!"

    show m pose2 confused at left, scale(0.5)

    m "Ruining?"

    m pose1 talk at left, scale(0.5)

    m "Oh!"

    n "She looks down to see a small flower she is crushing."

    show m pose1 sad at left, scale(0.5)

    m "Oh dear..."

    show a pose1 blush at left, scale(0.5)

    a "Not that, you idiot!"