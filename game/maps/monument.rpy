label monument:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_monument.mp3" fadein 1.0
    jump monumentskip

label monumentskip:
    # Automatically load background with a smooth transition
    $ current_location = "monument"
    if phase != 3:
        scene bg monument with Fade(0.1, 0, 0.1)
    else:
        scene bg monumentn with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    if (current_weekday, current_phase) in monument_events:
        jump expression monument_events[(current_weekday, current_phase)]
    else:
        jump monumentdef

define monument_events = {
}

label monumentdef:
    if monument_first == False:
        jump monument_ft
    else:
        call screen monument
    return
label monument_ft:
    show watta sleepy
    w "The Monument of the lost..."
    w "Is just a big graveyard really"
    show watta sweat
    w "Scary..."
    hide watta
    $ monument_first = True
    jump monumentdef

screen monument:
    use camera_on
    imagebutton:
        xpos 1483
        ypos 450
        auto "images/int/mon_left_%s.png"
        action Jump("dustwynd")
    imagebutton:
        xpos 1528
        ypos 244
        auto "images/int/mon_right_%s.png"
        action Jump("nekopia")
    if monument_to_cavern_unlock:
        imagebutton:
            xpos 454
            ypos 954
            auto "images/int/cavern_entrance_%s.png"
            action Jump("to_cavern_from_monument")
default aloy_unlock = False
default reni_unlock = False

default dustwynd_first = False
label dustwynd_first:
    w "This should be Aloy's house, judging by the smell."
    $ dustwynd_first = True
    jump dustwyndskip
label dustwynd:
    $ current_location = "dustwynd"
    play music "bgm_monument.mp3" fadein 1.0 if_changed
    if aloy_unlock == True:
        scene bg dustwyndl with Fade(0.1, 0, 0.1)
    else:
        scene bg dustwynd with Fade(0.1, 0, 0.1)
    if dustwynd_first == False:
        jump dustwynd_first
    jump dustwyndskip
label dustwyndskip:
    call screen dustwynd
screen dustwynd:
    imagebutton:
        xpos 1233
        ypos 323
        auto "images/int/noydoor_%s.png"
        action Jump("aloy") 
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("monumentskip")

label aloy:
    if aloy_unlock == False:
        "The door is locked"
        jump dustwyndskip
    jump dustwyndskip

default nekopia_first = False
default lane_to_monument_first = 0
label nekopia_first:
    show watta default
    w "This should be Reni's store, judging by the exterior."
    $ nekopia_first = True
    jump nekopiaskip
label nekopia:
    $ current_location = "nekopia"
    play music "bgm_monument.mp3" fadein 1.0 if_changed
    scene bg nekopia with Fade(0.1, 0, 0.1)
    if lane_to_monument_first == 1:
        show watta ahh
        w "That was really stinky...urgh"
        show watta default
        w "But hey!"
        w "We arrived here."
        $ lane_to_monument_first = 2
    if nekopia_first  == False:
        jump nekopia_first
    jump nekopiaskip
label nekopiaskip:
    hide watta
    call screen nekopia
screen nekopia:
    if lane_to_monument_first == 2:
        imagebutton:
            xpos 1628
            ypos 965
            auto "images/int/monument_to_lane_%s.png"
            action [Function(action_done), Jump("lane")]
    imagebutton:
        xpos 1068
        ypos 530
        auto "images/int/rendoor_%s.png"
        action Jump("reni")
    imagebutton:
        xpos 96
        ypos 295
        auto "images/int/renback_%s.png"
        action Jump("renback")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("monumentskip")

