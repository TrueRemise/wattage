default tsuyu_first_talk_done_stage = 0
default tsuyu_go_sane_at_two = 0

label tsuyu_test:
    stop music fadeout 0.5
    play music "bgm_tsuyu.mp3" fadein 1.0 
    if tsuyu_first_talk_done_stage == 0:
        jump tsuyu_first_talk
    elif tsuyu_first_talk_done_stage == 1:
        if tsuyu_go_sane_at_two < 2:
            jump tsuyu_going_insane
        elif tsuyu_go_sane_at_two == 2:
            jump tsuyu_going_saner
        else:
            jump tsuyu_going_sanerer


label tsuyu_first_talk:
    show bg blowey with Fade(0.1, 0, 0.1)
    show bg blowey at whiten
    ts "Boringggggggg..."
    show tsuyu cry at slide_in_right
    extend " Sooo boringgg"
    ts "I did hope he'd come again but not today apparently..."
    show watta default at slide_in_left
    w "Hello"
    show tsuyu surprised at bounce
    ts "Wwhat??"
    w "Huh?"
    show tsuyu huh at bounced
    ts " Did you hear it?"
    show watta huh
    w "Hear what?"
    show tsuyu frown
    ts "nvm.."
    show watta happy at bounced
    w "I do get why you feel lonely, is really empty."
    show tsuyu angry
    ts "{size=-20} So you did hear it..."
    show watta huh
    w "What did you say?" 
    show tsuyu default
    ts "Ye it's really lonely here, there aren't many visitor in this area you know, it's pretty much just me sitting through 9 hours everyday"
    show watta shocked
    w "9- What??"
    extend "  How many people work here?"
    show tsuyu frown at bounced
    show watta default
    ts "Just 2, I have to do the morning shift, and it's the most tiring thing ever, I just wanna, talk to someone"
    show watta huh
    w "I'm curious though what compelled you to do this job?"
    ts "Decent income... and to be honest there aren't many jobs available for me, this is like the best one yet."
    show tsuyu sad
    ts "just gotta... endure"
    show tsuyu default at bounced
    ts "Well at least I'm pretty good at my job, in the end I was tasked with the most important job"
    show tsuyu proud
    ts "To protect Blowey"
    show watta huh at bounced
    w "To protect what?"
    ts "Blowey, that's the name I gave her, cute isn't it?"
    show watta upset
    w "{size=-20}{i} this dude paranoid"
    show tsuyu sad
    ts "Sitting here for months but I never got to see what the inside world look like..."
    ts "After the incident no one really visits this place anymore"
    show tsuyu insane
    ts "OMG WHY DID IT HAPPEN I'M SO LONELY ARGHHHH"
    show watta upset at bounce
    w "Calm down! Calm down you're being too dramatic."
    show tsuyu depressed
    ts "I don't think anyone can hear me either"
    "{color=#000}Voice{/color}" "{size=+10}{font=Watta.ttf}i can{w=0.3}{nw}"
    show tsuyu angry at bounced
    ts "I know who you are! You're not here to visit me, you are just gonna ignore me and pass through to Blowey, you are just like THE REST OF THEM"
    w "{size=-20}{i} this man needs to calm down"
    show watta frown
    w "I just met you and i'm not being given the best first impression..."
    show tsuyu plead
    ts "Please, you are the only person to talk to me after so long, please stay for a bit longer"
    show watta upset
    w "But i'm busy."
    show tsuyu insane
    ts "It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. "
    w "{i}I should get out of here"
    $ notebook_unlock("Tsuyu")
    $ tsuyu_first_talk_done_stage = 1
    if sanco_talked_through_phone_before == True:
        $ add_surprise("Sanco", "daheo_tsu_doin")
    $ tsuyu_go_sane_at_two = 1
    jump northgate

label tsuyu_going_insane:
    show bg blowey with Fade(0.1, 0, 0.1)
    show bg blowey at whiten
    show tsuyu insane
    ts "{cps=*5}It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. It's so painful. "
    jump northgate

