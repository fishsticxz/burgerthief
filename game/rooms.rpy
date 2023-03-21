label playerHouse:
    scene bgbgbg
    hide click_screen
    show screen playerHouseScreen
    $ persistent.currentPlace = "playerHouse"
    $ renpy.pause(hard=True)
label workOutside:
    scene bgbgbg
    hide click_screen
    show screen workOutsideScreen
    $ persistent.currentPlace = "workOutside"
    $ renpy.pause(hard=True)
label mainStreet:
    scene bgbgbg
    hide click_screen
    show screen mainStreetScreen
    $ persistent.currentPlace = "mainStreet"
    $ renpy.pause(hard=True)
label westStreet:
    scene bgbgbg
    hide click_screen
    show screen westStreetScreen
    $ persistent.currentPlace = "westStreet"
    $ renpy.pause(hard=True)
label westStreetHall:
    scene bgbgbg
    hide click_screen
    show screen westStreetHallScreen
    $ persistent.currentPlace = "westStreetHall"
    $ renpy.pause(hard=True)
label workInside:
    scene bgbgbg
    hide click_screen
    show screen workInsideScreen
    $ persistent.currentPlace = "workInside"
    $ renpy.pause(hard=True)
label kutriKerros:
    scene bgbgbg
    hide click_screen
    show screen kutriKerrosScreen
    $ persistent.currentPlace = "kutriKerros"
    $ renpy.pause(hard=True)
label asiakasKerros:
    scene bgbgbg
    hide click_screen
    show screen asiakasKerrosScreen
    $ persistent.currentPlace = "asiakasKerros"
    $ renpy.pause(hard=True)
label kutriHuone:
    scene bgbgbg
    hide click_screen
    show screen kutriHuoneScreen
    $ persistent.currentPlace = "kutriHuone"
    $ renpy.pause(hard=True)

screen playerHouseScreen():
    tag click_screen
    image "pelaajankamppa.png" xpos 730 ypos 210
    imagebutton:
        xpos 1214
        ypos 630
        idle "sanky.png"
        hover "sankyHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "sanky"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    if persistent.items.count("keyboard") == False:
        imagebutton:
            xpos 914
            ypos 474
            idle "nappis.png"
            hover "nappisHover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 3), SetVariable("itemID", "nappis"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1178
        ypos 254
        idle "ovi.png"
        hover "oviHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "ovi"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    if persistent.items.count("keys") == False:
        imagebutton:
            xpos 1050
            ypos 466
            idle "kotiavain.png"
            hover "kotiavainHover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 3), SetVariable("itemID", "keys"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 822
        ypos 282
        idle "kaihdin.png"
        hover "kaihdinhover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "kaihdin"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 890
        ypos 362
        idle "naytto.png"
        hover "nayttohover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "naytto"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 782
        ypos 374
        idle "traakki.png"
        hover "traakkihover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "traakki"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)


screen workOutsideScreen():
    tag click_screen
    image "chompsiesoutside.png" xpos 730 ypos 210
    imagebutton:
        xpos 1178
        ypos 362
        idle "autobig.png"
        hover "autobrdr.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "auto"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 730
        ypos 206
        idle "kyltti.png"
        hover "kylttibrdr.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "kyltti"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 994
        ypos 370
        idle "brgrovi.png"
        hover "brgrovibrdr.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "tyoovi"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)

