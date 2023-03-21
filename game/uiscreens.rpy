screen uiScreen():
    image "uifinal.png" xalign 0.5 yalign 0.5
    vbox xpos 524 ypos 590 spacing 16:
        imagebutton:
            idle "maptxt.png"
            hover "maptxthover.png"
            if persistent.items.count("keys"):
                action [ToggleScreen("mapScreen"), ToggleVariable("mapUiOpen")]
            else:
                action Jump("cantLeave")
        imagebutton:
            idle "itemstxt.png"
            hover "itemstxthover.png"
            action [ToggleScreen("itemScreen"), ToggleVariable("invUiOpen")]
        imagebutton:
            idle "charstxt.png"
            hover "charstxthover.png"
            action [ToggleScreen("charTabScreen"), ToggleVariable("chartabUiOpen")]
        imagebutton:
            idle "optionstxt.png"
            hover "optionstxthover.png"
            action [ToggleScreen("preferences"), ToggleVariable("optionsScreenUiOpen")]
    if persistent.gamestate <= 1:
        image "morning.png" xpos 542 ypos 742
    if persistent.gamestate == 2 or persistent.gamestate == 3:
        image "midday.png" xpos 542 ypos 742
    if persistent.gamestate >= 4:
        image "evening.png" xpos 542 ypos 742

screen optionsScreen():
    image "options.png" xpos 730 ypos 210


screen mapScreen():
    image "map.png" xpos 730 ypos 210
    if persistent.gamestate >= 0:
        imagebutton:
            idle "kotinappi.png"
            hover "kotinappihover.png"
            xpos 1290
            ypos 358
            action [Hide("mapScreen"), Jump("playerHouse")]
    if persistent.gamestate >= 0:
        imagebutton:
            idle "borgornappi.png"
            hover "borgornappihover.png"
            xpos 962
            ypos 386
            action [Hide("mapScreen"), Jump("workOutside")]
    if persistent.gamestate >= 1:
        imagebutton:
            idle "kutrinappi.png"
            hover "kutrinappihover.png"
            xpos 742
            ypos 294
            action [Hide("mapScreen"), Jump("westStreet")]
    if persistent.gamestate >= 5:
        imagebutton:
            idle "mainstrtnappi.png"
            hover "mainstrtnappihover.png"
            xpos 886
            ypos 658
            action [Hide("mapScreen"), Jump("mainStreet")]

screen interactUiScreen():
    #this determines which interact icons are shown
    #0: eye 1: hand 2:bag 3:eye&bag 4: eye&hand 5:hand&bag 6:eye&bag&hand
    if interValue == 0 and interUiOpen:
        imagebutton:
            xpos 738
            ypos 826
            idle "eye.png"
            hover "eyeHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemlook")]
    if interValue == 1 and interUiOpen:
        imagebutton:
            xpos 738
            ypos 826
            idle "hand.png"
            hover "handHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemuse")]
    if interValue == 2 and interUiOpen:
        imagebutton:
            xpos 858
            ypos 826
            idle "bag.png"
            hover "bagHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump(itemID + "pickup")]
    if interValue == 3 and interUiOpen:
        imagebutton:
            xpos 798
            ypos 826
            idle "bag.png"
            hover "bagHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump(itemID + "pickup")]
        imagebutton:
            xpos 738
            ypos 826
            idle "eye.png"
            hover "eyeHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemlook")]
    if interValue == 4 and interUiOpen:
        imagebutton:
            xpos 738
            ypos 826
            idle "eye.png"
            hover "eyeHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemlook")]
        imagebutton:
            xpos 798
            ypos 826
            idle "hand.png"
            hover "handHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemuse")]
    if interValue == 5 and interUiOpen:
        imagebutton:
            xpos 738
            ypos 826
            idle "hand.png"
            hover "handHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemuse")]
        imagebutton:
            xpos 798
            ypos 826
            idle "bag.png"
            hover "bagHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump(itemID + "pickup")]
    if interValue == 6 and interUiOpen:
        imagebutton:
            xpos 798
            ypos 826
            idle "hand.png"
            hover "handHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemuse")]
        imagebutton:
            xpos 858
            ypos 826
            idle "bag.png"
            hover "bagHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump(itemID + "pickup")]
        imagebutton:
            xpos 738
            ypos 826
            idle "eye.png"
            hover "eyeHover.png"
            action [Hide("interactUiScreen"), SetVariable("interUiOpen", False), Jump("itemlook")]
