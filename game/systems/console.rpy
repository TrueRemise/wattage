default command_list = {
    "sol set": sol_set,
}

default console_open = False
default cmd_text = ""
default console_arg = 0  # for numeric commands

screen console_toggle():
    zorder 1000

    # Open/close console with TAB (you can change to P if you want)
    key "K_BACKQUOTE" action [ToggleScreen("console_screen"), SetVariable("console_open", not console_open)]

screen console_screen():
    modal True
    tag console

    frame:
        xalign 0.17
        yalign 1.0
        background "#ffffff00"
        xsize 350

        vbox:
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(sol_add, 100)
                text "+100 sol":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(sol_add, 1000)
                text "+1000 sol":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(sol_set, 0)
                text "0 sol":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(stone_add)
                text "+1 stone":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(stone_remove)
                text "-1 stone":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action Function(action_fill)
                text "replendish actions":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action SetVariable("travel_upgrade",2)
                text "Teleportation":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
            button:
                at hover_sway_stronger
                xsize 800
                ysize 50
                xalign 0.3
                yalign 0.5
                background Solid("#ffffffd9")
                hover_background Solid("#ffffffd9")
                action SetVariable("travel_upgrade",0)
                text "Walk like normal":
                    size 50
                    xalign 0.0
                    yalign 0.5
                    color "#000000"
                    hover_color "#ffc75e"
                    outlines [(2, "#000000", 0, 0)]
                    font "Nemu.ttf"
    key "K_BACKQUOTE" action [Hide("console_screen"), SetVariable("console_open", False)]

# -----------------------------
# -----------------------------