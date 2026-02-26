# File: game/systems/remi.rpy
label msg_sanco_0:
    show bg phone
    "No new messages from Sanco."
    call screen message_screen
    return


label msg_sanco_early:
    show bg phone
    sc "Watta I need some help!"
    sc "I need to speak to you before I forget."
    sc "Come to my house when you are free."
    sc "I need you to deliver a package."
    menu:
        "Can you remind me where it is?":
            jump you_dont_know_where_sanco_house_is
        "Okay sure then!":
            jump you_know_where_sanco_house_is
label you_dont_know_where_sanco_house_is:
    sc "Oh yeah I forgot you don't know? It's 139th row Bloomfield going through the monument."
label you_know_where_sanco_house_is:
    sc "Hope to see ya soon!"
    w "I'll see if I can after work." 
    $ sanco_talked_through_phone_before = True
    $ update_msg_phase("Sanco", "early1")
    call screen message_screen
    return

label msg_sanco_daheo_tsu_doin:
    show bg phone
    w "I'm uhh I was at the Northgate... But there is this one person that keeps blocking the path."
    sc "Uhh can you remind who that is again?"
    w "The one with white everything."
    sc "Oh Tsuyu, don't mind him too much. If you have something to cheer him up then he'll let you through."
    sc "Oh and alternatively, you can check that place after they switch the guard."
    w "Thanks for the info."
    call screen message_screen
    return

label msg_sanco_early1:
    show bg phone
    sc "Hi Watta, do you need anything?"
    menu:
        "Can you remind me where it is again?":
            jump you_dont_know_where_sanco_house_is
        "Nothing in particular, I'll get there soon.":
            jump you_know_where_sanco_house_is
    call screen message_screen
    return

label msg_sanco_ruins_lost:
    show bg phone
    "No response."
    show bg phone mad
    w "What the hell?"
    $ update_msg_phase("Sanco", "0")
    call screen message_screen
    return

default sanco_first_talk_done_stage = 0
default sanco_talked_through_phone_before = False
default sanco_talked_about_chii = False
default glass_daisy_timer = 0
default sanco_quest_acquired = False
default spiralia_direction_noted = False
default soul_of_corruption = False
default sanco_about_thorns = False
default sanco_about_blood = False
default sanco_about_remi = False
default sanco_about_owl = False
default sanco_end_toko_talk = False
default sanco_spiralia_location_woogie_help_toggle = False

label sanco_test:
    if sanco_first_talk_done_stage == 0:
        jump sanco_first_talk
    elif sanco_first_talk_done_stage == 1:
        jump sanco_second_talk

label sanco_first_talk:
    show bg floralia at whiten
    show sanco smile2 at fade_in_left
    sc "Welcome custom-"
    show sanco what
    sc "Oh!"
    show sanco smile at bounced
    sc "Watta, is that you? Welcome to Floralia!"
    show watta default at fade_in_right
    w "Hello Sanco"
    w "We finally meet in person."
    show sanco smile2
    sc "How have you been doin'?"
    w "Pretty good so far..."
    show sanco smile
    sc "I see, glad to hear that"
    call sanco_first_talk_branch from _call_sanco_first_talk_branch
    sc "..."
    w "What's been going on anyways?"
    show sanco smile
    sc "Oh, I'm getting a little bit busier these couple of weeks preparing for the Festival. I wanna send Toko this bouquet of Glass Daisy for his cooking assignment."
    sc "They are really strict about the ingredient requirements and this is the most I could do so please go help him out. "
    menu:
        "Oh I see, I'll try to do it then.":
            
            $ notebook_unlock("Sanco")
            call sanco_quest_acquired from _call_sanco_quest_acquired
        "Not now":
            sc "I see, it's totally fine, ask me when you are ready."
            sc "Ehh"
    show sanco smile at bounced
    sc "While you're here do you wanna talk about anything else?"
    $ sanco_first_talk_done_stage = 1
    menu:
        "Okie dokie":
            hide watta
            jump sanco_talk_skip
        "Nothing for now":
            hide watta
            hide sanco
            scene bg floralia
            jump floraliaskip


