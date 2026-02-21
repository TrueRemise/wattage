label field:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_field.mp3" fadein 1.0
    jump fieldskip

label fieldskip:
    # Automatically load background with a smooth transition
    $ current_location = "field"
    if phase != 3:
        scene bg field with Fade(0.1, 0, 0.1)
    else:
        scene bg fieldn with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    jump fielddef


label fielddef:
    if woogie and sanco_spiralia_location_woogie_help_toggle:
        stop music fadeout 0.5
        play music "bgm_woogie.mp3" fadein 1.0
        show watta frown at left
        show woogie inspect at right
        wo "{i}sniff sniff"
        wo "hmm"
        show woogie hmm with dissolve
        wo "So ya want to seek Spiralia huh?"
        wo "There are not many ways I know that can help ya get to the area."
        show woogie default
        wo "There is this path from the Monument, but ya can't get in through the main way."
        wo "They only let native people get through."
        show woogie laugh at bounce
        wo "Don't worry, there is still a way."
        if ruins_first_woogie:
            wo "If yaa remember that maze around the district last time, It leads to Spiralia also."
            wo "Better go check it out!"
        else:
            wo "There is some path that lead to it through the district."
            wo "Better go check it out!"
        hide woogie
        hide watta
        $ sanco_spiralia_location_woogie_help_toggle = False
        call screen field
    if field_first == False:
        jump field_ft
    else:
        call screen field
    return
label field_ft:
    show watta default
    w "This place is huge."
    w "If i'm not wrong, that Floralia store over there belongs to Sanco"
    hide watta
    $ field_first = True
    jump fielddef

screen field:
    imagebutton:
        xpos 45
        ypos 0
        auto "images/int/floralia_%s.png"
        action Jump("floralia")
    imagebutton:
        xpos 0
        ypos 230
        auto "images/int/westgate_%s.png"
        action Jump("westgate")
    imagebutton:
        xpos 1790
        ypos 70
        auto "images/int/eastgate_%s.png"
        action Jump("eastgate")


label floralia:
    $ current_location = "floralia"
    stop music fadeout 0.5
    play music "bgm_floralia.mp3" fadein 1.0
    scene bg floralia with Fade(0.1, 0, 0.1)
    jump floraliaskip
label floraliaskip:
    if sanco_first_talk_done_stage == 0:
        jump sanco_test
    call screen floralia

default sanco_presence = True
screen floralia:
    if sanco_presence == True:
        imagebutton:
            xpos 0
            ypos 160
            auto "images/char_int/sanco_floralia_%s.png"
            action Jump("sanco_test")
    imagebutton:
        xpos 1258
        ypos 237
        auto "images/int/floralia_door_%s.png"
        action Jump("field")


label westgate:
    $ current_location = "westgate"
    stop music fadeout 0.5
    play music "bgm_gate.mp3" fadein 1.0
    if phase != 3:
        scene bg westgate with Fade(0.1, 0, 0.1)
    else:
        scene bg westgaten with Fade(0.1, 0, 0.1)
    jump westgateskip
label westgateskip:
    call screen westgate
screen westgate:
    imagebutton:
        xpos 883
        ypos 273
        auto "images/int/northgate_%s.png"
        action Jump("westgate_test") 
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("field")
        
default rot = False
label eastgate:
    if not rot:
        $ current_location = "eastgate"
    else:
        $ current_location = "eastgate rot"
    stop music fadeout 0.5
    play music "bgm_gate.mp3" fadein 1.0
    if not rot:
        if phase != 3:
            scene bg eastgate with Fade(0.1, 0, 0.1)
        else:
            scene bg eastgaten with Fade(0.1, 0, 0.1)
    else:
        if phase != 3:
            scene bg eastgate rot with Fade(0.1, 0, 0.1)
        else:
            scene bg eastgate rotn with Fade(0.1, 0, 0.1)
    jump eastgateskip
label eastgateskip:
    call screen eastgate
screen eastgate:
    if rot:
        imagebutton:
            xpos 983
            ypos 603
            auto "images/int/gate_rot_%s.png"
            action Jump("eastgate_test") 
    else:
        imagebutton:
            xpos 883
            ypos 273
            auto "images/int/northgate_%s.png"
            action Jump("eastgate_test") 
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("field")

label westgate_test:
    "Only those with souls to nature may pass."
    if westgate_unlock == False:
        if soul_of_bloomfield == True:
            menu:
                "Present":
                    "You walked through the veil of fog..."
                    $ westgate_unlock = True
                    $ adjacent_unlock("park", "field")
                    $ move_to("park")
                "Leave":
                    jump westgateskip
    else:
        menu:
            "Pass":
                "You walked through the veil of fog..."
                $ move_to("park")
            "Leave":
                jump westgateskip
    jump westgateskip

