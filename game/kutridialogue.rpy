label interrogation:
    call kutridoorchoices from _call_kutridoorchoices

label kutridoorchoices:
    menu:
        "Knock on the door":
            call kutriknock from _call_kutriknock
        "Ring the bell":
            call brokenbelltwo from _call_brokenbelltwo
        "Leave it":
            call butwhy from _call_butwhy

label brokenbelltwo:
    "(...)"
    show jason normal at charbox
    j "Oh... The doorbell in this apartment is broken too. They should really get that fixed."
    hide jason
    call kutridoorchoices from _call_kutridoorchoices_1

label kutriknock:
    "(knock knock knock)"
    show jason normal at charbox
    j "Wait, who’s door is this anyway? What are we doing here-"
    hide jason
    call interrogationcontinues from _call_interrogationcontinues

label interrogationcontinues:
    "Who’s there?"
    menu:
        "Open up, this is the police!":
            call thepolice from _call_thepolice
        "The postman, I have a package you need to sign.":
            call thepostman from _call_thepostman
        "That’s not important, I just wanna talk!":
            call justsomeguy from _call_justsomeguy
    return

label justsomeguy:
    "Hmm... That sounds pretty suspicious, but alright..."
    "(The door opens)"
    show kutri neutral at charbox
    k "Oh! It's you- I mean uhhh, who are you?"
    menu:
        "Ha, so you recognize us! You took the order from us before, didn't you?":
            call trueform from _call_trueform
        "Oh uh, I'm just a temp worker at the burger place down the street, and this is my coworker, Jason.":
            call coworkers from _call_coworkers

label coworkers:
    hide kutri
    show jason normal at charbox
    j "Uhh, hi."
    show kutri neutral at charbox
    k "Right..."
    show kutri worried
    k "So... What do you want from me?"
    menu:
        "I want to catch the pesky thief stealing food from our workplace!":
            call peskythief from _call_peskythief
        "Let's just take it easy, you're not in trouble. Right, Jason?":
            call nottrouble from _call_nottrouble
        "Wait a minute. Is that. A ZK Ultra SuperStar poster on your wall??":
            call metootoo from _call_metootoo

label peskythief:
    show jason normal at charbox
    j "Exactly! That's you, isn't it?"
    show kutri surprised at charbox
    k "..."
    show jason tired
    j "Well?"
    call trueform from _call_trueform_1

label thepolice:
    "Huh? I haven’t done anything! Go away!"
    menu:
        "You’re not the one in trouble, we need your witness account for something that happened. For security reasons, I can’t discuss it here any further.":
            call witnessaccount from _call_witnessaccount
        "I’m afraid I can’t do that. If you don’t open the door right now we’re coming in for you!":
            call comingin from _call_comingin
    show kutri surprisecustomer at charbox
    c "Wait a minute! You’re not from the police, you’re from that burger place!"
    call iamthethief from _call_iamthethief
    return

label iamthethief:
    show kutri neutralcustomer at charbox
    c "I already paid for my order, didn't I? What do you want from me?"
    menu:
        "Well, someone did, but that was not you, was it?":
            call notyou from _call_notyou
        "True, but there's an issue...":
            call littleissue from _call_littleissue
        "I'm not taking any of your bullshit, thief!":
            call nobullshit from _call_nobullshit

label notyou:
    show kutri surprisecustomer at charbox
    c "What a wild accusation! Do you have any proof?"
    call accusations from _call_accusations

label accusations:
    menu:
        "We delivered the correct order a moment ago, and the person we met was definitely not you!":
            call wrongperson from _call_wrongperson
        "Someone had tampered with the addressboard downstairs, and you seem very suspicious!":
            call verysuspicious from _call_verysuspicious
        "Uhhh..... No....":
            call clueless from _call_clueless

label wrongperson:
    show kutri surprisecustomer at charbox
    c "Huh... Pretty sharp of you."
    call shapeshifter from _call_shapeshifter

label verysuspicious:
    show kutri silentcustomer at charbox
    c "......."
    call shapeshifter from _call_shapeshifter_1

label clueless:
    hide kutri
    show jason normal at charbox
    j "What do you mean???"
    hide jason
    show kutri happycustomer at charbox
    c "Heh, that's what I thought."
    hide kutri
    show jason tired at charbox
    j "No, that's not right... We do have something!"
    call accusations from _call_accusations_1