label sanco_first_talk_branch:
    if sanco_talked_through_phone_before == True:
        sc "Watta what brings you here out of every place?"
        show watta huh
        w "Uhh you were talking about delivering a package or something."
        show sanco what at bounced
        sc "Oh that!"
        show sanco smile2
        sc "You came at the perfect time actually, I already have the package ready for you."
        show watta smile
        w "Nice!"
        return
    else: 
        show sanco what
        sc "Hold on.... Hmmmmmmmmm"
        show watta sweat
        w "???"
        show sanco smile at bounced
        sc "Oh right! You came at the right time, Watta. I have something you can help with!"
        show watta smile
        w "Oh what is?"
        show sanco smile2
        sc "It's a package I wanted to send Toko.."
        w "Oh that sounds great!"
        return

label sanco_second_talk:
    show bg floralia at whiten_lesser
    show sanco smile2 at fade_in_left
    sc "What can I help you with today?"
    label sanco_talk_skip:
    if sanco_end_toko_talk:
        $ option_add("sanco", "Memory Loss", "sanco_about_condition", pos=0)
    if toko_bad_end or glass_daisy_check or exquisite_daisy_check:
        $ option_remove("sanco","Quest")
    if not sanco_talked_about_chii:
        if chii_first_talk_done_stage >= 1:
            $ option_add("sanco", "Chii", "sanco_about_chii", pos=1)
    if chii_meet_sanco_timer >= 1 and chii_meet_sanco_timer <= 3:
            $ option_add("sanco", "Chii's arrival", "sanco_about_chii_arrival", pos=1)
    elif chii_meet_sanco_timer == 5 and not soul_of_corruption:
        $ option_remove("sanco","Chii's arrival")
        $ option_add("sanco", "Chii", "sanco_about_chii_2", pos=1)
    if the_knower == 2 and not sanco_about_remi:
        $ option_add("sanco", "Remi", "sanco_about_remi", pos=0)
    elif the_knower == 2 and not sanco_about_owl:
        $ option_remove("sanco","Remi")
        $ option_add("sanco", "Meeting Owl", "sanco_about_owl", pos=0)
    if impenetrable_thorns and not sanco_about_thorns:
        $ option_add("sanco", "Thorns", "sanco_about_thorns", pos=1)
    elif soul_of_bloomfield and is_item_get("Defiled Blood") and not sanco_about_blood:
        $ option_remove("sanco","Thorns")
        $ option_add("sanco", "Defiled Blood", "sanco_about_blood", pos=1)
    elif soul_of_bloomfield and is_item_get("Defiled Blood") and sanco_about_blood and the_knower == 2 and sanco_about_owl and not soul_of_corruption:
        $ option_remove("sanco","Defiled Blood")
        $ option_remove("sanco","Meeting Owl")
        $ option_add("sanco", "Burn the thorns", "sanco_about_burning", pos=1)
    call screen sanco_screen

