default map_open = False

screen map_toggle():
    zorder 93
    key "K_m" action If(
        map_unl and not actions_locked and not all_locked or youcanonlygotosanco,
        true = [
            If(map_open,
                [Hide("map_screen"), SetVariable("map_open", False)],
                [Show("map_screen"), SetVariable("map_open", True)]
            )
        ],
        false = Function(renpy.notify, "You can't open the map right now.")
    )
        
screen map_screen():
    modal True
    tag map
    add "images/bg/bg map.png" xalign 0.5 yalign 0.5
    for loc, (x, y) in {
        "outhome": (1573, 700),
        "district": (1362, 640),
        "park": (1057, 671),
        "bridge": (863, 300),
        "monument": (1074, 18),
        "field": (462, 644),
        "centre": (415, 100),
        "beach": (39, 26),
        "lake": (64, 693),
        "spira": (1430, 308),
        "alley": (1624, 44),
    }.items():
        
        if loc in unlocked_locations:

            if first_work:
                if loc not in ["district", "outhome"]:
                    add "images/map/%s_idle.png" % loc xpos x ypos y:
                        matrixcolor SaturationMatrix(-1.0) * BrightnessMatrix(-0.4)

                elif not is_here(loc):
                    imagebutton auto "images/map/%s_%%s.png" % loc xpos x ypos y:
                        action Function(move_to, loc)
                else:
                    add "images/map/%s_idle.png" % loc xpos x ypos y
            else:
                # Travelable (normal)
                
                if is_travel_allowed(loc):
                    imagebutton auto "images/map/%s_%%s.png" % loc xpos x ypos y:
                        action Function(move_to, loc)

                elif not is_here(loc):
                    add "images/map/%s_idle.png" % loc xpos x ypos y:
                        matrixcolor SaturationMatrix(-1.0) * BrightnessMatrix(-0.4)

                # If it's the current location → show normal icon
                else:
                    add "images/map/%s_idle.png" % loc xpos x ypos y

        else:
            pass
            #add "images/map/%s_locked.png" % loc xpos x ypos y
        # --- YOU ARE HERE MARKER ---
        if is_here(loc):
            $ ox, oy = marker_offset.get(loc, (0, 0))
            add "gui/marker.png" xpos x + ox ypos y + oy


    # Close with ESC or right-click
    key "K_ESCAPE" action [
        Hide("map_screen"),
        Show("phone_screen"),
        SetVariable("map_open", False),
        SetVariable("phone_open", True)
    ]

init python:
    marker_offset = {
        "outhome":   (40, 100),
        "district":  (40, -70),
        "park":      (20, 20),
        "bridge":    (25, -40),
        "monument":  (40, 70),
        "field":     (30, -35),
        "centre":    (65, 65),
        "beach":     (45, 65),
        "lake":      (0, -50),
        "spira":     (0, -55),
        "alley":     (0, -35),
    }