screen workInsideScreen():
    tag click_screen
    image "chompsiesinside.png" xpos 730 ypos 210
    if persistent.gamestate <= 1:
        imagebutton:
            xpos 886
            ypos 326
            idle "bigjason.png"
            hover "bigjasonbrdr.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 4), SetVariable("itemID", "jason"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1250
        ypos 250
        idle "bigtv.png"
        hover "bigtvbrdr.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "tv"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1326
        ypos 806
        idle "backbutton.png"
        hover "backbuttonbrdr.png"
        action Jump("workOutside")
    if persistent.gamestate >= 0:
        imagebutton:
            xpos 762
            ypos 306
            idle "bigmanager.png"
            hover "bigmanagerbrdr.png"
            if interUiOpen == False and persistent.jasonDialogue >= 1:
                action [SetVariable("interValue", 4), SetVariable("itemID", "manager"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            elif interUiOpen == False and persistent.jasonDialogue == 0:
                action [SetVariable("interValue", 0), SetVariable("itemID", "manager"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)

screen mainStreetScreen():
    tag click_screen
    image "mainstreet.png" xpos 730 ypos 210
    imagebutton:
        xpos 794
        ypos 642
        idle "bystander3.png"
        hover "bystander3hover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 1), SetVariable("itemID", "bystanderthree"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 990
        ypos 654
        idle "bystander2.png"
        hover "bystander2hover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 1), SetVariable("itemID", "bystandertwo"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1194
        ypos 606
        idle "bystander1.png"
        hover "bystander1hover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 1), SetVariable("itemID", "bystanderone"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)

screen westStreetScreen():
    tag click_screen
    if persistent.gamestate <= 3:
        image "weststreet.png" xpos 730 ypos 210
    else:
        image "streetnocar.png" xpos 730 ypos 210
    imagebutton:
        xpos 730
        ypos 334
        idle "westdoor.png"
        hover "westdoorHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "weststreetdoor"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    if persistent.gamestate == 3 and persistent.managerDialogue >= 3:
        imagebutton:
            xpos 950
            ypos 446
            idle "jasonstanding.png"
            hover "jasonstandingHover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 4), SetVariable("itemID", "jason"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    if persistent.gamestate <= 3:
        imagebutton:
            xpos 1094
            ypos 506
            idle "wsauto.png"
            hover "wsautohover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 4), SetVariable("itemID", "wsauto"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    if persistent.gamestate >= 4:
        imagebutton:
            xpos 1166
            ypos 390
            idle "carguy.png"
            hover "carguyhover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 4), SetVariable("itemID", "carguy"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    if persistent.gamestate >= 4:
        imagebutton:
            xpos 1174
            ypos 658
            idle "tiretrack.png"
            hover "tiretrackhover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 0), SetVariable("itemID", "tiretrack"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)

screen westStreetHallScreen():
    tag click_screen
    image "aula.png" xpos 730 ypos 210
    imagebutton:
        xpos 742
        ypos 210
        idle "hissi.png"
        hover "hissiHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "hissi"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1130
        ypos 246
        idle "address.png"
        hover "addressHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "addressboard"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 894
        ypos 266
        idle "jasonstanding.png"
        hover "jasonstandingHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "jason"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1230
        ypos 242
        idle "taulu.png"
        hover "tauluHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "notice"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1174
        ypos 478
        idle "kasvi.png"
        hover "kasviHover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "hallplant"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1326
        ypos 806
        idle "backbutton.png"
        hover "backbuttonbrdr.png"
        action Jump("westStreet")

screen kutriKerrosScreen:
    tag click_screen
    image "kaytava.png" xpos 730 ypos 210
    imagebutton:
        xpos 926
        ypos 282
        idle "kaytavaovi.png"
        hover "kaytavaovihover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "kutriovi"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1326
        ypos 806
        idle "backbutton.png"
        hover "backbuttonbrdr.png"
        action Jump("westStreetHall")
screen asiakasKerrosScreen:
    tag click_screen
    image "kaytavatwo.png" xpos 730 ypos 210
    imagebutton:
        xpos 926
        ypos 282
        idle "kaytavaovi.png"
        hover "kaytavaovihover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "asiakasovi"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1326
        ypos 806
        idle "backbutton.png"
        hover "backbuttonbrdr.png"
        action Jump("westStreetHall")

screen hackermanScreen:
    tag click_screen
    image "login.png" xpos 730 ypos 210

screen hackermanScreentwo:
    tag click_screen
    image "bitwizard.png" xpos 730 ypos 210

screen addressboardScreen:
    tag click_screen
    image "addressboard.png" xpos 730 ypos 210

screen kutriHuoneScreen:
    tag click_screen
    image "kutrinhuone.png" xpos 730 ypos 210
    if persistent.gamestate >= 4:
        imagebutton:
            xpos 1170
            ypos 258
            idle "ikkunarikki.png"
            hover "ikkunarikkihover.png"
            if interUiOpen == False:
                action [SetVariable("interValue", 4), SetVariable("itemID", "ikkunarikki"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
            else:
                action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1046
        ypos 490
        idle "trash.png"
        hover "trashhover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "trash"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 730
        ypos 262
        idle "kone.png"
        hover "konehover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "kone"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 994
        ypos 238
        idle "poster.png"
        hover "posterhover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "poster"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 730
        ypos 426
        idle "johto.png"
        hover "johtohover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 0), SetVariable("itemID", "johto"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 894
        ypos 350
        idle "gamerchair.png"
        hover "gamerchairhover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "gamerchair"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 730
        ypos 634
        idle "patja.png"
        hover "patjahover.png"
        if interUiOpen == False:
            action [SetVariable("interValue", 4), SetVariable("itemID", "patja"), SetVariable("interUiOpen", True), Show("interactUiScreen")]
        else:
            action SetVariable("interUiOpen", False)
    imagebutton:
        xpos 1326
        ypos 806
        idle "backbutton.png"
        hover "backbuttonbrdr.png"
        action Jump("kutriKerros")
