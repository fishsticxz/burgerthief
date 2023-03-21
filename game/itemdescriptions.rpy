label sankydescription:
    "It’s smartbedTM, an electronic bed with an AI that takes its user’s lifestyle into account."
    "It’s got... quite the personality as well."
    $ renpy.pause(hard=True)

label nappisdescription:
    "It’s your “on the go coder’s holo screen keyboard”! It’s probably trying too hard to sound cool and hip."
    "Like the name implies, a little holographic screen can be projected from it."
    $ renpy.pause(hard=True)

label ovidescription:
    "That's your front door! Did you remember the keys?"
    $ renpy.pause(hard=True)

label keysdescription:
    "Those are your keys! Don't forget them!"
    $ renpy.pause(hard=True)

label kylttidescription:
    "So, Chompsie's huh... The place doesn’t look too hot from the outside, I hope the inside is better "
    $ renpy.pause(hard=True)

label tyoovidescription:
    "Chompsie's front door! We're open!"
    $ renpy.pause(hard=True)

label jasondescription:
    "The most tired looking android you've ever seen."
    $ renpy.pause(hard=True)

label managerdescription:
    "A formidable looking lady - judging from the sharp teeth and the coarse looking hair, she's probably a fangiel"
    $ renpy.pause(hard=True)

label weststreetdoordescription:
    "Whoa! It's an automatic door! It doesn't really look like that from the outside."
    $ renpy.pause(hard=True)

label tvdescription:
    if persistent.gamestate <= 3:
        "...and now, for the weather. It’s going to be another hot summer day. Beware of overheating, keep your AC’s on!"
    else:
        "There’s something wild happening right now on the main street!"
        "Someone has stolen a smart car and is now driving it recklessly through the city center, witnesses report."
        "Does this person even have a driver’s license? Our reporters are on the spot following the situation unfold live!"
    $ renpy.pause(hard=True)

label autodescription:
    "That’s the restaurant’s delivery car. It looks like it’s seen better days..."
    $ renpy.pause(hard=True)

label addressboarddescription:
    "It’s a digital address board! They use it to easily keep track of people moving in and out of the building."
    "It can be swiftly updated with a few clicks!"
    if persistent.gamestate == 3:
        "Maybe I could use something to access it?"
    $ renpy.pause(hard=True)

label hissidescription:
    "is a lift"
    $ renpy.pause(hard=True)

label kutriovidescription:
    "It’s apartment number 64"
    $ renpy.pause(hard=True)

label noticedescription:
    "“Important notice! For the last time, stop shitting in the laundry room! I’ll catch you next time! -Janitor”"
    "What in the world is going on in here..."
    $ renpy.pause(hard=True)

label hallplantdescription:
    "Wait... Is this one made of plastic?"
    $ renpy.pause(hard=True)

label asiakasovidescription:
    "asiakkaan ovi"
    $ renpy.pause(hard=True)

label traakkidescription:
    "Dracaena marginata! A dragon tree."
    "It has a cool name, and is surprisingly easy to take care of."
    "I’ve had it for 3 years and it’s still alive! An accomplishment for sure."
    $ renpy.pause(hard=True)

label nayttodescription:
    "I’ve been struggling with this code for a while now... It’s driving me nuts."
    $ renpy.pause(hard=True)

label kaihdindescription:
    "...I should really get those fixed."
    $ renpy.pause(hard=True)

label wsautodescription:
    "It’s someone’s self driving smartcar. It looks expensive!"
    $ renpy.pause(hard=True)

label tiretrackdescription:
    "Someone left here in a hurry..."
    $ renpy.pause(hard=True)

label posterdescription:
    "A limited edition ZK Ultra SuperStar poster..."
    $ renpy.pause(hard=True)

label konedescription:
    "There are so many screens!"
    "There are at least two different anime sites open... And some code."
    $ renpy.pause(hard=True)

label trashdescription:
    "Wow... It's so filthy in here."
    "The trash can is absolutely filled with what looks like burger wrappers from Chompsie’s..."
    $ renpy.pause(hard=True)

label ikkunarikkidescription:
    "They just jumped straight trough!"
    "All this for burgers?"
    "That must've hurt..."
    $ renpy.pause(hard=True)

label johtodescription:
    "How many things have been plugged here and how has it not caught fire?"
    "If anything it's at least a fire hazard... Wait is that spilled soda!?"
    $ renpy.pause(hard=True)

label gamerchairdescription:
    "That’s the most disgusting gamer chair I’ve ever seen!"
    "Does this person do anything else besides sit on their ass all day?"
    $ renpy.pause(hard=True)

label patjadescription:
    "I can guess that this bed has never been made... Ever."
    "Wait, is this also a kind of SmartBed?"
    $ renpy.pause(hard=True)

label carguydescription:
    "An extremely worried looking gentleman."
    $ renpy.pause(hard=True)
