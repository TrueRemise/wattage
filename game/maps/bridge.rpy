label bridge:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    play music "bgm_bridge.mp3" fadein 1.0 if_changed
    jump bridgeskip

label bridgeskip:
    # Automatically load background with a smooth transition
    $ current_location = "bridge"
    if phase != 3:
        scene bg bridge with Fade(0.1, 0, 0.1)
    else:
        scene bg bridgen with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    if (current_weekday, current_phase) in bridge_events:
        jump expression bridge_events[(current_weekday, current_phase)]
    else:
        jump bridgedef

define bridge_events = {
    ("Mon", "Dawn"): "bridgedef"
}

label bridgedef:
    if bridge_first == False:
        jump bridge_ft
    else:
        call screen bridge
    return
label bridge_ft:
    show watta default
    w "It's the bridge, I have just been here once since"
    w "People are calling it the Halfbridge for some reason."
    if woogie == True:
        show watta default at slide_to_left
        show woogie laugh2 at slide_in_right
        wo "Because it's made under 2 rulers"
        w "There are 2 rulers of this land?"
        wo "Sound like ya need some history 101 knowledge"
        w "Well..."
        wo "Won't be fun if im intruding all the time tho, I'll let ya figure it out on yer own"
        show watta upset
        w "Why are you turning this into a game?"
        hide woogie
    hide watta
    $ bridge_first = True
    jump bridgedef

screen bridge:
    imagebutton:
        xpos 1070
        ypos 555
        auto "images/int/bridge_side_%s.png"
        action Jump("underbridge")
    imagebutton:
        xpos 0
        ypos 510
        auto "images/int/bloomfield_%s.png"
        action Jump("northgate")

label underbridge:
    $ current_location = "underbridge"
    scene bg underbridge with Fade(0.1, 0, 0.1)
    jump underbridgeskip
label underbridgeskip:
    play music "bgm_bridge.mp3" fadein 1.0 if_changed
    call screen underbridge

screen underbridge:
    if nemu_lend_done == False:
        imagebutton:
            xpos 1225
            ypos 6
            auto "images/char_int/nemu_bridge_%s.png"
            action Jump("nemu_test")
    if nemu_first_talk_done_stage == 3:
        imagebutton:
            xpos 1125
            ypos 6
            auto "images/char_int/nemu_bridge_2_%s.png"
            action Jump("nemu_test")
    if nemu_first_talk_done_stage == 4 and is_item_get("Hydrophobic Lubricant"):
        imagebutton:
            xpos 1245
            ypos 0
            auto "images/int/bridge_to_lane_%s.png"
            action Jump("bridge_to_lane")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("bridgeskip")
    

    
label northgate:
    $ current_location = "northgate"
    stop music fadeout 0.5
    play music "bgm_gate.mp3" fadein 1.0
    if phase != 3:
        scene bg northgate with Fade(0.1, 0, 0.1)
    else:
        scene bg northgaten with Fade(0.1, 0, 0.1)
    jump northgateskip
label northgateskip:
    call screen northgate
screen northgate:
    imagebutton:
        xpos 883
        ypos 273
        auto "images/int/northgate_%s.png"
        action Jump("northgate_test") 
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("bridge")

label northgate_test:
    if phase == 0 or phase == 1:
        jump tsuyu_test
    else:
        jump iog_gate

label iog_gate:
    play music "bgm_iog.mp3"
    show bg blowey
    show iog default at right
    show watta default at left
    "" "{p}"
    iog "hot dog"
    call is_shaky_choice_disclaimer from _call_is_shaky_choice_disclaimer
    if is_unlocked("field"):
        call screen iog_gate_2
    call screen iog_gate


screen iog_gate():
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
                at hover_action
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Jump("iog_gate_check")
                text "Pay 200 to gain access":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("northgate")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
screen iog_gate_2():
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
                at hover_action
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Function(move_to,"field")
                text "Move in Bloomfield":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("northgate")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"