default already_read_reni_number = False
default already_write_reni_number = False
label reni:
    if reni_unlock == False:
        if already_read_reni_number == True:
            jump already_read_reni_number
        "The door is locked"
        extend " but"
        show watta default at left
        w "Something is noted at the door?"
        label already_read_reni_number:
        "{i}I had to leave this place for a while, if you need to contact me, here is my number:"
        extend "{size=+10} 917 143 4321"
        if is_item_get("Memorizing Sheet"):
            if already_write_reni_number == True:
                jump nekopiaskip
            call reni_write_down_number from _call_reni_write_down_number
        else:
            if already_read_reni_number == True:
                jump nekopiaskip
            w "Numbers."
        $ already_read_reni_number = True
        hide watta
        jump nekopiaskip

label renback:
        "Inaccessible"
        jump nekopiaskip

label reni_write_down_number:
    w "Lemme write it down"
    "Number Written in Memorizing Sheet"
    $ already_write_reni_number = True
    return


label monitoring:
    $ current_location = "monitoring"
    if snowie_monitoring_intro:
        jump snowie_monitoring_intro
    scene bg monitoring with Fade(0.1, 0, 0.1)
    jump monitoringskip
label monitoringskip:
    play music "bgm_monitoring.mp3" fadein 1.0 if_changed
    call screen monitoring

default mnt_secret_hall_open = False
screen monitoring:
    if not mnt_secret_hall_open:
        imagebutton:
            xpos 1630
            ypos 345
            auto "images/int/mnt_book_%s.png"
            action Jump("mnt_book")
    else:
        imagebutton:
            xpos 1583
            ypos 207
            auto "images/int/mnt_opened_%s.png"
            action Jump("mnt_book")
    imagebutton:
        xpos 0
        ypos 0
        auto "images/int/mnt_camera_%s.png"
        action Jump("mnt_camera")
    imagebutton:
        xpos 1087
        ypos 606
        auto "images/int/mnt_chair1_%s.png"
        action Jump("mnt_chair1")
    imagebutton:
        xpos 150
        ypos 624
        auto "images/int/mnt_chair2_%s.png"
        action Jump("mnt_chair2")
    imagebutton:
        xpos 0
        ypos 835
        auto "images/int/mnt_magazine_%s.png"
        action Jump("mnt_magazine")
    imagebutton:
        xpos 1050
        ypos 340
        auto "images/int/mnt_leave_%s.png"
        action Jump("mnt_leave")
    

label mnt_camera:
    w "There are a lot of camera screens here."
    w "To think we're being monitored like this..."
    w "Kinda scary..."
    jump monitoringskip
label mnt_chair1:
    w "It's a not so comfy chair."
    jump monitoringskip
label mnt_chair2:
    w "It's a comfy chair."
    if mnt_secret_hall_open:
        jump monitoringskip
    else:
        "Do you want to wait for Snowie?"
        menu:
            "Do you want to wait for Snowie?{fast}"
            "Ye sure time can wait.":
                scene bg monitoring with fade
                show watta default at left
                show snowie happy at right
                sn "Here you go."
                show watta delighted at bounced
                show snowie smile
                w "Wao nice thank you."
                show watta delighted at bounced
                pause 1.0
                show watta deter
                w "Is good!"
                show snowie happy at bounced
                sn "Is that so?"
                sn "I can get more if you want."
                sn "Wait a few minutes."
                show snowie happy at slide_out_right
                pause 1.0
                w "Hmm"
                pause 2.0
                show watta sleepy
                w "Hmm"
                w "Why do I suddenly feel sleepy,"
                w "Well a nap won't harm."
                w "I guess"
                scene bg black with Fade(1,2,2)
                hide watta
                stop music fadeout 4
                jump day_4_from_snowie
            "Hold on for about 2 seconds":
                jump monitoringskip
label mnt_magazine:
    w "The secret files..."
    jump monitoringskip
label mnt_leave:
    "Do you want to leave the house? You cannot turn back."
    menu:
        "Do you want to leave the house? You cannot turn back.{fast}"
        "I've got no time for this":
            $ actions_locked = False
            jump monument
        "Meh":
            jump monitoringskip
    jump monitoringskip
