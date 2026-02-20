default quests = {}  # empty at start

init python:
    quest_data = {
        "remi": {"image": "images/task/remiicon.png", "desc": ": Find and talk to Remi again."},
        "sari": {"image": "images/task/sariicon.png", "desc": ": Find Sari and talk to him about the sauce."},
        "sanco": {"image": "images/task/sancoicon.png", "desc": ": Deliver the Glass Daisy bouquet to Toko in Spiralia."},
        "toko": {"image": "images/task/tokoicon.png", "desc": ": Gather 5 specials ingredients: Daisy, Mushroom, Tomato, Fish, Lettuce."},
        "owl": {"image": "images/task/owlicon.png", "desc": ": Capture the 3 pictures: beach, monument, Spiralia."},
    }

    def quest_add(name):
        if name in quest_data:
            quests[name] = quest_data[name].copy()  # copy so original data isn’t overwritten

    def quest_end(name):
        if name in quests:
            del quests[name]

    def quest_desc_change(name, new_desc):
        if name in quests:
            quests[name]["desc"] = new_desc