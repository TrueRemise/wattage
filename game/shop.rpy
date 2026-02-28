# ---------------------
# Python setup
# ---------------------
default shop_items = [
    {
        "name": "Twisted Stone",                # internal name
        "price": "500",               # price text
        "desc": "An artifact my mom gave me, it's a conical spiral shaped stone that seemingly produces energy randomly when put close to some other artifacts. I have no idea what resonates with it and what doesn't but I think it's better to give this to the hands of someone with better knowledge.",  # description
        "image": "stone",      # normal image
    },
    {
        "name": "Pack O' Seeds",                # internal name
        "price": "50",               # price text
        "desc": "An artifact my aunt gave me, it's seemingly a normal plastic bag with tomato seeds inside, the strange thing is that it never runs out of seeds. I think it makes seeds overnight? It's really interesting but I never found any uses for it that didn't break any agricultural laws, so instead you can buy it for cheap. Make use of it at your own risk, though",  # description
        "image": "tomato",      # normal image
    },
    {
        "name": "Memorizing Sheet",                 
        "price": "100",                
        "desc": "An artifact my grandma gave me. At first glance it looks like a pen and notebook but it's said that whatever you'll remember whatever you write down for the rest of your life. I wrote a stupid joke in there once and now I'm haunted by its memory so i'm pretty scared of using it any further. Any used papers are scrapped but you can still use the rest.",                   
        "image": "paper",
    },
    {
        "name": "UES",  
        "price": "50",      
        "desc": "An artifact my brother gave me, in short for Ultimate Entertaining System, it's a seemingly normal handheld console player, but contains every games known to mankind. It doesn't support keyboard and mouse so it's limited, but that is a really addicting thing I would reccommend you not to spend too much time on it if you want to keep your mind sane.",  # description
        "image": "UES",      # normal image
    },
    {
        "name": "Hydrophobic Lubricant",
        "price": "150", 
        "desc": "A not-so-artifact my uncle gave me, it's a mixture of oil and a specific hydrophobic substance than can be applied on any kind of solid surface. When applied the object will consider every sources of water another solid object and will decline to be in contact with them, most magically you can apply this on your bike's tires and the whole ocean will be solid for you to travel on.",  # description
        "image": "lube",   
    },
]   # list of item names

default soul_of_bloomfield = False
init python:
    def shop_item_add(name, price, desc, image_base):
        shop_items.append({
            "name": name,
            "price": price,
            "desc": desc,
            "image": image_base,  
        })

    def shop_item_remove(name):
        global shop_items
        shop_items = [i for i in shop_items if i["name"] != name]

    def shop_item_sold(name,price):
        global sol, soul_of_bloomfield
        sol -= price
        if name == "Flower Charm":
            soul_of_bloomfield = True
            renpy.notify(f"You became one with Bloomfield!")
            key_item_add("Bloomfield's Charm")
        elif name == "Twisted Stone":
            renpy.call_in_new_context("stone_bought")
            key_item_add("Twisted Stone")
        elif name == "Memorizing Sheet":
            item_add(name)
            key_item_add("Memorizing Sheet")
            renpy.notify(f"Bought {name}!")
            renpy.show_screen("notebook_toggle")
            renpy.call_in_new_context("notebook_bought")
        elif name == "Hydrophobic Lubricant":
            item_add(name)
            key_item_add("Hydrophobic Lubricant")
            renpy.notify(f"Bought {name}!")
        else:
            item_add(name)
            renpy.notify(f"Bought {name}!")
        shop_item_remove(name)

    # placeholder for confirm screen
    def show_confirm_screen(name):
        renpy.call_in_new_context("confirm_screen", name)

    def shop_item_clicked(item):
        price = int(item["price"])
        if sol >= price:
            renpy.play("sfx/shop_select.mp3", channel="sound")
            renpy.show_screen("shop_confirm_screen", item=item)
        else:
            renpy.play("sfx/cantbuy.mp3", channel="sound")
            renpy.show_screen("shop_not_enough_screen", item=item)
# ---------------------
# Shop Item Screen
# ---------------------
transform hover_up:
    on hover:
        easein_cubic 0.30 yoffset -20
        pause 2
        easeout_cubic 5 yoffset 0
        repeat
    on idle:
        ease_cubic 0.1 yoffset 0

