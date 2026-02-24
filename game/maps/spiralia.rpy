label spira:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_spira.mp3" fadein 1.0
    jump spiraskip

label spiraskip:
    # Automatically load background with a smooth transition
    $ current_location = "spira"
    if phase != 3:
        scene bg spira with Fade(0.1, 0, 0.1)
    else:
        scene bg spiran with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    jump spiradef


label spiradef:
    if spira_first == False:
        jump spira_ft
    else:
        call screen spira
    return
label spira_ft:
    show watta shocked 
    w "Wao so this is-{w=0.5}{nw}"
    show watta shocked at shake
    b "STOP RIGHT THERE YOU-"
    unknown "{font=Iskra.ttf}{size=+40}Never gonna catch me!"
    show iskra default at slide_right_to_left
    show watta wtf at bounce
    pause 1
    show watta shocked at slide_to_left
    show bailey angry at slide_in_right
    b "YOU NI-"
    show watta wtf at bounced
    w "Woa woa woa calm down man don't say that"
    show watta frown
    show bailey pant at bounced
    b "It's over, she got away again"
    b "I have one job but I can never do it right"
    b "Arghhh"
    show watta sweat
    w "Is okay, is okay, at least you tried your best"
    if bailey_first_time_hall:
        show bailey shock
        b "Oh it's you the Nekomin from the meeting"
        b "Didn't expect to see you here."
        b "Well since you are here either way..."
        b "Might as well vent out a bit"
    show bailey mad
    b "The economy is already started crumbling, it's just a matter of time before it completely collapse."
    b "If I can't do my job right then nothing will be right anymore"
    show watta huh
    w "Is tough, but what caused that?"
    show bailey sus
    b "You are not a local, oh right those outfit proved"
    show watta happy
    w "Well I'm not but I do want to help, is close to festival after all"
    show bailey smile
    b "Really? That's nice, people like you are rare really."
    if ( day == 3 and (phase == 2 or phase == 3)):
        b "I would invite you to my office later, buttttt-"
        b "I have to attend something real quick"
        b "I will be back tomorrow."
        b "See ya"
    else:
        b "Here, come to my office I will explain more to you!"
    hide bailey
    hide watta
    $ spira_first = True
    jump spiradef

default lane_to_spira_first = False
screen spira:
    if lane_to_spira_first:
        imagebutton:
            xpos 917
            ypos 720
            auto "images/int/spira_to_lane_%s.png"
            action Jump("lane")
    if archeste_open == True:
        imagebutton:
            xpos 0
            ypos 0
            auto "images/int/archeste_%s.png"
            action Jump("archeste")
    imagebutton:
        xpos 1640
        ypos 0
        auto "images/int/railwork_%s.png"
        action Jump("railwork")
    use camera_on

label archeste:
    $ current_location = "archeste"
    scene bg archeste with Fade(0.1, 0, 0.1)
    stop music fadeout 0.5
    play music "bgm_archeste.mp3" fadein 1.0
    jump archesteskip
label archesteskip:
    scene bg archeste
    call screen archeste

screen archeste:
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("spira")
    imagebutton:
        xpos 0
        ypos 305
        auto "images/char_int/toko_archeste_%s.png"
        action Jump("toko_test")

    
label railwork:
    $ current_location = "railwork"
    if phase != 3:
        scene bg railwork with Fade(0.1, 0, 0.1)
    else:
        scene bg railworkn with Fade(0.1, 0, 0.1)
    stop music fadeout 0.5
    play music "bgm_railwork.mp3" fadein 0
    jump railworkskip
label railworkskip:
    call screen railwork
screen railwork:
    if not ( day == 3 and (phase == 2 or phase == 3)) and not bailey_unavailable:
        imagebutton:
            xpos 1383
            ypos 230
            auto "images/char_int/bailey_railwork_%s.png"
            action Jump("bailey_test") 
    if bailey_chant == True:
        imagebutton:
            xpos 0
            ypos 334
            auto "images/int/train_%s.png"
            action Jump("train_test")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("spira")


default bailey_following_lane_to_spira_talk2 = False
label lane:
    $ current_location = "fishing lane"
    scene bg lane with Fade(0.1, 0, 0.1)
    stop music fadeout 0.5
    play music "bgm_lane.mp3" fadein 1.0
    if bailey_following_oil and bailey_following_lane_to_spira_talk and not bailey_following_lane_to_spira_talk2:
        show bailey default
        b "That tunnel is the shortcut to the monument"
        b "Take it, it's not that long."
        $ adjacent_unlock("monument", "spira") 
        $ bailey_following_lane_to_spira_talk2 = True
        hide bailey
    if not lane_first:
        show watta default
        w "Wao, a lot of fishing tools."
        $ lane_first = True
        hide watta
    jump laneskip
label laneskip:
    call screen lane
screen lane:
    if nemu_first_talk_done_stage ==4:
        imagebutton:
            xpos 880
            ypos 10
            auto "images/char_int/nemu_lane_%s.png"
            action Jump("nemu_shop")
    imagebutton:
        xpos 50
        ypos 390
        auto "images/int/lane_to_monument_%s.png"
        action Jump("lane_to_monument")
    imagebutton:
        xpos 1756
        ypos 0
        auto "images/int/lane_to_spira_%s.png"
        action Jump("lane_to_spira")
    imagebutton:
        xpos 57
        ypos 930
        auto "images/int/lane_to_bridge_%s.png"
        action [Function(action_done), Jump("underbridge")]

label lane_to_spira:
    if not lane_to_spira_first and not is_unlocked("spira"):
        show black with Fade(0.1, 0, 0)
        stop music fadeout 3
        hide screen action_display
        $ renpy.pause(2, hard=True)
        show screen new_area_unlocked("Spiralia")
        $ renpy.pause(7, hard=True)
        show screen action_display
        $ loc_unlock("spira")
        $ lane_to_spira_first = True
        $ adjacent_unlock("monument", "spira") 
        jump spira
    else:
        jump spira


label lane_to_monument:
    if lane_to_monument_first == 0:
        $ lane_to_monument_first = 1
        if not bailey_following_oil:
            $ action_done()
        jump nekopia
    else:
        if not bailey_following_oil:
            $ action_done()
        jump nekopia

default lane_first = False
label bridge_to_lane:
    $ current_location = "fishing lane"
    scene bg bike loading with Fade(0.5,0.1,0.5)
    $ renpy.pause(2, hard=True)
    $ renpy.pause()  
    $ action_done()
    if lane_first:
        jump lane
    scene bg lane with Fade(0.1,0.1,0.1)
    stop music fadeout 0.5
    play music "bgm_lane.mp3" fadein 1.0
    show bg lane at whiten_lesser
    show nemu default at right
    show watta default at left
    pause 0.3
    show nemu uwu at bounce
    n "OMG Watta! Welcome to Fishing Lane!"
    show watta delighted
    w "I've arrived!"
    n "For now this place is mostly to upgrade your rod."
    show nemu brat
    n "I can help you forge your rod to be better, if you'd like."
    $ lane_first = True
    hide watta
    hide nemu
    jump laneskip