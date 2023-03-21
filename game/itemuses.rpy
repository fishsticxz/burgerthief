label oviuse:
    if persistent.items.count("keys"):
        show screen mapScreen
        $ renpy.pause(hard=True)
    else:
        "You shouldn't leave without your keys!"
        show screen playerHouseScreen
        $ renpy.pause(hard=True)

label wsautouse:
    "You can’t just take someone else’s car! Keep your hands off!"
    window hide
    $ renpy.pause(hard=True)

label sankyuse:
    if persistent.gamestate == 0:
        $ sankyEnding += 1
        if sankyEnding == 1:
            show bed scolding at charbox
            b "You can't go to sleep! You have to go to work!"
            hide bed
        if sankyEnding == 2:
            show bed scolding at charbox
            b "I'm being serious! There's no time to slack around!"
            hide bed
        if sankyEnding == 3:
            show bed data at charbox
            b "Are you trying to get fired from your new job?"
            hide bed
        if sankyEnding == 4:
            show bed scolding at charbox
            b "There's really no changing your mind, huh...."
            hide bed
        if sankyEnding == 5:
            $ renpy.force_autosave(take_screenshot=False, block=False)
            show bed scolding at charbox
            b "Fine then. I'm not going to stop you."
            hide bed
        if sankyEnding == 6:
            "Ahh.. The land of sleep calls me once again..."
            jump sankygameover
    if persistent.gamestate >= 1:
        show bed happy at charbox
        b "Looks like you're hard at work! Good job, user!"
        hide bed
        window hide
    show screen playerHouseScreen
    $ renpy.pause(hard=True)

label tyooviuse:
    call workInside from _call_workInside

label jasonuse:
    if persistent.jasonDialogue == 0:
        call jasonintroduction from _call_jasonintroduction
    if persistent.jasonDialogue == 1:
        call talktomanager from _call_talktomanager
    if persistent.jasonDialogue == 2:
        call letsgetgoing from _call_letsgetgoing
    if persistent.jasonDialogue == 3 and persistent.currentPlace == "workInside":
        call letsgetout from _call_letsgetout
    if persistent.jasonDialogue == 3 and persistent.currentPlace == "westStreetHall":
        call checkaddress from _call_checkaddress
    if persistent.jasonDialogue == 4:
        call addressreminder from _call_addressreminder
    if persistent.jasonDialogue == 5 and persistent.currentPlace == "westStreetHall":
        call letsdeliver from _call_letsdeliver
    if persistent.jasonDialogue == 6 and persistent.currentPlace == "westStreet":
        call confusedjason from _call_confusedjason
    if persistent.jasonDialogue == 6 and persistent.currentPlace == "westStreetHall":
        call checkitagain from _call_checkitagain
    if persistent.jasonDialogue == 7 and persistent.currentPlace == "westStreetHall":
        call letsdeliver from _call_letsdeliver_1
    if persistent.jasonDialogue == 8:
        call didyoufindanything from _call_didyoufindanything
    if persistent.jasonDialogue == 9:
        call thiswasmissing from _call_thiswasmissing

label manageruse:
    if persistent.managerDialogue == 0:
        call managerintroduction from _call_managerintroduction
    if persistent.managerDialogue == 1:
        call talktojason from _call_talktojason
    if persistent.managerDialogue == 2:
        call disaster from _call_disaster
    if persistent.managerDialogue == 3 and persistent.currentPlace == "workInside":
        call gonow from _call_gonow
    if persistent.managerDialogue == 4:
        call canjasonandihavethecar from _call_canjasonandihavethecar
    if persistent.managerDialogue == 5:
        call wherewhere from _call_wherewhere

label weststreetdooruse:
    call westStreetHall from _call_westStreetHall

label autouse:
    if persistent.gamestate <= 3:
        "You can’t use that! You don't need it to deliver anything!"
    if persistent.gamestate >= 4:
        "With this, I’ll catch up to the thief for sure!"
        $ persistent.gamestate = 5
    window hide
    show screen workOutsideScreen
    $ renpy.pause(hard=True)