label tsuyu_going_saner:
    show bg blowey with Fade(0.1, 0, 0.1)
    show bg blowey at whiten
    show tsuyu cry at right
    show watta default at left
    ts "Tsk..."
    ts "I'm sorry"
    show watta smile
    w "Is okay"
    show tsuyu sad
    ts "I didn't think it through."
    ts "My childish behaviour might lose me more friends,"
    show tsuyu plead
    show watta delighted
    ts "So as an apology I will lower the cost of entrance by half, what do you think?"
    $ tsuyu_go_sane_at_two =3
    if is_unlocked("field"):
        show tsuyu depressed
        show watta default
        ts "You already went thru Blowey???"
        show watta upset
        ts "OMG man"
        show tsuyu frown
        ts "Okay but really,"
        ts "What can I really do to..."
        show tsuyu surprised
        ts "Oh!"
        show tsuyu depressed
        ts "But like this is a big deal,..."
        show tsuyu default
        extend " So I will let you in for free, and also gonna give you something rare if you can cure my boredom."
        show watta default
        w "What would that be?"
        ts "Idk uhh..."
        extend " How about my blood?"
        show watta frown
        w "Why the hell would I need it for?"
        show tsuyu depressed
        ts "I don't know but I really can't think of anything better so please!"
    else:
        pass
    if is_item_get("UES"):
        call screen tsuyu_gate
    elif is_unlocked("field"):
        call screen tsuyu_gate_3
    else:
        call screen tsuyu_gate_2
    jump northgate

screen tsuyu_gate():
    modal True
    frame:
        background Solid("#ffffff00")
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            button:
                at hover_fade
                xsize 1000
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Jump("tsuyu_get_ues")
                text "I have something to give you...":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("northgate")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"

screen tsuyu_gate_2():
    modal True
    frame:
        background Solid("#ffffff00")
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            button:
                at hover_action
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Jump("tsuyu_gate_check")
                text "Pay 100 to gain access":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("northgate")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"

screen tsuyu_gate_3():
    modal True
    frame:
        background Solid("#ffffff00")
        xalign 0.5
        yalign 0.5
        xsize 800
        ysize 500
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.5
            button:
                at hover_action
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5
                background Solid("#a4383800")
                hover_background Solid("#FFFFFF00")
                action Jump("tsuyu_gate_check")
                text "Move in Bloomfield":
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
            button:
                at hover_fade
                xsize 800
                ysize 100
                xalign 0.5
                yalign 0.5  
                background Solid("#ff000000")
                hover_background Solid("#FFFFFF00")
                action Jump("northgate")
                text "Do nothing":
                    size 90
                    xalign 0.5
                    yalign 0.5
                    color "#000000"

label tsuyu_gate_check:
    if tsuyu_saved and not is_unlocked("field"):
        jump gate_jump
    else:
        $ move_to("field")
    if sol >= 100:
        $ sol -= 100
        show tsuyu proud
        ts "Pleasure doing business..."
        jump gate_jump
    else:
        show tsuyu angry 
        ts "This is not enough, don't try to scam me, get out!"
        jump northgate

default tsuyu_saved = False
label tsuyu_get_ues:
    show watta default
    show tsuyu frown
    ts "Huh? What is this?"
    show tsuyu surprised
    ts "Wait, where did you get this?"
    ts "I thought this was lost technology"
    show tsuyu plead
    ts "Damn, this is unbelieveable!"
    ts "Are you sure I can have this?"
    show watta delighted
    w "{i}nod"
    show tsuyu cry
    ts "Thank you!"
    ts "You saved my life man"
    if not is_unlocked("field"):
        show tsuyu proud
        ts "A promise is a promise, I'm letting you in just... don't tell anyone about this tho."
        ts "And also uhh..."
    show tsuyu default
    ts "Here. The rare item."
    $ item_add("Defiled Blood")
    $ item_remove("UES")
    show watta frown
    w "Ar"
    show tsuyu proud
    ts "I finally have something to cure my boredom."
    ts "Have a good day sir!"
    $ tsuyu_saved = True
    call screen tsuyu_gate_3
    jump northgate

label tsuyu_going_sanerer:
    show bg blowey with Fade(0.1, 0, 0.1)
    show bg blowey at whiten
    show tsuyu cry at right
    show watta default at left
    ts "Oh, it's you again."
    if tsuyu_saved:
        show tsuyu proud
        ts "Welcome savior!"
        call screen tsuyu_gate_3
    if is_item_get("UES"):
        call screen tsuyu_gate
    if is_unlocked("field"):
        call screen tsuyu_gate_3
    else:
        call screen tsuyu_gate_2
    jump northgate