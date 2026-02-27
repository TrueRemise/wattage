default sari_first_talk_done_stage = 0
default sari_exam_timer = 0
default sari_about_remi = False
default sari_about_iog = False

label msg_sari_0:
    sr "https://tenor.com/view/hikikomori-rose-sweet-anime-gif-9340309"
    w "https://tenor.com/view/rover-phoebe-fibi-phibi-wuthering-waves-gif-11077711965614799918"
    call screen message_screen
    return

label sari_first_talk:
    if the_knower == 2 and not sari_about_remi:
        $ option_add("sari", "Remi", "sari_about_remi", pos=0)
    if day >= 3 and not sari_about_iog:
        $ option_add("sari", "Iog", "sari_about_iog", pos=0)
    if sari_first_talk_done_stage == 0:
        jump sari_first_talk_real
    elif sari_first_talk_done_stage == 1 and not is_item_get("Sari's Sauce"):
        jump sari_first_talk_done_but_no_sauce
    elif sari_first_talk_done_stage == 1 and is_item_get("Sari's Sauce"):
        jump sari_sauce_check_at_first
    elif sari_first_talk_done_stage == 2:
        jump sari_waiting_for_sauce_check
    elif sari_first_talk_done_stage == 3:
        if is_item_get("Flavored Sauce"):
            jump sari_flavored_sauce
        jump sari_talk
label sari_first_talk_real:
    scene bg van with Fade(1, 0, 1)
    show bg van at whiten
    show sari smile at right
    show watta happy at left
    sr "Yoooooooooo! It's you"
    show watta frown
    show sari serious at shake
    sr "Hol' on..."
    show sari smile at bounced
    sr "All done!"
    sr "Finally seeing your ass again"
    show watta happy
    sr "Come take a seat!"
    show watta happy at bounced
    w "Alright! If you don't mind..."
    sr "Do you wanna try the new Tolantro Sauce of the Winterlands Watta?"
    show watta sweat at shaker
    show sari yummers
    sr "Extra hot. Extra deep. Best with a bowl of hot broth"
    w "No, not really thank you-"
    show sari sus at bounced
    sr "Why so-"
    sr "You didn't even get to hear what it's about"
    show watta upset
    w "..."
    sr "Did you even finish up the one I sent you long ago?"
    if not is_item_get("Sari's Sauce"):
        show watta upset at bounced
        w "About that one..."
        sr "Don't tell me you..."
        show sari michiru
        sr "Forgot it exists???"
        w "{size=-10}I'm sorry"
        sr "Whatever!"
        show sari speed
        sr "My sauces are pretty forgettable after all"
        show watta upset at shake
        pause 0.5
        show sari speak
        show watta huh
        sr "But speaking of which..."
        sr "It should have been expired by now"
        show sari close
        sr "I have... {w=0.5}{nw}"
        show sari michiru at shake
        show watta upset
        extend "never seen my sauce getting expired"
        show sari speak
        sr "I'm pretty curious what happened to it."
        sr "Before anything else, you should lemme see what it's like now"
        sr "Go home and find it..."
        show watta upset at shake
        w "{i}This dude"
        hide watta
        hide sari
        $ sari_first_talk_done_stage = 1
        $ quest_add("sari")
        $ quest_desc_change("sari", ": Go home and find Sari's Sauce and give it to Sari")
        jump vanskip
    else:
        show watta sweat at bounced
        w "About that one..."
        w "I forgot I had it in my fridge"
        show sari michiru at shake
        sr "Knew it!"
        show watta huh
        w "But I'm not sure if is still edible so-"
        show sari michiru at bounce
        sr "DEFINITELY NOT!"
        sr "It's been 4 months Watta"
        sr "Plus that shipping condition, that is just enough for a week, it should be expired by now."
        w "{size=-10}I'm sorry"
        show sari speed
        sr "Nevermind"
        show sari close
        sr "I have... {w=0.5}{nw}"
        show sari michiru at shake
        show watta upset
        extend "never seen my sauce getting expired"
        show sari speak
        sr "I'm pretty curious what happened to it."
        sr "Before anything else, you should lemme see what it's like now"
        w "Oh sure here is it!"
        show sari serious
        sr "Brought it with you didn't ya?"
        show sari sus
        sr "Strange"
        jump sari_sauce_check_at_first
    jump sari_first_talk

