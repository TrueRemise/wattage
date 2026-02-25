# File: game/systems/remi.rpy

label msg_toko_0:
    "No new messages from Toko."
    call screen message_screen
    return

label msg_toko_map:
    tk "A true skonger doesn't need to bring a map Watta they memorize everything."
    show bg phone mad
    w "Alright..?"
    show bg phone
    call screen message_screen
    return

default toko_first_talk_done_stage = 0
default glass_daisy_check = False
default exquisite_daisy_check = False
default toko_quest_acquired = False
default archeste_open = True
default toko_bad_end = False
default toko_about_remi = False
default toko_jumbo = False

label toko_test:
    if the_knower == 2 and not toko_about_remi:
        $ option_add("toko", "Remi", "toko_about_remi", pos=0)
    if toko_first_talk_done_stage == 0:
        jump toko_first_talk
    elif toko_first_talk_done_stage == 1:
        jump toko_second_talk

label toko_first_talk:
    show bg archeste at whiten
    show toko smile at fade_in_left
    show watta default at right
    tk "Oh heyyyy"
    tk "Didn't expect to see you here Watta"
    tk "How would you get here this early?"
    tk "Who gave you the direction..."
    w "Well i di-{nw}"
    show watta frown
    show toko close
    tk "No it isn't important..."
    show toko smile
    tk "What important is that we finally met Watta."
    tk "What can I help you with?"
    if is_item_get("Glass Daisy"):
        show watta smile at bounced
        w "Well I want to give you these..."
        extend " flowers from Sanco."
        show toko default
        tk "Wait..."
        tk "You met Sanco."
        show toko smile
        tk "Nice."
        tk "How is she?"
        w "Well she's-{nw}"
        tk "Is it the Glass bouquet?"
        show watta frown
        w "Ye?"
        tk "Nice."
        $ quest_desc_change("sanco", ": Go back to Sanco to report the situation.")
        $ glass_daisy_check = True
        $ exquisite_daisy_check = False
        $ item_remove("Glass Daisy")
        tk "Thank you man, them fresh too"
        tk "Also"
    elif is_item_get("Exquisite Daisy"):
        show watta smile at bounced
        w "Well I want to give you these..."
        extend " flowers from Sanco."
        show toko default
        tk "Wait..."
        tk "You met Sanco."
        show toko smile
        tk "Nice."
        tk "How is she?"
        w "Well she's-{nw}"
        tk "Is it the Glass bouquet?"
        show watta sad
        w "Well not really..."
        w "You see there are something happened that..."
        tk "Oh lemme see them."
        tk "Oh you made me worried."
        tk "This is still fine watta, this is usable"
        $ quest_desc_change("sanco", ": Go back to Sanco to report the situation.")
        $ glass_daisy_check = False
        $ exquisite_daisy_check = True
        $ item_remove("Exquisite Daisy")
        tk "Thank you man, I know delivering them is hard, don't stress yourself out too much..."
        tk "Also"
    elif is_item_get("Normal Daisy"):
        show watta smile at bounced
        w "Well I want to give you these..."
        extend " flowers from Sanco."
        show toko default
        tk "Wait..."
        tk "You met Sanco."
        show toko smile
        tk "Nice."
        tk "How is she?"
        w "Well she's-{nw}"
        tk "Is it the Glass bouquet?"
        show watta sad
        w "Well not really..."
        w "You see there are something happened that..."
        tk "Oh lemme see them."
        tk "This is..."
        show toko close2
        tk "This is terrible Watta{nw}"
        w "I know"
        tk "Well"
        tk "This is the worst thing ever that has happened to me..."
        show toko disappointed
        tk "Maybe I was damned to never recover from tat."
        tk "Maybe there is nothing as salvation, maybe we are all doomed"
        w "Is not that bad"
        tk "You don't understand how crucial this is Watta"
        tk "You never considered this seriously"
        w "..."
        show toko close2
        tk "Just leave, Watta, just leave"
        tk "It's enough, I'm sorry"
        w "..."
        scene bg black with Fade(1,0,0)
        $ quest_desc_change("sanco", ": Go back to Sanco to report the situation.")
        $ toko_bad_end = True
        $ archeste_open = False
        $ item_remove("Normal Daisy")
        jump spira
    else:
        w "It's fine I ca-{nw}"
        show toko default at bounced
        show watta upset
        tk "Wait."
        tk "Hold on a minute, I just got a message."
        tk "Well..."
        tk "Seems awkward here but..."
    tk "Can I ask you a favor?"
    show watta default
    w "Yes?"
    tk "Currently I'm in a cooking competition, and I need to pull of this thing called an L'de'bouchaque."
    tk "It will be a guarantee victory me as long as I make it possible"
    tk "But it requires a lot of, y'know, rare ingredients."
    tk "I have them all on a list here, take this."
    show watta default at bounced
    w "Kay"
    if is_item_get("Glass Daisy"):
        tk "Glass Daisy, the hardest one to find, which you already gave me"
    else:
        tk "Glass Daisy, the hardest one to gather, I already asked Sanco to prepare that for me, so you can ask her to deliver it to me."
        tk "She lives near north gate inside Bloomfield, in a store named Floralia. It should be easy to find."
    tk "Chopped Mushroom, which should be the red puffer mushroom kind, it's really far from here so I need help with that."
    tk "Some lettuce and tomatoes"
    tk "And a specific type of fish named the Jumbo fish, should be around in the West Sea."
    tk "Well that's all, if you can help me then I'd own you alot."
    menu:

        "Alrighty.":
            
            $ notebook_unlock("Toko")
            call toko_quest_acquired from _call_toko_quest_acquired
        "Not now":
            tk "It's fine don't stress yourself up."
            tk "Ye"
    show toko smile at bounced
    tk "It's settled, now we can be chill."
    hide watta
    $ toko_first_talk_done_stage = 1
    menu:
        "Talk":
            hide watta
            call screen toko_screen    
            jump toko_talk
        "Nothing for now":
            hide watta
            hide toko
            scene bg archeste
            jump archesteskip


