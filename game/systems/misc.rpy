init python:
    from collections import OrderedDict

    def option_add(char, option_key, label_name, pos=None):
        varname = f"{char}_options"
        d = getattr(renpy.store, varname, {})

        # Ensure it's OrderedDict for stable ordering
        if not isinstance(d, OrderedDict):
            d = OrderedDict(d)

        # Convert to list of items for inserting
        items = list(d.items())

        # Build the new pair
        new_pair = (option_key, label_name)

        if pos is None or pos >= len(items):
            # append
            items.append(new_pair)
        else:
            # insert at position
            items.insert(pos, new_pair)

        # Rebuild OrderedDict
        new_dict = OrderedDict(items)
        setattr(renpy.store, varname, new_dict)

    def option_remove(char, option_key):
        varname = f"{char}_options"
        d = getattr(renpy.store, varname, None)

        if d is not None:
            d.pop(option_key, None)


default is_shaky_choice_disclaimer = False
label is_shaky_choice_disclaimer:
    if is_shaky_choice_disclaimer == False:
        "DISCLAIMER!"
        "SHAKY CHOICES WILL COST AN ACTION IF YOU DO THEM!"
        $ is_shaky_choice_disclaimer = True
        return
    else:
        return

screen action_display():    
    zorder 190
    if not map_open and not phone_open:
        frame:
            xalign 0.0
            yalign 0.0
            background None
            vbox:
                null height -13
                frame:
                    background ("#ffffff00")
                    # Phase image (switches by phase index)
                    if phase == 0:
                        text "DAWN":
                            color "#000" 
                            size 35 
                            xalign 0.0
                            outlines [(3, "#ffffff", 0, 0)]
                    elif phase == 1:
                        text "NOON":
                            color "#000" 
                            size 35 
                            xalign 0.0
                            outlines [(3, "#ffffff", 0, 0)]
                    elif phase == 2:
                        text "DUSK":
                            color "#000" 
                            size 35 
                            xalign 0.0
                            outlines [(3, "#ffffff", 0, 0)]
                    elif phase == 3:
                        text "NIGHT":
                            color "#000" 
                            size 35 
                            xalign 0.0
                            outlines [(3, "#ffffff", 0, 0)]
                    elif phase == 4:
                        text "MIDNIGHT":
                            color "#000" 
                            size 35 
                            xalign 0.0
                            outlines [(3, "#ffffff", 0, 0)]
                
                null height -20

                #Action left indicator
                frame:
                    background ("#ffffff00")
                    hbox:
                        spacing 6.7
                        for i in range(max_actions):
                            if i < actions_left:
                                add "gui/act_on.png"
                            else:
                                add "gui/act_off.png"
                    
        frame:
            xalign 0.95
            yalign 0.083
            background None

            text "[sol]":
                color "#000" 
                size 45 
                xalign 1.0
                outlines [(2, "#ffffff", 0, 0)]

image bg bike loading:
    "misc/bike1.png"
    pause 0.2
    "misc/bike2.png"
    pause 0.2
    "misc/bike3.png"
    pause 0.2
    "misc/bike4.png"
    pause 0.2
    repeat
image bg bath loading:
    "misc/bath1.png"
    pause 0.3
    "misc/bath2.png"
    pause 0.3
    "misc/bath3.png"
    pause 0.3
    repeat

screen you_died():    
    zorder 990
    timer 3.0 action [Jump("forced_title_screen")]
    timer 1.0 action Play("sound", "sfx/death.mp3")
    frame:
        at you_died
        xsize 2500
        xalign 0.5
        yalign 0.5
        background "#000000b0" 
        text "YOU CANNOT BE SAVED":
            color "#aa1010" 
            size 85 
            xalign 0.5
            yalign 0.5
            font "Day.ttf"
transform you_died:
    alpha 0.0
    parallel:
        easeout 3.0 zoom 1.1
    parallel:
        easeout 1.5 alpha 1.0

label forced_title_screen:
    $ MainMenu(confirm=False)()

screen camera_on:
    if is_item_get("Image Capturer"):
        imagebutton:
            xanchor 1.0
            yanchor 1.0
            xpos 1862
            ypos 1056
            auto "images/misc/shoot_%s.png"
            action Show("camera_flash")
        text ", ".join(i.upper() for i in image_taken_list):
            xanchor 1.0
            yanchor 1.0
            xpos 1852
            ypos 1070
            size 30
            color "#000"


screen camera_flash():
    modal True
    zorder 300

    if image_taken<=2:
        timer 0.1 action Play("sound", "sfx/camera_flash.mp3")
        add Solid("#fff") at flash
    else:
        timer 0.1 action Function(camera_apply_effects)
        

    # After flash, apply effects and return
    timer 3 action Function(camera_apply_effects)

