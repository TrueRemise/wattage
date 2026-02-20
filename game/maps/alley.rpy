label alley:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"
    $ current_location = "alley"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_alley.mp3" fadein 1.0
    jump alleyskip

label alleyskip:
    # Automatically load background with a smooth transition
    scene expression world_bg with Fade(0.1, 0, 0.1)

    # --- Event jump logic ---
    if (current_weekday, current_phase) in home_events:
        jump expression dist_events[(current_weekday, current_phase)]
    else:
        jump alleydef


label alleydef:
    if alley_first == False:
        jump alley_ft
    else:
        call screen alley
    return
label alley_ft:
    show watta sleepy
    w "Ahh... the alley"
    w "This is where Sari works."
    if fridge == 2:
        w "Should ask him about the sauce..."
    hide watta
    $ alley_first = True
    jump alleydef

screen alley:
    imagebutton:
        xpos 250
        ypos 380
        auto "images/int/work_%s.png"
        action Jump("work")
    imagebutton:
        xpos 1679
        ypos 288
        auto "images/int/distpath_%s.png"
        action Function(move_to, "home")