default inv_open = False
default item_tooltip = None
init python:
    first_item_event_triggered = False  # Initially false

    # Function to add item and trigger the first item event
    def is_item_get(item_name):
        """Check if a location is accessible."""
        return item_name in inventory_items

    def item_add(item_name):
        global first_item_event_triggered

        # Add item to the inventory
        inventory_items.append(item_name)

        renpy.notify(f"You got {item_name}!")
        # Check if the first item event has been triggered
        if not first_item_event_triggered:
            first_item_event_triggered = True  # Mark event as triggered
            # Display the message in the text box (window)\
            renpy.say(None, f"You have received your first item!")
            renpy.show_screen("inventory_display_toggle")
            renpy.say(None, f"To open the inventory, press \"TAB\" or click the Aries symbol on the top right corner.")
            renpy.say(None, f"Item will automatically be used up, you don't need to use it manually.")
            renpy.pause(1)  # Wait for a second to show the message

    def item_remove(item_name):
        if item_name in inventory_items:
            inventory_items.remove(item_name)
            renpy.say(None, f"{item_name} has been used up!")

transform follow_mouse:
    function _follow_mouse
transform follow_mouse_lower:
    function _follow_mouse_lower
init python:
    def _follow_mouse(trans, st, at):
        mx, my = renpy.get_mouse_pos()
        trans.xpos = mx + 40
        trans.ypos = my + 100
        return 0.01   # refresh every 0.01s
    def _follow_mouse_lower(trans, st, at):
        mx, my = renpy.get_mouse_pos()
        trans.xpos = mx + 40
        trans.ypos = my + 40
        return 0.01   # refresh every 0.01s

transform inv_toggle_anim:
    anchor (0.5, 0.5)
    linear 0.1 rotate (180 if inv_open else 0)

transform inv_slide_down:
    # start 600 px above its normal position, then slide down to natural pos
    on show:
        yoffset -100
        linear 0.1 yoffset 0
    on hide:
        linear 0.1 yoffset -100

screen inventory_display_toggle():
    zorder 92

    # Press Tab to toggle the inventory AND flip inv_open
    key "K_TAB" action [ ToggleScreen("inventory_box"), SetVariable("inv_open", not inv_open) ]

    # Toggle button (uses gui/inv_idle, gui/inv_hover, etc.)
    imagebutton auto "gui/inv_%s.png" xpos 0.975 yalign 0.04:
        action [ ToggleScreen("inventory_box"), SetVariable("inv_open", not inv_open) ]
        at inv_toggle_anim

    on "hide" action Hide("inventory_box")

default item_descriptions = {"Knife" : "the roaring knife", 
    "Canned Breakfast" : "Healthy canned food for everybody", 
    "Sari\'s Sauce" : "Sauce gifted by Sari, labels written all in chinese, not sure what it tastes like", 
    "Flavored Sauce" : "Sauce tweaked by Bailey, labels written all in chinese, presumably tastes like wine", 
    "Pack O\' Seeds" : "The legendary seeds of Tomato!!!",
    "Memorizing Sheet" : "Saves you the time memorizing, hope it doesn't fall into the hands of college students...",
    "Glass Daisy" : "Divinely rare species of Daisy, can only be found on Uranus",
    "Exquisite Daisy" : "Insanely rare species of Daisy, can only be found by beating up Glass Daisy",
    "Normal Daisy" : "Can't believe you've done this...",
    "UES" : "Ultimate Boredom Beater",
    "Hydrophobic Lubricant" : "Who need a boat when you can ride on water?",
    "Fishing Rod" : "Nemu's long rod with baits.",
    "Facedown Card" : "I think it'd tell me what my dinner will be.",
    "Defiled Blood" : "Ew why would I consider this an item...",
    "Neko\'s Bracelet" : "This might be insanely rare but idk what to do...?",
    "Nekomin Badge" : "A secret badge of the higher beings?",
    "Image Capturer" : "A device used to decrypt the outside word's datas into still images",
    "Homegrown Tomatoes" : "Speaking of planting...",
    "Crime Note" : "Contains all the criminal activities Remi did within his childhood",
    "Oil Tank" : "Basic fluid tank, contains 20mb of oil but is surprisingly light.",
    }
default inventory_items = []
default item_description = ""

screen inventory_box():
    modal True
    tag inventory_box
    on "show" action SetVariable("item_tooltip", None)
    on "hide" action SetVariable("item_tooltip", None)
    # FRAME acts as the parent container. inv_slide_down is applied here,
    # so the background + everything inside the frame moves together.
    frame:
        background "gui/inv_menu.png"
        at inv_slide_down
        xalign 0.9
        yalign 0.0
        xpadding 24
        ypadding 24

        has vbox
        spacing 8

        text "Inventory" xalign 0.5

        # A fixed container inside the frame where we place item slots by pixel coordinates.
        fixed:
            # size of the area inside the frame where items sit (tweak as needed)
            xsize 640
            ysize 320
            xalign 0.5
            yalign 0.5

            # slot layout settings (tweak columns/spacing/slot sizes to fit your art)
            $ slot_w = 96
            $ slot_h = 96
            $ cols = 8
            $ spacing = -12
            $ start_x = 1
            $ start_y = -67

            # place items in a grid inside the fixed container
            for i, item in enumerate(inventory_items):


                $ this_x = start_x + (i % cols) * (slot_w + spacing)
                $ this_y = start_y + (i // cols) * (slot_h + spacing)

                imagebutton auto "images/items/%s_%%s.png" % item:
                    xpos this_x
                    ypos this_y
                    xsize slot_w
                    ysize slot_h
                    # Tooltip shows item NAME instead of description
                    hovered [SetVariable("item_tooltip", item_descriptions.get(item, "???")),SetVariable("item_tooltip_2", item)]
                    unhovered [SetVariable("item_tooltip", None),SetVariable("item_tooltip_2", None)]
                    action [SetVariable("item_tooltip", item_descriptions.get(item, "???")),SetVariable("item_tooltip_2", item)]
    if item_tooltip:
        frame:
            background "#0008"
            xminimum 100
            yminimum 20
            xalign 1.0

            text item_tooltip color "#fff" size 22

            at follow_mouse
        frame:
            background "#0008"
            xminimum 100
            yminimum 20
            xalign 1.0

            text item_tooltip_2 color "#fff" size 40

            at follow_mouse_lower