label toko_second_talk:
    show bg archeste at whiten_lesser
    show toko smile at fade_in_left
    tk "What do you want to bring up today?"
label toko_talk_skip:
    call screen toko_screen

default toko_options = {
    "Quest": "toko_quest",
    "Spiralia": "toko_about_spira",
    "Archeste": "toko_about_archeste",
    "Cooking": "toko_about_cooking",
    "Sanco": "toko_about_sanco",
    "Festival": "toko_about_festival",
    "Leave": "toko_byebye",
}
transform hover_sway_stronger:
    alpha 0.0
    xpos 40
    parallel:
        linear 0.3 alpha 1.0
    parallel:
        easein 0.5 xpos 0
    on hover:
        easein_cubic 0.30 xoffset 25
        pause 2
        easeout_cubic 5 xoffset 0
        repeat
    on idle:
        easeout 0.3 xoffset 0
screen toko_screen():
    tag toko_sub
    modal True
    zorder 95

    vbox:
        spacing 60
        xalign 0.7
        yalign 0.25

        if toko_options:
            $ shift = 0
            for name, target_label in toko_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#ffa1a1", "#E35B97", t)
                button:
                    at hover_sway_stronger
                    xsize 820
                    ysize 70
                    xalign 0
                    xoffset -shift
                    background Solid("#FFFFFF00")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)

                    text name:
                        size 110
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(13, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Toko.ttf"

                $ shift += 0

label toko_byebye:
    tk "Well said."
    hide toko
    scene bg archeste
    jump archesteskip

label toko_quest:
    show toko default
    if toko_quest_acquired == False:
        tk "Did you change your mind?"
        menu:
            "I'll do it":
                
                $ notebook_unlock("Toko")
                call toko_quest_acquired from _call_toko_quest_acquired_1
                jump toko_talk_skip
            "Still not now":
                tk "Alright dawg"
    if glass_daisy_check == False and exquisite_daisy_check == False:
        if is_item_get("Glass Daisy"):
            show watta default at right
            w "Toko"
            show toko default at bounced
            tk "Wassup?"
            show watta smile at bounced
            w "Well I want to give you these..."
            extend " flowers from Sanco."
            show toko default
            tk "Wait..."
            tk "You met Sanco."
            show toko smile
            tk "Nice."
            tk "How is she?"
            w "Well she is-{nw}"
            tk "Is it the Glass bouquet?"
            show watta frown
            w "Ye?"
            tk "Nice."
            show screen task_aquired("SANCO'S QUEST COMPLETED", "QUALITY: EXCELLENT", "images/task/tasksanco.png")
            $ quest_desc_change("sanco", ": Go back to Sanco to report the situation.")
            $ glass_daisy_check = True
            $ exquisite_daisy_check = False
            $ item_remove("Glass Daisy")
            tk "Thank you man, them fresh too"
        elif is_item_get("Exquisite Daisy"):
            show watta default at right
            w "Toko"
            show toko default at bounced
            tk "Wassup?"
            show watta smile at bounced
            w "Well I want to give you these..."
            extend " flowers from Sanco."
            show toko default
            tk "Wait..."
            tk "You met Sanco."
            show toko smile
            tk "Nice."
            tk "How is she?"
            w "Well she's-{nw}"
            tk "Is it the Glass bouquet?"
            show watta frown
            w "Well yes but not really..."
            w "You see there are something happened that..."
            tk "Oh lemme see them."
            tk "Oh you made me worried."
            tk "This is still fine watta, this is usable"
            show screen task_aquired("SANCO'S QUEST COMPLETED", "QUALITY: GOOD", "images/task/tasksanco.png")
            $ quest_desc_change("sanco", ": Go back to Sanco to report the situation.")
            $ glass_daisy_check = False
            $ exquisite_daisy_check = True
            $ item_remove("Exquisite Daisy")
            tk "Thank you man, I know delivering them is hard, don't stress yourself out too much..."
            
        elif is_item_get("Exquisite Daisy"):
            show watta smile at bounced
            w "Well I want to give you these..."
            extend " flowers from Sanco."
            show toko default
            tk "Wait..."
            tk "You met Sanco."
            show toko smile
            tk "Nice."
            tk "How is she?"
            w "Well she's-{nw}"
            tk "Is it the Glass bouquet?"
            show watta huh
            w "Well not really..."
            w "You see there are something happened that..."
            tk "Oh lemme see them."
            tk "This is..."
            show toko close2
            tk "This is terrible Watta{nw}"
            w "I know"
            tk "Well"
            tk "This is the worst thing ever that has ever happened to me..."
            show toko disappointed
            tk "Maybe I was damned to never recover from that."
            tk "Maybe there is no salvation, maybe we are all doomed"
            w "Is not that bad"
            tk "You don't understand how crucial this is Watta"
            tk "You never took this seriously"
            show watta sad
            w "..."
            show toko close2
            tk "Just leave, Watta, just leave"
            tk "You've done enough"
            w "I'm sorry..."
            w "..."
            scene bg black with Fade(1,0,0)
            show screen task_aquired("SANCO'S QUEST COMPLETED", "QUALITY: WORST", "images/task/tasksanco.png")
            $ quest_desc_change("sanco", ": : Go back to Sanco to report the situation.")
            $ toko_bad_end = True
            $ archeste_open = False
            $ item_remove("Normal Daisy")
            jump spira
        jump toko_talk_skip
    if toko_quest_acquired:
        tk "Oh... about the gathering..."
        tk "Let's see what you've got..."
        tk "Daisy... "
        if glass_daisy_check == True:
            extend "Glass Daisy, check."
        elif exquisite_daisy_check == True:
            extend " check."
        else:
            extend " uncheck"
        if is_item_get("Homegrown Tomatoes"):
            tk "Tomatoes... check"
        else:
            tk "Tomatoes... uncheck"
        if toko_jumbo:
            tk "Fishes... check"
        else:
            tk "Fishes... uncheck"
        tk "Lettuces... uncheck"
        tk "Mushrooms... uncheck"
    jump toko_talk_skip
label toko_about_spira:
    tk "Spiralia?"
    tk "Ye I can tell your first impression getting here is \"What the hell is going on?\", "
    extend "\"Why are the building shaped this way?\""
    tk "This is the favorite architecture design genre of the Queen, she's...{w=1} can say she's obsessed with spiral."
    tk "You don't know how much crazier they were back in her old reign, it was hell confusing.."
    tk "But I'd say the Queen did prove her designing skill to be amazing,"
    tk "She did make all of those curving spiral-y shaped skyscrapers with immense durability."
    tk "I really don't think the ruins was her fault really, I do think no tall building could withstand it."
    tk "The academy survived but as you can see it crooked to one side, "
    extend "and with this current mental state of the Queen hardly would it be rebuilt."
    tk "Spiral shaped house maybe a little cramped? But they are really good when we talk weather."
    tk "Rain, snow, actually there is no snow here if if there is it would not be a problem at all."
    tk "Even earthquake and tsunami all thanks to the hydrodynamic design, really good really."
    tk "Enough with the housing, the history of this land is a myth."
    tk "All I can tell is like around 100 years ago or so, when the Queen got here, she made this land the Queen's capital."
    tk "And immediately build an academy, she was really in a hurry back then."
    tk "Now there are 2 capitals, the centre and this one, the centre depends less on the queen, so the big depression doesn't affect them too much,"
    tk "But this area can't be said the same"
    tk "Due to this most people left Spira thus leading to this desserted state."
    tk "People decided to stay are just people who really can't move out of here."
    tk "Like me"
    jump toko_talk_skip
label toko_about_archeste:
    tk "This is my store, Archeste."
    tk "I sell instruments and stuffs, that's all to it,"
    tk "Due to being close to the academy, this used to be an excellent place for income,"
    tk "You know, students buying their stuffs, I also did try to be a tutor for a while"
    tk "But the incident and now I'm drying here, academy closed people moved to the centre, I'd say I still prefer here than most place,"
    tk "And I'll try my best to revive the Queen's capital"
    tk "But such is hard to accomplish"
    jump toko_talk_skip
label toko_about_cooking:
    show toko default
    tk "It's a competition around the monument,"
    tk "I said it's a competition but actually it's just, you prepare your food at home and bring it there,"
    tk "So more like a test about who can preserve their foods the best, extra point if you are far away from the hosting site"
    tk "Which I am"
    tk "The prize of this one is around, I dont't remember but it's a lot it would be enough to support me in her for at least 3 years."
    tk "I need to win this to continue my career."
    tk "If I fail I will have to, probably moving out of here,... it's a pretty big decision"
    tk "I hope that won't happen, because I'm confident in my recipe."
    tk "It's only a matter of gathering them."
    jump toko_talk_skip
label toko_about_sanco:
    show toko default
    tk "I wish Sanco continued pursuing her path."
    tk "Well she kinda did... what she's doing is similar"
    tk "But not in the direction I'm talking about"
    tk "We were pretty close back in the day, even when I was from another major, we often hang out"
    tk "And the storm hits and she's forced to go back to the field, I'm feeling kind of bad"
    show toko default
    jump toko_talk_skip
label toko_about_festival:
    show toko default
    tk "The festival might help a bit with the recovering"
    tk "Tho I belive thing won't change much after it ends."
    tk "I still need to get my hands on that cash pile"
    jump toko_talk_skip
label toko_about_remi:
    show toko default
    tk "Remi huh?"
    tk "Haven't heard of him for a while, he doesnt visit here much"
    tk "But I know that he's trying to hide again, too bad"
    tk "The best architecture abandoning everything important to him, to gain a little bit of solitude"
    tk "He did help me with the making of some of the electric based instrument here, so i own him that."
    tk "I just think he shouldn't just trying to hide everytime something gets to him it's just"
    extend " not good"
    tk "He's profound at keeping things in check but his mentality, I think he'd come back but for the time it's too bad"
    tk "Because I believe things will go much smoother if he tries to help us, but I guess there is someone that he doesn't want to show up to"
    tk "Too bad"
    $ toko_about_remi = True
    $ remi_opinion += 1
    $ option_remove("toko","Remi")
    jump toko_talk_skip

label toko_quest_acquired:
    show toko smile
    tk "Nice!"
    show screen task_aquired("TOKO'S QUEST ACQUIRED", "GATHER 5 INGREDIENTS", "images/task/tasktoko.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    $ quest_add("toko")
    $ notebook_unlock("Toko")
    $ toko_quest_acquired = True
    return