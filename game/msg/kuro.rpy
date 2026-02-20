# File: game/systems/kuro.rpy
default kuro_first_talk_done_stage = 0
default fish_tutorial_done = False

label kuro_test:
    if kuro_first_talk_done_stage == 0:
        jump kuro_first_talk
    elif kuro_first_talk_done_stage == 1:
        jump kuro_second_talk
    elif kuro_first_talk_done_stage == 2:
        stop music fadeout 0.5
        play music "bgm_island.mp3" fadein 1.0
        if not fish_tutorial_done:
            jump fishing_game_tutorial
        jump fishing_game

label kuro_first_talk:
    show kuro default at right
    show watta default at left
    kr "Helo helo!!! Welcome to island! Me like fish!"
    w "Hello, can't believe there's another person here on this tiny island."
    show kuro deter at bounce
    kr "Yes me live here, me name Kuro! Welcome"
    w "Hello Kuro, what do you usually do here?"
    show kuro happy at bounce
    kr "Yes! Me hunt fish! Fish a lot! Fish yummy! Yummy yummy!"
    show watta smile
    w "Fish? There sure are a lot of fishes here. How do you catch fish without tools?" 
    show kuro confused
    kr "Tool?"
    show kuro deter at bounce
    extend " No me no tool, me hunt! Me hunt fast, me hunt fish, me eat!"
    w "I see, that's a close to nature way to fish, have you tried a fishing rod?" 
    show kuro confused
    kr "Fishing rot? What is fishing rot?"
    w "It's a tool to catch fish! You put food on it and the fish will eat the food. Then you can catch even the fastest fish!"
    show kuro happy at bounce
    kr "Wao wao hunt fast fish!!"
    w "Yes, very good!"
    if is_item_get("Fishing Rod"):
        w "{i}I can teach her using the one Nemu gave me..."
    else:
        w "{i}I should buy a fishing rod to teach her"
    $ kuro_first_talk_done_stage = 1
    hide watta
    hide kuro
    jump islandskip

label kuro_second_talk:
    if is_item_get("Fishing Rod"):
        show kuro happy at right
        show watta smile at left
        kr "Wao helo helo back!"
        w "Here! This is a fishing rod!"
        show kuro default at bounce
        kr "Helo helo! Fishing rot helo!"
        w "First you need food, you stick food here, and then throw, and when fish eat this you drag fish up!"
        show kuro default at bounce
        kr "Wao wao hunt fish advanced!"
        w "Well if you want to learn I can teach you more!"
        show kuro happy at bounce
        kr "Wao wao helo!"
        call screen kuro_teach
    else:
        show watta default at left
        w "{i}I should find a fishing rod for her."
    hide watta
    hide kuro
    jump islandskip


screen kuro_teach():
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
                background Solid("#ffffff5b")
                hover_background Solid("#ffffff94")
                action Jump("kuro_teach_fish")
                text "Teach how to fish":
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
                background Solid("#ffffff5b")
                hover_background Solid("#ffffff94")
                action Jump("island")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"

label kuro_teach_fish:
    w "So this is how it works..."
    if phase != 3:
        scene bg island with Fade(1, 0, 1)
    else:
        scene bg islandn with Fade(1, 0, 1)
    show kuro default at right
    show watta smile at left
    kr "Wao wao fishing rot is amazing!!"
    kr "Me want catch more fish."
    w "Sure you can, we can catch more fishes in the future."
    show kuro happy at bounce
    kr "Yay yay"
    w "{i}I should come here to fish more often."
    $ item_remove("Fishing Rod")
    $ kuro_first_talk_done_stage = 2
    $ notebook_unlock("Kuro")
    $ action_done()
    hide watta
    hide kuro
    jump islandskip