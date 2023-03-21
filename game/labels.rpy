label fivemins:
    show bed scolding at charbox
    b "No can do! My suggestion is to go to sleep a little bit earlier tomorrow, so you can wake up energetic and refreshed!"
    return
label goodmorning:
    show bed happy at charbox
    b "Oh! It’s nice to see you in such a good mood, despite the poor amount of sleep last night! Not to mention the quality..."
    b "Nevertheless, I wish you a good day, user!"
    return
label newjob:
    show bed scolding at charbox
    b "It is of utmost importance that I stay on top of my user’s daily routines and changes in lifestyle, that might have an impact on the amount of rest needed per day!"
    show bed happy at charbox
    b "But don’t think about it any further, alright?"
    return

label order:
    show jason happy at charbox
    j "Alright then, coming right up..."
    show jason tired at charbox
    j "Wait, aren’t you the new employee? Don’t joke with me like this, can’t you see I’m already tired enough?"
    return
label towork:
    j "Oh, I see. About time I got some help around here. The manager is driving me nuts, but I’ve got bills to pay so no can do."
    return
label waytoohappy:
    show jason tired at charbox
    j "Okay okay I got it, but can you pipe it down please. You don’t know how bad android migraines can be."
    show jason normal at charbox
    return

label isurehopeso:
    show jason normal at charbox
    j "Let’s hope for the best. Maybe together we can even solve this and make sure no one else gets fired over this."
    return
label empath:
    show jason happy at charbox
    j "Thanks. A bad work environment does wonders to your psyche, and it’s not the good kind of wonders."
    return
label rude:
    show jason tired at charbox
    j "Ha ha. Very funny."
    return

label goodjobkid:
    show manager thinking at charbox
    m "I’m liking the enthusiasm. Don’t get too friendly, though. Right now I can’t trust anyone around here!"
    show manager normal at charbox
    return
label toofast:
    show manager thinking at charbox
    m "Not so fast, I have to tell you about some important things regarding this place."
    show manager normal at charbox
    return
label justdont:
    show manager thinking at charbox
    m "Don’t you attitude me, kiddo! Running a restaurant is serious business, and I ain’t got time for smiling right now."
    show manager normal at charbox
    return
label jep:
    show manager thinking at charbox
    m "You don’t know him... Just watch him, and you too will see how the orders just disappear into thin air."
    show manager normal at charbox
    return
label mood:
    show manager thinking at charbox
    m "For your own good, I’ll be taking that as a compliment."
    show manager normal at charbox
    return
label youlikepeople:
    show manager happy at charbox
    m "Finally, someone who believes me! You seem like a proper employee, kiddo."
    return

label betrayed:
    j "Company policy. The manager says fresh air and exercise is important, so we’re not allowed to use the car if the delivery route is short enough."
    show jason tired at charbox
    j "Bullshit if you ask me, but there’s nothing we can do about it."
    return
label enthusiasmatitsbest:
    show jason tired at charbox
    j "Uhh, that’s great. Enjoy your positivity and enthusiasm while it lasts."
    return
label rudeparttwo:
    show jason tired at charbox
    j "Stop joking with me. I’m already scared of losing my job, I don’t need another person blaming me for something I didn’t do."
    return
label firstknock:
    "(knock knock knock)"
    return
label brokenbell:
    "(...)"
    "It seems to be broken..."
    call deliverydelivery from _call_deliverydelivery_1
label normalgreeting:
    show kutri neutralcustomer at charbox
    c "Wonderful, thank you so much!"
    return
label overenthusiasm:
    show kutri happycustomer at charbox
    c "Haha, what’s with this greeting? You must be a new employee!"
    return
label chillgreeting:
    show kutri neutralcustomer at charbox
    c "Oh, that’s great. Thanks!"
    return
label givefoodornot:
    menu:
        "Here you go!":
            call givefood from _call_givefood
        "I don't think I'm going to!":
            call refuse from _call_refuse
    return
label givefood:
    hide kutri
    hide jason
    "Food order removed from inventory!"
    show kutri happycustomer at charbox
    c "Thank youuu, have a nice day! Bye now!"
    hide kutri
    "*the door closes*"
    return
label refuse:
    hide jason
    show kutri worriedcustomer at charbox
    c "Hey, what’s this about? Aren’t you going to give me my food?"
    show jason normal at charbox
    j "What are you doing? You know this is your job, right?"
    call givefoodornot from _call_givefoodornot
    return
