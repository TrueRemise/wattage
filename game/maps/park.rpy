label park:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    if phase != 3:
        scene bg park with Fade(0.1, 0, 0.1)
    else:
        scene bg parkn with Fade(0.1, 0, 0.1)
    # Music setup
    jump parkskip

label parkskip:
    # Automatically load background with a smooth transition
    $ current_location = "park"
    play music "bgm_park.mp3" fadein 1.0 if_changed
    if phase != 3:
        scene bg park
    else:
        scene bg parkn
    # --- Event jump logic ---
    if (current_weekday, current_phase) in park_events:
        jump expression park_events[(current_weekday, current_phase)]
    else:
        jump parkdef

define park_events = {
}

label parkdef:
    if park_first == False:
        jump park_ft
    else:
        call screen park
    return
label park_ft:
    $ park_first = True
    jump woogie_first_talk

default westgate_unlock = False
screen park:
    imagebutton:
        xpos 714
        ypos 423
        auto "images/int/van_door_%s.png"
        action Jump("van")
    if westgate_unlock == True:
        imagebutton:
            xpos 1734
            ypos 180
            auto "images/int/park_westgate_%s.png"
            action Function(move_to,"field")
    if day >= 3:
        imagebutton:
            xpos 1334
            ypos 320
            auto "images/char_int/iog_park_%s.png"
            action Jump("iog_stand")
    if remi_opinion >= 3 and the_knower == 2 and remi_first_talk_done_stage == 4:
        imagebutton:
            xpos 508
            ypos 645
            auto "images/char_int/remi_park_%s.png"
            action Jump("remi_test")

label van:
    $ current_location = "van"
    scene bg van with Fade(0.1, 0, 0.1)
    play music "bgm_sari.mp3" fadein 1.0 if_changed
    jump vanskip
label vanskip:
    scene bg van
    call screen van

screen van:
    imagebutton:
        xpos 1180
        ypos 8
        auto "images/char_int/sari_van_%s.png"
        action Jump("sari_first_talk")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("park")

default iog_stand_tip = False
default puppy_count = 0
default dog_count = 0
label iog_stand:
    show iog default
    iog "hot dog"
    if not iog_stand_tip:
        "These foods can be bought to increase your actions mid-game. Hot puppies will recover 1, while hot dogs will recover 3 actions, you can't go more than the cap so be mindful."
        "To eat the food, open phone and on top of the Messages bar will be the options to eat them, if you have any."
        $ iog_stand_tip = True
    call screen iog_stand
    
screen iog_stand():
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
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action If(sol >= 100,
                    If(puppy_count < 9,
                        [Play("sound", "sfx/purchase.mp3"), SetVariable("puppy_count", max(0, puppy_count+1)), SetVariable("sol", max(0, sol-100)), Function(renpy.notify, f"You got {puppy_count + 1} pupp(y/ies)")],
                        [Function(renpy.notify, "You can only buy 9 hot puppies at a time.")]
                    ),
                    [Play("sound", "sfx/bet_denied.mp3"), Function(renpy.notify, "bozo you dont have enough money")]
                )
                text "Buy a hot puppy for 100":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
                    outlines [(10, "#ffffff", 0, 0)]
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action If(sol >= 200,
                    If(dog_count < 3,
                        [Play("sound", "sfx/purchase.mp3"), SetVariable("dog_count", max(0, dog_count+1)), SetVariable("sol", max(0, sol-200)), Function(renpy.notify, f"You got {dog_count + 1} dog(s)")],
                        [Function(renpy.notify, "You can only buy 3 hot dogs at a time.")]
                    ),
                    [Play("sound", "sfx/bet_denied.mp3"), Function(renpy.notify, "bozo you dont have enough money")]
                )
                text "Buy a hot dog for 200":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
                    outlines [(10, "#ffffff", 0, 0)]
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action [Jump("park")]
                text "No":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
                    outlines [(10, "#ffffff", 0, 0)]

