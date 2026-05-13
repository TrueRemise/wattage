label lake:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    play music "bgm_lake.mp3" fadein 1.0 if_changed
    jump lakeskip

label lakeskip:
    # Automatically load background with a smooth transition
    $ current_location = "lake"
    if phase != 3:
        scene bg lake with Fade(0.1, 0, 0.1)
    else:
        scene bg laken with Fade(0.1, 0, 0.1)
        jump lake_at_night
    # --- Event jump logic ---
    jump lakedef

default owl_about_chii_safety_prep = False
default jungle_interaction_20_done = False
default youcanonlygotosanco = False
default youcanonlyrescuechii = False
label lakedef:
    if owl_about_chii_safety and not owl_about_chii_safety_prep:
        show owl default at left
        show watta default at right
        o "Well as I said before"
        o "I'll quickly examine the footprints around here"
        o "Gimme a moment"
        show owl default at slide_out_left
        w "Alright"
        $ renpy.pause(5, hard=True)
        show owl default at slide_in_left
        o "I'm back"
        o "She headed that direction, look for her around there..."
        o "I will go look around the other direction incase she made a detour"
        o "Once you found her, blow this whistle, I will go back"
        w "I see"
        o "Tie this long rope around you, so you can go back incase you are lost"
        o "I can also drag you back incase i found her first."
        w "I see, sounds like it works then"
        o "And remember, be back before 7pm"
        w "Alright"
        o "Tell me when you are ready, I'll wait for the signal"
        "New clickable in Swan Lake unlocked, interact to start the rescue search"
        hide owl
        hide watta
        $ owl_presence = True
        $ owl_about_chii_safety_prep = True
    if jungle_interacting_counter == 20 and not jungle_interaction_20_done:
        show watta default
        w "Chii found, gotta call Owl back"
        show watta blow
        pause 2.0
        show watta default
        w "For now Ill go get help from Sanco i think"
        $ jungle_interaction_20_done = True
        $ youcanonlygotosanco = True
        hide watta
    call screen lake
    return

screen lake:
    if owl_about_chii_safety_prep and not youcanonlygotosanco or owl_about_chii_safety_prep and youcanonlyrescuechii:
        imagebutton:
            xpos 1606
            ypos 0
            auto "images/int/to_jungle_%s.png"
            action Jump("jungle")
    imagebutton:
        xpos 106
        ypos 8
        auto "images/int/owlnest_%s.png"
        action Jump("owlnest")

label owlnest:
    $ current_location = "owlnest"
    play music "bgm_owlnest.mp3" fadein 1.0 if_changed
    if phase != 3:
        scene bg owlnest with Fade(0.1, 0, 0.1)
    else:
        scene bg owlnestn with Fade(0.1, 0, 0.1)
    jump owlnestskip
label owlnestskip:
    call screen owlnest

default owl_presence = True
screen owlnest:
    imagebutton:
        xpos 1300
        ypos 180
        auto "images/int/to_lake_%s.png"
        action If(
            not phase == 3,
            [   
                Jump("lake")
            ],
            Jump("owl_lake_night")
            )
    imagebutton:
        xpos 50
        ypos 207
        auto "images/int/balcony_%s.png"
        action Jump("balcony")
    if owl_presence:
        imagebutton:
            xpos 258
            ypos 217
            auto "images/char_int/owl_owlnest_%s.png"
            action Jump("owl_test")

label balcony:
    $ current_location = "balcony"
    play music "bgm_owlnest.mp3" fadein 1.0 if_changed
    if phase != 3:
        scene bg balcony with Fade(0.1, 0, 0.1)
    else:
        scene bg balconyn with Fade(0.1, 0, 0.1)
    jump balconyskip
label balconyskip:
    call screen balcony

screen balcony:
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("owlnest")
    imagebutton:
        xpos 1078
        ypos 0
        auto "images/int/gear_%s.png"
        action Jump("owl_bridge")

default jungle_first = False
default jungle_tp_ready = False
default jungle_interacting_counter = 0
label jungle:
    $ current_location = "jungle"
    play music "bgm_jungle.mp3" fadein 1.0 if_changed
    scene bg jungle with Fade(0.1, 0, 0.1)
    jump jungleskip
label jungleskip:
    if jungle_interacting_counter == 0:
        jump jungle_interaction_1
    if jungle_interacting_counter == 1:
        jump jungle_interaction_2
    if jungle_interacting_counter == 5:
        jump jungle_interaction_3
    if jungle_interacting_counter == 6:
        jump jungle_interaction_3_i
    if jungle_interacting_counter == 10:
        jump jungle_interaction_4
    if jungle_interacting_counter == 20:
        jump jungle_interaction_5
    if jungle_interacting_counter == 21:
        jump thicket
    call screen jungle

