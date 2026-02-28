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
    $ start_lan_reload_guard()
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

default persistent.save_scum = False
default persistent.lan_currency_last_save = 0
default persistent.lan_reload_guard_until = 0.0
init python:
    import time
    def lan_sync_currency_last_save():
        if getattr(renpy.store, "current_location", None) == "lan":
            persistent.lan_currency_last_save = sol

    def start_lan_reload_guard():
        persistent.lan_reload_guard_until = time.time() + 120.0

    def is_lan_reload_guard_active():
        return time.time() < persistent.lan_reload_guard_until

    def lan_save_scum_handling():
        if not is_lan_reload_guard_active():
            return False

        if sol < persistent.lan_currency_last_save:
            persistent.save_scum = True
            persistent.lan_reload_guard_until = 0.0
            renpy.call_in_new_context("lan_save_scum_context")
            return True

        return False
