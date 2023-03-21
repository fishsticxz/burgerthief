
define b = Character("SMARTBED TM")
define m = Character("MANAGER")
define j = Character("JASON")
define k = Character("KUTRI")
define c = Character("CUSTOMER")
define g = Character("BUSINESS GUY")
define d = Character("DUMBBED TM")
define s = Character("BYSTANDER")

image splash = "tittlescreen.png"
image sevenam = "alkuscreen.png"

transform charbox:
    xpos 514
    ypos 210
transform titlescreen:
    xpos 406
    ypos 88

#label splashscreen:
    #scene bgbgbg
    #show splash at titlescreen
    #with Pause(3)
#    show screen startbuttonScreen
#    $ renpy.pause(hard=True)
    #hide splash with dissolve
#return

## init python:

##    config.underlay.append(
##        renpy.Keymap(
##            mousedown_1 = lambda: renpy.run(renpy.play("audio/pop.wav", channel=u'sound')  )
##        )
##    )

screen startbuttonScreen():
    imagebutton:
        xpos 1110
        ypos 888
        idle "startbutton.png"
        hover "startbuttonbrdr.png"
        action [Hide("startbuttonScreen"), Jump("start")]

init -2:
    style say_thought:
        line_spacing 10
    style say_dialogue:
        line_spacing 10

label start:
    scene bgbgbg
    show sevenam at titlescreen
    with Pause(3)
    hide sevenam with dissolve
    call variables from _call_variables
    show screen uiScreen
    call beginningofgame from _call_beginningofgame
    return

label beginningofgame:
    scene bgbgbg
    show screen playerHouseScreen
    $ persistent.characters.append("bed")
    show bed happy at charbox
    b "Good morning!"
    show bed data at charbox
    b "You're starting at your new job today, and you've slept for a crisp 6 hours 14 minutes, of which 45 minutes have been REM sleep!"

    menu:
        "Ugh...... 5 more minutes please?":
            call fivemins from _call_fivemins
        "Good morning, SmartBed TM!":
            call goodmorning from _call_goodmorning
        "Wait, why do you know about my new job?":
            call newjob from _call_newjob

    b "Now hurry up, or you’ll be late!"
    hide bed
    window hide
    $ renpy.pause(hard=True)

label jasonintroduction:
    $ persistent.characters.append("jason")
    $ persistent.jasonDialogue = 1
    show jason tired at charbox
    j "Good morning, what can I get you?"
    show jason normal at charbox

    menu:
        "Uhhh... A burger and large fries?":
            call order from _call_order
        "Nothing dude, I’m here for work. I’m the new employee.":
            call towork from _call_towork
        "Good morning, fellow employee! I’m here for my 7:30 shift!":
            call waytoohappy from _call_waytoohappy
    show jason normal at charbox
    j "I’m Jason, pretty much the only employee here, if you don’t count the fry cooking machine."
    j "The manager keeps firing people because of some orders disappearing mysteriously, and now that there’s no one else working here anymore -"
    j "She thinks she’s cracked the case and I’m the culprit who keeps stealing the food."
    show jason tired
    j "I don’t even eat!!!"
    show jason normal

    menu:
        "Hmm, I hope she doesn’t get any ideas about me. I’ve got bills to pay too":
            call isurehopeso from _call_isurehopeso
        "Oh. That really sucks. I hope she gets off your case soon.":
            call empath from _call_empath
        "But... Maybe she’s right and it is you! I don’t know you, so... ":
            call rude from _call_rude
    j "Anyway, you should talk to the manager to get started."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label talktomanager:
    show jason normal at charbox
    j "Didn't I tell you to talk to the manager?"
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return


label managerintroduction:
    $ persistent.characters.append("manager")
    $ persistent.managerDialogue = 1
    $ persistent.jasonDialogue = 2
    show manager normal at charbox
    m "Mornin’. You must be the new employee. I’m the manager here, and I’ll be addressed as such."
    m "Good to see you’re on time. Wouldn’t wanna get fired on your first day, am I right?"
    show manager thinking
    m "Just kidding. But know that I don’t go easy on newbies!"
    menu:
        "Good morning to you too, ma’am!":
            call goodjobkid from _call_goodjobkid
        "Alright... Can I get to work then?":
            call toofast from _call_toofast
        "What’s with the attitude?":
            call justdont from _call_justdont
    m "You see, strange things have been happening in this here restaurant, and I feel like I’m just about to crack this case for good."
    show manager thinking
    m "Orders have been disappearing left and right, and after monitoring the situation, I suspect the culprit is one of my employees, Jason!"
    show manager normal
    m "This can’t go on for any longer, or unsatisfied customers will be the downfall of my precious restaurant!"
    m "I’m just waiting for the perfect moment to catch that tinhead red handed!"
    menu:
        "Jason... The android? Who doesn’t need to eat food?":
            call jep from _call_jep
        "Right... You’re quite the manager, it seems. (Whatever will pay my rent, I guess...)":
            call mood from _call_mood
        "That’s awful! I’ll help you catch the culprit!":
            call youlikepeople from _call_youlikepeople
    show manager happy
    m "Let’s get you to work then!"
    show manager normal at charbox
    m "Here’s your first delivery order. Take Jason with you, he’ll show you the ropes."
    show manager thinking at charbox
    m "Keep an eye on him though... I don’t want to see any more orders disappear!"
    $ persistent.items.append("foodorder")
    "Food order added to inventory!"
    hide manager
    window hide
    $ renpy.pause(hard=True)
    return