screen jungle:
    imagebutton:
        xpos 99
        ypos 0
        auto "images/int/jungle_1_%s.png"
        action Jump("jungle_counter_increase")
    imagebutton:
        xpos 678
        ypos 0
        auto "images/int/jungle_2_%s.png"
        action Jump("jungle_counter_increase")
    imagebutton:
        xpos 1388
        ypos 0
        auto "images/int/jungle_3_%s.png"
        action Jump("jungle_counter_increase")
    if jungle_tp_ready:
        button:
            at hover_fade
            xsize 300
            ysize 100
            xalign 0.5
            yalign 0.95
            background Solid("#a4383800")
            hover_background Solid("#FFFFFF00")
            action Jump("jungle_counter_reset")
            text "TP BACK":
                size 30
                xalign 0.5
                yalign 0.5
                color "#000000"
                hover_color "#a0721c"

label jungle_counter_increase:
    $ jungle_interacting_counter += 1
    jump jungle
label jungle_counter_reset:
    $ jungle_interacting_counter = 0 
    jump lake

label jungle_interaction_1:
    $ actions_locked = True
    show watta default at right
    show owl speak at left
    o "Okay I set things up"
    o "Good luck on the search"
    w "Okay"
    $ owl_presence = False
    hide watta
    hide owl
    call screen jungle
label jungle_interaction_2:
    w "There is no signal around here, I guess I will have to bruteforce the process"
    hide watta
    call screen jungle
label jungle_interaction_3:
    w "This area is so big"
    w "When will I be able to find her?"
    hide watta
    show bg res5 with Fade(1,0,1)
    w "Huh?"
    show bg res6 with dissolve
    w "Has Owl already found her?"
    w "Should i go back?"
    $ jungle_interacting_counter += 1
    menu:
        w "Should i go back?{fast}"
        "Yes":
            show bg black with Fade(1,0,0)
            "You headed back."
            show bg lake with fade
            show watta default 
            w "Huh?"
            w "Owl?"
            w "He's not here"
            w "Did he head back to his house?"
            hide watta
            call screen lake2
        "No":
            pass
    w "Maybe I should keep looking around in case i find any interesting things"
    jump jungle
label jungle_interaction_3_i:
    w "Should hurry up"
    hide watta
    call screen jungle
label jungle_interaction_4:
    scene bg res1 with Fade (1,0,1)
    w "This is endless"
    w "and is so tiring"
    w "Will i ever be able to find her?"
    show bg res2 with Fade (0.5,0,0.5)
    unknown "{size=-10}watta"
    show bg res3 with dissolve
    w "Im here??"
    show bg res4 with dissolve
    c "Help...{w=0.5} meeeee"
    w "{size=+29}OMG HOLD ON"
    jump chii_rescue_talk
label jungle_interaction_5:
    w "If i remember it correctly, should be this way..."
    scene bg black with Fade(2,0,0)
    $ jungle_interacting_counter = 21
    jump thicket

screen lake2:
    imagebutton:
        xpos 1606
        ypos 0
        auto "images/int/to_jungle_%s.png"
        action Jump("jungle2")
    imagebutton:
        xpos 106
        ypos 8
        auto "images/int/owlnest_%s.png"
        action Jump("owlnest2")
label jungle2:
    w "Guess i'm heading back to it..."
    jump jungle
label owlnest2:
    show bg owlnest with fade
    w "Owl?"
    show watta default
    w "He's not here"
    w "Not answering my messages either"
    w "Oh no"
    w "Should I go look for him then?"
    w "I guess im heading back to the jungle"
    jump jungle
    
### label chii_rescue_talk in chii.rpy

label thicket:
    $ current_location = "thicket"
    play music "bgm_thicket.mp3" fadein 1.0 if_changed
    scene bg thicket with Fade(0.1, 0, 0.1)
    jump thicketskip
label thicketskip:
    if youcanonlyrescuechii:
        jump chii_scissors_rescue
    call screen thicket

default thicket_mushroom_get = False
screen thicket:
    imagebutton:
        xpos 0
        ypos 0
        auto "images/char_int/chii_thicket_%s.png"
        action Jump("chii_thicket_interact")
    if not thicket_mushroom_get:
        imagebutton:
            xpos 600
            ypos 860
            auto "images/int/mushroom_%s.png"
            action Jump("thicket_mushroom_get")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("thicket_go_back")
        
image test_img = "images/test.png"
image test_tint_red:
    "images/test.png"
    matrixcolor TintMatrix("#ff0000")

image test_tint_green:
    "images/test.png"
    matrixcolor TintMatrix("#00ff00")

image test_tint_blue:
    "images/test.png"
    matrixcolor TintMatrix("#0000ff")

image test_tint_white_that_does_nothing:
    "images/test.png"
    matrixcolor TintMatrix("#ffffff")   # no tint

image test_tint_half_red:
    "images/test.png"
    matrixcolor TintMatrix("#ff8080")   # lighter red tint

image test_tint_dark_red:
    "images/test.png"
    matrixcolor TintMatrix("#800000")   # darker red
