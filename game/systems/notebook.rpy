
screen notebook_toggle():
    zorder 94
    imagebutton auto "gui/jrn_%s.png" xpos 0.959 ypos 0.142:
        action If(
            not all_locked,
            [   
                ToggleScreen("notebook_screen"),
            ],
            Function(renpy.notify, "You can't open the notebook right now.")
            )
    key "K_j" action If(
            not all_locked,
            [   
                ToggleScreen("notebook_screen"),
            ],
            Function(renpy.notify, "You can't open the notebook right now.")
            )
default notebook_tab = [
    {
        "name": "People",
        "image": "people",
        "unlocked": True
    },
    {
        "name": "Locations",
        "image": "locations",
        "unlocked": True
    },
    {
        "name": "Fishes",
        "image": "fishes",
        "unlocked": False
    },
    {
        "name": "Upgrades and Quests",
        "image": "upgrades",
        "unlocked": True
    },
    {
        "name": "Endings",
        "image": "people",
        "unlocked": False
    },
]
default notebook_chars_friends = [
    {
        "name": "Remi",
        "desc": "One of my oldest friends! Pretty unstable person, yet very talented. He's really good at designing stuffs.\nAfter an incident in the group, he isolated himself into the lighthouse at the beach, he told me to call him Hiko and keep himself as a secret to everyone.\n...\nHe loves the beach.",
        "image": "remi",
        "unlocked": True
    },
    {
        "name": "Renia",
        "desc": "Really friendly and outgoing person, though might be very strict and serious at times\nShe's a big attraction among the group, oftenly found busy irl. She has a great love for voice acting and pets.\nShe also owns a lot of dogs, with one of them really like my Rocko!\nReni's current house is a prop store named Nekopia to the east of the monument.",
        "image": "reni",
        "unlocked": False
    },
    {
        "name": "Toko",
        "desc": "A very talented composer, capable of playing many instruments(at once)\nHe's dating Sanco currently but he lives separatedly in Spiralia, I wonder if they get to meet up oftenly.\nToko's in an ugly situation rn doing everything to earn money at the moment due to his lack of customers.",
        "image": "toko",
        "unlocked": False
    },
    {
        "name": "Sanco",
        "desc": "A rather gentle soul...\nSanco always brings a relaxing atmosphere to the group! She used to be into sculpturing and crafting cute little items.\nShe had to move back to Bloomfield after the incident,\nWhile living there she makes money by selling handmade goods and jewelry!",
        "image": "sanco",
        "unlocked": False
    },
    {
        "name": "Sari",
        "desc": "My persistent poetic goofer, always making me rate his stuffs...\nCurrently living in his RV at the park after years of office work.\nHis sauce is actual banger! But the foods come along are meh...\nThankfully he lives rather close to work.",
        "image": "sari",
        "unlocked": False
    },
]
default notebook_chars = [
    {
        "name": "Woogie",
        "desc": "Self-proclaimed detective, seems quite knowledgeable about the land.\nAnnoyed me one day and haven't been able to shake her off since! Least she provides somewhat useful insight.\nHas a cute but equally chaotic stoat companion.",
        "image": "woogie",
        "unlocked": False
    },
    {
        "name": "Nemu",
        "desc": "Self-taught fisher!\nFirst time we met they were selling fishes all around, seems they want to teach me how to fish as well!\nShould spend some time to learn more from them...\nAlways a joyful presence to be around.",
        "image": "nemu",
        "unlocked": False
    },
    {
        "name": "Chii",
        "desc": "A plant(?) girl that moved into the Centre recently, says she's from Bloomfield.\nCurrently she sells many... useful(?) Artifacts that may or may not be helpful, but they are pretty hard to believe.\nShe also smells really minty for some reason.",
        "image": "chii",
        "unlocked": True
    },
    {
        "name": "Flan",
        "desc": "Current owner and showrunner of the bar (named RNG moner changer?) in the Centre. Sells alcoholic drinks and runs a \"very legal\" set of gambling games.\nTo her, sol does all the talking. Feels like she can smell poverty from a mile away.",
        "image": "flan",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "Someone who works at the North Gate near the bridge, seemingly very lonely.\nWhile first impressions weren't great, I can see him at least does his job well.\nPerhaps I can get on better terms if I can somehow solve his problems.",
        "image": "tsuyu",
        "unlocked": False
    },
    {
        "name": "Kuro",
        "desc": "A strange catgirl I found on a lonesome island, surrounded by many equally strange things.\nSeemingly does nothing but fishing all day, except for the rare occasions I spotted her hitting the large machine.\nMaybe that's how she got good reflexes.",
        "image": "kuro",
        "unlocked": False
    },
    {
        "name": "Iog",
        "desc": "An enigma, mysterious figure.\nI feel like they are... doing nothing more than standing for hours at a time.\nSpeaks in only one phrase that is hot dog\nI don't think i'll every understand them.",
        "image": "iog",
        "unlocked": False
    },
    {
        "name": "Tato",
        "desc": "Strange fox-like person I met at the beach, feels like she speaks in riddles.\nTalks a lot about our fate and futures, honestly sounds like nonsense.\nStrangely though, I feel compelled to listen to her...She might be up to some secrets?\nShe also knows my name somehow?",
        "image": "tato",
        "unlocked": False
    },
    {
        "name": "Bailey",
        "desc": "Guard working and living in Spiralia. Seems troubled.\nActually VERY troubled, feels like he's trying to solve every problems and do every works at once.\nHope I can someday provide him some hope amidst all the darkness he sees.",
        "image": "bailey",
        "unlocked": False
    },
    {
        "name": "Neko",
        "desc": "Popular idol with a huge amount of fan, I think she is moving to perform in the centre for a while.\nVery cheerful person, though she might be struggling with something recently.\n",
        "image": "neko",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "template.",
        "image": "iog",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "template.",
        "image": "iog",
        "unlocked": False
    },
    {
        "name": "Owl",
        "desc": "The guardian of Swan Lake. One of the people in the group despite not talking much. Seemingly has some kind of power as what Remi said?\nLooks like emotionless, but manages to create really good and expressional paintings.\nIsn't living like that really boring though?...",
        "image": "owl",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "Delinquent!",
        "image": "iog",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "Makes and sells guns!",
        "image": "iog",
        "unlocked": False
    },
    {
        "name": "Tsuyu",
        "desc": "template.",
        "image": "iog",
        "unlocked": False
    },
]
default notebook_key_items = []          # ordered list of item IDs
default notebook_key_item_data = {
    "Twisted Stone": {
        "name": "Twisted Stone",
        "desc": "Mystery stone found across Spiralia, having them in my bag boosts my energy for some reasons.",
        "image": "twisted stone"
    },
    "Memorizing Sheet": {
        "name": "Memorizing Sheet",
        "desc": "This notebook.",
        "image": "memorizing sheet"
    },
    "Hydrophobic Lubricant": {
        "name": "Hydrophobic Lubricant",
        "desc": "Help you ride your bike on water.",
        "image": "hydrophobic lub"
    },
    "Bloomfield's Charm": {
        "name": "Bloomfield's Charm",
        "desc": "The aura of Bloomfieldian.",
        "image": "bloomfield charm"
    },
    "Corrupted Charm": {
        "name": "Corrupted Charm",
        "desc": "The aura of the corrupted.",
        "image": "corrupted charm"
    },
    "Hot Dog": {
        "name": "Hot Dog",
        "desc": "Gives 3 actions.",
        "image": "hot dog"
    },

    "Hot Puppy": {
        "name": "Hot Puppy",
        "desc": "Gives 1 action, i drew 3 but mean just 1.",
        "image": "hot puppy"
    },
}
default notebook_key_item_count = {}   


