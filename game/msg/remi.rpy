# File: game/systems/remi.rpy
default remi_first_talk_done_stage = 0
default bottle_for_remi = False
default remi_opinion = 0

default the_knower = 0
default the_alley_knower = False

label msg_remi_0:
    "No new messages from Remi."
    call screen message_screen
    return

label msg_remi_early:
    r "Oh Watta, I forgot to bring a bottle before moving, I'm dehydrated, can I borrow a bottle?"
    w "Aight..."
    "You grabbed yourself a bottle of fresh water."
    $ bottle_for_remi = True
    $ update_msg_phase("Remi", "0")
    call screen message_screen
    return


label remi_test:
    #$ renpy.notify(f"{remi_first_talk_done_stage}")
    stop music fadeout 0.5
    play music "bgm_remi.mp3" fadein 1.0 
    if remi_first_talk_done_stage == 0:
        jump remi_first_talk
    elif remi_first_talk_done_stage == 1:
        jump remi_first_talk_2
    elif remi_first_talk_done_stage == 2:
        jump remi_second_talk
    elif remi_first_talk_done_stage == 3:
        jump remi_second_talk_2
    elif remi_first_talk_done_stage == 4 and remi_opinion >= 3:
        jump remi_third_talk
    elif remi_first_talk_done_stage == 5:
        jump remi_fourth_talk
    elif remi_first_talk_done_stage == 6:
        jump remi_fifth_talk
    elif remi_first_talk_done_stage == 7:
        jump remi_talk