label mnt_book:
    if not mnt_secret_hall_open:
        show watta frown
        w "This book looks off."
        show bg monitoring at shake
        play sound "sfx/contraption.mp3"
        "*clank*{w=0.5}{nw}"
        show watta deter at shaker
        w "What is happening..."
        w "Wait..."
        w "Something's opening up!"
        $ mnt_secret_hall_open = True
        hide watta
        jump monitoringskip
    else:
        show watta shocked
        w "A- A secret passage?"
        show watta deter
        w "Wait wait wait, this is interesting."
        w "Just a quick check before he comes back..."
        scene bg black with Fade(1,0,1)
        play sound "sfx/walking.mp3"
        stop music fadeout 2
        pause 2.0
        scene bg monitoringb with Fade(1,0,1)
        play music "bgm_hole.mp3" fadein 1.0 if_changed
        show watta huh
        w "It's kinda dark here."
        w "Is that a..."
        hide watta
        jump holeskip

label hole:
    $ current_location = "monitoring"
    scene bg monitoringb with Fade(0.1, 0, 0.1)
    jump holeskip
label holeskip:
    play music "bgm_hole.mp3" fadein 1.0 if_changed
    call screen hole
screen hole:
    imagebutton:
        xpos 600
        ypos 550
        auto "images/int/hole_%s.png"
        action Jump("mnt_hole")
    imagebutton:
        xpos 739
        ypos 36
        auto "images/int/mnt_sign_%s.png"
        action Jump("mnt_sign")



default jail_time_left = 30



label mnt_sign:
    "The RSA cryptosystem is one of the oldest widely used systems for secure data transmission.\nThe keys for the RSA algorithm are generated in the following way:"
    "1. Choose two large prime numbers p and q\n2. n = pq is used as the modulus for both the public and private keys.\n3. Compute {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n), where {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n) = (p - 1)(q - 1)."
    "4. Choose an integer e such that 1 < e < {font=Calibri.ttf}ϕ{/font=Calibri.ttf} (n) and gcd(e, {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n)) = 1; that is, e and {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n) are coprime.\n5. Determine d as d {font=Calibri.ttf}≡{/font=Calibri.ttf} e{font=Calibri.ttf}⁻¹{/font=Calibri.ttf} (mod {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n)); that is, d is the modular multiplicative inverse of e modulo {font=Calibri.ttf}ϕ{/font=Calibri.ttf}(n)."
    "Encryption: The message M, first turned into an integer m, such that 0 ≤ m < n, then compute the ciphertext c, using public key e, by:\nc{font=Calibri.ttf}≡{/font=Calibri.ttf}m{font=Calibri.ttf}ᵉ{/font=Calibri.ttf}(mod n)."
    "Decryption: m can be recovered from c by using the private key exponent d by computing:\nm{font=Calibri.ttf}≡{/font=Calibri.ttf}c{font=Calibri.ttf}ᵈ{/font=Calibri.ttf}(mod n)."
    "Given m, the original message M can be recovered by reversing the padding scheme, or discarded as corrupted if the padding is invalid."
    jump holeskip
label mnt_hole:
    w "This is a..."
    scene bg hole with Fade(0.2, 0, 0.2)
    w "It's a giant hole"
    w "Who could have dug this?"
    w "And..."
    extend " for what purpose?"
    w "Hold on..."
    show bg black with Fade(1, 0, 0.3)
    play sound "sfx/metal_scratch.mp3"
    w "The smell down below"
    pause 0.5
    w "No way..."
    w "Is that a.."

    $ quick_menu = False
    $ _game_menu_screen = None
    $ all_locked = True
    hide screen phone_toggle
    hide screen map_toggle
    hide screen console_toggle
    hide screen inventory_display_toggle
    hide screen action_display

    show bg hole2 with Fade(1, 0, 3)
    $ renpy.pause(2, hard=True)
    w "Is that a c{nw}"
    show bg white
    pause 0.1
    show bg black
    stop music
    play sound "sfx/metal_hit.mp3"
