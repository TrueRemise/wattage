default phone_open = False
default charged = False
default map_unl = False
default actions_locked = False
default all_locked = False

screen phone_toggle():
    zorder 92
    if phone_found == True:
        # Open/close phone with TAB (you can change to P if you want)
        key "K_q":
            action If(
                not all_locked and not cutscene_on,
                [   
                    ToggleScreen("phone_screen"),
                    SetVariable("phone_open", not phone_open),
                    Hide("map_screen"),
                    Hide("notebook_screen"),
                    SetVariable("map_open", False)
                ],
                Function(renpy.notify, "You can't open the phone right now.")
                )

        # Small HUD button
        imagebutton auto "gui/phn_%s.png" xpos 0.957 ypos 0.075:
            action If(
                not all_locked and not cutscene_on,
                [   
                    ToggleScreen("phone_screen"),
                    SetVariable("phone_open", not phone_open),
                    Hide("map_screen"),
                    Hide("notebook_screen"),
                    SetVariable("map_open", False)
                ],
                Function(renpy.notify, "You can't open the phone right now.")
                )
    else:
        key "K_q" action Function(press_q_without_phone)
init python:
    def press_q_without_phone():
        renpy.notify("I don't have my phone with me yet")
screen phone_screen():
    modal True
    tag phone


    if charged == False:
        add "gui/phone_low_bg.png" xalign 0.5 yalign 0.5
    else:
        add "gui/phone_bg.png" xalign 0.5 yalign 0.5

        # --- Phase & actions display ---
        
        frame:
            background None
            xpos 1156
            ypos 800
            vbox:
                xanchor 1.0
                xpos 0.32
                ypos 0.02
                spacing 15
                text (current_location).upper() color "#000" size 50
            vbox:
                spacing 3
                yalign 0.01

                # Phase image (switches by phase index)
                if day == 1:
                    add "gui/day_1.png"
                elif day == 2:
                    add "gui/day_2.png"
                elif day == 3:
                    add "gui/day_3.png"
                elif day == 4:
                    add "gui/day_4.png"
                elif day == 5:
                    add "gui/day_5.png"
                elif day == 6:
                    add "gui/day_6.png"
                elif day == 7:
                    add "gui/day_7.png"
                
                # Phase image (switches by phase index)
                if phase == 0:
                    add "gui/dawn.png"
                elif phase == 1:
                    add "gui/noon.png"
                elif phase == 2:
                    add "gui/dusk.png"
                elif phase == 3:
                    add "gui/night.png"
                elif phase == 4:
                    add "gui/midn.png"
                
                null height 2

                #Action left indicator
                hbox:
                    spacing 6.7

                    for i in range(max_actions):
                        if i < actions_left:
                            add "gui/act_on.png"
                        else:
                            add "gui/act_off.png"
                    
                null height -2

                text "   [sol]" color "#000" size 60 xalign 0.0

        # --- Debug button (force action drain) ---
        imagebutton auto "gui/doze_%s.png" xpos 1520 ypos 880:
            action If(
                    not actions_locked,
                    [
                        Function(action_done)
                    ],
                    Function(renpy.notify, "You can't sleep here.")
                )

        # --- Map button if unlocked ---
        if map_unl:
            imagebutton auto "gui/map_%s.png" xpos 1500 ypos 500:
                action If(
                    not actions_locked or youcanonlygotosanco,
                    [
                        Hide("phone_screen"),
                        Show("map_screen"),
                        SetVariable("map_open", True),
                        SetVariable("phone_open", False)
                    ],
                    Function(renpy.notify, "You can't open the map right now.")
                )
        imagebutton auto "gui/message_%s.png" xpos 1170 ypos 166:
            action If(
                not actions_locked,
                [
                    Function(renpy.call_in_new_context, "open_messages"),
                    Hide("phone_screen"),
                    SetVariable("phone_open", False),
                ],
                Function(renpy.notify, "You can't message right now.")
                )
        if puppy_count > 0:
            imagebutton auto "gui/puppy_%s.png" xpos 1170 ypos 111:
                action If(
                    not actions_locked,
                    [
                        If(not actions_left == max_actions,
                        [
                            Function(action_add),
                            SetVariable("puppy_count", max(0, puppy_count - 1)),
                        ],
                        Function(renpy.notify, "You are full.")
                        )
                    ],
                    Function(renpy.notify, "You can't eat right now.")
                    )
            text "[puppy_count]" xpos 1254 ypos 111 size 50 color "#000"
        if dog_count > 0:
            imagebutton auto "gui/dog_%s.png" xpos 1284 ypos 111:
                action If(
                    not actions_locked,
                    [
                        If(actions_left < max_actions,
                        [
                            Function(action_add),Function(action_add),Function(action_add),
                            SetVariable("dog_count", max(0, dog_count - 1)),
                        ],
                        If(actions_left == max_actions,
                        [
                            Function(renpy.notify, "You can't eat more dog.")
                        ],
                        ),
                        
                        ),
                    ],
                    Function(renpy.notify, "You can't eat right now.")
                    )
            text "[dog_count]" xpos 1369 ypos 111 size 50 color "#000"

        imagebutton auto "gui/work_%s.png" xpos 1170 ypos 500:
            action If(
                not actions_locked,
                [
                    Function(do_work),
                ],
                Function(renpy.notify, "You can't work right now.")
                )

    
    frame:
        background "#00000000"
        xpos 100
        ypos 240
        xsize 935
        ysize 770
        vbox:
            xpos 0.0
            ypos 0.0
            spacing 15
            if quests:
                for q in quests.values():
                    hbox:
                        spacing 10
                        add q["image"] xsize 50 ysize 50
                        text q["desc"] color "#000000" size 50 font "fonts/Terraria.ttf"
            else:
                text "        No active quests" color "#000000" size 80 xalign 0.5 font "fonts/Terraria.ttf"

    # Close with ESC or right-click
    key "K_ESCAPE" action [Hide("phone_screen"), SetVariable("phone_open", False)]

init python:
    def do_work():
        global first_work

        if actions_locked:
            renpy.notify("You can't work right now.")
            return

        if first_work:
            # First morning shift — doesn’t cost an action, unlocks the day
            renpy.notify("You should do your first shift from office")
        else:
            # Normal work after morning shift — costs an action
            sol_add(25)
            action_done()
            renpy.notify("You earned 25 sol.")
    