label addressboarduse:
    show screen addressboardScreen
    "Let's see..."
    if persistent.gamestate == 1:
        "Karl Dandleton: apt 059 - Todd Bonzalez: apt 060"
        "Sleve McDichael: apt 061 - Bobson Dugnutt: apt 062"
        "Willie Dustice: apt 063 - Rey McScriff: apt 064"
        "...There!"
        menu:
            "Read again":
                call addressboarduse from _call_addressboarduse
            "Close":
                call closeboard from _call_closeboard
    if persistent.gamestate == 2:
        "Jeromy Gride: apt 037 - Shown Furcotte: apt 038"
        "Glenallen Mixon: apt 039 - Tony Smehrik: apt 040"
        "Tim Sandaele: apt 041 - Rey McScriff: apt 042"
        "...There!"
        menu:
            "Read again":
                call addressboarduse from _call_addressboarduse_1
            "Close":
                call closeboardtwo from _call_closeboardtwo
    if persistent.gamestate == 3 and persistent.items.count("keyboard"):
        "Jeromy Gride: apt 037 - Shown Furcotte: apt 038"
        "Glenallen Mixon: apt 039 - Tony Smehrik: apt 040"
        "Tim Sandaele: apt 041 - Rey McScriff: apt 042"
        menu:
            "Read again":
                call addressboarduse from _call_addressboarduse_2
            "Close":
                call closeboardthree from _call_closeboardthree
            "Use keyboard":
                call hackerman from _call_hackerman
    else:
        "Jeromy Gride: apt 037 - Shown Furcotte: apt 038"
        "Glenallen Mixon: apt 039 - Tony Smehrik: apt 040"
        "Tim Sandaele: apt 041 - Rey McScriff: apt 042"
        "I wonder if I can use something to access this addressboard..."
    show screen westStreetHallScreen
    $ renpy.pause(hard=True)

label hissiuse:
    if persistent.gamestate == 1 and persistent.jasonDialogue == 5:
        call kutriKerros from _call_kutriKerros
    elif persistent.gamestate == 2 and persistent.jasonDialogue == 7:
        call asiakasKerros from _call_asiakasKerros
    elif persistent.gamestate >= 3 and persistent.listChecked == 1:
        menu:
            "Floor 3":
                call asiakasKerros from _call_asiakasKerros_1
            "Floor 5":
                call kutriKerros from _call_kutriKerros_1
    else:
        "Wait! You don't even know which floor you're going to!"
        $ renpy.pause(hard=True)
    return

label kutrioviuse:
    if persistent.gamestate == 1 and persistent.managerDialogue == 1:
        call deliverydelivery from _call_deliverydelivery
    if persistent.gamestate == 3 and persistent.listChecked == 1 and persistent.jasonDialogue <= 8:
        call interrogation from _call_interrogation
    if persistent.gamestate == 4 and persistent.listChecked == 1 and persistent.jasonDialogue >= 9:
        call kutriHuone from _call_kutriHuone
    else:
        call whatdoyouwant from _call_whatdoyouwant

label asiakasoviuse:
    if persistent.gamestate == 2:
        call correctdelivery from _call_correctdelivery
    if persistent.gamestate == 3 and persistent.listChecked == 1:
        call justasking from _call_justasking
    else:
        call whatdoyouwant from _call_whatdoyouwant_1

label carguyuse:
    if persistent.carguyDialogue == 0:
        call sunkeskustelu from _call_sunkeskustelu
    else:
        call jokutoinenjuttu from _call_jokutoinenjuttu

label ikkunarikkiuse:
    "Let's take a peek... Oh! There are stairs right behind this window."
    "It's probably faster to go down through the building though..."
    window hide
    $ renpy.pause(hard=True)

label bystanderoneuse:
    s "It was someone on a SolMobile!"
    s "If you go that way, you should be able to find them."
    s "I hope everyone's okay..."
    window hide
    $ renpy.pause(hard=True)

label bystandertwouse:
    s "Some weird person came through here craaazy fast! Like, ultra mega giga fast!"
    s "It was so cooooool!!!!"
    window hide
    $ renpy.pause(hard=True)

label bystanderthreeuse:
    s "People nowadays don’t know how to drive properly..."
    window hide
    $ renpy.pause(hard=True)

label gamerchairuse:
    show jason tired at charbox
    j "Ewww! Are you seriously sitting on that?!"
    hide jason
    window hide
    $ renpy.pause(hard=True)

label patjause:
    show dumbbed normal at charbox
    d "How many hours of sleep did you get? Fuck, uh, four, maybe? That sounds healthy, good job Chumplord69!"
    d "REM sleep? The fuck you bringing alt rock into this conversation for those guys haven't been relevant since 2002"
    hide dumbbed
    "...Nevermind. It's actually a Dumbbed."
    window hide
    $ renpy.pause(hard=True)