label youshouldknow:
    show manager angry at charbox
    m "A disaster, I tell you!"
    return
label youknowit:
    show manager wolf at charbox
    m "Exactly. You have a sharp mind, kiddo."
    return
label notagoodidea:
    show manager angry at charbox
    m "Hey, where do you think you’re going?!"
    return
label vouchforjason:
    hide manager
    show jason normal at charbox
    j "Yeah. We don’t know what happened - we can both confirm that we handed out the food to the customer!"
    hide jason
    show manager angry at charbox
    m "Well, the customer sure doesn’t think so!"
    return
label blamejason:
    hide manager
    show jason tired at charbox
    j "Hey!"
    hide jason
    show manager wolf at charbox
    m "You should’ve kept a closer eye on him!"
    m "I should’ve figured this is what happens when you put a rookie in charge of stuff like this..."
    return
label blamecustomer:
    show manager angry at charbox
    m "How dare you even suggest such a thing! The customer is always right, and that’s a hard rule in my establishment!"
    return
label veryodd:
    show jason happy at charbox
    j "I really hope so, for my sake and yours. We workers gotta stick together."
    return
label stillblamingjason:
    show jason tired at charbox
    j "You know you don’t have to lick the manager’s boots when she’s not even listening?"
    show jason normal at charbox
    j "Quit with it already. You’re not being funny."
    show jason tired at charbox
    j "At all."
    return
label burgermystery:
    show jason normal at charbox
    j "...You’re not taking this very seriously, are you?"
    j "I can not understand how you keep up that pep."
    return
label asiakaskoputus:
    "(knock knock knock)"
    return
label itworksthistime:
    "(ding dong)"
    return
label weresosorry:
    show customer sad at charbox
    c "You won’t have a chance to prove it, because this was the first and last time I’m trusting your services!"
    return
label notourfault:
    show customer pissed at charbox
    c "You think I’m going to believe a word of that bullshit? You’re clearly the ones at fault here."
    return
label customercheater:
    show customer sad at charbox
    c "How dare you suggest something like that? I’ve dealt with enough bullshit today, I don’t need incompetent food couriers on top of everything else!"
    show customer pissed at charbox
    c "You don’t even know how night shift can be."
    return
label twinsies:
    show jason normal at charbox
    j "That would be absurd, but I guess not entirely impossible..."
    j "Just... Very unlikely, considering the amount of different people we’ve delivered orders to in this building."
    return
label bigprank:
    show jason normal at charbox
    j "I don’t know how that would work... "
    j "This is a really big apartment complex, and I doubt people would have time to organize something like that."
    show jason normal at charbox
    j "Besides, why would people campaign against us? We’re just a fast food restaurant."
    return
label sceptic:
    show jason tired at charbox
    j "You know what, I’m getting really tired of your accusations."
    show jason normal at charbox
    j "If you weren’t my new coworker, I’d just leave you here and let you solve this by yourself, but the manager would throw a fit if I did that."
    show jason tired at charbox
    j "And you don’t want to see her angry."
    return
label founditout:
    show jason happy at charbox
    j "Good job, that gives me hope that this mess can be solved..."
    return
label noclue:
    show jason normal at charbox
    j "Keep looking, there has to be something that can explain this mystery."
    menu:
        "Alright, I'll keep looking.":
            call keeplooking from _call_keeplooking
        "Can you give me a hand?":
            call givemeahand from _call_givemeahand

    return
label keeplooking:
    show jason normal at charbox
    j "Good luck."
    return
label givemeahand:
    show jason normal at charbox
    j "Well... I don't really have anything with me right now."
    j "But you're free to swing by your home and pick up anything that you think might help us."
    j "Maybe that could be the key to something?"
    return
label burgerboy:
    show jason tired at charbox
    j "..."
    return
label passwords:
    menu:
        "12345":
            call defaultpassword from _call_defaultpassword
        "5318008":
            call boobies from _call_boobies
        "password":
            call seriously from _call_seriously
    return
label defaultpassword:
    "(Access denied.)"
    "Nope... At least the person who put this up isn’t stupid enough to leave the password as default."
    call passwords from _call_passwords
label boobies:
    "(Access denied.)"
    "A classic... Too bad that wasn’t it."
    call passwords from _call_passwords_1
label seriously:
    "(Access granted!)"
    "Seriously???"
    call welcome from _call_welcome
