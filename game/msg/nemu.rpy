default nemu_first_talk_done_stage = 0
default nemu_lend_done = False

label nemu_test:
    stop music fadeout 0.5
    play music "bgm_nemu.mp3" fadein 1.0 
    if nemu_first_talk_done_stage == 0:
        jump nemu_first_talk
    elif nemu_first_talk_done_stage == 1:
        jump nemu_second_talk
    elif nemu_first_talk_done_stage == 2:
        $ nemu_lend_done = True
        stop music fadeout 0.5
        play music "bgm_bridge.mp3" fadein 1.0
        jump underbridge
    elif nemu_first_talk_done_stage == 3:
        jump nemu_third_talk
    

label nemu_first_talk:
    show nemu cry at center
    show nemu cry at bounce
    n "Aaarghhh! Another terrible catch today..."
    n "If only I could get better.."
    show nemu shock at slide_to_right
    show watta default at fade_in_left
    n "Oh Watta you surprised me"
    show watta sweat
    w "I'm just wandering around but... you sound like you need some help, Nemu"
    show nemu dried at bounced
    n "Ah! It's nothing! I'm just a little bit short of money to buy a new rod..."
    show watta default
    w "Is how much?"
    show nemu uwu
    n "500 sol... But I only have 300 right now..."
    call is_shaky_choice_disclaimer from _call_is_shaky_choice_disclaimer_1
    call screen nemu_first_lend

label nemu_second_talk:
    show nemu default at right
    show watta default at left
    n "Oh hey it's you again Watta!"
    call screen nemu_first_lend

transform hover_zoom_bounce:
    on hover:
        easein_cubic 0.30 zoom 1.3
        easeout_cubic 0.3 zoom 1
        repeat
    on idle:
        ease_cubic 0.1 zoom 1

