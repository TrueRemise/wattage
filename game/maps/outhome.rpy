label outhome:
    $ current_weekday = get_day(day)        # e.g. "Mon"
    $ current_phase = phases[phase]         # e.g. "Night"

    # Update and store correct background for this phase
    $ bg_image = update_world_bg()

    # Music setup
    stop music fadeout 0.5
    play music "bgm_outhome.mp3" fadein 1.0
    jump outhomeskip

label outhomeskip:
    # Automatically load background with a smooth transition
    $ current_location = "outhome"
    if phase != 3:
        scene bg outhome with Fade(0.1, 0, 0.1)
    else:
        scene bg outhomen with Fade(0.1, 0, 0.1)
    # --- Event jump logic ---
    if (current_weekday, current_phase) in outhome_events:
        jump expression outhome_events[(current_weekday, current_phase)]
    else:
        jump outhomedef


define outhome_events = {
    ("Mon", "Dawn"): "opening",
    ("Tue", "Dawn"): "opening_2",
    ("Wed", "Dawn"): "opening_3",
    ("Thu", "Dawn"): "opening_4",
}

label outhomedef:
    call screen outhome
    return
default prologue_done = False
label opening:
    if prologue_done == True:
        jump opening2
    else:
        jump opening1 #in remi.rpy

screen remi_1_skipper():
    key "K_e" action Jump("remi_1_end")

label opening2:
    call screen outhome
    return
default bike_vis = True
default home_from_outhome = False
screen outhome:
    imagebutton:
        xpos 1180
        ypos 175
        auto "images/int/backyard_%s.png"
        action Jump("backyard")
    imagebutton:
        xpos 1711
        ypos 192
        auto "images/int/backhome_%s.png"
        action [
            SetVariable("home_from_outhome", True),
            Jump("home")
        ]
    if bike_vis == True:
        imagebutton:
            xpos 1375
            ypos 162
            auto "images/int/bike_%s.png"
            action Jump("bike")

label bike:
    show watta happy at right
    w "My old bike, I used it to commute to school."
    show watta frown
    w "Huh?"
    w "Who attached a map to it?"
    show watta hype
    w "Guess I'm using it..."
    hide watta
    "You have unlocked the map and fast travel"
    "Press M to open the map and pick location for traveling"
    "For now you can only travel to adjacent locations"
    "Each day there will be 5 phases, from dawn to midnight"
    "You will have 3 actions to do each phase before switching to the next phase (check under your Q menu)"
    "IF the phase is midnight, you will be sent to your home to do 1 action before sleeping"
    "Traveling will cost one of your actions"
    "Some quests might take one of your actions"
    "Good luck and have fun exploring"
    show screen action_display
    $ bike_vis = False
    $ map_unl = True
    show screen map_toggle
    jump opening2

default backyard_firsttime = True
default backyard_tomato_planted = 0
label backyard:
    $ current_location = "backyard"
    if backyard_firsttime == True:
        scene bg garden with fade
        show watta happy
        w "A garden I got from the previous owner."
        show watta huh
        w "I have nothing in it but a pot, though."
        hide watta
        $ backyard_firsttime = False
        if is_item_get("Pack O' Seeds"):
            jump backyard_has_seeds
        call screen backyard
    if is_item_get("Pack O' Seeds"):
        label backyard_has_seeds:
        scene bg garden with fade
        w "Let me plant a tomato..."
        w "Okay..."
        w "It should grow on its own..."
        hide watta
        $ backyard_tomato_planted = 1
        $ item_remove("Pack O' Seeds")
    if backyard_tomato_planted == 3:
        scene bg gardeng with Fade(0.1, 0, 0.1)
        call screen backyard
    else:
        scene bg garden with Fade(0.1, 0, 0.1)
        call screen backyard
default tomato_home_vis = True
screen backyard:
    if backyard_tomato_planted == 3 and tomato_home_vis:
        imagebutton:
            xpos 1006
            ypos 388
            auto "images/int/tomato_home_%s.png"
            action [Function(item_add, "Homegrown Tomatoes"), SetVariable("tomato_home_vis", False)]
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("outhomeskip")


default prologue_done_2 = False
label opening_2:
    if prologue_done_2 == True:
        jump opening2
    else:
        jump opening1_2

label opening1_2:
    $ cutscene_on = True
    show watta default
    w "Ugh.."
    if the_knower >= 1:
        w "A lot to keep track of yesterday."
        w "I still have no idea what Remi meant."
        w "Hope to see him again today..."
        w "Also"
    w "It's day 2 already,"
    if the_knower == 1 or fish_tutorial_done or bailey_first_talk_done_stage == 2 or sanco_about_blood:
        w "I feel like I did a lot yesterday..."
        w "Oh well, gotta stay active today as well."
    else:
        w "I feel like I did nothing yesterday..."
        w "Might as well have bedrotted all day..."
    "*puff*"
    w "Huh?"
    w "A flyer?"
    w "Strange, this is the first time someone dropped a flyer here."
    w "Let's see!"
    hide watta
    show bg neko0 with dissolve
    w "Concert today?"
    w "Wao, a rare occassion so why not check it out I guess?"
    w "Hope I can get to see some familiar faces"
    show screen day_trans("Day 2")
    $ renpy.pause(9.0, hard=True)
    show bg outhome with dissolve
    hide screen day_trans
    $ prologue_done_2 = True
    $ cutscene_on = False
    jump outhome

default prologue_done_3 = False
label opening_3:
    if prologue_done_3 == True:
        jump opening2
    else:
        jump opening1_3

label opening1_3:
    $ cutscene_on = True
    show watta default
    w "Ugh.."
    if neko_invitation:
        w "Neko invited to come and watch her performance today,"
        w "Should check it out."
    show watta default at slide_to_right
    show iog default at slide_in_left
    w "Huh?"
    iog "hot dog"
    show watta frown
    w "Hot dog?"
    iog "hot dog"
    show watta upset
    w "Haa??"
    iog "hak dog"
    show watta shocked
    w "WHAT?"
    scene bg black with Fade(0.1,0,0.5)
    hide watta
    hide iog
    show screen day_trans("Day 3")
    $ renpy.pause(9.0, hard=True)
    show bg outhome with dissolve
    hide screen day_trans
    "they moved"
    $ prologue_done_3 = True
    $ cutscene_on = False
    jump outhome


default prologue_done_4 = False
label opening_4:
    if prologue_done_4 == True:
        jump opening2
    else:
        jump opening1_4

label opening1_4:
    $ cutscene_on = True
    show watta default
    w "Ugh"
    w "Which day is it again?"
    scene bg black with Fade(0.1,0,0.5)
    hide watta
    show screen day_trans("Day 4")
    $ renpy.pause(9.0, hard=True)
    show bg outhome with dissolve
    hide screen day_trans
    if reni_phone_intro_done:
        $ set_message_phase("Renia", "aloy_back", one_time=True, notify=True)
    $ prologue_done_4 = True
    $ aloy_unlock = True
    $ cutscene_on = False
    jump outhome