default sanco_options = {
    "Quest": "sanco_quest",
    "Bloomfield": "sanco_about_bloomfield",
    "Floralia": "sanco_about_floralia",
    "Toko": "sanco_about_toko",
    "Festival": "sanco_about_festival",
    "Leave": "sanco_byebye",
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
screen sanco_screen():
    tag sanco_sub
    modal True
    zorder 95

    vbox:
        spacing 50
        xalign 0.7
        yalign 0.25

        if sanco_options:
            $ shift = 0
            for name, target_label in sanco_options.items():

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
                        size 120
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(13, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "sanco.ttf"

                $ shift += 0

label sanco_byebye:
    sc "Okay see you!"
    hide sanco
    scene bg floralia
    jump floraliaskip

label sanco_quest:
    if sanco_quest_acquired == False:
        sc "Are you ready now?"
        menu:
            "Yes, give me the flowers":
                $ notebook_unlock("Sanco")
                call sanco_quest_acquired from _call_sanco_quest_acquired_1
                jump sanco_talk_skip
            "Not now":
                sc "I see, it's totally fine, ask me when you are ready."
                jump sanco_talk_skip
    if ruins_first_sanco == False or spiralia_direction_noted == True:
        show sanco smile at bounced
        sc "Be safe out there"
        jump sanco_talk_skip
    else:
        show sanco wait at bounce
        sc "Oh my Elena I forgot to give you directions to Spiralia."
        sc "My fault there dearly."
        show sanco sweat
        sc "Let me tell you the directions..."
        if not is_item_get("Memorizing Sheet"):
            sc "It's Š'»®b|õÕÿ‡£®ùIkW ¡Q„‚m.²âqOÅzÙq¾D^wßÊ¢ãÓWà¯¾®,ªG.^ı­æ× ÆÁòTôM¡êt>}¢¶Ó"
            show watta frown at right
            w "Huh?"
            w "What is it again?"
            show sanco default at bounced
            sc "Huh?"
            w "Nothing nevermind"
            w "{i}I shouldn't bother her further, I need something to note it down on."
            hide watta
            jump sanco_talk_skip
        else:
            show watta deter at right
            w "Hold on Sanco"
            show sanco default at bounced
            sc "Yes?"
            w "Can you note it down here instead?"
            show sanco smile2
            sc "Yes of course,"
            "Directions noted in memorizing sheet."
            $ spiralia_direction_noted = True
            hide watta
            jump sanco_talk_skip
label sanco_about_bloomfield:
    show sanco smile at bounced
    sc "Bloomfield is a huge indoor residental area, it's also a giant greenhouse using artificial ceiling light everyday to cultivate plants."
    show sanco sweat
    sc "But recently I think it's used more as a bunker than a residental area..."
    show sanco sad
    sc "After the incident..."
    sc "Not many people want to visit this area anymore, and people here also don't want to set foot outside."
    sc "Like a cold war is going on..."
    show sanco smile2
    sc "But sad stories aside, this area is pretty old compared to the elsewhere."
    sc "Built under The Monarch's rule a really long ago, she believes a giant greenhouse is needed for cultivating crops, solving starvation while keeping a fairly low product price."
    show sanco smile at bounced
    sc "And her plan worked out excellently, the quality of the vegatation grown here exceeded all expectation."
    sc "Bumping terrain, high-grade soil, full spectrum and UV-rich ceiling light, together created a wonderful agronomical benefitting zone."
    sc "People would come here often to buy our plants or to start a farming business."
    sc "She did create the area big enough so people can move in and live here as well"
    show sanco sweat
    sc "The area initially received a lot of backlash from citizens..."
    sc "People say the light is too dim, the UV-B amount is not enough for a healthy basis..."
    sc "Some complained that the bumping ground is hard to traverse around, that's why we have cabins all around the place..."
    sc "Some asked why we would harvest wind power energy instead of solar one..."
    sc "Some just don't like the spheric house design that's made to spread light evenly across the area, though as you can see no one really minds that anymore."
    sc "I even got a huge lotus on top of my house."
    show sanco smile2
    sc "All that backlash was reasonable but I think many people would risk some minor quality of life for a little more financial benefits."
    sc "Which knowing who the Monarch is, she definitely knows and decided to do nothing about it."
    sc "Beside agriculturing we also have a lot of landmarks and places to enjoy ourselves in."
    sc "The foodstalls, restaurants, metros, marts are all marvelous places to visit once you're here"
    show sanco smile at bounced
    sc "And of course, my store, so feel at home!"
    jump sanco_talk_skip
label sanco_about_floralia:
    sc "This is my store, Floralia."
    show sanco sweat
    sc "The name and design is obviously Bloomfield style."
    sc "I sell accessories and jewelries here."
    show sanco what
    sc "Huh?"
    show sanco smile
    sc "Oh I'm not that rich at all, compared to most people here I'm just around middle-class at most."
    sc "I'm pretty much obsessed with handmade stuffs and just started dwelling into shiny things recently."
    show sanco smile2
    sc "Yes most of the accessories here are handmade"
    sc "It's been lovely so far!"
    show sanco smile at bounced
    sc "Some would look lovely on you too, Watta!"
    jump sanco_talk_skip
label sanco_about_toko:
    if toko_bad_end == True and not sanco_end_toko_talk:
        show sanco what at bounced
        sc "What? He got mad and kicked you out of the store?"
        show sanco sad
        sc "I see... He was reasonably mad for that"
        sc "You see... That competition is everything to Toko, he has everything prepared for it."
        sc "This mistake is quite.. severe as you can see"
        sc "Without winning this his store will hardly recover from the loss"
        sc "It's okay Watta just push this aside I will try to confront him,"
        sc "And we will find a way to get through this together..."
        $ quest_desc_change("sanco", ": Ask Sanco about the condition.")
        $ sanco_end_toko_talk = True
        jump sanco_talk_skip
    elif glass_daisy_check and not sanco_end_toko_talk:
        show sanco smile
        sc "Oh you delievered it to him on time. Thank you again!"
        show sanco what
        sc "What? You knew the direction to the area already?"
        sc "That's...{w=0.5} wonderful."
        sc "And you brought him the highest quality one as well"
        show sanco smile2
        sc "I can't think of how much to thank you. Watta."
        sc "You are a lifesaver"
        sc "Here, for your troubles, 300 sol"
        $ sol_add(300)
        sc "And..."
        label sanco_code_gen:
        show sanco smile
        extend " as a thank you gift I will give you this rare artifact as a reward."
        show sanco sweat
        sc "But I had to hide it far away from intruders, so it's now deep inside a cave within the ruins"
        sc "I did that back when my condition wasn't as bad."
        sc "I can't leave the field so would you mind getting it yourself Watta? I'm really sorry for the trouble..."
        show sanco smile
        sc "Luckily I still remember the path to it, it's something I never forget."
        "This is a stone challenge, each number will appear for a short while before moving to the next number, the sequence of numbers can be input as the ruins' code to access the stone,"
        "As a challenge, you are not allowed to use Memorizing Sheet, any other methods works fine,"
        "This will be said only once and will be randomly generated each time."
        show sanco smile2 at bounced
        sc "Are you ready?"
        sc "Three...{w=1} Two...{w=1} One...{w=1}{nw}"
        show sanco smile
        $ generate_stone_order()

        # disable saving to history
        $ _history = False

        python:
            for ruins_code in stone_order:
                renpy.say(sc, f"{{size=+80}}{ruins_code}{{w=0.3}}{{nw}}")

        # re-enable history
        $ _history = True

        window hide
        sc "Did you catch all of that?"
        show sanco smile2
        sc "Goodluck finding it!"
        $ quest_desc_change("sanco", ": Ask Sanco about the condition.")
        $ sanco_end_toko_talk = True
        $ option_remove("sanco","Toko")
        jump sanco_talk_skip
    elif exquisite_daisy_check and not sanco_end_toko_talk:
        show sanco smile
        sc "Oh you delievered it to him on time. Thank you again!"
        show sanco sweat
        sc "Ye can't really avoid it turning worse after night"
        show sanco sad 
        sc "That's my bad really if only I didn't forget to tell you the direction"
        sc "Oh my poor head"
        sc "But either way, "
        jump sanco_code_gen
    else:
        show sanco sad at bounced
        sc "Toko never liked this place, planting and stuff isn't for him."
        show sanco default
        sc "He decided to stay close to the academy and open a shop there to continue pursuing his dream."
        sc "He is the only 2 out of 7 to still be on track of their initial goals, alongside Reni."
        show sanco smile
        sc "Which is admirable really."
        sc "Though I would like it more if it isn't somewhere too far, in the end I respect his decision though"
label sanco_about_festival:
    show sanco smile
    sc "The Sidurina Festival is coming soon,"
    sc "I'm currently helping with the preparations in Bloomfield."
    sc "It's the biggest event here and pretty much also the reason we leave our home to socialize more."
    show sanco smile2 at bounced
    sc "A really lovely one honestly"
    jump sanco_talk_skip
label sanco_about_chii:
    show sanco what at bounced
    sc "Oh?"
    sc "You're saying there's a Bloomfield resident that moved to the Metra centre just yesterday?"
    sc "That's an odd case, it's been so long since someone here decided to move out other than tourists."
    show sanco sweat
    sc "Well I do want to meet her of course but I can't move out of here for various reasons."
    sc "Can you get me in contact?"
    $ option_remove("sanco","Chii")
    $ sanco_talked_about_chii = True
    jump sanco_talk_skip
label sanco_about_chii_arrival:
    show sanco what at bounced
    sc "What?"
    sc "They're coming all the way here?"
    sc "That's surprising, I didn't know they would put in effort to go all the way back here."
    show sanco sweat
    sc "Thanks for letting me know, I'll go get prepared."
    jump sanco_talk_skip
label sanco_about_chii_2:
    show sanco smile
    sc "Chii was a kind and innocent girl, a really rare kind of person."
    sc "She welcomed me with a lot of flowers and a gift."
    sc "We spent some time together doing handycraft."
    sc "It was quite delightfully in all honesty!"
    sc "We made some flower charms too! She asked if she can put one on sale and I couldn't really decline, she's a merchant after all."
    if soul_of_bloomfield == True:
        show sanco what at bounce
        sc "Oh you already bought them!"
        sc "Quite surprised to see..."
        sc "But either way."
    show sanco smile2
    sc "I'd like to meet her again sometime"
    jump sanco_talk_skip
label sanco_about_thorns:
    show sanco what at bounced
    sc "The impenetrable thorns?"
    show sanco sweat
    sc "It wasn't really a kind of plant, more like a sort of thorns magic casted by the monarch in an attempt to seal off the lake."
    sc "No one knows why it was sealed off, neither they know how to remove the seal, but people do follow and try to avoid that area altogether."
    sc "With Owl being the one volunteered to be sealed off along with it, to become the lake's guardian."
    show sanco sad
    sc "It's been a while since I have heard anything from them..."
    $ sanco_about_thorns = True
    jump sanco_talk_skip
label sanco_about_blood:
    show sanco shock
    sc "Is that..."
    extend " blood?"
    sc "Get it out please!"
    sc "No I am, serious. You don't understand how bad things can go with that."
    sc "The reason many people weren't let in is because many of them have the blood of heresy."
    sc "The blood of someone who goes against monarch Monna."
    show sanco sad
    sc "It was defined as the stain that go against all of monarch's nature."
    sc "And since the entirety of Bloomfield and its people are from her nature, this could cause a corruption."
    sc "Which is a big disruption of everything, I really can't put it into words."
    sc "This is why visitors are heavily gatekept to check for their bloods so they don't get in here and produce children with mixed blood"
    sc "We tried to let some in during the incident for shelter and things went so badly we had to really shut it down for good."
    show sanco shock
    sc "How did you get this?"
    show sanco sad
    sc "No actually just, get this out of here and toss it away for everyone's safety"
    sc "And don't talk to any one here about it..."
    $ sanco_about_blood = True
    jump sanco_talk_skip
label sanco_about_condition:
    show sanco what
    sc "So you..."
    show sanco sad
    extend " noticed?"
    sc "Yes I have this condition"
    sc "Ever since the incident, my memory was only getting worse."
    sc "I can hardly remember anything for more than a day."
    sc "Leading to a lot of problems"
    sc "I scared I would forget my way home if I venture outside, that's why I just stayed in one place"
    if is_item_get("Memorizing Sheet"):
        show sanco what
        sc "Memorizing sheet? I do use them Watta, they are produced here after all."
        show sanco sad
        sc "But these sheet are only for simple informations, all they will put in you brain are words that you wrote on it."
        sc "This will help for some trivial tidbits but won't be sufficient for people with severe memory loss, as it requires the brain to intake complex instructions."
    sc "If only there is a way I can recover from this, I would be able to enjoy many other things..."
    sc "And not staying in one place idly everyday"
    $ quest_desc_change("sanco", ": Help Sanco getting rid of her memory loss.")
    $ sanco_about_condition = True
    jump sanco_talk_skip
label sanco_about_remi:
    show sanco what
    sc "Remi?"
    show sanco smile
    sc "He's a good person really."
    sc "Before the incident he moved to the field sometimes for his studies, rated and evaluated the building here, and helped to build a huge network of cabin."
    sc "I did try to help but he told me to stay away as it could be really dangerous"
    sc "He's really serious with that though, he consider safety really highly."
    sc "It's been a while since I heard anything about him, is there anything happening?"
    w "{i}so he did nothing wrong to you then..."
    $ remi_opinion += 1
    $ sanco_about_remi = True
    jump sanco_talk_skip
label sanco_about_owl:
    show sanco what
    sc "You want to meet Owl?"
    sc "But there is no way but..."
    show sanco shock
    sc "You want to get to the lake?"
    show sanco what
    sc "Watta the lake is a restricted area, you are not allowed to get access."
    sc "What? You need Owl's ability..."
    sc "To gather the proofs of.."
    sc "..."
    show sanco sad
    sc "I see, so Remi asked for this"
    sc "As a soulbearer he's allowed to ask for this, but-"
    sc "I hope he's in his right mind right now, because doing this is not quite the right thing..."
    show sanco default
    sc "..."
    sc "So he wanted to get rid of the curse, again"
    sc "Does he still believe in it? The curse? Why does he believe in it so firmly?"
    sc "Does he really believe this would solve everything??"
    show sanco sad
    sc "I'm not really all-knowing as him since I spent most of my older days living here."
    sc "Really I don't want to disregard one of my friends, but, is it really the right thing?"
    sc "{cps=20}I don't know"
    sc "..."
    sc "I see..."
    sc "Well if anything... "
    show sanco sad
    extend "I guess..."
    show sanco close
    sc "{i}sigh"
    sc "It's true, "
    extend "the city has already reached it's lowest, nothing is as happy as they are years ago, I also believe we should not set foot in one place anymore."
    sc "Even if we are committing sins..."
    extend " sins..."
    menu:
        "sins?":
            show sanco mad
            sc "Please..."
    show sanco mad at shake
    sc "Please, no more,"
    show sanco mad at shake
    extend " no more..."
    menu:
        "Sanco?":
            show sanco mad at shake
            sc "Arghhhhh"
        "Sanco?":
            show sanco mad at shake
            sc "Arghhhhh"
    show sanco sigh at bounced
    sc "{i}phew"
    sc "I'm fine now Watta."
    sc "I hope Remi is right, I do feel like there were some kinds of curse upon me"
    sc "I can't enjoy life as much as before, It's tough for things to just going on like this"
    sc "We really...{w=0.5} should do something-"
    show sanco sad2
    sc "Do you have any idea Watta?"
    $ sanco_about_owl = True
    $ option_remove("sanco","Meeting Owl")
    jump sanco_talk_skip
label sanco_about_burning:
    show sanco shock
    sc "Burning the thorns using corruption?"
    sc "You can't be serious!"
    show sanco sad
    sc "But... maybe, it's the right solution,"
    show sanco sad2
    sc "Alright, I will help you with the making of the corrupted charm"
    sc "Only for the sake of the city though,"
    sc "Give me your charm..."
    scene bg black with Fade(0.5,1,0.5)
    scene bg floralia with Fade(0.5,1,0.5)
    show bg floralia at whiten_lesser
    show sanco default at left
    sc "Alright, here you go"
    "Acquired the Soul of the Corruption."
    sc "Before you go, Watta. Remember to chant this line."
    sc "Remembrance is the amber, light is the root, genesis is the blood."
    sc "O Elena, I seek assurance, grand me thine allowing, we shall be liberated."
    $ soul_of_corruption = True
    $ key_item_remove("Bloomfield's Charm")
    $ key_item_add("Corrupted Charm")
    show sanco sad2
    sc "Please, Watta"
    sc "Please take this seriously and save the city,"
    sc "Stay safe out there!"
    $ option_remove("sanco", "Burn the thorns")
    $ option_remove("sanco", "Chii")
    jump sanco_talk_skip


label sanco_quest_acquired:
    if day == 1:
        $ item_add("Glass Daisy")
        $ glass_daisy_timer = 1
        show sanco what
        sc "Oh yeah!"
        show watta deter at right
        w "Huh?"
        show sanco wait at bounce
        show watta default
        sc "One thing I forgot to mention, the flowers are really fragile they would break at the lightest touch so be mindful about it."
        sc "They will also starts to wear down after some time, so the quicker the better"
        show sanco sweat
        sc "I don't think Toko will mind that, but I will appreciate it if you could help us out"
        "Glass Daisy will rot and has quality degraded after night, make sure to deliver it before midnight."
        show watta sweat
        w "I will try to do that"
    else:
        $ item_add("Exquisite Daisy")
        $ glass_daisy_timer = 2
        show sanco what
        sc "Oh no!"
        show watta deter at right
        w "Huh?"
        show sanco wait at bounce
        show watta default
        sc "The flower are not really at its best stage right now, it was at its best yesterday"
        sc "I think because of time that rot it down, you gotta be hurry on this one Watta!"
        show sanco sweat
        sc "If you continue to leave it like this it will not able to retain the quality.."
        sc "I don't think Toko will mind that, but I will appreciate it if you could help us out"
        "Glass Daisy will rot and has quality degraded after night, make sure to deliver it before midnight."
        show watta sweat
        w "I will try to do that"
    show sanco smile2
    sc "I see, thanks for reaching out."
    hide watta
    show screen task_aquired("SANCO'S QUEST ACQUIRED", "DELIVER THE FLOWERS TO TOKO", "images/task/tasksanco.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    $ notebook_unlock("Sanco")
    $ quest_add("sanco")
    $ sanco_spiralia_location_woogie_help_toggle = True
    $ sanco_quest_acquired = True