label sari_first_talk_done_but_no_sauce:
    scene bg van
    show bg van at whiten
    show sari close
    sr "Nuh uh uh, show me the sauce first"
    hide sari
    jump vanskip

label sari_sauce_check_at_first:
    scene bg van with Fade(1, 0, 1)
    show bg van at whiten
    show sari squint at right
    show watta default at left
    sr "Incredible!"
    sr "I have never seen these pattern before"
    show sari smile
    show watta happy
    sr "This is good news! I can use this to make better and more unique sauce"
    sr "I must investigate further, I need more time."
    show sari speak at bounced
    sr "Thank you for bringing me this-"
    sr "Now give me time won't ya?"
    show watta upset
    w "{i}This dude, I can't talk to him at all"
    hide sari
    hide watta
    show screen task_aquired("SARI'S QUEST ACQUIRED", "TALK TO SARI AFTER IT'S DONE", "images/task/tasksari.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    $ sari_first_talk_done_stage = 2
    $ sari_exam_timer = 1
    $ quest_add("sari")
    $ quest_desc_change("sari",": Talk to Sari when he's done with the examination")
    $ item_remove("Sari's Sauce")
    jump vanskip

label sari_waiting_for_sauce_check:
    if sari_exam_timer <3:
        scene bg van
        show bg van at whiten
        show sari close
        sr "Give me some time brother -"
        hide sari
        jump vanskip
    else:
        show bg van at whiten
        show sari smile
        sr "This is good"
        sr "This is what I wanted"
        sr "I never liked fungus but, this is revolutionary..."
        sr "They're symbiotic...  creating something amazing in the process."
        show sari serious
        sr "But I cannot celebrate so fast..."
        show sari speak
        sr "I need you to deliver a sample to my assistant in Spiralia."
        sr "I need his opinion."
        sr "Bring this to the Spiralia's Railwork Hall, you will meet him there, ask him to try out this new sauce."
        $ item_add("Sari's Sauce")
        $ quest_desc_change("sari",": Deliver the sauce to Sari's assistant in Spiralia.")
        show sari close at bounced
        
        $ notebook_unlock("Sari")
        sr "Now if you have anything to talk about..."
        $ sari_first_talk_done_stage = 3
        menu:
            "Okie dokie":
                show sari close at slide_to_right
                hide watta
                jump sari_talk_skip
            "Nothing for now":
                hide watta
                hide sari
                scene bg van
                jump vanskip

default talk_about_hunger_first = False
label sari_talk:
    show bg van at whiten_lesser
    show sari smile at right
    sr "What do you need mate?"
label sari_talk_skip:
    if not talk_about_hunger_first:
        "In this game, having a full stomach is important."
        "Since your fridge is empty, you need to buy food home to get enough energy for the next day."
        "If food wasn't prepared, you will start the next day with 2 less actions at Dawn."
        "Remember to buy them through Sari's, and no the foods don't stack for several days, buying 2 in a row is wasting money."
        $ talk_about_hunger_first = True
    call screen sari_screen

default sari_options = {
    "Buy Food": "sari_buy_food",
    "Jonpark": "sari_about_jonpark",
    "Sari's Spice": "sari_about_spice",
    "Assistant": "sari_about_fe",
    "Festival": "sari_about_festival",
    "Leave": "sari_byebye",
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
screen sari_screen():
    tag sari_sub
    modal True
    zorder 95

    vbox:
        spacing 50
        xalign 0.5
        yalign 0.25

        if sari_options:
            $ shift = 0
            for name, target_label in sari_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#6625ff", "#e35b5b", t)
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
                        size 120
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(13, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "sari.ttf"

                $ shift += 30

label sari_byebye:
    sr "Kay."
    hide sari
    scene bg van
    jump vanskip

default sari_food_bought = False
label sari_buy_food:
    show sari default
    if food_prepared == True:
        show sari squint
        sr "You are buying a lot, you got babes at home?"
        show sari smile
        sr "Just kidding"
        show sari squint
        sr "...Unless?"
        jump sari_buy_food_skip
    else:
        pass
    sr "Wanna buy my sauce? The food comes in as free additions"
    label sari_buy_food_skip:
    menu:
        "Alright (-25 SOL)":
            if sol >= 25:
                show sari smile
                sr "Great, here you go"
                sr "You can waste the food but make sure to never waste the sauce"
                show sari squint
                sr "Or else..."
                $ sol -= 25
                $ food_prepared = True
                $ sari_food_bought = True
            else:
                show sari michiru
                sr "Weren't you taught to never come to a store without cash?"
                sr "Go get it"
        "Nah":
            show sari michiru
            sr "Then why would you ask about it in the first place?"
            sr "Don't give people false hope"
            show sari default
    jump sari_talk_skip
label sari_about_jonpark:
    show sari smile at bounced
    sr "This is where I work"
    show sari default
    sr "Why only here? Eh, I honestly just like this place"
    sr "Even if it's not a busy area."
    show sari smile
    sr "But it's a very peaceful place at least"
    show sari default
    sr "...At least compared to the other locations."
    show sari speak
    sr "I've been around here for as long as I remember, even before the van"
    sr "The fresh air is very nice, a much needed respite after the years of office work"
    show sari yummers
    sr "Oh you don't know how exceptional it is to try Everraisin on a hotdog here,"
    sr "I could eat it all day."
    jump sari_talk_skip
label sari_about_spice:
    sr "My life is bound to this simple van."
    show sari close
    sr "It's been quite a ride, now I'm concocting and selling spices and sauces."
    show sari default
    sr "Why sauce you asked?"
    show sari serious
    sr "Well until you drown in paperwork and sheets, I don't think you'll ever understand."
    sr "That being said, I don't think I can keep this up forever."
    show sari speak
    sr "This van used to look so much different before, it was pretty gorgeous I must say"
    jump sari_talk_skip
label sari_about_fe:
    show sari speak
    sr "My assistant?"
    show sari speed
    sr "He was once the peer of my career, he also helped me in making spices."
    sr "But his current job drives him far from here, leading him to uncharted land."
    show sari surprised
    sr "How to get to Spiralia?"
    show sari sus
    sr "I have no idea, my old head is catching up."
    sr "Maybe you should find a local and ask, maybe Toko."
    show sari squint
    sr "Oh wait I forgot he lives there TOO."
    jump sari_talk_skip
label sari_about_festival:
    show sari smile
    sr "The festival huh?"
    show sari speak
    sr "It'd be the same as usual for me, it's not like I'll get less work to do."
    sr "There aren't many interesting things for me out there anyways.."
    show sari smile
    sr "But it's different for you."
    show sari yummers
    sr "Go out and meet new people, Watta."
    sr "This is a canon event."
    jump sari_talk_skip
label sari_about_remi:
    show sari sus
    sr "Remi?"
    sr "Why him out of nowhere?"
    show sari speed
    sr "Well outside of the fact he is capable of pissing people off sometimes,"
    extend " with or without those \"lobotomy\" sessions."
    show sari default
    sr "He's good at his job I guess"
    extend ", he helped with the reconstruction and renovation of many buildings in this city."
    sr "So to many normal citizens he's a big figure,..."
    show sari sus
    sr "Huh? What did he piss me off about?"
    show sari speed
    sr "No one could piss me off Watta, but if you are dying to know what he did,"
    show sari speak
    sr "Put it simply, he lets his mood influence himself too much,"
    extend "Sometimes we invite him to join a game session and somehow he ruins it because somehow it makes him mad?"
    show sari speed
    sr "No idea tbh,"
    show sari speed
    extend " now I'm fine with him, I can see he did have a {i}tiny{/i} bit of improvement,"
    extend " I'd still invite him if we have extra slots."
    $ option_remove("sari","Remi")
    $ sari_about_remi = True
    $ remi_opinion += 1
    jump sari_talk_skip
label sari_about_iog:
    show sari default
    sr "That dude outside?"
    extend ", idk what he does tbh, but like..."
    sr "He sells food that goes along with my sauce, so it's a symbiotic relationship."
    show sari smile
    sr "No reason to complain about such an opportunity."
    $ notebook_unlock("Iog")
    $ option_remove("sari","Iog")
    $ sari_about_iog = True
    jump sari_talk_skip


label sari_flavored_sauce:
    show bg van at whiten
    show sari smile
    sr "Oh it's arrived, okay great!"
    sr "Bailey is a good tester, he can make quality stuff"
    show sari close
    sr "I will study this more, but for now that's all you need to do"
    show sari speak
    sr "Peace"
    hide sari
    hide watta
    show screen task_aquired("SARI'S QUEST COMPLETED", "QUALITY: GOOD", "images/task/tasksari.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    $ item_remove("Flavored Sauce")
    jump vanskip

    