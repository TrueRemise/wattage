default bailey_first_talk_done_stage = 0
default bailey_chant = False
default bailey_unavailable = False
default bailey_following_oil = False
default bailey_following_oil_talk = False
default bailey_body_returned = False
default bailey_refining_timer = 1

label bailey_test:
    if bailey_first_talk_done_stage == 0:
        jump bailey_first_talk
    elif bailey_first_talk_done_stage == 1:
        jump bailey_second_talk
    elif bailey_first_talk_done_stage == 2:
        jump bailey_third_talk

label bailey_first_talk:
    show watta default at left
    show bailey default at right
    b "So here's the problem"
    show bailey sus 
    b "This place was thriving before"
    show watta huh 
    b "That is... until the queen got really depressed"
    show bailey pant 
    b "I don't know why but it has gotten prettyyy bad..."
    b "She can't get herself to work anymore, and people's moods have gone down the drain"
    show bailey default 
    b "The city fell into a crisis, there was no one as good as her to be in charge"
    show watta shocked 
    b "Not even a monarch, he died a little bit before this all started"
    b "The 7 soulbearers also got their problems and can't really help much out either"
    show bailey neutral 
    b "And most confusing of all..."
    show watta sweat 
    w "Hmm?"
    show bailey mad 
    b "The queen doesn't even know what's bugging her and thus no one can really help her improve"
    b "The cause of her depression is surely some exterior problem, but no one can pinpoint exactly what."
    show bailey default 
    b "Maybe if we figure out the reason and fix it, she'll heal back up"
    show watta huh 
    b "But until that happens, our situation can't improve."
    show bailey sus 
    b "Since you are an outsider I don't want to get you involved in this"
    show bailey default 
    show watta default 
    b "But if you have any information please inform me, it will help me out a lot..."
    show watta smile 
    w "I'll let you know if I find anything."
    show bailey smile 
    b "Thanks"
    hide watta
    hide bailey
    $ bailey_first_talk_done_stage = 1
    $ notebook_unlock("Bailey")
    jump railworkskip

default bailey_give_sauce_normal = 0
label bailey_second_talk:
    show watta default at left
    show bailey default at right
    if bailey_give_sauce_normal == 4:
        b "The sauce is all done now."
        b "When I saw all the fungus I thought he sent me this as a joke, I was ready to throw it in the trash..."
        b "but as it turns out it's something we can work around."
        b "I was able to make it safer and after some testing it is now drinkable! It's very similar to wine, it can even get you drunk so don't chug it."
        b "...Oh you don't drink sauce? {w=0.5}That's weird!"
        hide watta
        hide bailey
        $ bailey_give_sauce_normal = 5
        $ item_add("Flavored Sauce")
        jump railworkskip
    else:
        if bailey_body_returned:
            jump bailey_body_returned
        else:
            b "Anything new?"
    if sari_first_talk_done_stage >= 3 and is_item_get("Sari's Sauce"):
        if bailey_give_sauce_normal == 0:
            menu:
                "I want to deliver this sauce to you":
                    b "Hmm?"
                    show bailey smile
                    b "Oh is it Sari's?"
                    b "Been a while since he sent me something, I almost thought he forgot about me..."
                    b "What did he want me to do with this anyways? I'm not the sauce guy."
                    show watta sweat
                    w "He just.. I don't know I think he wants you to examine it"
                    show bailey sus 
                    b "Huh? That's it? Alright"
                    show bailey smile 
                    b "Thanks btw"
                    $ bailey_give_sauce_normal = 1
                    $ item_remove("Sari's Sauce")
                    $ quest_desc_change("sari",": Wait for Bailey's examination to be completed.")
                    hide watta
                    hide bailey
                    jump railworkskip
                "Nothing":
                    pass
    if the_alley_knower and bailey_chant == False:
        menu:
            "Hinder is the amber, dark is the root, fire is the blood":
                show bailey shock
                b "What the?"
                b "Who let you twist it like tha-"
                show bailey pant
                b "Wait..."
                show watta deter
                w "???"
                show bailey sus
                b "It makes sense now, how did you figure this out?"
                show watta huh
                w "Someone told me..."
                b "I believe it was the right thing to do. Also, we need to..."
                show bailey mad
                b "...I'll give you access to the alley."
                show watta default
                w "The what?"
                show bailey neutral
                b "The alley, if what you said is correct, then we need to conduct it deeper into the root."
                b "For now I can't disclose more without confirmation, but to get that we need to dwelve deeper first.."
                show bailey sus
                show watta huh
                b "I will explain a bit more on the train..."
                hide watta
                hide bailey
                $ bailey_chant = True
                jump railworkskip
            "Nothing":
                pass    
    if bailey_train_no_oil and oil_lake_cavern_found and not bailey_following_oil_done:
        menu:
            "I found a giant oil pool":
                if not bailey_following_oil_talk:
                    show bailey shock
                    b "What the?"
                    b "For real?"
                    show bailey sus
                    b "But,{w=0.3} who owns it?"
                    show watta delighted
                    w "Seems like no one."
                    b "I can't believe it"
                    show bailey shock
                    extend " You found yourself an untouched oil pool!?"
                    show bailey mad
                    show watta sweat
                    b "We have been looking for one for months."
                    b "You can't be serious right now!"
                    show watta deter
                    w "Believe it or not it's there."
                    show bailey pant
                    b "Okay"
                    b "It can't be worse than this"
                    show bailey default
                    b "Show me the location"
                    show bailey smile
                    extend ", I'll call the crews for extraction later"
                    show watta smile
                    w "Okay follow me."
                    hide bailey
                    hide watta
                    $ bailey_unavailable = True
                    $ bailey_following_oil = True
                    $ bailey_following_oil_talk = True
                    jump railworkskip
                else:
                    show bailey angry
                    show watta upset
                    b "Again?"
                    show watta sweat
                    w "Last time there was an urgent, I will lead you to the pool this time fr."
                    show bailey default
                    b "Geez"
                    b "Please don't mess around with me like that anymore"
                    hide bailey
                    hide watta
                    $ bailey_unavailable = True
                    $ bailey_following_oil = True
                    jump railworkskip
            "Nothing":
                pass
    w "Nothing really"
    show bailey sus
    b "K"
    hide watta
    hide bailey
    jump railworkskip