label littleissue:
    show kutri neutralcustomer at charbox
    c "What could that be? Our transaction was fairly pleasant, wasn't it?"
    hide kutri
    show jason tired at charbox
    j "For you it might've been. The real customer wasn't as happy about it."
    hide jason
    show kutri surprisecustomer at charbox
    c "Huh..."
    call shapeshifter from _call_shapeshifter_2
    return

label nobullshit:
    show kutri worriedcustomer at charbox
    c "Uhhhh... Whatever could you mean?"
    hide kutri
    show jason tired at charbox
    j "I don't believe a word of that! Drop the facade already!"
    hide jason
    show kutri silentcustomer at charbox
    c "..."
    call shapeshifter from _call_shapeshifter_3
    return

label shapeshifter:
    c "Fine. You're right, I fooled you."
    call trueform from _call_trueform_2

label trueform:
    show kutri surprised at charbox
    k "Bask in the glory of my true form!"
    hide kutri
    show jason normal at charbox
    j "You're a shapeshifter??"
    hide jason
    show kutri happy at charbox
    k "So I am. And you've all been dancing according to my plan, up until today."
    hide kutri
    show jason normal at charbox
    j "Are you implying you're the one behind all of the stolen orders?"
    hide jason
    show kutri brows at charbox
    k "Yes, that's exactly what I'm saying! And now you've finally figured it out..."
    menu:
        "Why would you do this? Like, what's your motive?":
            call motive from _call_motive
        "Stop talking, thief, I don't need to hear anything more! We'll make you pay!":
            call comingwithus from _call_comingwithus

label motive:
    show kutri surprised at charbox
    k "...Hah, wouldn't you like to know!"
    show kutri happy
    k "As if I would tell you something like that!"
    show kutri flustered
    k "Did you think I'd share some kind of sappy story with you? No way!"
    show kutri brows
    k "Even the thought of it makes me laugh!"
    hide kutri
    show jason tired at charbox
    j "Enough talking!"
    call comingwithus from _call_comingwithus_1

label comingwithus:
    show jason normal at charbox
    j "You've caused enough trouble for me and many other workers."
    show jason tired at charbox
    j "You're coming with us and facing the wrath of our manager firsthand!"
    hide jason
    show kutri surprised at charbox
    k "Actually, I don't think so..."
    "(They pull out a gun)"
    hide kutri
    show jason normal at charbox
    j "What the fuck? Who knew a pesky burger thief would have a gun???"
    menu:
        "Oh, um... Uh Oh!!":
            call uhoh from _call_uhoh
        "Wait, is that a Galacta Blaster? Is it even legal to own those things?":
            call galactablaster from _call_galactablaster
        "...Is that a replica? Or a water gun?":
            call watergun from _call_watergun

label uhoh:
    show kutri happy at charbox
    k "Indeed. Now you just stay there, and don't move..."
    call cooperation from _call_cooperation

label galactablaster:
    show kutri surprised at charbox
    k "It is, and probably not. It's not like I have a permit."
    show kutri brows
    k "You'r pretty smart though, so you probably know what happens when you get on the dangerous side of this thing..."
    call cooperation from _call_cooperation_1

label watergun:
    show kutri surprised at charbox
    k "Well... Is it?"
    menu:
        "Ummm...":
            call ummm from _call_ummm
        "Actually, yes it is.":
            call yesitis from _call_yesitis

label ummm:
    hide kutri
    show jason normal at charbox
    j "Better just give it the benefit of the doubt..."
    hide jason
    show kutri happy at charbox
    k "That's what I thought."
    call cooperation from _call_cooperation_2

label yesitis:
    show kutri worried at charbox
    k "N-no it's not! It's a 100 percent real Galacta Blaster and I'm not afraid to use it!! I swear!"
    call pounce from _call_pounce

label cooperation:
    show kutri brows at charbox
    k "Thanks for your cooperation!"
    call pounce from _call_pounce_1

