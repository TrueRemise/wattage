default woogie_first_talk_done_stage = 0
default woogie = False

label woogie_test:
    stop music fadeout 0.5
    play music "bgm_woogie.mp3" fadein 1.0 
    if woogie_first_talk_done_stage == 0:
        jump woogie_first_talk
    elif woogie_first_talk_done_stage == 1:
        jump woogie_second_talk

label woogie_first_talk:
    stop music fadeout 0.5
    play music "bgm_park.mp3" fadein 1.0
    if phase !=3:
        scene bg park at whiten
    else:
        scene bg parkn at whiten
    show watta default
    w "This is the first time I ventured outside of the district."
    w "And this is the local park close to my workplace"
    w "If I recall correctly, this is where Sari works."
    w "I should go and greet him."
    if is_item_get("Sari's Sauce"):
        w "And ask him about the sauce..."
    unknown "{font=Woogie.ttf}{size=+5}{i}sniff sniff*"
    show watta huh at shake
    w "???"
    unknown "{font=Woogie.ttf}{size=+5}Something smells fishy here..."
    w "Huh??"
    unknown "{font=Woogie.ttf}{size=+5}Ya the perpetrator aren't ya?"
    w "What are you even talking about?"
    unknown "{font=Woogie.ttf}{size=+5}That's what a criminal would say... Hmm..."
    unknown "{font=Woogie.ttf}{size=+5}What's yer name hmm?"
    w "W-Watta??? Who even are you???"
    stop music fadeout 2.5
    show watta huh at slide_to_left
    show woogie black at slide_in_right
    unknown "{font=Woogie.ttf}{size=+5}Did ya know ya committed a really serious crime?"
    show watta shocked at shake
    w "???"
    unknown "{font=Woogie.ttf}{size=+5}Put yer hands behind yer back won't ya?"
    show watta wtf at shake
    w "Wait what did I do??? I didn't do anything???"
    unknown "{font=Woogie.ttf}{size=+5}{i}Pff"
    show woogie laugh3 at bounce
    unknown "{font=Woogie.ttf}{size=+5}Gyahahahaha!!"
    show watta frown
    play music "bgm_woogie.mp3"
    w "?"
    show woogie laugh3 at bounced
    unknown "{font=Woogie.ttf}{size=+5}Sorry I can't"
    unknown "{font=Woogie.ttf}{size=+5}Ya fell for it so easily this is so funny"
    show watta mad
    w "..."
    show woogie laugh4
    unknown "{font=Woogie.ttf}{size=+5}Okay okay sorry bad jokes aside..."
    w "..."
    show woogie default at bounced
    wo "I'm detective Woogie, the one and only BEST of the BEST detective of Sidurina!"
    wo "This is my companion, we solve crimes and eat wiener when it comes out"
    w "..."
    pause 0.5
    show woogie wait at bounce
    wo "Wait wait chill calm down it's supposed to be a lightweight joke, ya dont have to be that serious!"
    show watta mad at bounced
    w "Whatever..."
    show woogie wait at bounce
    wo "Be cool okay I didn't want to scare ya that badly, really it's just a joke man"
    show watta frown
    w "Urgh... so what are you doing here anyways?"
    show woogie laugh2 at bounce
    wo "Us? We are just doing our daily routine of solving crimes and making the world a better place."
    show watta mad at bounced
    w "Does it justify what you just did?"
    show woogie wait at bounce
    wo "I said we move on okay? I swear I won't do it again, geez..."
    show woogie stare with dissolve
    wo "By the way, I see ya have been loitering around, what's up with that?"
    show watta default
    w "Oh I'm just going around checking the city before the festival."
    show woogie laugh with dissolve
    wo "Festival, yes the festival. It's high time for crime and evil intention, don't let it sway yer mind."
    show watta frown
    w "I have no idea what you're talking about."
    show woogie laugh2 at bounce
    wo "Truth is, haha, I have been looking around for an assistant, ya know! Ya can be my very own Watson."
    show watta frown at bounced
    w "What no, I'm just here to meet my friends. I've no time for this childplay, let me go"
    show woogie cry at bounce
    wo "Wait wait wait hold on! Ya see my companion here... well truth is we can't communicate, so I do be desperately in need of an assistant."
    show watta frown
    w "None of my business"
    show woogie cry at bounce
    wo "Please please I've asked literally everyone else and no one agree. Please Watta I need this."
    show watta upset
    w "hmm"
    menu:
        "Agree":
            w "Fine, but don't demand anything from me nor am I obligated to do as you say."
            show woogie proud at bounced
            wo "Gyahaha, that's fine. I can just follow along and solve crimes on my own"
            show woogie laugh2
            wo "Thank ya so much anyways."
            wo "Now just keep on doing what ya do, don't mind me following from behind..."
            wo "Gyehehe..."
            $ woogie = True
            hide woogie
            hide watta
            "You have unlocked Woogie."
            $ notebook_unlock("Woogie")
            jump park
        "No is no":
            show woogie cry at bounce
            wo "It's so over, the world doesn't want to accept me..."
            wo "Okay sorry i'll leave, sorry for bothering"
            show woogie cry at slide_out_right
            show watta sleepy
            w "Such a bother"
            jump park