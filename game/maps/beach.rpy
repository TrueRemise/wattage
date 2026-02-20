label beach:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    play music "bgm_beach.mp3" fadein 1.0 if_changed
    if phase != 3:
        scene bg beach with Fade(0.1, 0, 0.1)
    else:
        scene bg beachn with Fade(0.1, 0, 0.1)
    jump beachskip

label beachskip:
    # Automatically load background with a smooth transition
    $ current_location = "beach"
    if phase != 3:
        scene bg beach
    else:
        scene bg beachn
    # --- Event jump logic ---
    jump beachdef


label beachdef:
    if beach_first == False:
        jump beach_ft
    else:
        call screen beach
    return
label beach_ft:
    $ beach_first = True
    jump beachdef

screen beach:
    use camera_on
    if not remi_first_talk_done_stage > 1 and phase == 2:
        imagebutton:
            xpos 1102
            ypos 506
            auto "images/char_int/remi_beach_%s.png"
            action Jump("remi_test")
    if tato_first_talk_done_stage == 0 and phase != 3:
        imagebutton:
            xpos 1704
            ypos 486
            auto "images/char_int/tato_beach_%s.png"
            action Jump("tato_test")
    if tato_first_talk_done_stage >= 2 and phase != 3:
        imagebutton:
            xpos 1490
            ypos 366
            auto "images/char_int/tato_beach_2_%s.png"
            action Jump("tato_test")
    if not is_item_get("Hydrophobic Lubricant") and is_item_get("Fishing Rod") and woogie:
        imagebutton:
            xpos 0
            ypos 580
            auto "images/int/to_island_%s.png"
            action [Jump("woogie_fishonthebeach")]
    if is_item_get("Hydrophobic Lubricant"):
        imagebutton:
            xpos 0
            ypos 580
            auto "images/int/to_island_%s.png"
            action [Function(action_done), Jump("island")]

label island:
    $ current_location = "island"
    stop music fadeout 0.5
    play music "bgm_kuro.mp3" fadein 1.0
    if phase != 3:
        scene bg island with Fade(0.1, 0, 0.1)
    else:
        scene bg islandn with Fade(0.1, 0, 0.1)
    jump islandskip
label islandskip:
    call screen island
screen island:
    imagebutton:
        xpos 1136
        ypos 332
        auto "images/char_int/kuro_island_%s.png"
        action Jump("kuro_test") 
    imagebutton:
        xpos 476
        ypos 732
        auto "images/int/to_bridge_%s.png"
        action [Function(action_done), Jump("bridge_from_island")]
    imagebutton:
        xpos 1132
        ypos 710
        auto "images/int/to_beach_%s.png"
        action [Function(action_done), Jump("beach")]


label woogie_fishonthebeach:
    stop music fadeout 0.5
    play music "bgm_woogie.mp3" fadein 1.0
    show watta default at left
    w "Let's see"
    show woogie huh at slide_in_right
    wo "Dud"
    show watta frown
    w "Hah?"
    wo "Are ya for real?"
    w "What?"
    show woogie laugh4 with dissolve
    wo "DUDE!"
    w "WHAT"
    show woogie laugh4 at bounced
    wo "{size=+15}DUDE!!"
    w "WHAAT"
    show watta mad
    pause 0.5
    wo "{size=+15}DUDE MAN"
    show woogie laugh3 at bounce
    wo "{size=+15}THIS IS A BEACH"
    wo "{size=+15}WHO WOULD FISH RIGHT ON THE BEACH DUDE?"
    extend " WWWWWWW"
    show watta mad
    show woogie laugh3 at bounce
    wo "{size=+15}YA ARE NOT REAL MAN"
    w "..."
    show woogie laugh4
    wo "When I say fish at the sea, "
    extend "I meant to get in the deep water zone man."
    show woogie laugh3 at bounce
    wo "WHAT KIND OF FISH ARE YA EXPECTING HERE DUDE"
    show woogie laugh4
    wo "FISH OF DECEASE?"
    show woogie laugh3 at slide_out_right
    wo "OMG I CANT"
    jump beach