label pounce:
    k "Anyway... I gotta bounce!"
    "(CRASH)"
    hide kutri
    show jason normal at charbox
    j "...They grew wings and jumped out of the window."
    $ persistent.jasonDialogue = 9
    $ persistent.gamestate = 4
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label thepostman:
    "Oh, alright! Just a moment, I’ll open the door for you..."
    "(The door opens)"
    show kutri neutralcustomer at charbox
    "So, where’s my packag-"
    show kutri worriedcustomer
    "Wait, you’re not the postman! You’re from the burger place!"
    show kutri surprisecustomer at charbox
    "I don’t know what you're doing here, but you definitely don’t have my ZK Ultra SuperStar figure!"
    menu:
        "You're not the same person who we delivered the order to just a moment ago, are you?":
            call soitwasyou from _call_soitwasyou
        "Wait, you know ZK Ultra SuperStar? That’s my favorite show!":
            call metoo from _call_metoo
    return

label soitwasyou:
    show kutri worriedcustomer at charbox
    c "Oh uhhh, whatever could you mean?"
    show kutri happycustomer
    c "You came here to deliver my order before, yes? And that was it!"
    show jason normal at charbox
    j "That sounds... Very suspicious."
    hide jason
    call iamthethief from _call_iamthethief_1
    return

label metoo:
    show kutri happycustomer at charbox
    c "Oh yeah, I’m the number one fan!"
    show kutri neutralcustomer
    c "I have... A couple of posters... And some figurines too! Would you like to see?"
    menu:
        "Yeah sure!":
            call kutrifriendship from _call_kutrifriendship
        "Absolutely not, you might have good taste, but you’re still suspicious!":
            call soitwasyou from _call_soitwasyou_1
    return

label metootoo:
    show kutri happy at charbox
    c "Oh yeah, I’m the number one fan!"
    show kutri smile
    c "I have... A couple of posters... And some figurines too! Would you like to see?"
    menu:
        "Yeah sure!":
            call kutrifriendshiptoo from _call_kutrifriendshiptoo
        "Absolutely not, you might have good taste, but you’re still suspicious!":
            call soitwasyoutoo from _call_soitwasyoutoo
    return

label kutrifriendship:
    show kutri happycustomer
    c "Cool, come in and take a look!"
    hide click_screen
    show screen kutriHuoneScreen
    $ persistent.currentPlace = "kutriHuone"
    menu:
        "Whoa, there's so much stuff! You really are a big fan!":
            call bigfan from _call_bigfan
        "Duuude, is that the limited edition poster??":
            call limitededition from _call_limitededition
        "Hah, I've seen better... You should see MY collection!":
            call mycollection from _call_mycollection
    return

label kutrifriendshiptoo:
    show kutri happy
    c "Cool, come in and take a look!"
    hide click_screen
    show screen kutriHuoneScreen
    $ persistent.currentPlace = "kutriHuone"
    menu:
        "Whoa, there's so much stuff! You really are a big fan!":
            call bigfantoo from _call_bigfantoo
        "Duuude, is that the limited edition poster??":
            call limitededitiontoo from _call_limitededitiontoo
        "Hah, I've seen better... You should see MY collection!":
            call mycollectiontoo from _call_mycollectiontoo
    return

label bigfan:
    show kutri happycustomer at charbox
    c "Haha yeah, I really am! I've been watching it for years, who could've guessed the 6th season would top all of the previous ones!"
    show kutri surprisecustomer
    c "I'm really excited about the spin-off videogame they're releasing next year..."
    call coolguy from _call_coolguy
    return

label bigfantoo:
    show kutri happy at charbox
    c "Haha yeah, I really am! I've been watching it for years, who could've guessed the 6th season would top all of the previous ones!"
    show kutri surprised
    c "I'm really excited about the spin-off videogame they're releasing next year..."
    call coolguycool from _call_coolguycool
    return

label limitededition:
    show kutri happycustomer at charbox
    c "It sure is! I even got it signed by the voice actor at a con!"
    call coolguy from _call_coolguy_1
    return

label limitededitiontoo:
    show kutri smile at charbox
    c "It sure is! I even got it signed by the voice actor at a con!"
    call coolguycool from _call_coolguycool_1
    return

label mycollection:
    show kutri surprisecustomer at charbox
    c "Ooh, I wonder what you could have if it's even better than mine!"
    show kutri neutralcustomer
    c "...Maybe I can come see it sometime?"
    call coolguy from _call_coolguy_2
    return