label bailey_third_talk:
    show bailey default at right
    sr "What do you need?"
label bailey_talk_skip:
    call screen bailey_screen

default bailey_train_no_oil = False
label train_test:
    if not bailey_train_no_oil:
        show bailey pant at right
        show watta default at left
        b "Hold on a second I forgot something."
        show watta deter
        w "???"
        b "The path to alley is pretty far, and sadly the train is out of fuel"
        show bailey default
        show watta default
        b "The thing is, along with the depression, the fossil fuel industry close down..."
        show bailey pant
        b "And with what we have left is not sufficent for the railroad anymore."
        b "Now the Railroad is kind of useless. With the shut down of the Alley this station turned into a ruin."
        show bailey mad
        b "I guess I will have to ask them reserved an amount enough for this trip, but it will take forever. Shittt..."
        show watta sad
        w "That sucks..."
        $ bailey_train_no_oil = True
    else:
        "Need powered..."
    hide bailey
    hide watta
    jump railworkskip

default bailey_first_time_hall = False
label bailey_hall_talk:
    show bailey neutral
    if not bailey_first_time_hall:
        if spira_first:
            b "Oh it's you again!"
            show bailey smile
            b "Already become a Nekomin I see."
        else:
            b "Oh a new Nekomin?"
            show bailey shock
            b "When did you enroll? I haven't heard about a new one coming"
            show bailey neutral
            b "Well either way"
        b "Since this is your first time being here..."
        show bailey smile
        b "We are all wanting to help our beloved Neko shine."
        b "So we have to encourage her and aid her through this dilemma"
        b "Well, the details will be discussed later, so just have to wait here for now."
        show bailey neutral
        b "Come talk to me if you want to kill time."
        $ bailey_first_time_hall = True
        hide bailey
        jump hallskip
    else:
        b "Do you want to kill the time?"
        menu:
            "Kill time":
                jump tsukino_meeting_begin
            "Nah":
                jump hallskip

label bailey_following_action_done:
    $ phone_open = False
    show bailey angry
    b "Why is it taking so long?"
    show bailey mad
    b "I don't have forever, stop messing around."
    b "Goodbye"
    hide bailey
    "Bailey has left the party."
    $ bailey_following_oil = False
    $ bailey_unavailable = False
    return
label bailey_following_going_elsewhere:
    $ phone_open = False
    show bailey default
    b "Is that the location?"
    w "Uh I..."
    show bailey angry at bounce
    b "I don't have forever, stop messing around."
    hide bailey
    return
default bailey_following_lane_to_spira_talk = False
label bailey_following_thru_district:
    hide screen phone_screen
    hide screen map_screen
    if not bailey_following_lane_to_spira_talk:
        show bailey default at right
        show watta default at left
        b "You want to get to monument through that path?"
        b "Are you insane? That is so long."
        if lane_first:
            w "Okay okay chill..."
            hide watta
            hide bailey
            $ bailey_following_lane_to_spira_talk = True
        else:
            show watta sad
            w "But I don't know any other path..."
            show bailey smile
            b "Oh it's fine, I can teach you the short cut, even though it's"
            show bailey pant
            extend " a little bit eurghh.."
            hide watta
            hide bailey
            "Shortcut from Spiralia to Monument has been unlocked, clickable unlocked in Spiralia."
            $ lane_to_spira_first = True
            $ bailey_following_lane_to_spira_talk = True
            return
    else:
        show bailey angry
        b "Stop going there!"
    return
    
