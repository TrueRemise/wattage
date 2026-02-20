screen task_aquired(name, desc, icon):
    modal True
    zorder 200
    
    timer 5.4 action Play("sound", "sfx/task.wav")

    # Step 1: Black solid
    add Solid("#000") as black:
        at firstfade

    add "images/task/task1.png" xalign 0.5 yalign 0.5:
        at frame_appear
    add "images/task/task2.png" xalign 0.5 yalign 0.5:
        at bg_top_slide

    add "images/task/taskl2.png":
        at door_left2
    add "images/task/taskr2.png":
        at door_right2
        

    add "images/task/taskl2.png":
        at door_left2
    add "images/task/taskr2.png":
        at door_right2

    # Step 1.5: Doorframes
    add "images/task/taskl.png":
        at door_left

    add "images/task/taskr.png":
        at door_right
    # Step 4: Textbox (under top part)  
    frame:
        background None
        xalign 0.5
        yalign 0.822
        xsize 1400
        ysize 200
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            # Step 5: Icon
            add icon xalign 0.5 ypos -285:
                at icon_fade
        
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 20
            # Step 6 + 7: Headline and description
            text name:
                font "fonts/Day.ttf"
                size 80
                color "#FFFFFF"
                xalign 0.5
                at headline_fade

            text desc:
                font "fonts/Day.ttf"
                size 50
                color "#CCCCCC"
                xalign 0.5
                at desc_fade
    timer 13.0 action Hide("task_aquired")

# --- TRANSFORMS ---
transform frame_appear:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 9.0
    linear 1.0 alpha 0.0
transform bg_top_slide:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 2.0
    ease 3 ypos 0.7
    pause 4.0
    linear 1.0 alpha 0.0
transform door_left:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 0.5
    xpos 0
    ease 2 xpos -0.5
transform door_right:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 0.5
    xpos 1
    ease 4 xpos 1.5
transform door_left2:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 2.5
    xpos 0
    ease 3.9 xpos -0.5

transform door_right2:
    alpha 0.0
    pause 2.0
    alpha 1.0
    pause 2.5
    xpos 1
    ease 7.5 xpos 1.5

transform textbox_reveal:
    alpha 0.0
    pause 6.0
    linear 3.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0
transform icon_fade:
    alpha 0.0
    pause 6.0
    linear 3.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0

transform headline_fade:
    alpha 0.0
    pause 5.4
    linear 1.0 alpha 1.0
    pause 4.6
    linear 1.0 alpha 0.0

transform desc_fade:
    alpha 0.0
    pause 6.2
    linear 1.0 alpha 1.0
    pause 3.8
    linear 1.0 alpha 0.0

transform firstfade:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 10.5
    linear 1.5 alpha 0.0
transform lastfade:
    alpha 0.0
    pause 12
    linear 1.5 alpha 1.0
transform longfade:
    pause 13.0
    linear 1.0 alpha 0.0



screen stone_aquired():
    modal True
    zorder 200
    
    timer 2.04 action Play("sound", "sfx/upgrade1.wav")
    timer 4.8 action Play("sound", "sfx/buildup.wav")
    timer 6.0 action Play("sound", "sfx/upgrade2.wav")

    # Step 1: Black solid
    add Solid("#000") as black:
        at firstfade_sooner

    add "images/task/stone.png" xalign 0.5 yalign 0.5:
        at frame_fadein_and_later_die

    add "images/task/stone_cage1_a.png" xalign 0.5 yalign 0.5:
        at frame_fadein_later_and_shake_and_die_a
    
    add "images/task/stone_cage1_b.png" xalign 0.5 yalign 0.5:
        at frame_fadein_later_and_shake_and_die_b

    add Solid("#ffffff") as white:
        at white_jumpscare

    add "images/task/stone_cage2.png" xalign 0.5 yalign 0.5:
        at frame_jumpscare_later_and_shake

    add "images/task/stone_bg.png" xalign 0.5 yalign 0.5:
        at frame_jumpscare_later_and_fade_into_dust

    add "images/task/stone.png" xalign 0.5 yalign 0.5:
        at frame_resurrection_from_the_ashes

    # Step 4: Textbox (under top part)  
    frame:
        background None
        xalign 0.5
        yalign 0.822
        xsize 1400
        ysize 200
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 20
            # Step 6 + 7: Headline and description
            text "Twinned Fragment Acquired":
                font "fonts/Day.ttf"
                size 80
                color "#FFFFFF"
                xalign 0.5
                at headline_fade_faster

            text "Actions Permanently Boosted by 1":
                font "fonts/Day.ttf"
                size 50
                color "#CCCCCC"
                xalign 0.5
                at desc_fade_faster
    timer 13.0 action Hide("stone_aquired")

# --- TRANSFORMS ---
transform firstfade_sooner:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 10.5
    linear 1.5 alpha 0.0
transform frame_fadein_and_later_die:
    alpha 0.0
    pause 2.0
    linear 0.2 alpha 1.0
    pause 3.8
    linear 1.0 alpha 0.0