image test_sat_0:
    "images/test.png"
    matrixcolor SaturationMatrix(0.0)   # grayscale

image test_sat_half:
    "images/test.png"
    matrixcolor SaturationMatrix(0.5)

image test_sat_1:
    "images/test.png"
    matrixcolor SaturationMatrix(1.0)

image test_sat_2:
    "images/test.png"
    matrixcolor SaturationMatrix(2.0)

image test_sat_3:
    "images/test.png"
    matrixcolor SaturationMatrix(3.0)
image test_bright_negfull:
    "images/test.png"
    matrixcolor BrightnessMatrix(-1)
image test_bright_neghalf:
    "images/test.png"
    matrixcolor BrightnessMatrix(-0.5)

image test_bright_0:
    "images/test.png"
    matrixcolor BrightnessMatrix(0.0)

image test_bright_half:
    "images/test.png"
    matrixcolor BrightnessMatrix(0.5)

image test_bright_1:
    "images/test.png"
    matrixcolor BrightnessMatrix(1.0)
image test_combo_1:
    "images/test.png"
    matrixcolor TintMatrix("#32a1ef") * SaturationMatrix(1.5)

image test_combo_2:
    "images/test.png"
    matrixcolor SaturationMatrix(0.0) * BrightnessMatrix(0.2)

image test_combo_3:
    "images/test.png"
    matrixcolor TintMatrix("#ff29c9") * BrightnessMatrix(0.2)

image test_combo_4:
    "images/test.png"
    matrixcolor SaturationMatrix(2.0) * BrightnessMatrix(-0.2)
screen matrix_test():

    default index = 0

    $ tests = [
        ("test_img", "None"),

        # Tint
        ("test_tint_red", 'TintMatrix("#ff0000")'),
        ("test_tint_green", 'TintMatrix("#00ff00")'),
        ("test_tint_blue", 'TintMatrix("#0000ff")'),
        ("test_tint_white_that_does_nothing", 'TintMatrix("#ffffff")'),
        ("test_tint_half_red", 'TintMatrix("#ff8080")'),
        ("test_tint_dark_red", 'TintMatrix("#800000")'),

        # Saturation
        ("test_sat_0", "SaturationMatrix(0.0)"),
        ("test_sat_half", "SaturationMatrix(0.5)"),
        ("test_sat_1", "SaturationMatrix(1.0)"),
        ("test_sat_2", "SaturationMatrix(2.0)"),
        ("test_sat_3", "SaturationMatrix(3.0)"),

        # Brightness
        ("test_bright_negfull", "BrightnessMatrix(-1)"),
        ("test_bright_neghalf", "BrightnessMatrix(-0.5)"),
        ("test_bright_0", "BrightnessMatrix(0.0)"),
        ("test_bright_half", "BrightnessMatrix(0.5)"),
        ("test_bright_1", "BrightnessMatrix(1.0)"),

        # Combined
        ("test_combo_1", 'TintMatrix("#ffcccc") * SaturationMatrix(1.5)'),
        ("test_combo_2", 'TintMatrix("#ccccff") * SaturationMatrix(0.0)'),
        ("test_combo_3", 'TintMatrix("#aaffff") * BrightnessMatrix(0.3)'),
        ("test_combo_4", 'SaturationMatrix(2.0) * BrightnessMatrix(-0.3)'),
    ]
    $ current_img, current_code = tests[index]

    add current_img xalign 0.5 yalign 0.45

    frame:
        xalign 0.5
        yalign 0.9
        background "#00000000"
        padding (15, 10)

        text current_code:
            color "#000000"
            size 30
            font "DejaVuSans.ttf"
    frame:
        xalign 0.5
        yalign 0.83
        background "#00000000"
        padding (15, 10)

        text current_img:
            color "#000000"
            size 100
            font "DejaVuSans.ttf"


    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action SetScreenVariable("index", (index - 1) % len(tests))

    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action SetScreenVariable("index", (index + 1) % len(tests))
label chii_thicket_interact:
    show chii cryj
    #c "Go and save the world Watta"
    c "TintMatrix(col) is simply just multiplying colors"
    c "SaturationMatric(sat) is Gray_image + color*sat (sat from 0 to 1)"
    c "BrightnessMatrix(brg) is just linear add/sub of the col channels"
    hide chii
    show bg white
    call screen matrix_test()
    jump thicketskip
label thicket_mushroom_get:
    w "First time seeing this kind of mushroom, better get some"
    "You got mushroom."
    $ thicket_mushroom_get = True
    $ item_add("Mushrooms")
    jump thicketskip
label thicket_go_back:
    if not jungle_interacting_counter == 21:
        menu:
            "In case you don't know, this will move you back to the lake, not any new scene."
            "Y":
                $ jungle_interacting_counter = 20
                jump lake
            "N":
                jump thicketskip
    else:
        jump lake