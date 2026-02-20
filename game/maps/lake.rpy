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


label lakedef:
    if lake_first == False:
        jump lake_ft
    else:
        call screen lake
    return
label lake_ft:
    show watta sleepy
    w "Ahh... the lake"
    w "This is where Sari works."
    if fridge == 2:
        w "Should ask him about the sauce..."
    hide watta
    $ lake_first = True
    jump lakedef

screen lake:
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