label day_4_from_snowie:
    $ renpy.pause(4, hard=True)
    $ quick_menu = True
    $ _game_menu_screen = "save"
    $ all_locked = False
    $ actions_locked = True
    #play music "bgm_cavern.mp3" fadein 1.0 if_changed
    show screen day_trans_suspense("Day 4")
    show screen console_toggle
    show screen action_display
    $ day = 4
    $ actions_left = max_actions -2
    $ phase = 0
    scene bg jail
    pause 5
    show watta sleepyb at right
    w "Wha- "
    w "What is this?"
    show watta frownb at bounced
    w "What is this place? Why do i have no memory at all"
    w "Have to get out of here"
    show watta huhb
    w "Wait"
    w "Where is my..."
    show watta grahhb at shaker
    show bg jail at shake
    w "WHO TOOK MY BAG?"
    w "OMG"
    w "YOU'LL PAY FOR THIS!"
    hide watta
    "Objective: Get out of here."
    show screen jail_timer("jail_time_up")

default oil_lake_first = False
default cavern_room = "jail"
label cavern:
    $ current_location = "cavern"
    if cavern_room == "jail":
        scene bg jail with Fade(0.1, 0, 0.1)
    elif cavern_room == "1":
        scene bg cavern1 with Fade(0.1, 0, 0.1)
        if bailey_following_oil:
            jump bailey_following_oil_scene
    elif cavern_room == "2":
        scene bg cavern2 with Fade(0.1, 0, 0.1)
    elif cavern_room == "3":
        scene bg cavern3 with Fade(0.1, 0, 0.1)
    elif cavern_room == "4":
        scene bg cavern4 with Fade(0.1, 0, 0.1)
    jump cavernskip
label cavernskip:
    play music "bgm_cavern.mp3" fadein 1.0 if_changed
    if cavern_room == "jail":
        call screen cavern_jail
    elif cavern_room == "1":
        if not oil_lake_first:
            $ oil_lake_first = True
            jump oil_lake_first
        call screen cavern1
    elif cavern_room == "2":
        call screen cavern2
    elif cavern_room == "3":
        call screen cavern3
    elif cavern_room == "4":
        call screen cavern4

default jail_screwdriver_own = False
default jail_wrench_own = False
default jail_hammer_own = False
default jail_saw_own = False
default jail_card_own = False
default jail_mirror_broke = False
default jail_pipe_broke = False
default jail_bed_broke = False
default jail_pillow_relocated = False
default jail_mat_relocated = False
default jail_hatch_opened = False
default jail_door_opened = False
default jail_tap_opened = False
default jail_box_revealed1 = False
default jail_box_revealed2 = False
default jail_box_revealed3 = False
default jail_let_that_sink_in = False
default jail_hole_checked = False
default jail_d_generated = False