label talktojason:
    show manager normal at charbox
    m "Talk to Jason and get going with the order!"
    hide manager
    window hide
    $ renpy.pause(hard=True)
    return

label letsgetgoing:
    $ persistent.jasonDialogue = 3
    $ persistent.gamestate = 1
    show jason normal at charbox
    j"You got the order? Good job."
    j"Looks like the address is West street 6B and the order recipient is Rey McScriff."
    j"It’s not too far from here, so let’s get walking."
    menu:
        "Wait, walking? You have a delivery car, don’t you?":
            call betrayed from _call_betrayed
        "Alright, let’s go! I can’t wait to deliver my first order!":
            call enthusiasmatitsbest from _call_enthusiasmatitsbest
        "Are you going to steal this food too?":
            call rudeparttwo from _call_rudeparttwo
    j"Let’s go. We can’t keep the customer waiting."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label letsgetout:
    show jason normal at charbox
    j "Come on, let's deliver this order."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label checkaddress:
    $ persistent.jasonDialogue = 4
    show jason normal at charbox
    j "Alright, so our delivery is for a person called Rey McScriff, remember?"
    j "Can you check what their apartment number is? There seems to be an address board on the wall."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label addressreminder:
    show jason normal at charbox
    "Rey McScriff. Hurry up."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label closeboard:
    $ persistent.jasonDialogue = 5
    show screen westStreetHallScreen
    show jason happy at charbox
    j "Good job, let’s get going then."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label closeboardtwo:
    $ persistent.jasonDialogue = 7
    show screen westStreetHallScreen
    show jason happy at charbox
    j "Good job, let’s get going then."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label closeboardthree:
    window hide
    $ renpy.pause(hard=True)
    return

label letsdeliver:
    show jason normal at charbox
    j "Let’s get going."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label deliverydelivery:
    $ persistent.managerDialogue = 2
    menu:
        "Knock on the door":
            call firstknock
        "Ring the bell":
            call brokenbell
    "(The door opens)"
    show kutri neutralcustomer at charbox
    menu:
        "Hello, we have your order from Chompsie’s!":
            call normalgreeting
        "Good day to you, valued customer! We’re from Chompsie’s Fast Food Restaurant and we’re here to deliver your deeee-licious order!":
            call overenthusiasm
        "Hey there, we’ve got your grub.":
            call chillgreeting
    c "Hand it over now!"
    call givefoodornot
    show jason happy at charbox
    $ persistent.items.remove("foodorder")
    j "Alright, good job completing your first delivery."
    show jason tired at charbox
    j "I hope you won’t need me to accompany you the next time, I already have enough orders to deliver on my own..."
    show jason normal at charbox
    j "Let’s go back to the restaurant now."
    $ persistent.gamestate = 2
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label disaster:
    $ persistent.managerDialogue = 3
    $ persistent.jasonDialogue = 6
    "Oh, looks like she’s talking on the phone..."
    show manager normal at charbox
    m "What? Your order... I see. We’re so sorry. We will get this fixed right away."
    show jason tired at charbox
    j "Uh oh, looks like I’m in trouble again..."
    hide jason
    show manager normal at charbox
    m "There you are..."
    show manager angry at charbox
    m "HOW COULD YOU LET THIS HAPPEN?!?"
    menu:
        "Uhh, let what happen, exactly?":
            call youshouldknow
        "Oh no, has there been another food theft?":
            call youknowit
        "*try to sneak out of the door*":
            call notagoodidea
    m "A customer just called and told me that the food you went out to deliver hasn’t been received..."
    show manager wolf at charbox
    m "Even though the order has been confirmed as so."
    show manager angry at charbox
    m "Care to explain what that’s about?"
    menu:
        "We delivered the order correctly, and I can vouch for Jason! He didn’t do anything!":
            call vouchforjason
        "Uhhhh... If something happened it definitely wasn’t my fault!! Jason probably did it!":
            call blamejason
        "Wait... Maybe the customer is lying?":
            call blamecustomer
    show manager angry at charbox
    m "I don’t know what you two have done to mess this up, but you’ll be fixing it right now!"
    show manager wolf
    m "Take this, and make it absolutely sure it finds its way to our valued customer ASAP."
    $ persistent.items.append("foodorder")
    "New food order added to inventory!"
    show manager wolf at charbox
    m "When you come back, we’ll be talking about this."
    hide manager
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label gonow:
    show manager angry at charbox
    m "Get going. Now."
    hide manager
    window hide
    $ renpy.pause(hard=True)
    return

