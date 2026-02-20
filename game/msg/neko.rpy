# File: game/systems/neko.rpy

default neko_first_talk_done_stage = 0
default neko_quest_start = False
default neko_invitation = False
default neko_lied_to = False
default neko_backstage_close_next_phase = False
default neko_second_end = False

label neko_test:
    stop music fadeout 0.5
    play music "bgm_neko.mp3" fadein 1.0 
    if neko_first_talk_done_stage == 0:
        jump neko_first_talk
    elif neko_first_talk_done_stage == 1:
        jump neko_second_talk
    elif neko_first_talk_done_stage == 2:
        $ neko_lend_done = True
        stop music fadeout 0.5
        play music "bgm_bridge.mp3" fadein 1.0
        jump underbridge

label neko_first_talk:
    scene bg makeup at whiten_lesser
    show neko madi at left
    show tsukino black at right
    nk "No I would never do that!"
    "Mane" "But it's your dream, you have to!"
    nk "Then it's not my dream anymore."
    "Mane" "C'mon, it can't be that bad to try."
    nk "I'll do anything but that."
    show neko neutrali
    nk "Now that my part is over, let's just pack things up and leave"
    "Mane" "All I'm saying is..."
    "Mane" "If you try it once you'll see it's not so bad"
    show neko angryi
    nk "We're not mentioning it anymore"
    show neko neutrali
    nk "Where is my bracelet again..."
    nk "I think I dropped it somewhere outside, let me go out and check for a bit"
    "Mane" "*sigh*"
    scene bg big screen with Fade(0.5,0,0.5)
    show watta wtf at center
    show watta wtf at bounce
    w "She's heading out"
    show watta default at slide_to_left
    show neko defaulti at slide_in_right
    nk "Hello-"
    nk "Wait...."
    show watta deter 
    w "???"
    nk "Nevermind"
    show neko neutrali
    nk "Have you seen my bracelet somewhere?"
    "WARNING: IMPORTANT DECISIONS AHEAD!"
    menu:
        "Is this yours?":
            show neko defaulti
            nk "Oh wonderful thank you so much"
            show neko neutrali
            show watta happy 
            nk "Ehh-"
            nk "What's your name?"
            show watta delighted 
            w "Is Watta"
            show neko defaulti
            nk "Thank you Watta,"
            nk "If you don't mind would you come to my next concert tomorrow at the same place at 5pm?"
            show watta smile 
            w "Ehh... Okay I guess?"
            nk "Great, expect to see you there, see you again Watta!"
            hide neko
            w "That was sudden"
            $ neko_invitation = True
            if woogie == True:
                show woogie default at right
                wo "Fascinating..."
                wo "Ya got invited, that's an honor."
                w "Hmm"
                wo "Please don't invest too much time on this though, we don't need a concert we need to investigate..."
                show watta upset 
                w "We'll investigate the concert, okay?"
                hide woogie
            hide watta
        "Never saw one":
            show neko neutrali
            show watta huh 
            nk "Where could it be?"
            nk "Sorry to bother you then"
            nk "{i}sigh"
            show watta sad  
            show neko defaulti at slide_out_right
            if woogie == True:
                pause 1.5
                show woogie default at right
                wo "So ya did it..."
                show woogie hmm
                wo "Ya lied to her. Can't blame ya tho, it's hard to resist the temptation"
                show watta upset 
                w "..."
                show woogie proud
                wo "Well don't invest too much time on this, we don't need the concert we need to investigate..."
                show watta mad 
                w "YOU want to investigate"
                hide woogie
            else:
                show watta sad 
                w "I lied"
                w "..."
                w "Is this really the right thing to do???"
            $ item_add("Neko\'s Bracelet")
            hide watta
            $ neko_lied_to = True
    $ neko_first_talk_done_stage = 1
    if phase != 3:
        scene bg big screen with Fade(0.1, 0, 0.1)
    else:
        scene bg big screenn with Fade(0.1, 0, 0.1)
    $ neko_backstage_close_next_phase = True
    $ notebook_unlock("Neko")
    $ action_done()
    jump big_screenskip

label neko_second_talk:
    if neko_invitation:
        nk "Oh someone found it for me..."
        "Mane" "That's great to hear!"
        "Mane" "I also got everything ready, we can leave now"
        nk "Perfect!"
    else:
        nk "Nah I didn't find it"
        nk "We should hurry and get back to the studio"
        "Mane" "It's fine I can always prepare a new one for you..."
        nk "It's not about that..."
        "Mane" "I also got everything ready we can leave now"
        nk "Alright~"
    $ backstage_open = False
    $ action_done()
    jump big_screenskip