screen cavern_jail:
    if not jail_screwdriver_own:
        imagebutton:
            xpos 1770
            ypos 698
            auto "images/jail/screwdriver_%s.png"
            action Jump("jail_screwdriver")
    imagebutton:
        xpos 0
        ypos 65
        auto "images/jail/mirror_%s.png"
        action Jump("jail_mirror")
    if jail_mirror_broke:
        add "images/jail/mirror_broke.png":
            xpos 0
            ypos 65
    if not jail_pipe_broke and jail_wrench_own and jail_hole_checked:
        imagebutton:
            xpos 0
            ypos 715
            auto "images/jail/pipe_%s.png"
            action Jump("jail_pipe")
    if jail_pipe_broke:
        add "images/jail/pipe_fixed.png":
            xpos 0
            ypos 715
    if not jail_hammer_own:
        imagebutton:
            xpos 55
            ypos 1019
            auto "images/jail/hole_%s.png"
            action Jump("jail_hole")
    imagebutton:
        xpos 20
        ypos 402
        auto "images/jail/tap_%s.png"
        action Jump("jail_tap")
    if jail_tap_opened:
        imagebutton:
            xpos 20
            ypos 402
            idle "images/jail/water.png"
            hover "images/jail/water.png"
    if not jail_hatch_opened and jail_screwdriver_own:
        imagebutton:
            xpos 1809
            ypos 144
            auto "images/jail/screw_%s.png"
            action Jump("jail_open_hatch")
        imagebutton:
            xpos 1813
            ypos 388
            auto "images/jail/screw_%s.png"
            action Jump("jail_open_hatch")
    if jail_hatch_opened:
        add "images/jail/opened_hatch.png":
            xpos 1809
            ypos 144
        if not jail_wrench_own:
            imagebutton:
                xpos 1852
                ypos 450
                auto "images/jail/wrench_%s.png"
                action Jump("jail_wrench")
    if not jail_mat_relocated:
        imagebutton:
            xpos 356
            ypos 838
            auto "images/jail/mat_%s.png"
            action Jump("jail_mat")
    else:
        add "images/jail/veiled.png":
            xpos 290
            ypos 828
        if not jail_saw_own:
            imagebutton:
                xpos 290
                ypos 828
                auto "images/jail/saw_%s.png"
                action Jump("jail_saw")
    if jail_saw_own:
        imagebutton:
            xpos 1342
            ypos 228
            auto "images/jail/chain_%s.png"
            action Jump("jail_chain")
    if not jail_pillow_relocated:
        imagebutton:
            xpos 1422
            ypos 538
            auto "images/jail/pillow_%s.png"
            action Jump("jail_pillow")
    else:
        add "images/jail/pillowed.png":
            xpos 1410
            ypos 538
        if not jail_card_own:
            imagebutton:
                xpos 1410
                ypos 538
                auto "images/jail/card_%s.png"
                action Jump("jail_card")
    if not jail_box_revealed1:
        imagebutton:
            xpos 1528
            ypos 872
            auto "images/jail/box_%s.png"
            action Jump("jail_box")
    elif jail_box_revealed1 and not jail_box_revealed2:
        add "images/jail/box_out.png":
            xpos 1344
            ypos 789
        imagebutton:
            xpos 1344
            ypos 855
            auto "images/jail/box1_%s.png"
            action Jump("jail_box")
    elif jail_box_revealed2 and not jail_box_revealed3:
        add "images/jail/box_stone.png":
            xpos 1344
            ypos 789
        imagebutton:
            xpos 1413
            ypos 855
            auto "images/jail/stone_%s.png"
            action Jump("jail_stone_cutscene")
    else:
        add "images/jail/box_empty.png":
            xpos 1344
            ypos 789
label jail_stone_cutscene:
    hide screen jail_timer
    show screen stone_aquired()
    $ renpy.pause(11, hard=True)
    $ stone_add()
    $ key_item_add("Twisted Stone")
    hide screen task_aquired
    $ jail_box_revealed3 = True
    pause 1
    jump jail_time_up

label jail_screwdriver:
    "You got a screwdriver."
    $ jail_screwdriver_own = True
    jump cavernskip
label jail_wrench:
    "You got a wrench."
    $ jail_wrench_own = True
    jump cavernskip
label jail_saw:
    "You got a saw."
    $ jail_saw_own = True
    jump cavernskip
label jail_open_hatch:
    "You unscrewed the screws."
    $ jail_hatch_opened = True
    jump cavern
label jail_hole:
    if not jail_pipe_broke:
        "A deep hole, there is something inside it..."
        $ jail_hole_checked = True
    elif jail_pipe_broke and not jail_tap_opened:
        "There is no water running inside you idiot."
    else:
        "You found something."
        "It's a hammer."
        "You got a hammer."
        $ jail_hammer_own = True
    jump cavernskip
label jail_pipe:
    "I can reroute the pipe here to fill in the hole..."
    $ jail_pipe_broke = True
    jump cavernskip