label confusedjason:
    show jason tired at charbox
    j "I can’t believe this has happened again... Somehow it’s always this same building."
    j "You saw how we handed out the stuff to the person who ordered it, right? I can not comprehend where in that situation the food gets stolen."
    show jason happy at charbox
    j "Even my super-advanced computing chips aren’t enough to wrap my head around this situation."
    menu:
        "That certainly is odd... Let’s see if we can figure something out.":
            call veryodd
        "You probably did some kind of illusion trick and stole the food right in front of my eyes!":
            call stillblamingjason
        "Wow, it’s a mystery... Not a murder mystery, but a burger mystery! I can’t wait to solve it!":
            call burgermystery
    show jason normal at charbox
    j "Anyway. Let’s deliver this order, and get it right this time..."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label checkitagain:
    show jason normal at charbox
    j "Could you check the address board again, just in case?"
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label correctdelivery:
    $ persistent.jasonDialogue = 8
    $ persistent.gamestate = 3
    menu:
        "Knock on the door":
            call asiakaskoputus
        "Ring the doorbell":
            call itworksthistime
    show customer pissed at charbox
    c "Fucking finally! You pretty much ruined my chill movie time with your shitty service."
    c "You can be sure I’m not ordering from you again!"
    menu:
        "We’re so sorry. We promise this will never happen again.":
            call weresosorry
        "It’s not our fault, we don’t know what happened!":
            call notourfault
        "I think you’re the one trying to fool us and get another meal for free!":
            call customercheater
    c "Nothing like this has ever happened when I’ve ordered from other fast food places around here."
    c "I’ll go back to ordering from Crispie’s, thank you very much."
    $ persistent.items.remove("foodorder")
    "Food order removed from inventory!"
    hide customer
    show jason normal at charbox
    j "Please reconsider..."
    "(SLAM)"
    show jason tired at charbox
    j "Welp. There goes another customer. I just don’t know how this keeps happening."
    show jason normal at charbox
    j "From what I’ve observed, it always goes like this: The order is made via call, someone delivers it - "
    j "When the order has been received, we mark it as done on our software, and the customer gets automatically charged for it."
    show jason tired at charbox
    j "When we make it back to the restaurant, there’s an angry customer on the line, complaining that their order hasn’t been delivered."
    j "The manager then makes us deliver a new portion, and the customer acts like we’ve never seen each other before."
    show jason normal at charbox
    j "According to multiple people’s accounts, the customers don’t look any different from what we saw before, except for an occasional change of clothes..."
    j "But like, people change their clothes when they’re home right? That’s normal."
    menu:
        "Maybe... All the customers have identical twins living in the same building?":
            call twinsies
        "What if it’s a giant prank organized by all the residents in this building? Perhaps they have something against your restaurant...":
            call bigprank
        "...I still think it’s you.":
            call sceptic
    show jason normal at charbox
    j "Anyway... We should probably investigate the situation."
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label didyoufindanything:
    show jason normal at charbox
    j "Did you figure out something?"
    menu:
        "Yeah, I think I did.":
            call founditout
        "No, I still have no clue what happened.":
            call noclue
        "Wouldn’t you like to know, burger boy?":
            call burgerboy
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label hackerman:
    scene bgbgbg
    hide click_screen
    show screen hackermanScreen
    "Bitwizard Digital Addressboard. Please input password to access."
    menu:
        "12345":
            call defaultpassword
        "5318008":
            call boobies
        "password":
            call seriously
label welcome:
    show screen hackermanScreentwo
    "Welcome to Bitwizard Digital Addressboard! What would you like to do?"
    call boardmenu
    $ renpy.pause(hard=True)
    return

label justasking:
    call choiceschoices
    $ renpy.pause(hard=True)
    return

label waitwait:
    "(...)"
    "(The door opens)"
    show customer normal at charbox
    c "...What is it?"
    call questions
    $ renpy.pause(hard=True)
    return