label neko_intro:
    scene bg neko1 with Fade(1,0.5,1)
    pause 1
    w "Huh? Is this the stage where it takes place?..."
    w "Maybe..."
    w "I should go check it out"
    show bg neko2 with dissolve
    pause 1
    w "{i}Omg"
    w "{i}This is so crowded"
    w "{i}Much more than I thought it would be."
    w "{i}I have never seen so many people gathering here before."
    w "{i}Let me see if I can see anything on the stage."
    show bg neko3 with dissolve
    pause 1
    w "{i}So that's the performer"
    w "{i}I can barely see her"
    w "{i}An idol of some kind."
    w "{i}Well guess it's not bad to enjoy this for a little bit"
    $ screen_unlocked = True
    show bg neko4 with dissolve
    $ renpy.pause(3, hard=True)
    $ big_screen_not_happen_again = True
    scene bg big screen with Fade(3, 1, 1)
    if woogie == True:
        show watta default at left
        show woogie default at right
        w "That was good"
        show woogie hmm
        wo "Not excellent."
        wo "I didn't come here to watch this"
        show watta sweat
        w "C'mon it's good to chill out sometimes"
        w "???"
        show watta huh
        w "What is this?"
        show watta shocked
        show woogie huh
        w "Oh it's the girl's bracelet"
        show woogie inspect
        wo "Oh wow!"
        show watta smile
        w "Well I should return it."
        show woogie squint
        wo "Wait wait wait!"
        wo "I think ya should keep it"
        show watta huh
        w "Keep it?"
        show woogie laugh
        wo "Neko is an incredibly famous person."
        wo "Having one of her wearings as a souvenir would give great fortune"
        wo "Ya can then sell it for great price or just hang it in yer house as a lucky charm,"
        show woogie laugh2
        wo "Good either way"
        show watta mad
        w "No way you're serious, we're not stealing here."
        show woogie hmm
        wo "Alright whatever ya do I'm not interested in it either way.."
        w "Tsk, so much for stopping crime."
        show bg big screen at shake
        unknown "{size=+40}NO!!!"
        show woogie wait
        show watta default
        wo "What was that?"
        w "Better go check that out"
        wo "I think it comes from the backstage."
        hide watta
        hide woogie
        $ neko_quest_start = True
        call screen big_screen
    else:
        show watta default
        w "That was good"
        show watta huh
        w "Hmm?"
        w "What is this?"
        show watta shocked
        w "Oh! is her bracelet."
        show watta smile
        w "I should return it to her"
        show bg big screen at shake
        unknown "{size=+40}NO!!!"
        w "What was that?"
        w "Lemme check the source of that sound"
        hide watta
        $ neko_quest_start = True
        call screen big_screen