screen shop_screen():

    default count = len(shop_items)
    default gap = 1.0 / (count + 1)
    default hovered_item = None    # screen-level variable

    frame:
        xalign 0.5
        yalign 0.4
        background None

        # Layer for items
        for i, item in enumerate(shop_items):
            fixed:
                xalign gap * (i + 1)
                yalign 0.45
                fit_first True
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.5

                    imagebutton:
                        idle "items/shop_%s_idle.png" % item["image"]
                        hover "items/shop_%s_hover.png" % item["image"]
                        at hover_up
                        action Function(shop_item_clicked, item)

                        hovered SetScreenVariable("hovered_item", item)
                        unhovered SetScreenVariable("hovered_item", None)
                    # Price below
                    text "[item['price']] SOL":
                        xalign 0.5
                        yalign 1.2
                        size 60
                        color "#000000"
                        font "Shop.ttf"
    hbox:
        spacing 45
        xalign 0.967
        yalign 0.998

        if shop_options:
            $ shift = 0
            for name, target_label in shop_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#09ff00", "#ff0000", t)
                button:
                    at hover_sway
                    xsize 180
                    ysize 85
                    xalign 0
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)

                    text name:
                        size 100
                        xalign 0
                        yalign 0.5
                        color "#000000"
                        hover_color hover_color
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Shop.ttf"
                $ shift += 100
    
    frame:
        xalign 0.7
        yalign 0.68
        background "#ff545400"
        text "[sol] SOL":
            xalign 0.5
            yalign 1.2
            size 60
            color "#000000"
            font "Shop.ttf"
        # --- DESCRIPTION BOX ---
    if hovered_item:

        frame:
            background "#ffffff00"
            xalign 0.05
            yalign 0.99
            xsize 1350
            ysize 380

            fixed:
                # Item Name (fixed at 50px from top)
                text hovered_item["name"]:
                    size 120
                    color "#000000"
                    font "Shop.ttf"
                    xpos 2
                    ypos 5   # ← FIXED POSITION

                # Description (fixed lower)
                text hovered_item["desc"]:
                    size 48
                    color "#000000"
                    font "Shop.ttf"
                    xpos 8
                    ypos 130   # ← FIXED POSITION


default shop_options = {
    "Chat": "chii_talk",
    "Leave": "chii_byebye",
}
transform hover_sway:
    on hover:
        easein_cubic 0.30 xoffset 12
        pause 2
        easeout_cubic 5 xoffset 0
        repeat
    on idle:
        linear 0.15 xoffset 0
    
# ---------------------
# Confirmation Screen
# ---------------------
screen shop_confirm_screen(item):
    tag shop_confirm
    zorder 200
    frame:
        xalign 0.99
        yalign 0.85
        xsize 450
        ysize 280
        background "#00000000"

        vbox:
            spacing 25
            xalign 0.5
            yalign 0.9

            frame:
                background "#00000000"
                xsize 500
                ysize 300
                xalign 0.5
                ypos 30
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.9
                    text "Do you want to buy":
                        size 64
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"
                    text "[item['name']]?":
                        size 58
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"
                    text "You will have [sol - int(item['price'])] Sol left.":
                        size 45
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"

            hbox:
                spacing 50
                xalign 0.5

                button:
                    at hover_sway
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/purchase.mp3"), Function(shop_item_sold, item["name"], int(item["price"])), Hide("shop_confirm_screen")]

                    text "Buy":
                        size 80
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#27ff6b"
                        outlines [(1.5, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Shop.ttf"

                button:
                    at hover_sway
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), Hide("shop_confirm_screen")]

                    text "No":
                        size 80
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#ff0000"
                        outlines [(1.5, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Shop.ttf"

screen shop_not_enough_screen(item):
    tag shop_confirm
    zorder 200
    frame:
        xalign 0.99
        yalign 0.80
        xsize 450
        ysize 280
        background "#00000000"

        vbox:
            spacing 25
            xalign 0.5
            yalign 0.9

            frame:
                background "#00000000"
                xsize 500
                ysize 300
                xalign 0.5
                ypos 30
                vbox:
                    spacing 10
                    xalign 0.5
                    yalign 0.9
                    text "You can not buy":
                        size 70
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"
                    text "[item['name']]":
                        size 58
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"
                    text "You need [int(item['price']) - sol] more Sol.":
                        size 53
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        font "Shop.ttf"


label stone_bought:
    show screen stone_aquired()
    $ renpy.pause(11, hard=True)

    $ stone_add()
    
    hide screen task_aquired
    return

label notebook_bought:
    "You bought the note."
    "You started writing down what's important to you."
    "Press \"j\" to open the notebook, alternately you can click the Gemini icon near the top right corner."
    return