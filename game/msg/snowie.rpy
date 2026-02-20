default snowie_first_time_hall = False
default snowie_first_quest = False
label snowie_hall_talk:
    if not meeting_choice_retire:
        show snowie happy
        if not snowie_first_time_hall:
            sn "Oh! Welcome!"
            sn "Are you new here? Haven't seen you around til today"
            sn "How long have you been one?"
            sn "Oh just recently?"
            sn "It's fine the duration doesn't matter, it's more about your enthusiasm"
            sn "That is what truelly define a Nekomin"
            sn "This meeting is for an important announcement regarding Neko"
            show snowie sad
            sn "Mhm hope it's not something too bad trough..."
            $ snowie_first_time_hall = True
            hide snowie
            jump hallskip
        else:
            show snowie sad
            sn "Hope it's not too bad..."
            hide snowie
            jump hallskip
    else:
        show snowie default
        $ actions_locked = True
        sn "Oh ye do you want to visit my workshop?"
        w "Huh? Why so sudden?"
        sn "Oh I share this with all the Nekomin I think you'd wanna see too!"
        w "Oh yes ofc"
        show snowie happy at bounced
        sn "Great!"
        sn "Meet me outside then!"
        $ snowie_hall_presence = False
        $ snowie_first_quest = True
        jump hallskip

label snowie_monitoring_intro:
    scene bg monitoring with Fade(1, 0, 1)
    show snowie happy at right
    pause 0.3
    show snowie happy at bounce
    show watta smile at left
    play music "bgm_monitoring.mp3" fadein 1.0 if_changed
    sn "Here we are"
    w "Wao this place is pretty."
    show snowie smile
    sn "Ye I work as security in this area, so..."
    sn "You gonna see a lot of screen."
    show snowie happy at bounced
    sn "Come and sit, make yourself home!"
    w "Alright!"
    sn "Imma get some tea first, hold on a minute."
    w "Alright."
    show snowie smile at slide_out_right
    hide watta
    hide snowie
    $ snowie_monitoring_intro = False
    jump monitoringskip