label neko_invited_intro:
    scene bg neko1 with Fade(1,0.5,1)
    pause 1
    w "Let's see, same time, same place.."
    w "Looks like her concert is already ongoing."
    w "I should go check it out"
    show bg neko2 with dissolve
    pause 1
    w "{i}I wonder what will happen this time."
    show bg neko5 with dissolve
    pause 1
    nk "And now as usual, for the interlude, I'll be inviting a special guest."
    nk "Known for helping me with a certain task."
    show bg neko6 with dissolve
    pause 1
    w "huh?"
    nk "Whoever looks like the one on the screen please come on the stage!"
    show bg neko61 with dissolve
    pause 1
    w "WHAT?"
    show bg neko2 with fade
    pause 1
    show bg neko7
    pause 1
    w "Oh?"
    w "I didn't mean to..."
    show bg neko71 at shake
    pause 2
    w "..."
    w "Oh thanks."
    show bg black with fade
    nk "Please come on the stage."
    show bg neko8 with fade
    nk "Hello there! Can you tell us a bit about yourself?"
    show bg neko82 with dissolve
    w "Hah uh..."
    menu:
        "Fish!":
            show bg neko83 with dissolve
            nk "{size=+10}!"
            show bg neko84 with dissolve
            nk "I like fish too!"
            show bg neko81 with dissolve
            nk "Okay so, you are Watta right?"
            nk "What do you want to talk about today?"
        "I am Watta.":
            show bg neko84 with dissolve
            nk "Nice having you Watta!"
            show bg neko81 with dissolve
            nk "Okay so Watta, what do you wanna talk about today?"
        "My name is Walter Sheperd Watta, I live at 112 Otashima Lane, Alene, Sidurina, 423235. I have something to talk about...":
            show bg neko83 with dissolve
            nk "Wow! That was specific!"
            show bg neko81 with dissolve
            nk "What do you want to talk about?"
        "My name s Watashima Watta, I'm 22 years old. My house is in the south-eastern section of Sidurina, where all the foodstalls are, and I am single,...":
            show bg neko84 with dissolve
            nk "Calm down calm down! Think of this as a funshow,"
            nk "No need to be so formal"
            show bg neko81 with dissolve
            nk "Moving on"
            extend "... so Watta, what do you wanna talk about today?"
    menu:
        "Do you see the endless road?":
            w "You see the endless road? There is something of mine that is longer than that, and you have to go through the road to find out what it is."
            nk "Oh? What could it be?"
            w "It's friendship."
        "What weird water wheel":
            w "What weird water wheel would watta weave whether watta would weave water wheel weirdly"
        "Im Watta atta":
            w "Im Watta atta batta chatter splatter, data latta rattle that’ll shatter."
        "option 1":
            "a"
        "option 1":
            "a"
        "option 1":
            "a"
        "option 1":
            "a"
        "option 1":
            "a"
        "option 1":
            "a"
    show bg neko62 with dissolve
    pause 0.5
    show bg neko63 at shake
    pause 0.5
    show bg black with Fade(2,0,0)
    "The concert concluded in euphoria."
    if not phase == 3:
        $ phase =3
        $ actions_left = max_actions
        show bg big screenn with Fade(0,0,2)
    else:
        show bg big screenn with Fade(0,0,2)
    show watta default at left
    show neko defaulti at right
    nk "You really fired up the audience Watta"
    nk "Thank you"
    w "Is nothing, it was fun there"
    w "But I think I did badly"
    nk "Oh not really."
    "Voice1" "That sheep one was cool"
    nk "See, people loved you Watta, you can be a cool perfomer if you have the confidence."
    w "Thank you"
    nk "{size=-10}you can replace me one day."
    w "What?"
    nk "Nothing"
    pause 0.5
    show watta default at slide_to_left_edge
    show neko default at slide_to_mid_left
    show tsukino black at slide_in_right_edge
    "Mane" "What are you doing out here at this time again?"
    "Mane" "Oh it's y..."
    nk "Introduce to you, this is my mane-chan."
    "Mane" "..."
    nk "Tsukino this is Watta who helped me with the bracelet"
    show tsukino angry at right
    tkn "You"
    w "Huh? me?"
    nk "You two know each other?"
    w "No i don'{w=0.5}{nw}"
    tkn "We have to go now Neko,"
    nk "Wait why so sudden?"
    show tsukino angry at slide_to_mid_left
    pause 0.3
    show neko default at slide_out_right
    show tsukino angry at slide_out_right
    nk "At least get me say goodbye to my fr-- Ahh!"
    show watta default at slide_to_left
    w "WHAT IS GOING ON?"
    pause 0.5
    w "What?"
    hide watta
    $ neko_second_end = True
    jump big_screen


default neko_tsukino_intro_talk_again = False
default neko_tsukino_intro_no_more = False
label neko_tsukino_intro:
    scene bg neko1 with Fade(1,0.5,1)
    pause 1
    w "Oh there is also a concert happening today"
    w "Gonna find a good spot this time."
    if phase != 3:
        scene bg big screen with Fade(1, 0, 1)
    else:
        scene bg big screenn with Fade(1, 0, 1)
    play music "bgm_bigscreen.mp3" fadein 1.0 if_changed
    show watta default
    w "Hmm"
    show watta default at slide_to_left
    show tsukino default at slide_in_right
    tkn "Hey you."
    w "Huh?"
    tkn "This is restricted area, not for audience, please leave."
    w "Oh sorry I didnt mean to..."
    tkn "Leave."
    menu:
        "Show Nekomin Badge":
            show tsukino surprised
            tkn "What?"
            tkn "How did you get that?"
            show tsukino angry
            tkn "Nvm it's starting soon c'mon."
            w "Huh?"
            tkn "Follow me."
            show tsukino angry at slide_out_right
            $ bailey_hall_presence = True
            $ snowie_hall_presence = True   
            jump tsukino_hall_intro
        "Leave":
            $ neko_tsukino_intro_talk_again = True
            jump centre

label neko_tsukino_intro_again:
    if phase != 3:
        scene bg big screen with Fade(0.2, 0, 0.2)
    else:
        scene bg big screenn with Fade(0.2, 0, 0.2)
    show tsukino angry
    tkn "I already told you to scram."
    tkn "Don't anger me."
    menu:
        "Show Nekomin Badge":
            show tsukino surprised
            tkn "What?"
            tkn "How did you get that?"
            show tsukino angry
            tkn "Nvm it's starting soon c'mon."
            w "Huh?"
            tkn "Follow me."
            show tsukino angry at slide_out_right
            if woogie:
                tkn "Ye you the blonde one, not the blue-haired one"
                show woogie cry at left
                wo "What?"
                show woogie bleh at bounced
                wo "As if I would join, BLEHH"
            $ bailey_hall_presence = True
            $ snowie_hall_presence = True   
            jump tsukino_hall_intro
        "Leave":
            jump centre