label boardmenu:
    menu:
        "See resident list":
            call residentlist from _call_residentlist
        "Check recent changes":
            call recentchanges from _call_recentchanges
        "Log out":
            call logout from _call_logout
label residentlist:
    $ persistent.listChecked = 1
    "Jeromy Gride: apt 037 - Shown Furcotte: apt 038"
    "Glenallen Mixon: apt 039 - Tony Smehrik: apt 040"
    "Tim Sandaele: apt 041 - Rey McScriff: apt 042"
    "...Just a long list of the weirdest names I've seen."
    call boardmenu from _call_boardmenu
label recentchanges:
    $ persistent.listChecked =  1
    "Today at 10:28, Rey McScriff moved from apt. 064 to apt. 042"
    "Today at 10:27, Kutri Zielo moved to apt. 064"
    "Yesterday at 13:15, Dean Wesrey moved from apt. 089"
    call boardmenu from _call_boardmenu_1
label logout:
    "Thank you for using the BitWizard Digital Addressboard!"
    "See you soon, user!"
    window hide
    call westStreetHall from _call_westStreetHall_1
    $ renpy.pause(hard=True)
    return
label leaveit:
    window hide
    $ renpy.pause(hard=True)
label choiceschoices:
    menu:
        "Knock on the door":
            call asiakaskoputustwo from _call_asiakaskoputustwo
        "Ring the doorbell":
            call itworksthistimetwo from _call_itworksthistimetwo
        "Leave it":
            call leaveit from _call_leaveit
    return
label newchoices:
    menu:
        "Knock on the door":
            call asiakaskoputustwo from _call_asiakaskoputustwo_1
        "Ring the doorbell":
            call itworksthistimetwo from _call_itworksthistimetwo_1
        "Leave it":
            call leaveit from _call_leaveit_1
        "Wait":
            call waitwait from _call_waitwait
label asiakaskoputustwo:
    if knockAmount <= 3:
        $ knockAmount + 1
        "(knock knock knock)"
        "(...)"
        call newchoices from _call_newchoices
    else:
        "STOP BOTHERING ME"
        call leaveit from _call_leaveit_2
label itworksthistimetwo:
    if ringAmount <= 3:
        $ ringAmount + 1
        "(ding dong)"
        "(...)"
        call newchoices from _call_newchoices_1
    else:
        "LEAVE ME ALONE"
        call leaveit from _call_leaveit_3
label questions:
    menu:
        "Do you perhaps have a twin?":
            call haveatwin from _call_haveatwin
        "Did you recently move into this apartment? Like, earlier today?":
            call didyoumove from _call_didyoumove
        "Did you enjoy your meal?":
            call enjoymeal from _call_enjoymeal
    c "Did you need something else?"
    menu:
        "Yeah, I just wanted to ask you...":
            call questions from _call_questions
        "No, I’m good. Thanks for your help!":
            call imgood from _call_imgood
label haveatwin:
    show customer normal at charbox
    c "...No? What makes you ask that? That’s a weird question to just pop on people."
    return
label didyoumove:
    show customer normal at charbox
    c "Uhh... No. I’ve been living in this apartment for the past 3 years."
    return
label enjoymeal:
    show customer normal at charbox
    c "Is that all you’re asking? Well, the fries were pretty good."
    c "Don’t think I’m going to order again though."
    return

label whatdoyouwant:
    "...Probably not a good idea to touch that again."
    window hide
    $ renpy.pause(hard=True)


label variables:
    $ knockAmount = 0
    $ ringAmount = 0
    $ interValue = 0
    $ itemID = "none"
    $ interUiOpen = False
    $ invUiOpen = False
    $ chartabUiOpen = False
    $ mapUiOpen = False
    $ optionsScreenUiOpen = False
    $ persistent.listChecked = 0
    $ persistent.items = []
    $ persistent.characters = []
    $ persistent.gamestate = 0
    $ persistent.jasonDialogue = 0
    $ persistent.managerDialogue = 0
    $ persistent.kutriDialogue = 0
    $ persistent.carguyDialogue = 0
    $ sankyEnding = 0
    $ persistent.currentPlace = "playerHouse"
    return

label sankygameover:
    "You got fired for not showing up to work!"
    "Game Over!"

label gameover:
    $ MainMenu(confirm=False)()

label itemuse:
    call expression itemID + "use" from _call_expression

label itemlook:
    call expression itemID + "description" from _call_expression_1