label mycollectiontoo:
    show kutri surprised at charbox
    c "Ooh, I wonder what you could have if it's even better than mine!"
    show kutri flustered
    c "...Maybe I can come see it sometime?"
    call coolguycool from _call_coolguycool_2
    return

label coolguy:
    show kutri surprisecustomer at charbox
    c "Honestly, you seem like a cool person... I'll tell you a secret."
    c "I'm actually a shapeshifter and a hobbyist hacker. I've been stealing food from that fast food place for months."
    show kutri  worriedcustomer
    c "Somehow, it's kept working out for me..."
    show kutri worried
    k "This is what my true form looks like... Hope you don't freak out."
    menu:
        "Aww, you look just fine! Don't worry about it.":
            call justfine from _call_justfine
        "Wow, you're so cute!":
            call socute from _call_socute
        "HUH... You're a weird looking guy.":
            call weirdlooking from _call_weirdlooking
    show kutri surprised
    k "...You're not going to rat me out, are you? We're like, pals now, right?"
    menu:
        "Of course not! You seem like a nice person, albeit a little misguided...":
            call niceperson from _call_niceperson
        "...That's where you're wrong.":
            call rattingout from _call_rattingout
        "Uh... Jason? What do you think?":
            call jasonthink from _call_jasonthink
    return

label coolguycool:
    show kutri surprised at charbox
    k "Honestly, you seem like a cool person... I'll tell you a secret."
    show kutri worriedcustomer
    k "I'm actually a shapeshifter and a hobbyist hacker. I've been stealing food from that fast food place for months."
    show kutri worried
    k "Somehow, it's kept working out for me..."
    show jason normal at charbox
    j "..."
    show kutri worried
    k "I guess that's the place you guys work at... Sorry."


label niceperson:
    show kutri smile at charbox
    k "Hell yeah! Let's be best friends!"
    show kutri neutral at charbox
    k "...Are you gonna make me stop stealing food though?"
    menu:
        "I'll buy you some food, you don't need to steal!":
            call buysome from _call_buysome
        "No, in fact I'll help you steal even more food! I have insider knowledge of that place!":
            call bestfriends from _call_bestfriends
        "Yeah, if you wanna be friends you'll have to lose the stealing... I'll help you!":
            call nostealing from _call_nostealing

label bestfriends:
    show kutri brows at charbox
    k "Hell yeah!"
    hide kutri
    "You decided to become friends with Kutri and steal food from Chompsie's together."
    "You got fired for being a prime suspect!"
    "Game Over!"

label buysome:
    show kutri smile at charbox
    k "Aww, that's nice of you! Maybe I'll be able to stop stealing then..."
    hide kutri
    "You decided to become friends with Kutri!"
    "The burger thief was never found, as far as the manager knows, but the stealing stopped..."
    "Along with that, Chompsie's gained a new customer!"
    "Good job!"

label nostealing:
    show kutri neutral at charbox
    k "Awww man.... You're no fun!"
    k "I... Guess I can try my best though..."
    hide kutri
    "You decided to become friends with Kutri!"
    "The burger thief was never found, as far as the manager knows, but the stealing stopped..."
    "Good job!"

label rattingout:
    show kutri neutral at charbox
    k "Aww man..."
    call comingwithus from _call_comingwithus_2

label jasonthink:
    show jason normal at charbox
    j "I dunno... This person HAS been stealing food from our restaurant for months now."
    j "I think they need to face some consequences."
    show kutri neutral at charbox
    k "Aww..."
    call comingwithus from _call_comingwithus_3

label justfine:
    show kutri smile at charbox
    k "Hehe, thanks!"
    return

label socute:
    show kutri flustered at charbox
    k "Aww... You didn't have to say that!"
    return

label weirdlooking:
    show kutri neutral at charbox
    k "Hey, I have feelings too!"
    return

label butwhy:
    show jason tired at charbox
    j "Why did we come here, if we’re not going to anything?"
    hide jason
    window hide
    $ renpy.pause(hard=True)
    return

label witnessaccount:
    "I don’t think I’ve seen any crimes happen, I barely leave my house!"
    "But uhhh... If I must, I can give it a look. I doubt I know anything, though..."
    "(The door opens)"
    return
label comingin:
    "Uhh... Are you being serious? I... Guess I’ll have to open it then..."
    "(The door opens)"
    return