default bailey_body_returning = False
default bailey_following_oil_done = False
label bailey_following_oil_scene:
    show watta default at left
    show bailey default at right
    w "Here we go"
    show bailey shock
    b "What the?"
    b "Right under the monument?"
    show bailey pant
    b "Wait.."
    show bailey smile
    show watta smile
    extend " this is magnificent"
    b "With this high quality in such amount..."
    b "We can totally make use of this."
    pause 1
    unknown "{font=Vivi.ttf}What do you think you are doing?"
    show watta default at bounced
    show bailey default at bounced
    scene bg oilgun with Fade(1,0.4,2)
    pause 1.0
    b "Wait wait wait we can totally-{nw}"
    show bg white
    pause 0.1
    show bg black
    stop music
    play sound "sfx/gunshot.mp3"
    scene bg cavern1 with Fade(2,4,2)
    play music "bgm_cavern.mp3" fadein 1.0 if_changed
    show watta default at left
    show vivi default at right
    unknown "{font=Vivi.ttf}Such a hassle."
    w "You killed him???"
    unknown "{font=Vivi.ttf}Don't worry,"
    extend " he's just sedated, not a single cell was harmed."
    w "Phew..."
    unknown "{font=Vivi.ttf}Watta... {w=0.5}one question."
    unknown "{font=Vivi.ttf}When I told you to leave this place immediately."
    unknown "{font=Vivi.ttf}Why, in the world would you think it's fine to invite someone here?"
    w "I'm sorry"
    unknown "{font=Vivi.ttf}And it's also the freaking dog, what a problem."
    w "Dog?"
    unknown "{font=Vivi.ttf}You want some oil?"
    unknown "{font=Vivi.ttf}These buckets are enough for a round trip to the Alley."
    unknown "{font=Vivi.ttf}Take them."
    $ item_add("Oil Tank")
    w "Oh thanks."
    unknown "{font=Vivi.ttf}There is a hidden oil rig in the Alley around this location."
    if not is_item_get("Memorizing Sheet"):
        unknown "{font=Vivi.ttf}You bring no notes?."
        unknown "{font=Vivi.ttf}Here is some cash, go out there and buy one."
        unknown "{font=Vivi.ttf}I will just write down in my own note."
        pause 1.0
        unknown "{font=Vivi.ttf}Here."
    else:
        "The oil rig location was noted down in the notebook."
    unknown "{font=Vivi.ttf}And about this person, I will take care of them later."
    unknown "{font=Vivi.ttf}You should expect to see them at their local place tomorrow."
    unknown "{font=Vivi.ttf}Also."
    unknown "{font=Vivi.ttf}Obviously."
    unknown "{font=Vivi.ttf}Don't invite anyone down here again."
    unknown "{font=Vivi.ttf}You are an exception, remember that Watta."
    unknown "{font=Vivi.ttf}Now leave."
    $ bailey_following_oil = False
    $ bailey_body_returning = True
    $ bailey_following_oil_done = True
    jump monument

label bailey_body_returned:
    show watta default at left
    show bailey mad at right
    b "Watta"
    show watta deter
    w "Hmm??"
    show bailey pant
    b "I had such a crazy dream yesterday."
    show watta sweat
    b "And it was insanely real as well"
    show bailey default
    b "So in the dream I was sitting here like usual, and you came up to me and said:"
    show watta deter
    extend "\"I found a hugeeee pool of oil\""
    w "uhh huh"
    show bailey shock
    b "And I was like\"No way\" but you led me to the place and it was real."
    show bailey angry
    show watta upset
    b "But a gang member or someone showed up and they point the gun at me,"
    b "I don't remember why but he said I was trespassing their grounds and shot me dead."
    show bailey sus
    b "Super crazy"
    show watta deter
    w "Ye it's crazy"
    show watta sweat
    pause 2
    show watta upset
    w "Also I bought some oil see if it can work"
    show bailey smile
    b "Oh these crude oil definitely work yes yes."
    show bailey neutral
    show watta deter
    b "Also damn you must be rich if you can just... LEND me oil."
    b "While you're at it, why not lend me some cash as well?"
    show bailey smile
    b "Just joking"
    b "We will need to refine the oil first before fueling."
    b "Might take some times"
    show watta smile
    w "Alright"
    show bailey neutral
    b "Go do something while waiting."
    $ bailey_refining_timer = 2
    $ bailey_body_returned = False
    jump railwork