label remi_first_talk:
    $ cutscene_on = True
    stop music fadeout 0.5
    show bg remi beach22 with Fade(1,1,1)
    pause 0.5
    show bg remi beach221 with dissolve
    pause 0.5
    show bg remi beach222 with dissolve
    pause 0.5
    r "Huh... you..."
    w "Ye..."
    r "..."
    r "Didn't expect that..."
    show bg remi beach2 with dissolve
    w "What did you expect then..."
    if bottle_for_remi == True:    
        r "Well when I said I would meet you at the beach, you know I never really expected you to come."
        w "So what now?"
    else:
        show bg remi beach21 with dissolve
        r "How'd you find me here?"
        w "I don't know, maybe a coincidence?"
        show bg remi beach2 with dissolve
    r "..."
    w "..."
    show bg remi beach23 with dissolve
    r "...Can you hear it?"
    w "Hear what?"
    show bg remi beach1 with dissolve
    play music "bgm_wave.mp3" fadein 1.0 
    r "The sound of people arguing, the business of the centre, the chattering that should be everywhere..."
    r "They are not here"
    r "Instead what we get are just waves crashing, and maybe the wind noises"
    r "... there is nothing else."
    pause 1.5
    r "And that's good."
    r "...For me personally, this is something that brings sanity."
    r "One of the reasons I chose to move into the lighthouse..."
    r "..."
    r "...I want to be like that, Watta."
    menu:
        "Wanna relax?":
            pass
        "...":
            r "Ye... like that."
            r "I can keep enjoying it like this, but..."
            r "I feel much better being like this... alone"
            r "...So if you don't mind... I'd like to enjoy the beach by my lonesome"
            w "...okay sure then"
            $ quest_desc_change("remi", ": Find and talk to Remi again next time.")
            $ remi_first_talk_done_stage = 1
            $ cutscene_on = False
            $ action_done()
            jump beach
    show bg remi beach2 with dissolve
    w "Huh? You want to relax?"
    r "No, I want to be someone that people can feel relaxed with, that they can seek to ease their troubles."
    r "I want to be helpful."
    show bg remi beach26 with dissolve
    r "And not the... urgh.. the opposite"
    r "A dude that deters people."
    r "Not my taste really."
    menu:
        "You fumbled":
            pass 
        "You need to learn to keep your emotions in check, Remi.":
            r "You think I don't know that? Do you know how hard it is to bottle up my emotions?"
            w "I don't mean you should-{nw}"
            show bg remi beach24 with dissolve
            r "EVERYTIME WATTA, I BOTTLE IT UP AND IT'S NEVER ENOUGH."
            r "AND WORST OF ALL? IT ALWAYS AFFECTS THEM"
            w "...Sorry"
            show bg remi beach261 with dissolve
            r "..."
            w "{i}...he seems pretty mad, I should leave him be"
            $ quest_desc_change("remi", ": Find and talk to Remi again next time.")
            $ remi_first_talk_done_stage = 1
            $ cutscene_on = False
            $ action_done()
            jump beach
    w "Well you don't always... make the best choices, Remi."
    show bg remi beach261 with dissolve
    r "You don't have to bring that up..."
    w "What?"
    r "grrrr"
    show bg remi beach24 with dissolve
    r "I KNOW THAT WATTA."
    r "I know that. It's all my fault, I messed things up."
    show bg remi beach241 with dissolve
    w "Sorry."
    show bg remi beach262 with dissolve
    r "It's hard not to feel this bitter everyday man."
    r "Feels like anything I try ends up negatively affecting others... especially them."
    show bg remi beach24 with dissolve
    r "What's the point of existing if everything you do is...{w=0.5} well, harmful..."
    w "..."
    show bg remi beach262 with dissolve
    r "I've resigned myself at this point, they're better off with me gone."
    r "Everything will be better honestly, nothing to halt their steps anymore."
    r "With a new identity they will no longer need to worry about a 'Remise' in their life anymore, as said person will no longer exist."
    w "..."
    show bg remi beach251 with dissolve
    w "...You're approaching this the wrong way."
    pause 0.5
    show bg remi beach25 with dissolve
    r "What else do I do Watta? I tried everything and from every angle someone gets hurt and I end up depressed. What else could I possibly do?"
    menu:
        "Just stop caring":
            r "What, stop caring about what they think or say?"
            show bg remi beach251 with dissolve
            w "...something like that yeah."
            show bg remi beach21 with dissolve
            r "I already tried and did that Watta, it's not possible"
            extend ", plus that doesn't solve the issue now does it?"
            w "Maybe?"
            show bg remi beach291 with dissolve
            r "I just can't stop caring, it's my nature, hard to change"
            r "..."
            show bg remi beach2 with dissolve
            r "I appreciate you listening to me, but I think I just need to think about this more on my own."
            w "Do you think...{nw}"
            show bg remi beach201
            r "No more just..{w=0.5} give me time man."
            w "...sorry"
            $ quest_desc_change("remi", ": Find and talk to Remi again next time.")
            $ remi_first_talk_done_stage = 1
            $ cutscene_on = False
            $ action_done()
            jump beach
        "Nothing...":
            pass
    show bg remi beach251 with dissolve
    w "...nothing?"
    show bg remi beach25 with dissolve
    r "What"
    r "Are you messing with me??"
    show bg remi beach24 at shake
    r "HOW IS THAT SOLVING THE PROBLEM???"
    show bg remi beach251 with dissolve
    w "...Remi"
    w "Look around again, did you forget why you are here?."
    show bg remi beach21 with dissolve
    r "..."
    show bg remi beach211 with dissolve
    pause 0.5
    show bg remi beach1 with dissolve
    w "The beach"
    w "Is very nice and relaxing, yes... And no matter what I do, It'll never get provoked..."
    w "You see what I mean?"
    r "..."
    w "The beach goes with the flow, its waves come in and go without any sort of force. That's enough to make a relaxing atmosphere."
    w "Could you imagine if it forcefully tried to get closer anytime someone came to relax with it? You'd get wet and have to move each time."
    w "But letting the waves do their thing and flow as they please?"
    w "Yes, it brings you sanity..."
    w "Maybe, much like the beach, you just need to go with the flow and not fight against it, Remi."
    show bg remi beach291 with dissolve
    r "But it's not use anymore Watta, things are bad and bridges were burnt. There is nothing left for me anymore."
    show bg remi beach28 with dissolve
    w "If people stopped showing up, would the beach cease?"
    w "Of course not, the beach would continue like normal, unbothered. With time, people will eventually come back."
    w "Is all you need to do, give it time and don't force anything."
    show bg remi beach2 with dissolve
    r "..."
    show bg remi beach202 with dissolve
    w "Look man..."
    w "Don't force anything with them right now, you made them pretty mad and forcing them into a conversation to apologize will only cause issues."
    w "Be the waves that come and go, don't be the earthquake that causes a disaster."
    show bg remi beach212 with dissolve
    w "And maybe with some time... people will be comfortable and relax around you again."
    show bg remi beach26 with dissolve #Placeholder. Remi looking down, pondering. Watta just looks at him
    r "..."
    r "...I see..."
    r "I've been a fool..."
    show bg remi beach27 with dissolve #Placeholder. Watta looks back at him, smiling. Remi is giving his own weak, tired smile.
    r "Thank you Watta...{w=0.5} I think... {w=0.5} I think I'll give this some thought..."
    r "Please let me sit alone for a while, I'll go back to the lighthouse after I'm done pondering."
    show bg remi beach28 with dissolve #Placeholder. Watta happily responds, Remi looks down again a little sad, but happy. Bittersweet?
    w "Of course! Just don't do anything stupid, OK?"
    r "...I'll try."
    show bg remi beach29 with dissolve #Placeholder. Remi looking down bittersweet. Watta gone/standing up and about to leave
    r "..."
    show bg remi beach30 with dissolve #Placeholder, Remi yelling out to a watta that has gone offscreen
    r "Wait!"
    w "???"
    scene bg beach with Fade(1,1,1)
    stop music fadeout 0.5
    play music "bgm_remi.mp3" fadein 1.0 
    show bg beach at whiten_lesser
    show watta default at left
    show remi default at right
    r "Before you go... I want to be helpful again so..."
    r "Please remember this..."  
    r "Hindrance is the amber, dark is the root, fire is the blood"
    w "????"
    show watta frown at bounced
    w "What does that mean?"
    show remi erm
    r "Seek the one who's in charge of the railways."
    r "It will come in handy later..."
    r "I will do a walk around the centre next time, around the late time, hope to see you there."
    show remi close
    r "For now..."
    $ the_alley_knower = True
    $ quest_desc_change("remi", ": Find and talk to Remi again next time.")
    $ remi_first_talk_done_stage = 1
    $ cutscene_on = False
    $ action_done()
    jump beach