default current_tab = "People"
screen notebook_screen():
    zorder 195
    modal True
    tag notebook
    add "images/bg/bg white.png"
    add "gui/notebook_ui.png"
    default hovered_char = None
    default hovered_item = None
    use notebook_tab_screen
    if current_tab == "People":
        add "images/notebook/tab_selector.png": 
            xalign 0.9775
            yalign 0.037
        use notebook_char_friend_screen
        use notebook_char_screen
    if current_tab == "Locations":
        add "images/notebook/tab_selector.png": 
            xalign 0.9775
            yalign 0.265
        use notebook_char_friend_screen
        use notebook_char_screen
    if current_tab == "Upgrades and Quests":
        add "images/notebook/tab_selector.png":
            xalign 0.9775
            yalign 0.723
        use notebook_key_item_screen
    if hovered_char or hovered_item:
        frame:
            background None
            xpos 900
            ypos 80
            xsize 690
            ysize 890

            fixed:
                if hovered_char:
                    text hovered_char["name"]:
                        size 160
                        color "#000000"
                        font "Iskra.ttf"
                        xpos 10
                        ypos -10
                elif hovered_item:
                    text hovered_item["name"]:
                        size 100
                        color "#000000"
                        font "Iskra.ttf"
                        xpos 10
                        ypos 10

                text (hovered_char["desc"] if hovered_char else hovered_item["desc"]):
                    size 60
                    color "#000000"
                    font "Iskra.ttf"
                    xpos 22
                    ypos 140
    imagebutton:
        auto "images/notebook/cancel_%s.png"
        xalign 0.005
        yalign 0.005
        action [Hide("notebook_screen")]
    key "K_ESCAPE" action [Hide("notebook_screen")]
    key "K_j" action [Hide("notebook_screen")]
screen notebook_tab_screen():

    add "images/notebook/tab_main.png":
        xalign 0.975
        yalign 0.45

    frame:
        xalign 0.9744
        yalign 0.45
        background None

        grid 1 5 spacing -5:

            for tab in notebook_tab:

                # FIXED SLOT
                if tab["unlocked"]:
                    imagebutton:
                        auto "images/notebook/tab_%s_%%s.png" % tab["image"]
                        action SetVariable("current_tab", tab["name"])
                else:
                    imagebutton:
                        idle "images/notebook/tab_locked.png"