default image_taken = 0
default image_taken_list = []
init python:
    def camera_apply_effects():
        global image_taken, image_taken_list

        image_taken += 1
        # === YOUR EFFECTS ===
        if image_taken <= 3:
            if current_location == "beach":
                renpy.notify("Beach photo taken!")
                image_taken_list.append("beach")
            if current_location == "spira":
                renpy.notify("Spiralia photo taken!")
                image_taken_list.append("spiralia")
            if current_location == "monument":
                renpy.notify("Monument photo taken!")
                image_taken_list.append("monument")
        else:
            renpy.notify("You can't take anymore more photos")

        # Close flash overlay
        renpy.hide_screen("camera_flash")


transform flash:
    alpha 0.0
    pause 0.3
    linear 0.0 alpha 1.0
    pause 0.1
    linear 2.5 alpha 0.0

init python:
    from collections import Counter

    def list_matches_pattern(lst, pattern):
        return Counter(lst) == Counter(pattern)

    def horror_crash():
        raise Exception("The game is not supposed to continue.")
init python:
    def hide_all_screens():
        for scr in renpy.config.screen_list.keys():
            renpy.hide_screen(scr)

label horror_redirect:
    if persistent.horror_crash:
        $ persistent.horror_crash = False
        # Force hide all screens
        hide screen horror_timer
        #hide screen phone_toggle
        #hide screen map_toggle
        #hide screen console_toggle
        #hide screen inventory_display_toggle
        #hide screen quick_menu
        # Stop previous music
        jump horror_message
    return


label horror_message:
    $ preferences.text_cps = 0.05
    $ quick_menu = False
    $ _game_menu_screen = None
    $ save_lock = True
    $ all_locked = True
    $ actions_locked = True
    $ renpy.block_rollback()
    # Show the horror overlay
    show screen horror_trap
    return




label after_load:
    $ preferences.text_cps = 50
    if persistent.horror_crash:
        show screen horror_timer
    $ lan_load_persistent_state()
    if lan_punishable_period > 0.0:
        $ lan_punishable_period = 30.0
        if current_location == "lan":
            $ lan_punishable_outside_since = 0.0
        else:
            $ lan_punishable_outside_since = renpy.get_game_runtime()
        $ lan_save_persistent_state()
    $ renpy.notify(f"Lan save check: last={lan_currency_last_save}, period={lan_punishable_period}")
    if current_location == "lan":
        $ lan_save_scum_handling()
    return




default persistent.horror_crash = True
default show_death_png = False
default show_black_death_png = False
default show_white_death_png = False
default show_bsod_death_png = False
default show_bsod20_death_png = False
default show_error_death_png = False
screen horror_trap():
    zorder 99999
    modal True
    key "K_ESCAPE" action NullAction()
    key "K_MENU" action NullAction()
    key "alt_K_F4" action NullAction()
    key "K_F4" action NullAction()
    key "K_F11" action NullAction()
    timer 8.5 repeat True action Preference("display", "fullscreen")
    timer 18.0 action Play("music", "bgm_musicbox.mp3", fadein=1.0)
    timer 0.5 action SetVariable("show_white_death_png", True)
    timer 0.1 action SetVariable("freeze_ui", True)
    #timer 3.0 action SetVariable("show_error_death_png", True)
    timer 5.1 action Play("sound", "sfx/error.mp3")
    timer 8.5 action SetVariable("show_bsod_death_png", True)
    timer 13.5 action SetVariable("show_bsod20_death_png", True)
    timer 8.3 action Stop("sound")
    timer 15.0 action SetVariable("show_black_death_png", True)
    #timer 13.0 action Play("sound", "sfx/ambient.mp3")
    timer 18.0 action SetVariable("show_death_png", True)
    timer 1.0 action Stop("music")
    if show_white_death_png:
        add "images/bg/bg white.png" alpha 0.5 at fade_in
    if show_error_death_png:
        add "images/misc/error.png"
    if show_bsod_death_png:
        add "images/misc/bsod0.png"
    if show_bsod20_death_png:
        add "images/misc/bsod.png"
    if show_black_death_png:
        add "images/bg/bg black.png"
    if show_death_png:
        add "images/misc/death.png" #at fade_in_slowly
        #text "EPSTEIN ISLAND":
        #    size 80
        #    xalign 0.5
        #    yalign 0.3
        
        #    color "#373737"
        #    font "Day.ttf"

screen horror_timer():
    # Invisible, non-blocking
    zorder -100
    timer 20.0 action Function(renpy.call, "horror_redirect")