default remi_neko_bracelet_talk = False
label remi_first_talk_2:
    show remi default at right
    show watta default at left
    if is_item_get("Neko's Bracelet") and not remi_neko_bracelet_talk:
        call remi_neko_bracelet_talk from _call_remi_neko_bracelet_talk
    elif is_item_get("Neko's Bracelet") and remi_neko_bracelet_talk:
        r "Did you return it to her?"
        menu:
            "Actually I'll give you this":
                r "Huh? changed your mind so quickly."
                w "Well if you need it for living..."
                show remi surprised
                r "I appreciate it Watta, thank you for caring about my well being..."
                show remi smile
                r "I might be able to afford better medication from now on..."
                r "Here, a cool item, take it and don't question anything."
                $ item_remove("Neko's Bracelet")
                $ sol_add(200)
                $ item_add("Nekomin Badge")
            "Not yet":
                r "Then do it right away"
                $ remi_neko_bracelet_talk = True
    else:
        r "Just let me cool down for a bit..."
        w "Alright"
    hide watta
    hide remi
    jump beach

label opening1:
    $ cutscene_on = True
    show screen remi_1_skipper  
    show watta sleepy
    w "Ugh.."
    w "Is pretty hot outside-"
    w "I'm still not used to this place even after a week."
    w "Really should be moving today"
    window hide
    with None 
    show watta deter at shaker
    show bg outhome at shake
    $ renpy.pause(2.3, hard=True)
    show watta deter at bounced
    w "HUH???"
    show screen day_trans("Day 1")
    $ renpy.pause(9.0, hard=True)
    hide screen day_trans
    unknown "{size=80}This is unreal!{/size}"
    show watta frown
    w "Ohh! Is that..."
    show watta frown at slide_to_right
    show remi menace at slide_in_left
    stop music fadeout 0.5
    play music "bgm_remi.mp3" fadein 1.0
    $ renpy.pause(1.3, hard=True)
    r "Can't believe this has happened to me twice in a row..."
    r "I'm no longer trusting a SINGLE vending machine."
    show watta delighted
    w "Oh, hi Remi."
    show remi look
    r "Oh...?"
    r "You startled me..."
    show remi close
    r "As I said before, don't call me by that name in public."
    show remi hah 
    r "..."
    r "I'm just walking out like usual, getting used to the festival, also need some exercise they said."
    show remi look
    r "About the festival..."
    r "I'm not really all-knowing about it, all I know is that it's just the anniversary of this land's creation."
    r "With some funny things going on at the time it takes place."
    w "..."
    show remi erm
    show watta huh
    r "..."
    show remi look
    r "Can you lend me a quarter? I don't wanna get robbed by this vendy as well."
    show watta happy
    w "Oh... right here.."
    r "Thanks."
    show remi default at shake
    $ renpy.pause(1.0, hard=True)
    r "Oh nice."
    $ renpy.pause(1.0, hard=True)
    show remi drink at bounced
    $ renpy.pause(1.0, hard=True)
    show watta huh
    w "How's it going over there anyways?"
    $ renpy.pause(0.5, hard=True)
    show remi drink2
    show watta huh
    w "..."
    show remi close at bounced
    $ renpy.pause(1.0, hard=True)
    show remi erm
    r "I'm not going back."
    r "Too much of a toll on my mental health."
    show watta sweat
    w "Is not that bad.."
    show remi close
    r "It's that bad Watta"
    show remi default
    r "Even if I come back, I'll eventually leave again."
    r "I can't keep myself sane in there."
    show remi erm
    show watta upset
    r "Also..."
    show remi drink at bounced
    pause 1
    show remi look
    r "Don't you have to work, Watta?"
    r "Don't mind me but, I'm just not feeling good today... so you should not be wasting time with me..."
    r "Don't be late."
    if bottle_for_remi == True:
        show watta deter at bounced
        w "Oh wait!"
        r "???"
        w "Did you ask me about bringing a water bottle?"
        show remi hah
        r "Oh ye..."
        r "I did but..."
        extend " I just realized you have this working vendy here near your place."
        show remi look
        r "So I got my drinks..."
        r "Thanks anyways."
        r "..."
        show remi smile
        r "I'll be at the beach this afternoon, if you want to you can meet me there and we can talk more."
        r "For now..."
    show remi close
    r "Here's your quarter back, Imma continue walking, later"
    show watta upset at slide_back
    show remi close at slide_out_left
    $ renpy.pause(1.3, hard=True)
    w "This man..."
    w "I have to get him back into group somehow.."
    stop music fadeout 0.5
    hide watta with dissolve
    show screen task_aquired("REMI'S QUEST ACQUIRED", "GET REMI BACK TO \"THE GROUP\"", "images/task/taskremi.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    hide screen blackout
    play music "bgm_outhome.mp3" fadein 1.0
    label remi_1_end:
    hide screen remi_1_skipper  
    hide watta
    hide remi
    "You have unlocked tasks"
    "Check the tasks available by pressing Q"
    "Beware of bike jumpscare"
    $ quest_add("remi")
    $ update_msg_phase("Remi", "0")
    if is_item_get("Sari's Sauce"):
        $ quest_add("sari")
    $ prologue_done = True
    $ cutscene_on = False
    jump opening2

default remi_second_talk_bad = False
label remi_second_talk:
    $ cutscene_on = True
    show remi default at right
    show watta default at left
    r "Hello"
    call remi_talk_before_second_talk from _call_remi_talk_before_second_talk
    r "Night outside of the centre is pretty scary, although it's not the darkness that is scary..."
    show remi close
    show watta sweat
    r "...Okay may be darkness is a part of it but there is something much worse."
    show remi erm
    r "The lack of people Watta."
    show remi hmm
    show watta huh
    r "Living in a pretty deserted area feels lonely."
    r "And while I did this to myself I also never get to... really break out of myself."
    show remi hah
    r "My life back in the centre was also really lonely, with me barely setting foot out of the house."
    r "Communicating online feels so much less as stressful"
    show remi smile
    show watta frown
    r "Now that I got to touch grass more often, I do feel more at peace."
    w "You are trying your best to not interact with them aren't you?"
    show remi ill
    r "Maybe, I'm avoiding them like a coward"
    menu:
        "Like a cockroach":
            show remi menace
            show watta shocked
            r "No no no no no no, that's so over the line"
            show watta upset
            r "I don't wanna be compared with"
            extend " f-ing roaches!"
            w "Wait no I didn't-"
            r "Do I deserve to die that bad Watta? How about I die here and now?"
            show remi distraught
            show watta sad
            r "Stupid."
            $ quest_desc_change("remi", ": Find and ask 3 people about Remi")
            $ remi_first_talk_done_stage = 3
            $ cutscene_on = False
            $ remi_second_talk_bad = True
            $ action_done()
            jump big_screen
        "Like a rat":
            pass
    show remi hah
    show watta sweat
    r "Yo- ... you could say it like that, I don't mind it anymore"
    w "I already said, if you don't put an effort to change, things will stay the same."
    show remi hmm
    r "And I like it like this Watta, it feels much more peaceful and comfy, at least I don't have to..."
    extend "suffer depression when I do something wrong to them again.."
    r "I'm always prone to repeating mistakes, I don't want them to experience that again."
    show watta frown
    w "Remi they would literally prefer to talk about it instead of-"
    show remi close
    r "Shh, don't call me that,"
    menu:
        "Erasing yourself solves nothing you know.":
            pass
        "If you won't talk to them I can just ask them to come here":
            show watta huh
            show remi angry2
            r "Do {w=1}not"
            r "Weren't you the one who told me NOT to force it?"
            show watta sad
            w "Well I did... but..."
            show remi mad
            r "There is no good to face them now, Watta"
            r "It's not cooled down yet."
            r "I believe it will just be a loop of agony as I continued being a jerk."
            r "I can be one right now to you, so just..."
            show remi close
            r "Please leave me be for now"
            w "Okay..."
            $ quest_desc_change("remi", ": Find and ask 3 people about Remi")
            $ remi_first_talk_done_stage = 3
            $ cutscene_on = False
            $ remi_second_talk_bad = True
            $ action_done()
            jump big_screen
    show remi look
    r "You don't get it..."
    show watta huh
    w "People are wanting you to come back, they miss you..."
    show watta frown
    w "Even when you did fumble, what happened? You learned from your mistake, people have also come to understand you a bit more and..."
    show remi ill
    show watta mad
    w "No friendship is ever smooth sailing!"
    r "Thing... {w=0.5}"
    extend "thing is... I'm scared."
    show remi default
    r "What you said is true, I might want to reconcile with them, but I'm scared."
    r "Scared of losing again, scared of going back to my uncontrollable self, leading to a bigger mistake. I'm scared of {w=1}even facing them at this point."
    menu:
        "The waves are never afraid to be near people":
            pass
        "They're more afraid of you never approaching them":
            show remi close
            r "Ah... so I have been a burden."
            show watta huh
            r "I see... {w=1}I suppose I'll... think about it for a bit."
            show remi hmm
            r "Please let me be for now"
            show watta sad
            w "Okay..."
            $ quest_desc_change("remi", ": Find and ask 3 people about Remi")
            $ remi_first_talk_done_stage = 3
            $ cutscene_on = False
            $ remi_second_talk_bad = True
            $ action_done()
            jump big_screen
    show remi look
    show watta smile
    r "What do you-"
    menu:
        "Stop being so afraid to approach them":
            show remi ill
            r "But the waves don't approach people, people approach them."
            r "and I know they'd NEVER go out of their way for me."
            show remi up
            r "Ugh, I really am just a burden aren't i?"
            show watta sad
            w "You're not, Remi"
            r "It's okay Watta, I know i've been burdening you"
            show remi look
            r "Leave me be for now, I've wasted enough of your time"
            show watta upset
            w "You haven't but okay..."
            $ quest_desc_change("remi", ": Find and talk to Remi again next time.")
            $ remi_first_talk_done_stage = 3
            $ cutscene_on = False
            $ remi_second_talk_bad = True
            $ action_done()
            jump big_screen
        "Because they know that friends are always willing through work through problems together":
            pass
    show remi hmm
    r "But won't I be a burden?"
    show watta smile
    w "Is okay. You wouldn't be."
    show remi ill
    r "I just don't want to make people feel bad you know, but you're right, I'm too scared of taking risks"
    r "Maybe that's what I need to do now"
    show watta delighted
    w "If you really can't make a move I can go gather people's thoughts for you"
    w "I know i told you before to do nothing"
    show watta hype
    w "But enough time had passed, now is the time for action."
    show remi look
    r "You don't need to really, I don't want them to be bothered"
    show watta deter
    r "We all have the curse after all"
    show watta huh
    w "Curse? What are you talking about"
    show remi erm
    r "The Great Depression, it doesn't just affect the queen, it's on her descendants as well-"
    show watta shocked
    r "So not just me having issues but every single one of the Soulbearers got affected as well. It'd be the best if we could..."
    show remi close
    show watta deter
    r "...Speaking of Soulbearers. Reni, Toko, myself, Ow-{w=1}, you should seek Owl, Watta."
    show watta ahh
    w "Owl? Wait wait wait you're switching topics way too quickly. Isn't he in a heavily restricted area now?"
    show remi look
    r "He's in the abandoned lake yes, but he possesses an insane ability"
    r "Time capturing."
    show watta deter
    w "??? What?"
    show remi default
    r "It's complicated just go seek him."
    show watta ahh
    w "Yeah but howww???"
    show remi smile
    r "Find your way to the lake, how I don't really know. I haven't been to Bloomfield for quite long, Sanco might be able to help."
    r "For now go find Sanco and talk about it, from there meet Owl and you won't need to seek me again."
    show watta huh
    w "But hey what would I talk to Owl about?"
    show remi default
    r "Tell him the same thing I told you last time"
    show remi surprised
    show watta mad
    w "Hinder is the- what? I forgot"
    show remi distraught
    r "Hindrance is the amber, dark is the root, fire is the blood"
    show watta upset
    r "Don't forget it again"
    show remi default
    show watta smile
    w "Hmmm, alright I will try to remember then."
    r "Thank you, this is for the better of all."
    r "Go seek Owl and tell him that, then it better be resolved."
    r "Oh and one thing"
    w "Huh?"
    r "Avoid going to the lake at night, Owl told me that"
    w "I see"
    $ quest_desc_change("remi", ": Find and ask people about Remi, including Owl.")
    $ the_knower = 2
    $ remi_first_talk_done_stage = 3
    $ cutscene_on = False
    if is_item_get("Neko's Bracelet"):
        show remi hah
        r "By the way uhh..."
        r "Neko's bracelet."
        show remi default
        r "You should... {w=0.5}really just return it back to her."
        r "But if you are not going to..."
        show remi hmm
        r "I have this deal Watta,..."
        r "I'll trade it for this mostly cool item and some money."
        show watta huh
        w "What are you going to do with it?"
        show remi look
        r "Huh? It's not really important Watta, I need to..."
        r "Imma put this on an auction and get some money Watta, I need money to live after all."
        show watta frown
        w "...kay? Then why pay me for it?"
        show remi smile
        r "Gotta make the deal fair, so how's that sound?"
        menu:
            "Deal":
                r "I appreciate it Watta, thank you for caring about my well being..."
                show remi smile
                r "I might be able to afford better medication from now on..."
                r "Here, a cool item, take it and don't question anything."
                $ item_remove("Neko's Bracelet")
                $ sol_add(200)
                $ item_add("Nekomin Badge")
            "No deal":
                r "It's okay... I'm not interested all that much"
                show remi default
                r "Just, there are a ton of bad people out there who could get their hands on it."
                r "You can assume me being one so, just try to return it to her"
                r "That's for the best, don't let it get in anyone else's hands..."
                r "For the best."
                $ remi_neko_bracelet_talk = True
    $ action_done()
    jump big_screen

label remi_neko_bracelet_talk:
    r "Huh, this is..."
    r "Her bracelet?"
    show remi hah
    r "To be honest the method of how you got that is almost intriguing..."
    r "But I'm not one to question as I am not really interested in it."
    show remi default
    r "You should... {w=0.5}really just return it back to her."
    r "But if you are not going to..."
    show remi hmm
    r "I have this deal Watta,..."
    r "I'll trade it for this mostly cool item and some money."
    show watta huh
    w "What are you going to do with it?"
    show remi look
    r "Huh? It's not really important Watta, I need to..."
    r "Imma put this on an auction and get some money Watta, I need money to live after all."
    show watta frown
    w "...kay? Then why pay me for it?"
    show remi smile
    r "Gotta make the deal fair, so how's that sound?"
    menu:
        "Deal":
            r "I appreciate it Watta, thank you for caring about my well being..."
            show remi smile
            r "I might be able to afford better medication from now on..."
            r "Here, a cool item, take it and don't question anything."
            $ item_remove("Neko's Bracelet")
            $ sol_add(200)
            $ item_add("Nekomin Badge")
        "No deal":
            r "It's okay... I'm not interested all that much"
            show remi default
            r "Just, there are a ton of bad people out there who could get their hands on it."
            r "You can assume me being one so, just try to return it to her"
            r "That's for the best, don't let it get in anyone else's hands..."
            r "For the best."
            $ remi_neko_bracelet_talk = True
    return

label remi_second_talk_2:
    show remi default at right
    show watta default at left
    if is_item_get("Neko's Bracelet") and not remi_neko_bracelet_talk:
        call remi_neko_bracelet_talk from _call_remi_neko_bracelet_talk_1
    elif is_item_get("Neko's Bracelet") and remi_neko_bracelet_talk:
        r "Did you return it to her?"
        menu:
            "Actually I'll give you this":
                r "Huh? changed your mind so quickly."
                w "Well if you need it for living..."
                show remi surprised
                r "I appreciate it Watta, thank you for caring about my well being..."
                show remi smile
                r "I might be able to afford better medication from now on..."
                r "Here, a cool item, take it and don't question anything."
                $ item_remove("Neko's Bracelet")
                $ sol_add(200)
                $ item_add("Nekomin Badge")
            "Not yet":
                r "Then do it right away"
                $ remi_neko_bracelet_talk = True
    elif not remi_second_talk_bad:
        r "Hope you can get this done, sorry for asking too much..."
        w "Is fine"
    else: 
        show remi surprised
        r "Leave me alone"
        w "Kay"
    hide watta
    hide remi
    play music "bgm_bigscreen.mp3" fadein 1.0 if_changed
    jump big_screenskip


label remi_talk_before_second_talk:
    show remi smile
    r "I saw what you did up there Watta, it was cool."
    r "You got the chance with... Neko herself."
    show remi erm
    r "I would also have had one if I didn't reject it."
    r "It's just {w=0.5}too stressful for me."
    show remi default
    r "The crowd can be, it's obvious, but there is also something that is quite terrifying here."
    r "To put it,"
    return

default crime_note_readable = False
label remi_third_talk:
    $ cutscene_on = True
    show remi default at right
    show watta default at left
    play music "bgm_remi.mp3" fadein 1.0 
    r "Do you ever see a car running and wonder how it feels like to have your fingers crushed over by the wheels?"
    show watta deter
    w "What?"
    show remi close
    r "Nevermind."
    show remi look
    r "I have this note... It has all of my past crimes written down."
    show watta wtf
    w "Wait what?"
    r "Yes I was kind of..." 
    show remi hah
    show watta sweat
    extend "well, very... immature back then."
    show remi erm
    r "Do you think that for horrible crimes, ones not started by poverty."
    show watta upset
    r "Aside from greed being a factor, do you think it's also because of jealousy?"
    w "Huh?"
    show remi ill
    show watta huh
    r "I stopped doing them not because I stopped having jealousy, but because it became pretty boring."
    r "I worked my status up because once you're at the top of the world... nothing will mess with your feelings anymore."
    show watta frown
    r "By being at the top I can believe that nothing is above me. Thus none of the four modern sins, including jealousy, can affect me."
    show remi mad
    r "Every time I watch someone doing something skillful, I reassure myself \"At least im better than them\" and that helps me defeat the negative feelings."
    show watta mad
    w "Don't you think that's a little arrogant?" 
    show watta huh
    extend "Like looking down on everything?"
    show remi hah
    r "Maybe, but funny enough it is a good self-care technique for me."
    show watta mad
    w "What's wrong with being humble?"
    show remi distraught
    r "It can work, but i'm not lowering my self worth. Plus being humble doesn't exactly help my jealousy."
    r "Especially when jealousy is simply caused because I think i'm missing out on something that someone else is experiencing."
    show remi default
    show watta sleepy
    r "and the funny thing is that sometimes you CAN achieve the same thing, but more likely than not you won't and you'll just stay jealous."
    show watta frown
    w "What's the point you're trying to make man?"
    show remi close
    r "This is what caused me to fear trying to come back."
    r "My jealousy won't let me enjoy peace as my inner self keeps trying to fuel up my rage bar."
    show watta sad
    r "I'll continue to crash out again and again. It's an endless cycle."
    w "It's okay Remi, we all do feel that as well, it's just...    "
    show remi hmm
    show watta mad
    w "You need to share your feeling man. And then we will start working with it over time."
    show watta sad
    w "Don't expect changes to be sudden."
    show remi ill
    r "You say that calmly but would you still be when i ramble about the same problem for the hundredth time?"
    show watta huh
    w "People know you well Remi. They can tolerate you way better when you talk as opposed to when you hide."
    w "You are smart Remi, you can learn. You can totally adapt after a while."
    show remi look
    r "..."
    show remi hmm
    r "..."
    show remi up
    r "I don't wanna live like this"
    show watta smile
    r "But fine, I'll try, just, give me some time."
    show remi smile
    r "Thank you for gathering people's info on me by the way, even though i didn't ask for it."
    r "Here, take this, a piece of my past."
    $ item_add("Crime Note")
    show remi erm
    show watta deter
    r "I want to dispose of my past, and also I think you should be aware of it, I don't wanna be so insecure about myself anymore."
    r "Just don't... share it with anyone."
    show watta default
    w "Alright"
    show remi smile
    r "Meet me at the beach tomorrow. I will let you into the lighthouse."
    r "I'm going home now. Also dont let Sari know I was here."
    show remi default
    r "Bye"
    show watta smile
    w "Cya"
    $ crime_note_readable = True
    $ quest_desc_change("remi", ": Meet Remi at the beach tomorrow.")
    $ remi_first_talk_done_stage = 5
    $ cutscene_on = False
    $ action_done()
    jump parkskip


label remi_fourth_talk:
    "This talk should not exist"

default remi_crime_note_read = False
label remi_fifth_talk:
    $ cutscene_on = True
    show remi default at right
    show watta default at left
    r "Let's go, shall we?"
    $ lighthouse_unlock = True
    scene bg lighthouse with Fade(1,1,1)
    show bg lighthouse at whiten
    show remi default at right
    r "Sorry if it's a little bit messy"
    r "Not like I ever expected to get a guest"
    show watta smile at left
    w "It's okay"
    r "So"
    extend ", did you read the note?"
    if not remi_crime_note_read:
        show watta deter
        w "The what? The crime note?"
        show remi distraught
        r "Sound like you haven't read it then"
        r "That's fine"
    else:
        show watta default
        w "Ye I did"
        show remi default
        r "What do you think of me now, Watta?"
        show watta happy
        w "Nothing about you has changed for me Remi, you're still you"
        w "Even tho is"
        show remi hah
        r "It's pretty messed up yes,"
        r "But people grow to learn too, everyone can change"
        r "There is no natural bad people you know"
        w "..ye..."
        r "It can be forgotten now."
        r "Give me the note, i will dispose it off later"
        $ item_remove("Crime Note")
    r "You see"
    show remi erm
    r "I'm planning to go back"
    show watta shocked
    r "Back to everyone"
    show watta hype
    w "That's great to hear!"
    show remi hmm
    r "But i do wonder if events are gonna"
    extend " repeat agan"
    show watta smile
    w "They all know who you are Remi"
    show remi look
    w "You just need to be more open with people"
    show watta happy
    w "Letting what's troubling you out"
    show remi ill
    r "That time when you came over, like{w=0.5} a few months ago"
    r "Before this mess happened"
    show watta huh
    show remi look
    r "We were at... where was it again?"
    show watta smile
    w "Was it the beach?"
    show remi smile
    r "Yes the beach, I miss that time Watta."
    r "That was exactly the first and only time all of us were together in the same picture"
    show remi hmm
    r "I tried finding it again but to no avail, i think it's lost media now"
    show watta sad
    w "Oh"
    show remi look
    r "I'm sorry"
    show watta smile
    w "Don't be, i don't think any of them will mind"
    show remi up
    r "I really miss everyone Watta. I wish to relive some of these moments, sadly they're all just memories now."
    r "Though..."
    show watta happy
    show remi smile
    r "Thank you for spending time with me"
    r "I feel much better now, gotta make my way back soon."
    show remi hah
    r "Thanks, Watta"
    show screen task_aquired("REMI'S QUEST COMPLETED", "QUALITY: GOOD", "images/task/taskremi.png")
    $ quest_end("remi")
    
    pause 3.0
    r "While you're here, let's have a nice chat."
    $ remi_first_talk_done_stage = 7
    menu:
        r "Got anything on your mind?{fast}"
        "Ask him any question":
            hide watta
            call screen remi_screen    
            jump remi_talk
        "Nothing for now":
            hide watta
            hide remi
            jump lighthouseskip
    jump lighthouseskip
    
label remi_talk:
    show bg lighthouse at whiten
    show remi smile at fade_in_right
    r "A"
label remi_talk_skip:
    call screen remi_screen

default remi_options = {
    "Leave": "remi_byebye",
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
screen remi_screen():
    tag remi_sub
    modal True
    zorder 95

    vbox:
        spacing 60
        xalign 0.7
        yalign 0.25

        if remi_options:
            $ shift = 0
            for name, target_label in remi_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#a1ffb8", "#3cf16f", t)
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
                        font "Remi.ttf"

                $ shift += 0

label remi_byebye:
    r "Adios."
    hide remi
    scene bg archeste
    jump lighthouseskip