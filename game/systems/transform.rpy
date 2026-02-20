# transforms.rpy
# Common character movement / effects
screen blackout():
    zorder 200  # above everything, even dialogue box
    modal True  # blocks clicks
    add Solid("#000") as black:
        at black_fade
    timer 2.0 action Hide("blackout")

screen day_trans(day_text):
    modal True
    zorder 200

    add Solid("#000") as black:
        at fade_in_and_out

    text day_text:
        font "fonts/Day.ttf"
        size 100
        color "#FFFFFF"
        xalign 0.5
        yalign 0.55
        at fade_in_delayed_day

    $ day_number = int(day_text.split()[1])

    text "[8 - day_number] days left until the festival":
        font "fonts/Day.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.56
        at fade_in_delayed
    timer 9.0 action Hide("day_trans")

screen day_trans_suspense(day_text):
    modal True
    zorder 200

    add Solid("#ffffff") as black:
        at fade_out
    add Solid("#000") as black:
        at fade_no_in_and_out
    timer 0.1 action [Play("sound", "sfx/night_start.mp3")]
    timer 0.4 action [Play("audio", "sfx/suspense.mp3")]
    timer 3 action [Play("music", "audio/bgm_cavern.mp3")]
    text day_text:
        font "fonts/Day.ttf"
        size 100
        color "#FFFFFF"
        xalign 0.5
        yalign 0.55
        at fade_in_no_delayed_day
    $ day_number = int(day_text.split()[1])
    text "[8 - day_number] days left until the festival":
        font "fonts/Day.ttf"
        size 40
        color "#FFFFFF"
        xalign 0.5
        yalign 0.56
        at fade_in_delayed
    timer 9.0 action Hide("day_trans_suspense")


transform black_fade:
    alpha 0.0
    linear 1 alpha 1.0   # fade in quickly

transform shake:
    linear 0.05 xoffset 15
    linear 0.05 xoffset -15
    linear 0.05 xoffset 0
    repeat 5
transform shaker:
    linear 0.05 xoffset -15
    linear 0.05 xoffset 15
    linear 0.05 xoffset 0
    repeat 5

transform bounce:
    easeout 0.2 yoffset -40
    easein 0.2 yoffset 0
    repeat 2
transform bounced:
    easein 0.3 yoffset 40
    easeout 0.3 yoffset 0

transform left:
    alpha 0.0
    xalign 0.1
    yalign 1.0
    ease 0.3 alpha 1.0

transform right:
    alpha 0.0
    xalign 0.9
    yalign 1.0
    ease 0.3 alpha 1.0
transform slide_in_left:
    xalign -0.5
    yalign 1.0
    ease 0.6 xalign 0.1

transform slide_in_right:
    yalign 1.0
    xalign 1.5
    ease 0.5 xalign 0.9
transform slide_in_right_edge:
    yalign 1.0
    xalign 1.5
    ease 0.6 xalign 1.1

transform slide_left_to_right:
    xalign -0.7
    yalign 1.0
    ease 0.5 xalign 2.0
transform slide_right_to_left:
    xalign 2.0
    yalign 1.0
    ease 0.5 xalign -0.7
transform slide_to_right:
    ease 0.6 xalign 0.9
transform slide_to_right_edge:
    ease 0.6 xalign 0.99
transform slide_to_left:
    ease 0.6 xalign 0.1
transform slide_to_left_edge:
    ease 0.6 xalign 0.0
transform slide_to_mid:
    ease 0.6 xalign 0.5
transform slide_to_mid_left:
    ease 0.6 xalign 0.35

transform slide_out_left:
    ease 0.6 xalign -0.9

transform slide_out_right:
    ease 0.5 xalign 1.9

transform slide_back:
    ease 0.6 xalign 0.5

transform fade_in:
    alpha 0.0
    linear 0.5 alpha 1.0
transform fade_in_slowly:
    alpha 0.0
    linear 2.5 alpha 1.0

transform fade_out:
    linear 0.5 alpha 0.0

transform fade_in_left:
    xalign -0.4
    yalign 1.0
    alpha 0.0
    parallel:
        ease 1 alpha 1.0
    parallel:
        ease 1 xalign 0.1

transform fade_in_right:
    yalign 1.0
    xalign 1.4
    alpha 0.0
    parallel:
        ease 1 alpha 1.0
    parallel:
        ease 1 xalign 0.9


transform pulse:
    ease 0.25 zoom 1.2
    ease 0.25 zoom 1.0
    repeat 2

transform fade_in_and_out:
    alpha 0.0
    linear 2.0 alpha 1.0
    pause 5.0
    linear 2.0 alpha 0.0

transform fade_no_in_and_out:
    alpha 0.0
    pause 0.1
    alpha 1
    pause 7.0
    linear 2.0 alpha 0.0

transform fade_in_delayed_day:
    alpha 0.0
    pause 2.0
    linear 1.0 alpha 1.0
    ease_cubic 1.5 yoffset -70
    pause 2.5   
    linear 1.0 alpha 0.0

transform fade_in_no_delayed_day:
    alpha 1.0
    pause 3
    ease_cubic 1.5 yoffset -70
    pause 2.5   
    linear 1.0 alpha 0.0

transform fade_in_delayed:
    alpha 0.0
    pause 4.0
    linear 1.0 alpha 1.0
    pause 2.0
    linear 1.0 alpha 0.0

transform fade_in_delayed2:
    alpha 0.0
    pause 2.0
    linear 1.0 alpha 1.0
    pause 4.0
    linear 1.0 alpha 0.0
transform fade_in_delayed3:
    alpha 0.0
    linear 1.0 alpha 1.0
    pause 4.0
    linear 1.0 alpha 0.0
    

transform wait_abit_then_move_up:
    pause 1.5
    ease 0.5 yoffset -40

transform alpha_half:
    alpha 0.5

transform whiten:
    matrixcolor None                   # normal
    linear 2 matrixcolor SaturationMatrix(-0.2) * BrightnessMatrix(0.5)

transform whiten_lesser:
    matrixcolor None                   # normal
    linear 2 matrixcolor SaturationMatrix(-0.2) * BrightnessMatrix(0.1)

transform flashing:
    block:
        matrixcolor TintMatrix("#b2b2ff")
        pause 0.6593
        matrixcolor TintMatrix("#ffb2b2")
        pause 0.6593
        repeat
    pause 0.3297

transform hover_fade:
    on hover:
        linear 0.14 zoom 1.1
    on idle:
        linear 0.14 zoom 1.0

transform hover_fade_lesser:
    on hover:
        linear 0.05 zoom 1.01
    on idle:
        linear 0.05 zoom 1.0

transform hover_action:
    on hover:
        block:
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
            xoffset renpy.random.randint(-5, 5)
            yoffset renpy.random.randint(-5, 5)
            pause 0.1
        repeat
    on idle:
        xoffset 0
        yoffset 0



transform shake_zoomed:
    zoom 1.02
    block:
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
        xoffset renpy.random.randint(-5, 5)
        yoffset renpy.random.randint(-2, 2)
        pause 0.02
    repeat