default thorns_first_woogie = False
default impenetrable_thorns = False
label eastgate_test:
    if rot:
        if lake_first:
            $ move_to("lake")
        jump field_to_lake_cutscene_2
    "Impenetrable thorns refuse all. {p}None may enter the Swanlake."
    $ impenetrable_thorns = True
    if woogie and thorns_first_woogie == False:
        stop music fadeout 0.5
        play music "bgm_woogie.mp3" fadein 1.0
        show watta frown at left
        show woogie inspect at right
        wo "{i}sniff sniff"
        wo "hmm"
        show woogie hmm with dissolve
        wo "The impenetrable thorns"
        wo "I have read about them but never witnessed them firsthand."
        wo "It is said the queen sealed this off with her strongest barrier, preventing everyone from accessing the lake."
        show woogie default
        wo "As for the reason? It was kept a secret, so I don't really know what led to it"
        wo "Just know that you can't get past it so easily..."
        show woogie laugh at bounce
        wo "For now!"
        wo "Find a way to get rid of them won't ya!"
        show woogie proud
        wo "I believe in you Watton"
        show woogie proud at slide_out_right
        pause 1
        show watta mad
        w "Is Watta"
        hide woogie
        hide watta
        $ thorns_first_woogie = True
        stop music fadeout 0.5
        play music "bgm_gate.mp3" fadein 1.0
    if soul_of_corruption:
        menu:
            "Present":
                jump field_to_lake_cutscene
            "Leave":
                jump eastgateskip
    jump eastgateskip

label field_to_lake_cutscene:
    scene bg black with Fade(2,0,0)
    show bg field1 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    w "{i}Let's do this."
    show bg field2 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    show bg field3 with Dissolve(1)
    $ renpy.pause(1, hard=True)
    w "Remembrance is the amber,"
    show bg field4 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    extend " light is the root, "
    show bg field5 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    extend " genesis is the blood."
    show bg field6 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    show bg field7 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    show bg field8 with Fade(0.7,0,0.7)
    $ renpy.pause(0.5, hard=True)
    show bg field9 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    show bg field10 with Fade(2,1,3)
    $ renpy.pause(3, hard=True)
    show bg black with Fade(2,0,0)
    $ rot = True
    jump eastgate

label field_to_lake_cutscene_2:
    stop music fadeout 0.5
    play music "bgm_sari.mp3" fadein 1.0
    scene bg eleva with Fade(0.1,0,0.1)
    $ renpy.pause(3, hard=True)
    if phase == 3:
        "Rollback while you still can."
    $ renpy.pause()
    if phase == 3:
        jump lake_at_night
    show bg field11 with Fade(1,1,1)
    $ renpy.pause(1, hard=True)
    show bg field12 at shake
    $ renpy.pause(1, hard=True)
    show bg field13 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    show bg field14 with Dissolve(1)
    $ renpy.pause(0.5, hard=True)
    show bg field15
    $ renpy.pause(0.2, hard=True)
    show bg field16 at shake
    w "Eek!!"
    $ renpy.pause(0.5, hard=True)
    show bg field17 with Fade(1,0,1)
    $ renpy.pause(2, hard=True)
    show bg black with Fade(1,0,1)
    show screen new_area_unlocked("Swan Lake")
    $ renpy.pause(7, hard=True)
    hide screen new_area_unlocked
    $ renpy.pause(2, hard=True)
    show bg black with Fade(2,0,0)
    play music "bgm_lake.mp3" fadein 3
    scene bg lake with Fade(0.1, 0, 3)
    $ renpy.pause(3, hard=True)
    show watta ahh
    w "OMG that was so scary."
    w "Are those even real swans?"
    show watta ahh
    w "They don't move at all so..."
    w "Hopefully not..."
    $ loc_unlock("lake")
    $ lake_first = True
    $ action_done()
    $ current_location = "lake"
    hide watta
    call screen lake



label lake_at_night:
    $ quick_menu = False
    $ _game_menu_screen = None

    hide screen phone_toggle
    hide screen map_toggle
    hide screen console_toggle
    hide screen inventory_display_toggle

    $ save_lock = True
    $ all_locked = True
    $ actions_locked = True

    scene bg laken with Fade(0.5, 0, 0.5)
    stop music fadeout 0.5
    play music "bgm_owlnest.mp3" fadein 1.0

    $ renpy.block_rollback()
    $ renpy.pause(0.01, hard=True)

    "This is your biggest mistake"

    $ renpy.block_rollback()
    $ renpy.pause(0.01, hard=True)

    "Do not visit the lake at night"

    $ renpy.block_rollback()
    $ persistent.horror_crash = True

    call screen you_died