label jail_tap:
    if jail_tap_opened:
        $ jail_tap_opened = False
    elif not jail_tap_opened:
        $ jail_tap_opened = True
    jump cavernskip
label jail_mirror:
    if not jail_hammer_own:
        "It's a mirror, you can clearly see yourself without your bag."
    elif jail_hammer_own and not jail_mirror_broke:
        "You broke the mirror."
        $ jail_mirror_broke = True
        jump cavern
    else:
        if not jail_d_generated:
            $ generate_rsa_d()
            $ jail_d_generated = True
        "There is something inside."
        "It's a code: d = [rsa_d_input]."
    jump cavernskip
label jail_mat:
    $ generate_rsa_n()
    "You flipped the mat."
    "There is a code that says: n = [rsa_n_input]"
    $ jail_mat_relocated = True
    jump cavern
label jail_pillow:
    "You dislodged the pillow."
    $ jail_pillow_relocated = True
    jump cavern
label jail_card:
    $ generate_rsa_c()
    "You picked up the card."
    "It says: c = [rsa_c_input]"
    $ jail_card_own = True
    jump cavern
label jail_box:
    if not jail_box_revealed1:
        "You pulled out the box."
        "The box is relocated from its original position."
        $ jail_box_revealed1 = True
    elif jail_box_revealed1:
        "This box require a code to be opened."
        show screen jail_box_code_input
    jump cavernskip

default jail_box_code = ""     
screen jail_box_code_input():
    tag add_contact
    modal True
    zorder 210

    # semi-transparent backdrop
    add Solid("#ffffff29") xalign 0.5 yalign 0.5
    add "gui/ui_watta.png" xalign 0.5 yalign 0.5
    frame:
        xalign 0.5
        yalign 0.51
        xsize 900
        ysize 420
        background None
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5  
            text "Enter the code:" size 70 color "#000000" xalign 0.5
            hbox:
                spacing 12
                xalign 0.5
                yalign 0.5  
                input:
                    value VariableInputValue("jail_box_code")
                    length 3
                    allow "0123456789"
                    color "#000000ff"
                    size 85
                    copypaste True

            text "Digits Only, Max 3" size 28 color "#aaa" xalign 0.5
            null height 20

            hbox:
                spacing 50
                xalign 0.5

                button:
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), Hide("add_contact_screen"), Function(jail_box_code_check)]

                    text "Confirm":
                        size 60
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#c0af19"

                button:
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), SetVariable("jail_box_code", ""), Hide("jail_box_code_input")]

                    text "Cancel":
                        size 60
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#8da417"

default rsa_n_input = 0
default rsa_c_input = 0
default rsa_d_input = 0
init python:
    import random

    def _get_valid_rsa_input(value, min_value, max_value):
        if isinstance(value, (list, tuple)):
            value = value[0] if len(value) == 1 else None

        try:
            value = int(value)
        except (TypeError, ValueError):
            value = None

        if value is None or value < min_value or value > max_value:
            return random.randint(min_value, max_value)

        return value

    def rsa_m_calculating():
        c = _get_valid_rsa_input(renpy.store.rsa_c_input, 20, 50)
        d = _get_valid_rsa_input(renpy.store.rsa_d_input, 20, 50)
        n = _get_valid_rsa_input(renpy.store.rsa_n_input, 100, 999)

        renpy.store.rsa_c_input = c
        renpy.store.rsa_d_input = d
        renpy.store.rsa_n_input = n

        result = 1

        for _ in range(d):
            result = (result * c) % n

        return result

    def generate_rsa_n():
        renpy.store.rsa_n_input = random.randint(100, 999)

    def generate_rsa_c():
        renpy.store.rsa_c_input = random.randint(20, 50)

    def generate_rsa_d():
        renpy.store.rsa_d_input = random.randint(20, 50)