default save_scum = False
default lan_currency_last_save = 0
default lan_punishable_period = 0.0
default lan_punishable_outside_since = 0.0
default lan_joined_sol = 0
init python:
    def _as_int(value, default=0):
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    def _as_float(value, default=0.0):
        try:
            return float(value)
        except (TypeError, ValueError):
            return default

    def lan_normalize_state_values():
        """
        Ensure LAN state is always numeric so comparisons never hit NoneType.
        """
        renpy.store.lan_currency_last_save = _as_int(getattr(renpy.store, "lan_currency_last_save", 0), 0)
        renpy.store.lan_punishable_period = _as_float(getattr(renpy.store, "lan_punishable_period", 0.0), 0.0)
        renpy.store.lan_punishable_outside_since = _as_float(getattr(renpy.store, "lan_punishable_outside_since", 0.0), 0.0)
        renpy.store.lan_joined_sol = _as_int(getattr(renpy.store, "lan_joined_sol", 0), 0)

    def lan_load_persistent_state():
        if not hasattr(persistent, "lan_currency_last_save"):
            persistent.lan_currency_last_save = 0
        if not hasattr(persistent, "lan_punishable_period"):
            persistent.lan_punishable_period = 0.0
        if not hasattr(persistent, "lan_punishable_outside_since"):
            persistent.lan_punishable_outside_since = 0.0
        if not hasattr(persistent, "lan_joined_sol"):
            persistent.lan_joined_sol = 0

        renpy.store.lan_currency_last_save = persistent.lan_currency_last_save
        renpy.store.lan_punishable_period = persistent.lan_punishable_period
        renpy.store.lan_punishable_outside_since = persistent.lan_punishable_outside_since
        renpy.store.lan_joined_sol = persistent.lan_joined_sol
        lan_normalize_state_values()

    def lan_save_persistent_state():
        lan_normalize_state_values()
        persistent.lan_currency_last_save = renpy.store.lan_currency_last_save
        persistent.lan_punishable_period = renpy.store.lan_punishable_period
        persistent.lan_punishable_outside_since = renpy.store.lan_punishable_outside_since
        persistent.lan_joined_sol = renpy.store.lan_joined_sol

    def lan_clear_punishable_period():
        renpy.store.lan_punishable_period = 0.0
        renpy.store.lan_punishable_outside_since = 0.0
        lan_save_persistent_state()

    def lan_sync_currency_last_save():
        if getattr(renpy.store, "current_location", None) == "lan":
            renpy.store.lan_currency_last_save = sol
            lan_save_persistent_state()

    def lan_start_punishable_period(seconds=30.0):
        renpy.store.lan_punishable_period = float(seconds)
        if getattr(renpy.store, "current_location", None) == "lan":
            renpy.store.lan_punishable_outside_since = 0.0
        else:
            renpy.store.lan_punishable_outside_since = renpy.get_game_runtime()
        lan_save_persistent_state()

    def lan_refresh_punishable_period():
        lan_normalize_state_values()
        if renpy.store.lan_punishable_period <= 0.0:
            return

        if sol > renpy.store.lan_joined_sol:
            lan_clear_punishable_period()
            return

        if getattr(renpy.store, "current_location", None) == "lan":
            if renpy.store.lan_punishable_outside_since > 0.0:
                renpy.store.lan_punishable_period = 30.0
            renpy.store.lan_punishable_outside_since = 0.0
            lan_save_persistent_state()
            return

        now = renpy.get_game_runtime()
        if renpy.store.lan_punishable_outside_since <= 0.0:
            renpy.store.lan_punishable_outside_since = now
            lan_save_persistent_state()
            return

        elapsed = now - renpy.store.lan_punishable_outside_since
        renpy.store.lan_punishable_period = max(0.0, renpy.store.lan_punishable_period - elapsed)
        renpy.store.lan_punishable_outside_since = now

        if renpy.store.lan_punishable_period <= 0.0:
            lan_clear_punishable_period()
            return

        lan_save_persistent_state()

    def lan_on_enter():
        lan_load_persistent_state()
        lan_refresh_punishable_period()
        renpy.store.lan_joined_sol = sol
        if renpy.store.lan_punishable_period > 0.0:
            renpy.store.lan_punishable_period = 30.0
            renpy.store.lan_punishable_outside_since = 0.0
        lan_sync_currency_last_save()
        lan_save_persistent_state()

    def lan_on_leave():
        lan_refresh_punishable_period()
        if renpy.store.lan_punishable_period > 0.0 and renpy.store.lan_punishable_outside_since <= 0.0:
            renpy.store.lan_punishable_outside_since = renpy.get_game_runtime()
        lan_save_persistent_state()

    def lan_on_sol_changed(previous_sol, current_sol):
        previous_sol = _as_int(previous_sol, 0)
        current_sol = _as_int(current_sol, 0)
        if getattr(renpy.store, "current_location", None) == "lan" and current_sol < previous_sol:
            lan_start_punishable_period(30.0)

        if renpy.store.lan_punishable_period > 0.0 and current_sol > renpy.store.lan_joined_sol:
            lan_clear_punishable_period()
            return

        lan_save_persistent_state()

    def lan_save_scum_handling():
        lan_load_persistent_state()
        lan_refresh_punishable_period()
        if renpy.store.lan_punishable_period <= 0.0:
            return False

        if sol > renpy.store.lan_currency_last_save:
            renpy.store.save_scum = True
            lan_clear_punishable_period()
            renpy.jump("lan_save_scum_context")
            return True

        return False