screen notebook_char_friend_screen():

    add "images/notebook/friends.png"
    frame:
        xalign 0.08
        yalign 0.16
        background None

        grid 5 1 spacing 4  :

            for char in notebook_chars_friends:

                # FIXED SLOT
                if char["unlocked"]:
                    button:
                        xsize 140
                        ysize 160
                        background "#ffffffff"
                        focus_mask True
                        add "images/notebook/%s.png" % char["image"]:
                            anchor (0.5, 0.5)
                            xpos 50
                            ypos 70
                            at hover_fade
                        action [
                            SetScreenVariable("hovered_char", char),
                            SetScreenVariable("hovered_item", None),
                        ]
                        hovered [
                            SetScreenVariable("hovered_char", char),
                            SetScreenVariable("hovered_item", None),
                        ]
                else:
                    button:
                        xsize 140
                        ysize 160
                        background "#49ff4c00"
                        focus_mask True

screen notebook_char_screen():

    frame:
        xalign 0.08
        yalign 0.8
        background None

        grid 5 4 spacing 1  :

            for char in notebook_chars:

                # FIXED SLOT
                if char["unlocked"]:
                    button:
                        xsize 140
                        ysize 160
                        background "#ffffffff"
                        focus_mask True
                        add "images/notebook/%s.png" % char["image"]:
                            anchor (0.5, 0.5)
                            xpos 50
                            ypos 70
                            at hover_fade
                        action [
                            SetScreenVariable("hovered_char", char),
                            SetScreenVariable("hovered_item", None),
                        ]
                        hovered [
                            SetScreenVariable("hovered_char", char),
                            SetScreenVariable("hovered_item", None),
                        ]
                else:
                    button:
                        xsize 140
                        ysize 160
                        background "#49ff4c00"
                        focus_mask True

screen notebook_key_item_screen():

    add "images/notebook/questline.png"
    frame:
        xalign 0.08
        yalign 0.25
        background None

        grid 4 4 spacing 24:

            for item_id in notebook_key_items:

                $ item = notebook_key_item_data[item_id]
                $ count = notebook_key_item_count[item_id]

                button:
                    xsize 160
                    ysize 160
                    background "#5cff3c00"
                    focus_mask True
                    add "images/notebook/%s.png" % item["image"]:
                        anchor (0.5, 0.5)
                        xpos 75
                        ypos 70
                        at hover_fade
                    action [
                        SetScreenVariable("hovered_item", item),
                        SetScreenVariable("hovered_char", None),
                    ]
                    hovered [
                        SetScreenVariable("hovered_item", item),
                        SetScreenVariable("hovered_char", None),
                    ]
                    if count > 1:
                        text str(count):
                            color "#000000"
                            size 55
                            xalign 0.9
                            yalign 0.99
init python:
    def notebook_unlock(char_name):
        for char in notebook_chars:
            if char["name"] == char_name:
                char["unlocked"] = True
                if not char["unlocked"] == True:
                    renpy.notify(f"Journal unlocked for {char_name}")
                else:
                    pass
                return True 
        return False   
    def notebook_rewrite(char_name, new_desc):
        for char in notebook_chars:
            if char["name"] == char_name:
                char["desc"] = new_desc
                renpy.notify(f"Journal updated for {char_name}")
                return True
        return False

    def refresh_key_item_inventory(clear_all=False):
        if clear_all:
            notebook_key_items[:] = []
            notebook_key_item_count.clear()

        renpy.notify("Notebook key-item inventory refreshed.")

    def key_item_add(item_id):
        if item_id not in notebook_key_item_data:
            renpy.notify(f"Item '{item_id}' not found in notebook_key_item_data.")
            return

        if item_id not in notebook_key_items:
            notebook_key_items.append(item_id)
            notebook_key_item_count[item_id] = 1
        else:
            notebook_key_item_count[item_id] = notebook_key_item_count.get(item_id, 0) + 1

        renpy.notify(f"Obtained: {notebook_key_item_data[item_id]['name']}")

    def key_item_remove(item_id):
        if item_id not in notebook_key_item_data:
            renpy.notify(f"Item '{item_id}' not found in notebook_key_item_data.")
            return

        count = notebook_key_item_count.get(item_id, 0)
        if count <= 0:
            renpy.notify(f"You don't have {notebook_key_item_data[item_id]['name']}.")
            return

        if count > 1:
            notebook_key_item_count[item_id] = count - 1
        else:
            notebook_key_item_count.pop(item_id, None)
            if item_id in notebook_key_items:
                notebook_key_items.remove(item_id)
 
        renpy.notify(f"Removed: {notebook_key_item_data[item_id]['name']}")