init python:
    def jail_box_code_check():
        global jail_box_code, jail_box_revealed2
        jail_code_raw = jail_box_code.strip()

        if not jail_code_raw:
            renpy.notify("Please enter a number.")
            return None

        try:
            jail_code = int(jail_code_raw)
        except ValueError:
            renpy.notify("Please enter a valid number.")
            return None

        
        jail_right_code = rsa_m_calculating()
        if jail_code == jail_right_code:
            renpy.notify("Code is correct.")
            jail_box_revealed2 = True
            jail_box_code = ""
            renpy.hide_screen("jail_box_code_input")

        else:
            renpy.notify("Wrong code.")

screen jail_timer(jumpto):
    # A timer that runs once. When it hits 0, Jump is called.
    timer 1.0 action If(
        jail_time_left > 0,
        true=SetVariable("jail_time_left", jail_time_left - 1),
        false=[Hide("jail_timer"), Jump(jumpto)]
    ) repeat True

label jail_chain:
    "You sawed the bedholder off."
    play sound "sfx/contraption.mp3"
    scene bg jail2 at shake
    unknown "What is that noise?"
    pause 2
    jump jail_time_up

label jail_time_up:
    hide screen jail_box_code_input
    unknown "{font=Vivi.ttf}Huh?"
    unknown "{font=Vivi.ttf}Why are you here?"
    unknown "{font=Vivi.ttf}You're not supposed to be here."
    unknown "{font=Vivi.ttf}Hold on I will open the door for you."
    pause 2
    scene bg jailfront with Fade(1,0,1)
    show vivi bruh at right
    show watta sleepyb at left
    pause 1.0
    show vivi speak at bounced
    unknown "{font=Vivi.ttf}Wait,{w=1} is this your bag? I found it hanging outside."
    show watta delighted at bounced
    w "Thank you"
    show vivi bruh
    unknown "{font=Vivi.ttf}You are... again"
    unknown "{font=Vivi.ttf}Not supposed to be here Watta."
    unknown "{font=Vivi.ttf}Who put you here?"
    show watta default
    w "Well I don't remember but..."
    show watta frown at bounced
    w "How do you know my name?"
    show vivi huh
    unknown "{font=Vivi.ttf}That isn't important for now."
    unknown "{font=Vivi.ttf}It's most possibly him again."
    show vivi frown
    unknown "{font=Vivi.ttf}I will deal with that later."
    show watta default
    w "Who?"
    unknown "{font=Vivi.ttf}..."
    w "And who are you?"
    show vivi speak at bounced
    unknown "{font=Vivi.ttf}You don't need to know my name, it's not something you should concern yourself with."
    unknown "{font=Vivi.ttf}For now, get out of here as soon as possible Watta, I hope we won't meet again."
    show watta upset
    w "What the?"
    show vivi angry
    unknown "{font=Vivi.ttf}It's urgent, do it."
    show watta wtf at bounce
    w "Oh okay alright."
    show vivi bruh
    unknown "{font=Vivi.ttf}At the end of this hallway, turn right and go all the way to the loft ladders then climb up."
    unknown "{font=Vivi.ttf}And never go back again"
    $ cavern_room = "3"
    show screen phone_toggle
    show screen map_toggle
    show screen console_toggle
    show screen inventory_display_toggle
    jump cavern


screen cavern1:
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("to_cavern2")
    imagebutton:
        xpos 32
        ypos 360
        auto "images/int/cavern_ladder_%s.png"
        action Jump("to_monument_from_cavern")
    imagebutton:
        xpos 312
        ypos 600
        auto "images/int/oil_lake_%s.png"
        action Jump("to_oil_lake")
screen cavern2:
    imagebutton:
        xpos 817
        ypos 424
        auto "images/int/cavern_log_%s.png"
        action Jump("to_cavern_log_read")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("to_cavern1")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("to_cavern3")
screen cavern3:
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("to_cavern2")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("to_cavern4")
screen cavern4:
    imagebutton:
        xpos 787
        ypos 368
        auto "images/char_int/cavern_vivi_%s.png"
        action Jump("to_vivi_cavern_promptu")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("to_cavern3")