image bg eleva = Movie(play="images/eleva.webm", loop=True, size=(1920,1080))
label iog_gate_check:
    if sol >= 200:
        $ sol -= 200
        iog "hot dog"
        label gate_jump:
        show black with Fade(1, 0, 0)
        hide iog
        hide watta
        hide tsuyu
        show screen bloomfield_entrance with Fade(0, 0, 1)
        $ renpy.pause(5.7)    # 4s wait + 0.7 animation
        hide screen bloomfield_entrance
        stop music fadeout 0.5
        play music "bgm_field.mp3" fadein 1.0
        scene bg bloom2 with Fade(0.3, 0, 0.3)
        w "Wao! This is my first time in a place like this"
        w "Is.... {w=0.5}hugeee!"
        scene bg bloom3 with Fade(0.3, 0, 0.3)
        play sound "sfx/walking.mp3"
        pause 3.0
        scene bg bloom4 with Fade(0, 0, 0)
        play sound "sfx/door_open.mp3"
        pause 3.0
        stop music fadeout 0.5
        play music "bgm_sari.mp3" fadein 1.0
        scene bg eleva with Fade(0.1,0,0.1)
        show screen eleva_skipper  
        $ _skipping = False
        $ renpy.pause(2, hard=True)
        "Welcome to the elevator."
        $ renpy.pause(2, hard=True)
        "This time the journey to Bloomfield."
        $ renpy.pause(5, hard=True)
        "..."
        $ renpy.pause(5, hard=True)
        "This elevator seems kind of long isn't it?"
        $ renpy.pause(5, hard=True)
        "Where is the cut?"
        $ renpy.pause(2, hard=True)
        "Well..."
        $ renpy.pause(2, hard=True)
        "While we wait, let me tell you a story."
        $ renpy.pause(2, hard=True)
        "A story about bravery, courageousness and valor."
        $ renpy.pause(2, hard=True)
        "100 years ago, in this very land."
        $ renpy.pause(2, hard=True)
        "There were 2 queens."
        $ renpy.pause(2, hard=True)
        "One known for kindness, "
        extend "the other for her virtue."
        $ renpy.pause(2, hard=True)
        "Huh?"
        extend " You don't want to hear stories?"
        extend " And just want this elevator to end as soon as possible?"
        "Well truth is... "
        extend "So do I."
        $ renpy.pause(2, hard=True)
        "But would you rather sit through all of this alone or at least with me?"
        "No?"
        "You want me to hijack the code?"
        "Let me try."
        $ renpy.pause(5, hard=True)
        "I'm back, but I'm sad to say..."
        extend "I was not permitted to do that."
        extend " Unfortunate."
        "However, on the way back I bought a creampuff, want to try it?"
        "Oh yeah, I can't {w=0.5}interact with you."
        "I'm just a{w=0.5} you know, {w=0.5}narrator."
        "Hmm."
        $ renpy.pause(5, hard=True)
        "Got some news."
        "The developer said he messed up the code."
        "So... this scene will play indefinitely."
        "But... {w=0.5}he seems to be working on a skipping code."
        "He said pressing \"E\" while on it will trigger emergence exit."
        "He also said he set that key to skip the elevator from the very start?"
        "This is terrible..."
        "Well."
        $ renpy.pause(5, hard=True)
        "What are you waiting for? Press \"E\" now."
        $ renpy.pause(5, hard=True)
        "{size=+15}Press{w=1} \"E\" {w=1}now."
        $ renpy.pause(5, hard=True)
        "Do you not know where the E key is on your keyboard?"
        extend " It's to the left of the R key, to the right of the W key, above D key and below either 3 or 4 {w=2}I'm not an expert."
        $ renpy.pause(2, hard=True)
        "{size=+35}PRESS THE KEY!"
        $ renpy.pause(5, hard=True)
        "Oh I get you now, you just want to enjoy the background music huh?"
        "Well too bad you can enjoy the same song inside Sari's van, so we have no reason to be here. {w=5}Press E to skip the elevator."
        $ renpy.pause(10, hard=True)
        "You just want to mess with me don't you?"
        "Very well..."
        $ renpy.pause(10, hard=True)
        "I'm sorry I swear I will be better!"
        "Please don't let me wait forever."
        "Are you even there? HEY!!"
        "Why can I only text, this brokeass dev cannot even hire a voice actor for his game. I want to scream but I have no voice!!"
        $ renpy.pause(5, hard=True)
        "Damn the player went AFK."
        "Whatever..."
        "I'll play League"
        $ renpy.pause(30, hard=True)
        "Hold on what?"
        "Oh you fixed it."
        "Finally"
        "You felt bad for me?"
        "Awww"
        "Okay let's get to work"
        jump eleva_end_skip
        label eleva_end:
        "See you.{w=1}{nw}"
        label eleva_end_skip:
        show black with Fade(3, 0, 0)
        stop music fadeout 3
        $ renpy.pause(2, hard=True)
        hide screen eleva_skipper
        $ _skipping = True
        show screen new_area_unlocked("Bloomfield")
        $ renpy.pause(7, hard=True)
        hide screen new_area_unlocked
        $ renpy.pause(2, hard=True)
        play sound "sfx/ding_dong.mp3"
        $ renpy.pause(2, hard=True)
        play music "bgm_field.mp3" fadein 3
        if phase != 3:
            scene bg field with Fade(0., 0, 3)
        else:
            scene bg fieldn with Fade(0, 0, 3)
        $ renpy.pause(3, hard=True)
        w "This place."
        w "So this is Bloomfield"
        if chii_talked_about_bloomfield == True:
            w "This is the place Chii talked about..."
        w "Interesting..."
        w "That store named Floralia, that's Sanco house."
        w "I should go check it out."
        
        $ loc_unlock("field")
        $ field_first = True
        $ action_done()
        $ current_location = "field"
        call screen field
    else:
        iog "hot dog"
        jump northgate
        
screen eleva_skipper():
    key "K_e" action Jump("eleva_end")

screen bloomfield_entrance():
    modal True
    fixed:
        # Background
        add "bg/bloom/bg bloom1.png"
        # Animated gate
        add "bg/bloom/bg bloom1_a.png" at gate_anim
        add Solid("#000") at fade_in_bloomfield
    timer 8.0 action Hide("bloomfield_entrance")
transform gate_anim:
    xpos 1735
    ypos 850
    anchor (0.974, 0.5)       # set anchor to 90% right, 50% vertical
    transform_anchor True   # important: rotate around the anchor
    rotate 0
    pause 2
    ease_cubic 6 rotate 90
transform fade_in_bloomfield:
    alpha 0.0
    pause 7
    linear 1.0 alpha 1.0

default bridge_from_island_first = False
label bridge_from_island:
    if bridge_from_island_first == False:
        $ current_location = "bridge"
        if phase != 3:
            scene bg bridge with Fade(0.1, 0, 0.1)
        else:
            scene bg bridgen with Fade(0.1, 0, 0.1)
        show watta shocked at left
        w "Oh what?"
        w "Never thought riding the river randomly would bring me here..."
        $bridge_from_island_first = True
        hide watta
    jump bridge

