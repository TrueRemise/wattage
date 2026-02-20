label district:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_district.mp3" fadein 1.0
    jump districtskip

label districtskip:
    # Automatically load background with a smooth transition
    $ current_location = "district"
    if phase != 3:
        scene bg district with Fade(0.1, 0, 0.1)
    else:
        scene bg districtn with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    if (current_weekday, current_phase) in district_events:
        jump expression district_events[(current_weekday, current_phase)]
    else:
        jump districtdef


define district_events = {
    ("Mon", "Dawn"): "district_ft"
}

label districtdef:
    call screen district
    return
default dist_prologue_done = False
label district_ft:
    if dist_prologue_done == False:
        jump district_ft1
    else:
        jump districtdef
label district_ft1:
    show watta sleepy
    w "Ahh"
    w "We've arrived..."
    w "Due to the upcoming festival I only need to work for the morning shift, then I'm all free."
    w "I wanna visit my friends after this."
    $ dist_prologue_done = True
    hide watta
    jump districtdef
screen district:
    imagebutton:
        xpos 250
        ypos 380
        auto "images/int/work_%s.png"
        action Jump("work")
    if first_work == False:
        imagebutton:
            xpos 1679
            ypos 288
            auto "images/int/distpath_%s.png"
            action Jump("ruins")

image bg work = Movie(play="images/work.webm", loop=True, size=(1920,1080))
label work:
    if first_work == True:
        show watta default
        w "Let's get this over with."
        hide watta
        scene bg work with Fade(0.1,0,0.1)
        $ renpy.pause(2, hard=True)
        $ renpy.pause()  
        scene expression bg_image with Fade(0.1, 0, 0.1)
        show watta cry
        w "Sheesh..."
        hide watta
        if charged == False:
            show watta sweat
            w "Least I got to charge my phone!"
            $ charged = True
        "You got 100 sol"
        $ sol_add(work)
        if work_first_time == False:
            "You only need to work once in the morning right after waking up, the first shift of the day won't cost you actions and it's mandatory."
            "You can work again to get more money (sol), however it takes 3 actions every time you do, so use your time carefully."
            "Alternately you can work remotely through your phone, though it will only give you 25 sol. Costs 1 action as a tradeoff"
            $ work_first_time = True
            $ update_msg_phase("Sanco", "0")
        if first_work == True:
            "You have done your morning shift"
            $ first_work = False
            jump districtskip
    else:
        if phase != 3 or actions_left >2:
            menu:
                "That's what I'm here for!":
                    show watta upset
                    w "...Guess i'll do some overtime."
                    hide watta
                    scene bg work with Fade(0.1,0,0.1)
                    $ renpy.pause(2, hard=True)
                    $ renpy.pause()  
                    scene expression bg_image with Fade(0.1, 0, 0.1)
                    show watta ahh
                    w "Please... no more..."
                    hide watta
                    $ action_done()
                    $ action_done()
                    $ action_done()
                    $ sol_add(work)
                    jump districtskip
                "There was a misinput! MISINPUT! CALMDOWN!":
                    jump districtdef
        else:
            show watta upset
            w "I don't think I can cheese the game this way..."
            hide watta
            jump districtdef

default ruins_first = False
default ruins_first_woogie = False
default ruins_first_sanco = False
default spiralia_direction_noted_noted = False
label ruins:
    $ current_location = "ruins"
    scene bg ruins with Fade(0.1, 0, 0.1)
    jump ruinsskip
label ruinsskip:
    if ruins_first == False:
        w "What is this place?"
        w "There is no map for it?"
        $ ruins_first = True
    if woogie and ruins_first_woogie == False:
        stop music fadeout 0.5
        play music "bgm_woogie.mp3" fadein 1.0
        show watta frown at left
        show woogie inspect at right
        wo "{i}sniff sniff"
        wo "hmm"
        show woogie laugh2 with dissolve
        wo "This is Spiralia Ruins!"
        wo "Once the marvelous Spirali Gatebridge"
        wo "It was built as a gateway to Spiralia itself, where the Queen lives."
        show woogie default
        wo "After the incident, this was turned into nothing but ruins."
        wo "And since the gateway was also of not needed anymore, it was shut off."
        wo "Now ya can only enter Spiralia from the North."
        show woogie laugh at bounce
        wo "I say shut off, but it was just left as it be."
        wo "You can still get to Spiralia this way, it'll just be a big mess of a maze."
        wo "Most of the locals remember how to get there by experience."
        show watta frown at bounced
        w "Well... you're a local aren't you?"
        show woogie default
        wo "I am, but I never went to Spiralia, got no business to do there, so I don't know the way."
        wo "Maybe ya should find yourself someone who knows the way."
        show woogie proud
        wo "Woogler out!"
        show woogie at slide_out_right
        pause 0.5
        w "..."
        hide woogie
        $ ruins_first_woogie = True
    if sanco_quest_acquired == True and ruins_first_sanco == False:
        w "Well this should be the path to Spiralia."
        w "I don't wanna be lost... so..."
        w "I should ask Sanco again for the map."
        $ update_msg_phase("Sanco","ruins_lost")
        $ruins_first_sanco = True
    if spiralia_direction_noted_noted == False:
        if spiralia_direction_noted == True:
            w "Let's see, I can follow the written direction"
            if woogie == True:
                show woogie inspect at right
                wo "Wow ya have it noted down."
                wo "Bring me along won't ya?"
                w "Whatever"
                hide woogie
            $ spiralia_direction_noted_noted = True
            jump ruins_to_spira
    hide watta  
    stop music fadeout 0.5
    play music "bgm_ruins.mp3" fadein 1.0
    call screen ruins
