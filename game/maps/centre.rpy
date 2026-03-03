label centre:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_centre.mp3" fadein 1.0
    jump centreintrotest

label centreskip:
    # Automatically load background with a smooth transition
    $ current_location = "centre"
    if phase != 3:
        scene bg centre with Fade(0.1, 0, 0.1)
    else:
        scene bg centren with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    $ actions_locked = False
    $ all_locked = False
    jump centredef

label centreintrotest:
    if centre_first == False:
        hide screen action_display
        jump chii_intro
    else:
        jump centreskip


label centredef:
    call screen centre
    return
label centre_ft:
    show watta sleepy
    hide watta
    $ centre_first = True
    jump centredef

default screen_unlocked = False
screen centre:
    if (day == 2 and (phase == 2 or phase == 3)) or screen_unlocked:
        imagebutton:
            xpos 785
            ypos 310
            auto "images/int/centre_center_%s.png"
            action Jump("big_screen")
    imagebutton:
        xpos 0
        ypos 65
        auto "images/int/rng_%s.png"
        action Jump("rng")
    if not chii_settled or chii_meet_sanco_timer <= 2 or chii_go_to_lake_timer > 2:
        imagebutton:
            xpos 1390
            ypos 50
            auto "images/int/floral_closed_%s.png"
            action Jump("floral")
    else:
        imagebutton:
            xpos 1390
            ypos 50
            auto "images/int/floral_%s.png"
            action Jump("floral")


label rng:
    $ current_location = "lan"
    scene bg rng with Fade(0.1, 0, 0.1)
    stop music fadeout 0.5
    play music "bgm_rng.mp3" fadein 1.0
    jump rngskip
label rngskip:
    show rng flashing
    #$ save_lock = True
    jump lan_test

label floral:
    $ current_location = "floral respite"
    jump floralskip
label floralskip:
    if sanco_talked_about_chii == True:
        $option_add("shop_chat", "sanco", "chii_about_sanco")
    if not chii_settled or chii_meet_sanco_timer <= 2 or chii_go_to_lake_timer > 2:
        scene bg floral respitel with Fade(0, 0, 0)
        if chii_meet_sanco_timer <= 2 or chii_go_to_lake_timer > 2:
            show black at alpha_half
            stop music
            play music "bgm_empty.mp3"
            "But nobody came.{fast}"
            jump centre
    else:
        scene bg floral respite with Fade(0.1, 0, 0.1)
    jump chii_test

default big_screen_not_happen_again = False
label big_screen:
    $ current_location = "big screen"
    if day == 2 and (phase == 2 or phase == 3) and prologue_done_2 == True and neko_first_talk_done_stage == 0 and not big_screen_not_happen_again:
        jump neko_intro
    if day == 3 and neko_invitation and (phase == 2 or phase == 3) and neko_second_end == False:
        jump neko_invited_intro
    if day == 3 and neko_lied_to and (phase == 2 or phase == 3) and neko_second_end == False and is_item_get("Nekomin Badge"):
        if not neko_tsukino_intro_talk_again and not neko_tsukino_intro_no_more:
            jump neko_tsukino_intro
        elif neko_tsukino_intro_talk_again:
            jump neko_tsukino_intro_again
    if phase != 3:
        scene bg big screen with Fade(0.1, 0, 0.1)
    else:
        scene bg big screenn with Fade(0.1, 0, 0.1)
    play music "bgm_bigscreen.mp3" fadein 1.0 if_changed
    jump big_screenskip
label big_screenskip:
    call screen big_screen

default backstage_open = True
screen big_screen:
    if neko_quest_start == True and backstage_open:
        imagebutton:
            xpos 1340
            ypos 0
            auto "images/int/backstage_%s.png"
            action Jump("neko_test")
    if ((neko_first_talk_done_stage == 1 and phase == 3 and remi_first_talk_done_stage > 1 and not backstage_open and remi_first_talk_done_stage <4 and remi_opinion <3) or (day > 2 and phase == 3 and remi_first_talk_done_stage > 1 and remi_first_talk_done_stage <4 and remi_opinion <3)):
        imagebutton:
            xpos 860
            ypos 350
            auto "images/char_int/remi_screen_%s.png"
            action Jump("remi_test")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("centre")
    if hall_open:
        imagebutton:
            xpos 1752
            ypos 400
            auto "images/int/right_%s.png"
            action Jump("hall")
    
default hall_open = False
default snowie_hall_presence = False
default bailey_hall_presence = False
label hall:
    $ current_location = "hall"
    scene bg hall with Fade(0.1, 0, 0.1)
    jump hallskip
label hallskip:
    scene bg hall
    play music "bgm_hall.mp3" fadein 1.0 if_changed
    call screen hall
screen hall:
    if bailey_hall_presence:
        imagebutton:
            xpos 1445
            ypos 190
            auto "images/char_int/bailey_hall_%s.png"
            action Jump("bailey_hall_talk")
    if snowie_hall_presence:
        imagebutton:
            xpos 935
            ypos 270
            auto "images/char_int/snowie_hall_%s.png"
            action Jump("snowie_hall_talk")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("hall_leave_confirmation")

default snowie_monitoring_intro = False
label hall_leave_confirmation:
    if not snowie_first_quest:
        "Do you want to leave the hall? You cannot turn back."
        menu:
            "Ye I got to try out the worse option":
                $ actions_locked = False
                jump big_screen
            "Meh":
                jump hallskip
    else:
        if phase != 3:
            scene bg big screen with Fade(0.1, 0, 0.1)
        else:
            scene bg big screenn with Fade(0.1, 0, 0.1)
        show snowie happy
        sn "The workshop is right besides the monument, you should be able to get there quickly."
        sn "Follow me!"
        show snowie happy at slide_out_left
        if woogie:
            show woogie huh at slide_in_right
            wo "Hmmmmm"
            show woogie stare
            wo "Is that yer new friend Walter?"
            show woogie sus with dissolve
            wo "Be cautious when making new friends Walter"
            wo "They can be spooky sometimes,"
            show woogie laugh
            wo "Only I, shall be the trusted one."
            hide woogie
        $ snowie_first_quest = False
        $ snowie_monitoring_intro = True
    jump monitoring
        
