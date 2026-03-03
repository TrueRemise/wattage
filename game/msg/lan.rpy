# Example default options
default bar_options = {
    "Menu": "lan_menu",
    "Arcade": "technical",
    "Gamble": "blackjack_test",
    "Chitchat": "lan_talk",
    "Leave": "lan_byebye",
}
init python:
    def hex_to_rgb(hex_str):
        return int(hex_str[1:3], 16), int(hex_str[3:5], 16), int(hex_str[5:7], 16)

    def rgb_to_hex(r, g, b):
        return "#%02x%02x%02x" % (r, g, b)
    
    def lerp_color(start_hex, end_hex, t):
        """
        t = 0.0 -> start color, t = 1.0 -> end color
        """
        r1, g1, b1 = hex_to_rgb(start_hex)
        r2, g2, b2 = hex_to_rgb(end_hex)
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        return rgb_to_hex(r, g, b)

screen bar_screen():
    tag bar_sub
    modal True
    zorder 95

    vbox:
        spacing 50
        xalign 0.4
        yalign 0.25

        if bar_options:
            $ shift = 0
            for name, target_label in bar_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#BA5AC8", "#E35B97", t)
                button:
                    at hover_fade
                    xsize 820
                    ysize 70
                    xalign 0
                    xoffset -shift
                    background Solid("#FFFFFF00")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)

                    text name:
                        size 120
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(10, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Bar.ttf"

                $ shift += 30


default lan_first_talk_done_stage = 0
default lan_talked_on_island = False

image rng flashing:
    "bg/bg rng_blue.png"
    pause 0.6593
    "bg/bg rng_red.png"
    pause 0.6593
    repeat
image lan_mouth_talk:
    "char_int/lan_mouth.png"
    pause 0.12
    "char_int/lan_mouth2.png"
    pause 0.12
    repeat

image mouth_rest = "lan_mouth"
image lan_bar:
    Composite(
        (0000, 1000),
        (340, 365), "lan_mouth_talk",
    )

default lan_reset = True
label lan_test:
    $ actions_locked = True
    if lan_save_scum_handling():
        #$ save_lock = False
        jump centre

    $ lan_sync_currency_last_save()

    if rng_from_bj == True:
        jump lan_bj
    elif lan_first_talk_done_stage == 0:
        jump lan_first_talk
    elif is_item_get("Neko's Bracelet"):
        jump lan_neko_bracelet
    elif lan_first_talk_done_stage == 1 and lan_reset == True:
        jump lan_second_talk
    elif sol<10:
        jump lan_second_broke
    else:
        call screen bar_screen

label lan_first_talk:
    if lan_talked_on_island == True:
        show lan_bar
        lan "Oh it's you from the island."
        lan "Welcome! What can I help you with?"
        hide lan_bar
    else:
        show lan_bar
        lan "Oh! A new customer! What can I help you with?"
        hide lan_bar
    show watta sweat at slide_in_left
    w "uhhh..."
    w "I don't know actually..."
    show lan_bar
    lan "Sounds like you're struggling with life, then you're at the right place!"
    hide lan_bar
    w "..."
    show lan_bar
    lan "Nothing can beat the stress-filled mind better than a glass of Maracerumbe, or a tint of Exquelacha on your tongue, everything here is top quality!"
    lan "Once you are satisfied with your drinks you can try out our new cash-making arcade games."
    lan "Totally no rng, only skill based ✅"
    lan "If you want to talk about rng though..."
    hide lan_bar
    w "{i}Well I don't want to, but leaving now might be a little bit rude won't it?"
    if sol<10:
        show lan_bar
        lan "Since you are new here I'll tell you this"
        w "Huh?"
        show watta upset
        lan "We are not really fond of broke people here..."
        lan "So please leave and come back when you are a little bit hmmm richer."
        hide lan_bar
    show watta sweat at slide_out_left
    $ lan_first_talk_done_stage = 1
    call screen bar_screen
    jump lan_test

label lan_second_talk:
    if sol<10:
        label lan_second_broke:
        show lan_bar
        lan "I can see thru you mf, I see you have less than 10 sol..."
        lan "In which case you can't do anything here because everything requires you to have at least 10, you get me?"
        lan "Even talking to me cost more than 10."
        lan "That's a joke but that's also my idea broker."
        lan "Your punishment will be to read this whole long ass dialogue everytime you come here penniless."
        lan "Comeback when you have at least 10."
        lan "Broker"
        hide lan_bar
        call screen bar_screen
    else:
        show lan_bar
        lan "Hello again! What brings you here today?"
        lan "A drink? Arcade? Or to .{w=0.2}.{w=0.2}.{w=0.2} gamble it all?"
        hide lan_bar
        call screen bar_screen

label lan_skip_to_bar_screen:
    $ renpy.block_rollback()
    call screen bar_screen

label lan_byebye:
    $ actions_locked = False
    #$ save_lock = False
    if sol < 10:
        show lan_bar
        lan "Get the hell outta here broker"
        hide lan_bar
        $ lan_on_leave()
        jump centre
    elif lan_reset == True:
        show lan_bar
        lan "Cya!"
        hide lan_bar
        $ lan_reset = False
        $ lan_on_leave()
        jump centre
    else:
        $ lan_on_leave()
        jump centre
label technical:
    "In development"
    jump lan_skip_to_bar_screen

label lan_talk:
    if sol <10:
        show lan_bar
        lan "Guess I can be a little bit softer when it comes to this..."
        lan "Broker"
        hide lan_bar
        call screen bar_chat_screen
    else:
        show lan_bar
        lan "What can I help you with?"
        hide lan_bar
        call screen bar_chat_screen

label lan_talk_skip:
    call screen bar_chat_screen

default bar_chat_options = {
    "Who are you?": "lan_who",
    "What is this place?": "lan_where",
    "*Flirt": "lan_flirt",
    "THIS IS A ROBBERY!!": "lan_robbery",
    "Back": "lan_skip_to_bar_screen",
}
screen bar_chat_screen():
    tag bar_sub
    modal True
    zorder 95

    vbox:
        spacing 50
        xalign 0.4
        yalign 0.25

        if bar_options:
            $ shift = 0
            for name, target_label in bar_chat_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#BA5AC8", "#E35B97", t)
                button:
                    at hover_fade
                    xsize 820
                    ysize 70
                    xalign 0
                    xoffset -shift
                    background Solid("#FFFFFF00")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)

                    text name:
                        size 80
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(10, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Bar.ttf"

                $ shift += 30


label lan_who:
    if sol < 10:
        show lan_bar
        lan "I'm Flan, the founder of Lan Co., specializing in entertainment and services."
        lan "You clearly know how tedious it is to operate something like this, while following administrative procedures and paperwork regulations for this cornered industry."
        lan "But just sit back and enjoy, this place is far from danger- I got some irl tricks that get the job done..."
        lan "and don't worry about us stealing from you, we're pretty clean..."
        lan "Consider it a dream come true."
        lan "No dream for you tho broker"
    else:
        show lan_bar
        lan "I'm Flan, the founder of Lan Co., specializing in entertainment and services."
        lan "You clearly know how tedious it is to operate something like this, while following administrative procedures and paperwork regulations for this cornered industry."
        lan "But just sit back and enjoy, this place is far from danger- I got some irl tricks that get the job done..."
        lan "and don't worry about us stealing from you, we're pretty clean..."
        lan "Consider it a dream come true."
    $ notebook_unlock("Flan")
    hide lan_bar
    jump lan_talk_skip


label lan_where:
    if sol < 10:
        show lan_bar
        lan "This is one of the \"rng money changer\" buildings across the city, with me being the one directly running it."
        lan "Why the funny name you ask?"
        lan "Nothing too complicated I just want the name to be simple and self-explanatory, which you can already tell what you are in for..."
        lan "Gambling"
        lan "Anyways, no casino or anything grand like that, only \"family friendly\" games are allowed~"
        lan "We have a legal bar, a legal arcade aisle and a legal gambling aisle, all legal btw."
        lan "Use your money wisely it's not really our responsibilty if you get in big trouble."
        lan "Think before spending."
        lan "Oh wait you clearly did not think before spending"
        lan "Look at you, you broke as hell now mf"
    else:
        show lan_bar
        lan "This is one of the \"rng money changer\" buildings across the city, with me being the one directly running it."
        lan "Why the funny name you ask?"
        lan "Nothing too complicated I just want the name to be simple and self-explanatory, which you can already tell what you are in for..."
        lan "Gambling"
        lan "Anyways, no casino or anything grand like that, only \"family friendly\" games are allowed~"
        lan "We have a legal bar, a legal arcade aisle and a legal gambling aisle, all legal btw."
        lan "Use your money wisely it's not really our responsibilty if you get in big trouble."
        lan "Think before spending."
    $ notebook_unlock("Flan")
    hide lan_bar
    jump lan_talk_skip


label lan_flirt:
    if sol < 10:
        show lan_bar
        lan "This is a bar, not a place to insult people"
        lan "Take care of your wallet first"
        lan "Worthless mf"
        lan "Get the hell out"
        hide lan_bar
        jump lan_talk_skip
    elif sol < 10000:
        show lan_bar
        lan "What are you thinking, flirting this old grandma?"
        lan "There are a lot more things to do out there, don't spend your time with someone like me."
        lan "But maybe flirting me again and again will work out?"
        hide lan_bar
        pause 5.0
        show lan_bar
        lan "Nah it won't don't try it"
        lan "If you give me 10000 however..."
        hide lan_bar
        jump lan_talk_skip
    else: 
        show lan_bar
        lan "You are not real..."
        lan "That was a joke."
        lan "Take it easy..."
        hide lan_bar
        jump lan_talk_skip

label lan_robbery:
    if sol < 10:
        show lan_bar
        lan "Pfff"
        lan "I might actually believe it."
        lan "You are so broke I would believe you would do this"
        lan "Good job"
        lan "Now get the hell out"
        hide lan_bar
        jump lan_talk_skip
    else:
        show lan_bar
        lan "This is 25 dawg."
        lan "Grow up."
        lan "You don't want me to stuff your ass with this old Marambe bottle now do you?"
        hide lan_bar
        jump lan_talk_skip

label lan_bj:
    show lan_bar
    lan "Did you regret your choice?"
    hide lan_bar
    $ rng_from_bj = False
    jump lan_skip_to_bar_screen

default blackjack_first_time = True
label blackjack_test:
    if sol < 10:
        jump lan_broke
    elif blackjack_first_time:
        stop music fadeout 0.5
        play music "bgm_tutorial.mp3" fadein 1.0  volume 0.4
        scene bg bj with Fade(1, 0, 1)
        show bg bj at whiten_lesser
        show flan smirk at slide_in_right
        lan "Alright fellas!"
        lan "Heard you're new here..."
        lan "I will give you a briefing on how this game works."
        show flan default
        lan "This is WhiteLiar, the rules are simple."
        lan "You both start with 2 cards, you can choose to hit for more cards or stand, it's up to you"
        show flan close
        lan "Who get the closest to 21 after both stood will win."
        lan "Be careful not to be too greedy or else you'll get more than 21."
        lan "In that case it's a bust and you lose no matter how close you are to 21, of course if both lose it's a tie"
        show flan smirk
        lan "The difference between WhiteLiar and BlackJack tho, each one of you will take turn to draw a card until someone stands,"
        lan "The other will continue to hit until they also stand. But here's the catch."
        show flan close
        lan "You are forced to stand when you bust, but you won't tell anyone that you busted, so that they won't know if it's safe to stop yet."
        lan "That's the main point of lying, but not literally lying, in this game."
        show flan default
        lan "Have fun playing, and remember..."
        show flan close
        lan "Think before spending!"
        lan "Oh ye one thing you can quit the game mid-way with a small fee of 20 Sol, do it when you feel like you are about to lose or you want to change your bet."
        lan "Don't worry it won't be considered cheating here, at least when you pay your fee hehe."
        show flan malicious at slide_out_right
        lan "Later"
        hide flan
        "Each 3 games on the same day will cost 1 of your action, and yes refreshing the game doesn't count."
        "If the bet is 0 you can safely play the game forever without taking actions."
        "The number of tries left until action taken will be shown on the top left corner of the screen after you won a game."
        scene bg bj
        stop music fadeout 0.5
        play music "bgm_blackjack.mp3" fadein 1.0 volume 0.4
        $ blackjack_first_time = False
        jump blackjack_bet
    else:
        stop music fadeout 0.5
        play music "bgm_blackjack.mp3" fadein 1.0 volume 0.4
        jump blackjack_bet

label lan_broke:
    show lan_bar
    lan "Brokeass mf what do you think you can do here without money?"
    lan "Come back when you have at least 10."
    hide lan_bar
    jump lan_skip_to_bar_screen


label lan_menu:
    call screen bar_item_screen
default bar_items = [
    {
        "name": "Nrg Cocktail",                # internal name
        "price": "50",               # price text
        "desc": "We drink literal energy now huh?",  # description
        "effect": "+1 action",  # description
        "image": "energy",      # normal image
    },
    {
        "name": "Rng Cocktail",                 
        "price": "30",                
        "desc": "Can't be rng money changer without rng.",
        "effect": "50/50 chance of getting nothing or 50 Sol.",
        "image": "rng",
    },
    {
        "name": "Nrg Cocktail2",                # internal name
        "price": "50",               # price text
        "desc": "We drink literal energy now huh?",  # description
        "effect": "+1 action",  # description
        "image": "energy",      # normal image
    },
] 
default bar_buy_text = "Buy"
default bar_buy_color = "#ffffff"
transform hover_up:
    on hover:
        easein_cubic 0.30 yoffset -20
        pause 2
        easeout_cubic 5 yoffset 0
        repeat
    on idle:
        ease_cubic 0.1 yoffset 0
transform bar_swipe_left:
    easein_cubic 0.30 xoffset 840
transform bar_swipe_right:
    easein_cubic 0.30 xoffset -820
screen bar_item_screen():

    if bar_buy_text != "Buy":
        timer 0.5 action SetVariable("bar_buy_text", "Buy")
        timer 0.5 action SetVariable("bar_buy_color", "#ffffff")
    default hovered_item = None    # screen-level variable
    add "bg/bar/bar_menu.png":
        xpos -800
        yalign 0.5
        at bar_swipe_left

    add "bg/bar/bar_menu2.png":
        xpos 1800
        yalign 0.94
        at bar_swipe_right
    frame:
        xpos -720
        yalign 0.31
        background None
        at bar_swipe_left
        hbox:
            xalign 0.9
            yalign 0.3
            spacing 50
        # Layer for items
            for i, item in enumerate(bar_items):
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5
                    frame:
                        xsize 200
                        ysize 200
                        xalign 0.5
                        yalign 0.5
                        background None
                        imagebutton:
                            xalign 0.5
                            yalign 1.0
                            idle "bg/bar/bar_%s.png" % item["image"]
                            hover "bg/bar/bar_%s.png" % item["image"]
                            at hover_up
                            action Function(bar_try_buy_item, item["name"], int(item["price"]))

                            hovered SetScreenVariable("hovered_item", item)
                            unhovered SetScreenVariable("hovered_item", None)
                    # Price below
                    text "[item['name']]":
                        xalign 0.5
                        yalign 1.2
                        size 30
                        color "#ffffff"
                        font "Bar.ttf"
        
    frame:
        xpos -720
        yalign 0.9
        background None
        at bar_swipe_left
        hbox:
            spacing 140
            xalign 0.2
            yalign 0.9

            button:
                xsize 180
                ysize 80
                xalign 0.5
                yalign 0.9
                background Solid("#00000000")
                hover_background Solid("#FFFFFF00")
                action [Jump("lan_skip_to_bar_screen")]

                text "Exit":
                    size 60
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#a127ff"
                    font "Bar.ttf"
            fixed:
                xsize 80
                ysize 80
                frame:
                    xalign 0.7
                    yalign 0.68
                    background "#ff545400"
                    text "[sol]":
                        xalign 0.5
                        yalign 1.2
                        size 60
                        color "#ffffff"
                        font "Bar.ttf"
            button:
                xsize 280
                ysize 80
                xpos 140
                yalign 0.9
                background Solid("#00000000")
                hover_background Solid("#FFFFFF00")
                action Function(bar_try_buy_item, item["name"], int(item["price"]))

                if hovered_item:
                    text bar_buy_text:
                        size 60
                        xanchor 1.0
                        yalign 0.5
                        color bar_buy_color
                        font "Bar.ttf"
    
    if hovered_item:

        frame:
            background "#ffffff00"
            xpos 755
            ypos 730
            xsize 1350
            ysize 380

            fixed:
                xalign 0.5
                # Item Name (fixed at 50px from top)
                text (hovered_item["name"] + " (" + hovered_item["price"] + ")"):
                    xalign 0.5
                    size 70
                    color "#ffffff"
                    font "Bar.ttf"
                    ypos 0   # ← FIXED POSITION

                # Description (fixed lower)
                text hovered_item["desc"]:
                    xalign 0.5
                    size 33
                    color "#b6b6b6"
                    font "Bar.ttf"
                    ypos 90   # ← FIXED POSITION
                # Description (fixed lower)
                text hovered_item["effect"]:
                    xalign 0.5
                    size 35
                    color "#ff97f1"
                    font "Bar.ttf"
                    ypos 180   # ← FIXED POSITION
init python:
    import random
    def bar_item_sold(name, price):
        global bar_buy_text, bar_buy_color
        global sol, action
        bar_buy_text = "Bought"
        bar_buy_color = "#e53eff"
        sol_lose(price)
        if name == "Rng Cocktail":
            roll = random.randint(1, 2)
            if roll == 1:
                sol_add(50)
        if name == "Nrg Cocktail":
            action_add()
        lan_sync_currency_last_save()
        renpy.block_rollback()
    def bar_item_not_enough(name, price):
        global bar_buy_text, bar_buy_color
        global sol
        bar_buy_text = "Get Out"
        bar_buy_color = "#ff3e3e"
    def bar_try_buy_item(name, price):
        global sol
        if sol >= price:
            renpy.play("sfx/purchase.mp3")
            renpy.notify(f"Bought {name}!")
            bar_item_sold(name, price)
        else:
            renpy.play("sfx/bet_select.mp3")
            renpy.notify(f"Can't afford {name}!")
            bar_item_not_enough(name, price)

default lan_neko_bracelet_repeat = False
label lan_neko_bracelet:
    if lan_neko_bracelet_repeat == False:
        show lan_bar
        lan "Is that what I think it is?"
        lan "You got your hands on a great fortune"
        lan "That might seem like a normal bracelet, but for a big Neko fan? That would be something worth dying for."
        lan "I'd buy that one for 1000 sol, how's that sound?"
        hide lan_bar
    else:
        show lan_bar
        lan "Did you change your mind?"
        hide lan_bar
    menu:
        "Sold!":
            show lan_bar
            lan "Pleasure doing business with you."
            hide lan_bar
            $ sol_add(1000)
            $ lan_sync_currency_last_save()
            $ item_remove("Neko's Bracelet")
        "Nuh uh":
            show lan_bar
            lan "Holding onto it dearly I see."
            lan "Well I can't really blame you."
            lan "I myself only care about its worth so I'm no better"
            lan "But if you ever change your mind... you know who to seek"
            hide lan_bar
            $ lan_neko_bracelet_repeat = True
    jump lan_skip_to_bar_screen


label lan_save_scum_context:
    show rng flashing
    hide watta
    show lan_bar
    $ renpy.block_rollback()
    lan "Hey"
    $ renpy.block_rollback()
    lan "I will not tolerate save scumming."
    hide lan_bar
    w "But I..."
    show lan_bar
    lan "Reloading a save to get better luck? Nice try diddy"
    lan "If you don't want me to call the cop on you, give me a little bit of bribe won't ya"
    lan "50 sol would be enough"
    lan "Now get the hell out"
    $ sol_lose(50)
    $ lan_first_talk_done_stage = 1
    hide lan_bar
    $ save_scum = False
    $ lan_on_leave()
    jump centre