screen ruins:
    imagebutton:
        xpos 80
        ypos 0
        auto "images/int/ruins_1_%s.png"
        action Jump("ruins_input_1")
    imagebutton:
        xpos 420
        ypos 0
        auto "images/int/ruins_2_%s.png"
        action Jump("ruins_input_2")
    imagebutton:
        xpos 780
        ypos 0
        auto "images/int/ruins_3_%s.png"
        action Jump("ruins_input_3")
    imagebutton:
        xpos 1080
        ypos 0
        auto "images/int/ruins_4_%s.png"
        action Jump("ruins_input_4")
    imagebutton:
        xpos 1590
        ypos 0
        auto "images/int/ruins_5_%s.png"
        action Jump("ruins_input_5")
    button:
        at hover_fade
        xsize 300
        ysize 100
        xalign 0.5
        yalign 0.95
        background Solid("#a4383800")
        hover_background Solid("#FFFFFF00")
        action Jump("district")
        text "TP BACK":
            size 30
            xalign 0.5
            yalign 0.5
            color "#000000"
            hover_color "#a0721c"

default spiralia_order = [1,2,3,4,5,4,3,2,1]
default stone_order = [ ]
default ruins_player_progress = []
init python:
    def ruins_input(ruins_code):
        global ruins_player_progress

        ruins_player_progress.append(ruins_code)

        # check current progress = prefix of solution
        expected = spiralia_order[:len(ruins_player_progress)]
        expected2 = stone_order[:len(ruins_player_progress)]

        if ruins_player_progress == expected:
            # completed the full sequence
            if len(ruins_player_progress) == len(spiralia_order):
                ruins_player_progress = []
                renpy.jump("ruins_to_spira")
        elif ruins_player_progress == expected2:
            # completed the full sequence
            if len(ruins_player_progress) == len(stone_order):
                ruins_player_progress = []
                renpy.jump("ruins_to_stone")
        else:
            # wrong input → reset
            ruins_player_progress = [ruins_code]

init python:
    import random

    def generate_stone_order():
        renpy.store.stone_order = [random.randint(1,5) for _ in range(12)]

label ruins_input_1:
    $ruins_input(1)
    scene bg ruins with Fade(0.1, 0, 0.1)
    call screen ruins
label ruins_input_2:
    $ruins_input(2)
    scene bg ruins with Fade(0.1, 0, 0.1)
    call screen ruins
label ruins_input_3:
    $ruins_input(3)
    scene bg ruins with Fade(0.1, 0, 0.1)
    call screen ruins
label ruins_input_4:
    $ruins_input(4)
    scene bg ruins with Fade(0.1, 0, 0.1)
    call screen ruins
label ruins_input_5:
    $ruins_input(5)
    scene bg ruins with Fade(0.1, 0, 0.1)
    call screen ruins

default stonecave_note_read = False
default ruins_to_spira_first = False
label ruins_to_spira:
    if ruins_to_spira_first == False:
        hide screen ruins
        hide screen action_display
        show black with Fade(3, 0, 0)
        stop music fadeout 3
        $ renpy.pause(2, hard=True)
        show screen new_area_unlocked("Spiralia")
        $ renpy.pause(7, hard=True)
        show screen action_display
        $ ruins_to_spira_first = True
        $ adjacent_unlock("district", "spira")
        $ loc_unlock("spira")
    $action_done()
    jump spira
label ruins_to_stone:
    hide screen ruins
    $ stonecave_note_read = False
    scene bg stone cave with Fade(0.1,0,0.1)
    stop music fadeout 0.5
    play music "bgm_railwork.mp3" fadein 2.0
    $ current_location = "stone cave"
    jump stonecaveskip
label stonecaveskip:
    scene bg stone cave
    call screen stonecave

default stonecave_stone_found = False
screen stonecave:
    timer 6 repeat True action SetVariable("stonecave_note_read", False)
    imagebutton:
        xpos 888
        ypos 637
        auto "images/int/cave_note_%s.png"
        action [Play("sound", "sfx/bet_select.mp3"), SetVariable("stonecave_note_read", True)]
    if not stonecave_stone_found:
        imagebutton:
            at stone_moving
            xpos 857
            ypos 250
            auto "images/int/cave_stone_%s.png"
            action Jump("stonecave_stone_cutscene")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("ruins")
    if stonecave_note_read:
        text "A fragment of the monarch, preserved":
            at fade_hold_out
            size 80
            xalign 0.5
            yalign 0.86
            color "#ffffff"
            hover_color "#ffc75e"
            outlines [(1.5, "#ffffff", 0, 0)]
            font "Day.ttf"
transform stone_moving:
    ease 5 yoffset -50
    ease 5 yoffset 0
    repeat
transform fade_hold_out:
    alpha 1
    pause 3
    ease 2 alpha 0.0

label stonecave_stone_cutscene:
    show screen stone_aquired()
    $ renpy.pause(11, hard=True)

    $ stone_add()
    
    hide screen task_aquired
    $ stonecave_stone_found = True
    jump stonecaveskip