label to_cavern1:
    $ cavern_room = "1"
    jump cavern
label to_cavern2:
    $ cavern_room = "2"
    jump cavern
label to_cavern3:
    $ cavern_room = "3"
    jump cavern
label to_cavern4:
    $ cavern_room = "4"
    jump cavern

default vivi_cavern_promptu = False
default oil_lake_cavern_found = False
label to_vivi_cavern_promptu:
    if not vivi_cavern_promptu:
        show vivi angry2
        unknown "{font=Vivi.ttf}This is not the way, it's the other way"
        $ vivi_cavern_promptu = True
    else:
        show vivi angry2
        unknown "{font=Vivi.ttf}Please don't make me do this the hard way"
    hide vivi
    jump cavernskip
label to_cavern_log_read:
    "I don't understand these languages."
    "Maybe a translator would be able to help."
    jump cavernskip
label oil_lake_first:
    show watta default at left
    w "Wow this is a..."
    w "Huge underground lake."
    w "Wait this is.."
    show watta wtf at bounce
    w "Is oil!"
    w "In such a massive amount."
    w "So crazy!"
    $ oil_lake_cavern_found = True
    hide watta
    jump cavernskip

default monument_to_cavern_unlock = False
default to_monument_from_cavern_first = False
label to_monument_from_cavern:
    if not to_monument_from_cavern_first:
        w "Let's see..."
        w "Ohh it's shut from inside."
        w "So this is a path for evacuation"
        w "I wonder how people usually get out tho"
        if phase != 3:
            scene bg monument with Fade(0.1, 0, 0.1)
        else:
            scene bg monumentn with Fade(0.1, 0, 0.1)
        pause 0.5
        show watta default
        w "Wait this is "
        show watta deter
        extend "right under the monument."
        hide watta
        "You have unlocked a pathway to the cavern, it's under the smaller gravestone like statue."
        "Actions are unlocked."
        pause 2.0
        show watta frown
        w "Wait"
        show watta shocked at shake
        w "I didnt work today."
        show watta sleepy
        w "Nvm I could just ask for a day off."
        if woogie:
            play music "bgm_woogie.mp3" fadein 1.0 
            show watta sleepy at slide_to_left
            show woogie stare at slide_in_right
            wo "Konnichiwa watashi wa hungry fella daro."
            show watta upset
            w "What? Why are you...{w=0.5}{nw}"
            w "Were you waiting here the whole time?"
            show woogie laugh2 with dissolve
            wo "In-deed."
            wo "As an elite detective, detecting is one thing but taking care of yer assistant is also important."
            wo "Such is why I can't leave ya here all alone"
            show woogie laugh
            extend " and naked."
            show watta sweat
            w "Wao you're actually caring"
            show watta upset at bounced
            w "But you should find something better to do rather than waiting here and wasting time."
            show woogie sus
            wo "Fact is I came across this area right when ya climbed outside."
            show woogie proud
            wo "So yes, no time wasted."
            show watta default
            w "Such an interesting coincidence."
            show woogie hmm
            wo "There is no such thing as a coincidence, Walrus."
            show woogie default
            wo "The fact that ya climbed out right when I arrive mean yar energetically aligned with me..."
            wo "And our detective career,"
            wo "That decided already Walrus, let us dive in."
            show watta frown
            w "Whatever.."
        hide watta
        $ actions_locked = False
        $ to_monument_from_cavern_first = True
        $ monument_to_cavern_unlock = True
        $ monument_first = True
    jump monument

label to_oil_lake:
    "Do you want to jump into the oil lake?"
    menu:
        "Do you want to jump into the oil lake?{fast}"
        "Yes":
            call screen you_died
        "No":
            jump cavernskip

label to_cavern_from_monument:
    $ cavern_room = "1"
    jump cavern