screen nemu_first_lend():
    modal True
    frame:
        background Solid("#ffffff00")
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            button:
                at hover_action
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Jump("nemu_sol_check")
                text "Give Nemu 200 Sol":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#ffc75e"
                    outlines [(10, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_zoom_bounce
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("nemu_didnt_help")
                text "DO NOT HELP":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#ff0000"
                    outlines [(10, "#000000", 0, 0)]
                    font "Nemu.ttf"

label nemu_sol_check:
    hide screen nemu_first_lend
    if sol > 200:
        jump nemu_first_lend_succ
    elif sol == 200:
        jump nemu_you_need_more_than_that
    else:
        jump nemu_first_lend_fail

label nemu_first_lend_fail:
    show watta default at bounced
    w "Here you go!"
    show nemu proud
    n "Thank you Watta but-"
    show nemu uwu at bounced
    n "This isn't enough"
    show watta deter
    w "Oops, I think I miscounted-"
    show nemu cry
    n "It's alright Watta, keep the money, I think you need that more than me"
    show nemu cry at bounced
    n "Don't stress yourself over this."
    $ nemu_first_talk_done_stage = 1
    hide nemu
    hide watta
    stop music fadeout 0.5
    play music "bgm_bridge.mp3" fadein 1.0
    jump underbridgeskip    

label nemu_you_need_more_than_that:
    show watta default at bounced
    w "Here you go!"
    show nemu proud
    n "Thank you Watta but-"
    show nemu uwu at bounced
    n "I see that's all of your money"
    show nemu cry
    n "It's alright Watta, keep the money, I think you need that more than me"
    show nemu cry at bounced
    n "Don't stress yourself over this."
    $ nemu_first_talk_done_stage = 1
    hide nemu
    hide watta
    stop music fadeout 0.5
    play music "bgm_bridge.mp3" fadein 1.0
    jump underbridgeskip

label nemu_didnt_help:
    show nemu cry
    n "It's fine I totally understand."
    show nemu cry at bounced
    n "I appreciated it Watta, but I can grind for it on my own!"
    n "Cya!"
    $ nemu_first_talk_done_stage = 1
    hide nemu
    hide watta
    stop music fadeout 0.5
    play music "bgm_bridge.mp3" fadein 1.0
    jump underbridgeskip

label nemu_first_lend_succ:
    show nemu cry
    n "Oh my god thank you so much!"
    show watta smile
    w "No problem"
    show nemu cry at bounced
    n "I will do everything to pay you back Watta"
    n "But for now I have to get my hands on that before it's too late"
    show nemu brat
    n "Oh by the way! Please take this rod as a gift for your trouble!"
    show watta sweat
    w "Oh no you don't need to-"
    show nemu ewe at bounce
    n "PLEASE TAKE IT, AND THESE BAITS TOO! GOODBYE!"
    show nemu uwu at slide_out_right
    show watta wtf
    w "WAIT!"
    show watta upset
    w "OMG"
    if woogie:
        stop music fadeout 0.5
        play music "bgm_woogie.mp3" fadein 1.0
        show woogie squint at right
        wo "{i}oh howly"
        wo "That's a nice looking rod of yers."
        show woogie inspect with dissolve
        wo "Hol on a bit!"
        wo "These water quality."
        wo "{i}slurp slurp"
        show woogie sus with dissolve
        wo "Hence why he can't fish any."
        show watta default
        w "Huh?"
        show woogie default
        wo "This water is too basic."
        show watta frown
        w "Basic?"
        show woogie sus with dissolve
        wo "Ye as in opposite of acidic."
        wo "Seems like a build-up of Ca(OH)2"
        show watta shocked
        w "{cps=40}WHAT THE FU{nw}"
        show woogie laugh at bounce
        wo "This is why he can hardly fish any here, and neither can ya."
        wo "Well I believe the sea at the west are still available for fishing."
        show watta frown
        show woogie default
        wo "Try get your way there and see if we can catch any fishes."
        show woogie proud
        show woogie proud at slide_out_right
        wo "Woogler out!"
        hide woogie
    $ item_add("Fishing Rod")
    $ notebook_unlock("Nemu")
    $ sol -= 200
    $ nemu_first_talk_done_stage = 2
    $ nemu_lend_done = True
    hide nemu
    hide watta
    stop music fadeout 0.5
    play music "bgm_bridge.mp3" fadein 1.0
    $ action_done()
    jump underbridgeskip

default nemu_manhake = False
default nemu_third_talk_done = False
label nemu_third_talk:
    show nemu brat at right
    show watta default at left
    if not nemu_third_talk_done:
        n "Watta!"
        show watta smile
        w "Hello"
        show nemu uwu
        n "Thank you so much for the money last time, I bought a better rod and now I can fish everything!"
        show watta delighted
        w "Wao, happy to hear!"
        show nemu proud
        n "I think this is bringing me fortune, I might open a shop soon at fishing lane."
        n "Fishing lane is just a river ride west of here, you'll find it."
        show nemu default
        n "I will move there soon enough, but for now I need to get my hands on the rare ManHake, that's my current goal."
        show watta hype
        w "Oh nice! Can I help?"
        show nemu uwu
        n "Totally, here are some left-over upgrades, install them on your rod and you'll be able to catch more varieties more easily"
        $ upgrade_rod("maxweight", 5)
        $ upgrade_rod("luck", 10)
        $ upgrade_rod("resilience", 10)
        $ upgrade_rod("size", 10)
        "Your rod is now stronger"
        $ nemu_third_talk_done = True
    elif nemu_manhake:
        show nemu cry
        show watta smile
        n "OMG Watta you caught it for me thank you so much."
        n "Here's the pay"
        $ sol_add(200)
        "You got 200 sol!"
        show nemu proud
        n "Okay now see ya! I'm moving to the new location!"
        show nemu brat
        show watta default
        n "Do you have a map? Oh perfect!"
        extend " Here is the path to the fishing lane, hope to meet you there someday"
        $ nemu_first_talk_done_stage = 4
    else:
        n "Good luck on it Watta!"
    hide nemu
    hide watta
    stop music fadeout 0.5
    play music "bgm_bridge.mp3" fadein 1.0
    jump underbridgeskip


image nemu_mouth_talk:
    "bg/fishing/fish_nemu_speak_1.png"
    pause 0.12
    "bg/fishing/fish_nemu_speak_2.png"
    pause 0.12
    repeat
image nemu_box_talk:
    "bg/fishing/fish_dialogue_1.png"
    pause 0.12
    "bg/fishing/fish_dialogue_2.png"
    pause 0.12
    repeat
image nemu_bar:
    Composite(
        (0000, 1000),
        (190, 40), "nemu_mouth_talk",
        (0, 385), "nemu_box_talk",
    )

default nemu_talking = False
default nemu_talking_bye = False
default nemu_talking_line = None
label nemu_shop:
    stop music fadeout 0.5
    play music "bgm_rod.mp3" fadein 1.0 
    scene fish_nemu with Fade(0.1,0,0.1)
    $ rod_level_preview = rod_level
    python:
        for stat in rod_preview:
            rod_preview[stat] = 0
    call screen rod_screen
default rod_lines = [
    {
        "name": "size",                # internal name
        "desc": "I will fuse materials to enlarge your fly, makes it easier to catch quirky fishes!",  # description
        "height": "0",                # internal name
    },
    {
        "name": "luck",                 
        "desc": "I will bless the fly with the power of love, more kinds of fishes will fall for it!.",
        "height": "0",                # internal name
    },
    {
        "name": "resilience",                # internal name
        "desc": "I will customize the grip with various materials, lessening how shakey it is!",  # description
        "height": "10",                # internal name
    },
    {
        "name": "maxweight",                # internal name
        "desc": "I will empower your line, strengthening its ability to reel bigger fish!",  # description
        "height": "-10",                # internal name
    },
] 
default rod_preview = {
    "size": 0,
    "luck": 0,
    "resilience": 0,
    "maxweight": 0,
}
default upgrade_cost = 50
default rod_level = 0
default rod_level_preview = 0
default rod_sessions_presses = 0
default rod_hold_stat = None
default rod_hold_dir = 0
default rod_hold_ticks = 0

init python:
    ROD_STAT_CAP = 250
    def _rod_upgrade_cost_for_level(level):
        return int(1 + level * 0.6)

    def rod_preview_total_points():
        return sum(rod_preview.values())

    def rod_get_preview_stat_value(stat_name):
        return rod[stat_name] + rod_preview[stat_name]

    def rod_get_upgrade_cost():
        cost = 0
        for lvl in range(rod_level + 1, rod_level_preview + 1):
            cost += _rod_upgrade_cost_for_level(lvl)
        return max(cost, 0)

        if rod_hold_stat is None or rod_hold_dir == 0:
            return

        rod_hold_ticks += 1

        # 0.5s delay before auto-repeat starts (timer runs every 0.02s => 25 ticks)
        if rod_hold_ticks < 25:
            return

        # For the next 2 seconds, apply 1 level every 5 ticks (0.1s).
        # 2 seconds at 0.02s/tick = 100 ticks, so this stage ends at tick 124.
        if rod_hold_ticks < 125 and ((rod_hold_ticks - 25) % 5 != 0):
            return

        if rod_hold_dir > 0:
            rod_preview_increase(rod_hold_stat)
        else:
            rod_preview_decrease(rod_hold_stat)

    def rod_get_upgrade_cost():
        cost = 0
        for lvl in range(rod_level + 1, rod_level_preview + 1):
            cost += _rod_upgrade_cost_for_level(lvl)
        return max(cost, 0)

    def rod_get_level_preview():
        global rod_level, rod_level_preview
        return rod_level_preview

    def rod_can_increase(stat_name):
        next_preview_level = rod_level_preview + 1
        next_total_cost = rod_get_upgrade_cost() + _rod_upgrade_cost_for_level(next_preview_level)
        return sol >= next_total_cost

    def rod_preview_increase(stat_name):
        global rod_level_preview

        if rod_get_preview_stat_value(stat_name) >= ROD_STAT_CAP:
            renpy.play("sfx/bet_denied.mp3")
            renpy.notify("MAX LEVEL REACHED!")
            return
        
        if not rod_can_increase(stat_name):
            renpy.play("sfx/bet_denied.mp3")
            if message:
                renpy.notify(message)
            if is_hold_repeat:
                rod_hold_block_feedback_played = True

        rod_preview[stat_name] += 1
        rod_level_preview += 1

        renpy.play("sfx/bet_select.mp3")



    def rod_preview_decrease(stat_name):
        global rod_level_preview

        if rod_preview[stat_name] <= 0:
            renpy.play("sfx/bet_denied.mp3")
            return

        rod_preview[stat_name] -= 1
        rod_level_preview = max(rod_level, rod_level_preview - 1)
        renpy.play("sfx/bet_select.mp3")


    def rod_confirm_upgrades():
        global sol, rod_level, rod_level_preview

        total_selected = rod_preview_total_points()
        if total_selected == 0:
            renpy.notify("No upgrades selected.")
            return

        total_cost = rod_get_upgrade_cost()
        if sol < total_cost:
            renpy.play("sfx/bet_denied.mp3")
            renpy.notify("Not enough sol!")
            return

        for stat, amount in rod_preview.items():
            rod[stat] = min(rod[stat] + amount, ROD_STAT_CAP)

        sol -= total_cost
        rod_level = rod_level_preview

        for stat in rod_preview:
            rod_preview[stat] = 0

        renpy.play("sfx/rod_upgrade.mp3")
        renpy.notify("Upgrades applied!")

screen rod_screen():
    timer 0.1 action [SetScreenVariable("nemu_talking", True)]
    fixed:
        xsize 600
        xpos 688
        ypos 154

        vbox:
            spacing 35
            xalign 0.0
            yalign 0.0

            # Each stat row
            for line in rod_lines:
                $ name = line["name"]
                $ base = rod[name]
                $ preview = rod_preview[name]
                $ final_val = base + preview
            
                hbox:
                    spacing 55
                    xalign 0.5

                    # Decrease button
                    button:
                        xsize 40
                        ysize 40
                        yalign 0.46
                        background Solid("#ffffff00")
                        action Function(rod_preview_decrease, name)
                        hovered [Function(rod_start_hold, name, -1), SetScreenVariable("nemu_talking_line", line)]
                        unhovered [Function(rod_stop_hold), SetScreenVariable("nemu_talking_line", None)]
                        text "<":
                            yalign 0.5
                            size 55
                            color "#000000"
                            hover_color "#fff019"
                            font "Nemu.ttf"
                            outlines [(1, "#000", 0, 0)]

                    # Number
                    fixed:
                        xsize 120
                        ysize 120
                        text "[final_val]":
                            xalign 0.5
                            yalign 0.5
                            font "Nemu.ttf"
                            size 55
                            color ("#1cc21c" if preview > 0 else "#000000")
                            outlines ([(1.5, "#1cc21c", 0, 0)] if preview > 0 else [(1, "#000", 0, 0)])

                    # Increase button
                    button:
                        xsize 40
                        ysize 40
                        yalign 0.43
                        background Solid("#ffffff00")
                        action Function(rod_preview_increase, name)
                        hovered [Function(rod_start_hold, name, 1), SetScreenVariable("nemu_talking_line", line)]
                        unhovered [Function(rod_stop_hold), SetScreenVariable("nemu_talking_line", None)]
                        text ">":
                            yalign 0.5
                            size 55
                            color "#000000"
                            hover_color "#fff019"
                            font "Nemu.ttf"
                            outlines [(1, "#000", 0, 0)]
    fixed:
        xsize 600
        xpos 845
        ypos 715
        vbox:
            spacing -10
            xalign 0.0
            yalign 0.0
            # Cost Display
            text "[rod_get_level_preview()]" size 55 color "#000000" xalign 0.0 font "Nemu.ttf" outlines [(1, "#000", 0, 0)]
            # Cost Display
            text "[rod_get_upgrade_cost()]" size 55 color "#000000" xalign 0.0 font "Nemu.ttf" outlines [(1, "#000", 0, 0)]
        # Confirm Button
        imagebutton:
            xpos -170
            ypos 120
            auto "bg/fishing/fish_upgrade_%s.png"
            action [Play("sound", "sfx/rod_upgrade.mp3"),Function(rod_confirm_upgrades)]
        imagebutton:
            xpos 118
            ypos 118
            auto "bg/fishing/fish_exit_%s.png"
            action [SetScreenVariable("nemu_talking_bye", True)]


    if nemu_talking:

        timer 3 action [SetScreenVariable("nemu_talking", False)]
        # The mouth animation
        add "nemu_bar" xpos 1260 ypos 200
        frame:
            xpos 1320
            ypos 690
            xsize 480
            ysize 320
            background None
            # The actual text
            text "Hello Watta! Do you want to upgrade your rod???":
                at shakey
                size 50
                color "#000000"
                outlines [(2, "#000")]
                font "Nemu.ttf"
    if nemu_talking_bye:

        timer 0.01 action Function(rod_stop_hold)
        timer 0.01 action [SetScreenVariable("nemu_talking", False)]
        timer 1 action [Jump("lane")]
        # The mouth animation
        add "nemu_bar" xpos 1260 ypos 200
        frame:
            xpos 1320
            ypos 690
            xsize 480
            ysize 320
            background None
            # The actual text
            text "See ya Watta!":
                at shakey
                size 50
                color "#000000"
                outlines [(2, "#000")]
                font "Nemu.ttf"
    if nemu_talking_line:

        timer 0.01 action [SetScreenVariable("nemu_talking", False)]
        # The mouth animation
        add "nemu_bar" xpos 1260 ypos 200
        frame:
            xpos 1320
            ypos 690
            xsize 480
            ysize 320
            background None
            # The actual text
            text nemu_talking_line["desc"]:
                at shakey
                size 50
                color "#000000"
                outlines [(2, "#000")]
                font "Nemu.ttf"
transform shakey:
    block:
        yoffset 1
        pause 0.1
        xoffset 1
        yoffset -1
        pause 0.1
        xoffset -1
        repeat
label _exit_rod_shop:
    $ renpy.pause(2.5)    # wait for goodbye to finish
    hide screen rod_screen
    return