label imgood:
    show customer normal at charbox
    c "Alright, bye then."
    window hide
    hide customer
    $ renpy.pause(hard=True)
    return

label sunkeskustelu:
    $ persistent.carguyDialogue = 1
    show carguy worried
    g"Help! Help! My new self-driving car has been stolen!"
    show carguy talking
    g"I can’t believe this... Just when the boss gave me a big enough raise to finally get the car of my dreams..."
    menu:
        "Oh no! Did you see the crime happening?":
            call didyousee
        "Yeah, whatever gramps, I’m in the middle of something else right now!":
            call stillveryrude
        "Ooh, was it the SolMobile model Z-1100 G7? With the LimitedAI from VisdomVorks Industries?":
            call arewethecarguy
    g"I can probably tell you something about the incident, if you have any questions!"
    call firsttheguestions

label didyousee:
    show carguy worried at charbox
    g"Only briefly - I heard the sound of the engine and ran out immediately! Good thing I live on the second floor, I got out in just a moment!"
    return
label stillveryrude:
    show carguy worried
    g"Oh... You look like you’re in a hurry too, perhaps the person you’re looking for is also the same guy who took my car?"
    show carguy normal
    g"Wouldn’t you please at least hear me out on this..."
    return
label arewethecarguy:
    g"Yes, exactly! You’re quite knowledgeable about nowadays technology!"
    return
label firsttheguestions:
    menu:
        "Did you see who stole it?":
            call stealingperson
        "What’s on the register plate?":
            call registerplate
        "Which direction did they go?":
            call directionsfromthecarguy
    return
label stealingperson:
    show carguy worried at charbox
    g "I think it was someone wearing a bright red jacket? I’m sorry I can’t say anything else about the culprit, my eyes aren’t the way they used to be..."
    show carguy normal
    g "Is there anything else you’d like to know?"
    call finallyout

label registerplate:
    show carguy normal at charbox
    g "The register number is L0V3-69. I chose it because my husband’s birthday is on the sixth of september!"
    show carguy normal
    g "Is there anything else you’d like to know?"
    call finallyout

label directionsfromthecarguy:
    show carguy worried at charbox
    g "I think they drove the car towards the main street... They left in quite the hurry, I hope they’re not causing any trouble in the traffic..."
    show carguy normal
    g "Is there anything else you’d like to know?"
    call finallyout

label finallyout:
    menu:
        "Did you see who stole it?":
            call stealingperson
        "What’s on the register plate?":
            call registerplate
        "Which direction did they go?":
            call directionsfromthecarguy
        "Nope, I’m good!":
            call loppukeskustelu

label loppukeskustelu:
    $ persistent.managerDialogue = 4
    show carguy worried at charbox
    g "If you want to chase after them, I think you’ll need your own car... Best of luck on your quest! And I hope I can get my car back unscathed..."
    hide carguy
    show jason happy at charbox
    j "A car huh... You could probably borrow the delivery car back at work, but I’m not sure if the manager would like that..."
    show jason normal at charbox
    j "She’ll prooobably forgive you if you manage to catch the thief stealing our food though?"
    hide jason
    window hide
    $ renpy.pause(hard=True)

label canjasonandihavethecar:
    $ persistent.managerDialogue = 5
    show manager thinking at charbox
    m "Hey, what’s going on?"
    menu:
        "I’m borrowing the car to catch the burger thief!":
           call imborrowing
        "Can I borrow the car to catch the burger thief?":
            call caniborrow
        "Nothing!":
            call nothing

label imborrowing:
    show manager gasp at charbox
    m "Hey, wait! What does that mean! You can’t just do that!"
    "Bye!"
    hide manager
    window hide
    $ renpy.pause(hard=True)
label caniborrow:
    show manager gasp at charbox
    m "Uhh, what? What does that mean? I guess?"
    "Thanks!"
    hide manager
    window hide
    $ renpy.pause(hard=True)
label nothing:
    show manager thinking at charbox
    m "That sounds really suspicious!"
    show manager gasp at charbox
    m "Hey, where are you going?"
    "Gotta go!"
    hide manager
    window hide
    $ renpy.pause(hard=True)

label wherewhere:
    show manager gasp at charbox
    m "Hey, wait a minute!"
    "I have no time!"
    hide manager
    window hide
    $ renpy.pause(hard=True)

label thiswasmissing:
    show jason normal at charbox
    j "Everything that's happening is way too wild..."
    hide jason
    window hide
    $ renpy.pause(hard=True)

label jokutoinenjuttu:
    show carguy normal at charbox
    c "I hope you can find the thief..."
    show carguy talking
    c "And my car of course, hopefully in one piece!"
    hide carguy
    window hide
    $ renpy.pause(hard=True)