transform frame_fadein_later_and_shake_and_die_a:
    alpha 0.0
    pause 3.0
    linear 1.0 alpha 1.0
    pause 1.1
    xoffset 1
    yoffset 1
    pause 0.1
    xoffset -1
    yoffset -1
    pause 0.1
    xoffset 2
    yoffset -2
    pause 0.1
    xoffset -2
    yoffset 2
    pause 0.1
    xoffset -4
    yoffset 4
    pause 0.1
    xoffset -6
    yoffset -6
    pause 0.1
    xoffset -10
    yoffset -10
    pause 0.1
    xoffset 12
    yoffset -12
    pause 0.1
    xoffset 0
    yoffset 0
    pause 0.1
    xoffset 10
    yoffset -10
    pause 0.1
    linear 0.0 alpha 0.0
transform frame_fadein_later_and_shake_and_die_b:
    alpha 0.0
    pause 3.0
    linear 1.0 alpha 1.0
    pause 1.0
    xoffset -1
    yoffset -1
    pause 0.1
    xoffset 1
    yoffset -1
    pause 0.1
    xoffset -2
    yoffset 2
    pause 0.1
    xoffset 2
    yoffset 2
    pause 0.1
    xoffset 4
    yoffset -4
    pause 0.1
    xoffset 6
    yoffset 6
    pause 0.1
    xoffset -5
    yoffset -5
    pause 0.1
    xoffset -8
    yoffset 8
    pause 0.1
    xoffset 0
    yoffset 0
    pause 0.1
    xoffset -8
    yoffset 8
    pause 0.2
    linear 0.0 alpha 0.0
transform white_jumpscare:
    alpha 0.0
    pause 6.0
    alpha 1.0
    linear 1.0 alpha 0.0
transform frame_jumpscare_later_and_shake:
    alpha 0.0
    pause 6.0
    alpha 1.0
    xoffset 4
    yoffset 4
    pause 0.1
    xoffset -4
    yoffset -4
    pause 0.1
    xoffset 2
    yoffset 2
    pause 0.1
    xoffset -2
    yoffset -2
    pause 0.1
    xoffset 0
    yoffset 0
    pause 4.6
    linear 1.0 alpha 0.0
transform frame_jumpscare_later_and_fade_into_dust:
    alpha 0.0
    pause 6.0
    alpha 1.0
    linear 1.0 alpha 0.5
    pause 4.0
    linear 1.0 alpha 0.0
transform frame_resurrection_from_the_ashes:
    alpha 0.0
    pause 6.0
    alpha 1.0
    xoffset 4
    yoffset -4
    pause 0.1
    xoffset -4
    yoffset 4
    pause 0.1
    xoffset -2
    yoffset 2
    pause 0.1
    xoffset 2
    yoffset -2
    pause 0.1
    xoffset 0
    yoffset 0
    pause 4.6
    linear 1.0 alpha 0.0
transform headline_fade_faster:
    alpha 0.0
    pause 7.4
    linear 1.0 alpha 1.0
    pause 2.6
    linear 1.0 alpha 0.0
transform desc_fade_faster:
    alpha 0.0
    pause 8.2
    linear 1.0 alpha 1.0
    pause 1.8
    linear 1.0 alpha 0.0


screen new_area_unlocked(location):
    modal True
    zorder 200
    
    timer 1 action Play("sound", "sfx/upgrade1.wav")

    # Step 1: Black solid

    add Solid("#ffffff") as white:
        at white_jumpscare_2

    add "images/task/location_boom.png" xalign 0.5 yalign 0.5:
        at boom_jumpscare

    add ("images/task/location_%s.png" % location) xalign 0.5 yalign 0.5:
        at only_fade_after_a_while

    frame:
        background None
        xalign 0.5
        yalign 0.822
        xsize 1400
        ysize 200
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 20
            # Step 6 + 7: Headline and description
            text "[location] unlocked":
                font "fonts/Day.ttf"
                size 80
                color "#FFFFFF"
                xalign 0.5
                at headline_fade_fasterer

            text "Accessible Through the Map":
                font "fonts/Day.ttf"
                size 50
                color "#CCCCCC"
                xalign 0.5
                at desc_fade_fasterer
    timer 8.0 action Hide("new_area_unlocked")

transform white_jumpscare_2:
    alpha 0.0
    pause 1.0
    alpha 1.0
    linear 0.5 alpha 0.0
transform boom_jumpscare:
    alpha 0.0
    pause 1.0
    alpha 1.0
    linear 0.6 alpha 0.0
transform headline_fade_fasterer:
    alpha 0.0
    pause 2.4
    linear 1.0 alpha 1.0
    pause 2.6
    linear 1.0 alpha 0.0
transform desc_fade_fasterer:
    alpha 0.0
    pause 3.4
    linear 1.0 alpha 1.0
    pause 1.6
    linear 1.0 alpha 0.0
transform only_fade_after_a_while:
    alpha 0.0
    pause 1
    alpha 1.0
    pause 5
    linear 1.0 alpha 0.0