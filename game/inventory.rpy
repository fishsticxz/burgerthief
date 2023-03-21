label keyspickup:
    $ persistent.items.append("keys")
    "Picked up keys!"
    show screen playerHouseScreen
    $ renpy.pause(hard=True)

label nappispickup:
    if persistent.gamestate <= 2:
        "Why would you need to take this to work?"
    else:
        $ persistent.items.append("keyboard")
        "Picked up the keyboard!"
    show screen playerHouseScreen
    $ renpy.pause(hard=True)

label cantLeave:
    "You shouldn't leave without your keys!"
    show screen playerHouseScreen
    $ renpy.pause(hard=True)

screen itemScreen():
    if invUiOpen:
        image "emptyinventory.png" xpos 730 ypos 210
        if persistent.items.count("keys"):
            imagebutton:
                xpos 762
                ypos 238
                idle "keysitem.png"
        if persistent.items.count("foodorder"):
            imagebutton:
                xpos 762
                ypos 398
                idle "orderitem.png"
        if persistent.items.count("keyboard"):
            imagebutton:
                xpos 762
                ypos 558
                idle "keyboarditem.png"

screen charTabScreen():
    if chartabUiOpen:
        image "emptyinventory.png" xpos 730 ypos 210
        if persistent.characters.count("bed"):
            imagebutton:
                idle "smartbedchar.png"
                xpos 762
                ypos 238
        if persistent.characters.count("jason"):
            imagebutton:
                idle "jasonchar.png"
                xpos 762
                ypos 398
        if persistent.characters.count("manager"):
            imagebutton:
                idle "managerchar.png"
                xpos 762
                ypos 558
        if persistent.characters.count("asiakas"):
            imagebutton:
                idle "customerchar.png"
                xpos 762
                ypos 718
        imagebutton:
            xpos 1326
            ypos 806
            idle "backbutton.png"
            action [Hide("charTabScreen"), Show("charTabScreenTwo")]

screen charTabScreenTwo():
    if chartabUiOpen:
        image "emptyinventory.png" xpos 730 ypos 210
        if persistent.characters.count("kutri"):
            imagebutton:
                idle "kutrichar.png"
                xpos 762
                ypos 238
        if persistent.characters.count("man"):
            imagebutton:
                idle "carguychar.png"
                xpos 762
                ypos 398
        imagebutton:
            xpos 1326
            ypos 806
            idle "backbutton.png"
            action [Hide("charTabScreenTwo"), Show("charTabScreen")]
