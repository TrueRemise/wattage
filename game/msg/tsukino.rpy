
default meeting_choice_retire = False
default meeting_choice_spy = False


label tsukino_hall_intro:
    scene bg hall with fade
    scene bg hall at whiten_lesser
    show tsukino default
    tkn "The meeting will start in 30 minutes."
    tkn "Stay put."
    $ snowie_first_time_hall = False
    $ actions_locked = True
    jump hall

label tsukino_meeting_begin:
    scene bg black with fade
    "The meeting commenced."
    scene bg meeting with fade
    tkn "Okay are we all here?"
    tkn "Imma get this straight"
    stop music
    tkn "Neko is quitting her career."
    scene bg meeting at shake
    play music "bgm_suspense.mp3" fadein 4.0 if_changed
    "All" "WHATT?"
    show bailey shock at slide_in_right
    b "No way!"
    show snowie what at slide_in_left
    sn "This can't be true!"
    show snowie what at slide_out_left
    show tsukino close at slide_in_left
    tkn "Sadly it's the truth."
    tkn "I've decided it's the best to only let the high-ranked Nekomins know by now."
    show tsukino default
    tkn "As I believe there is a way to solve this."
    show bailey mad
    b "Bu... "
    extend "But why tho?"
    show tsukino close
    tkn "She said her mental health is deteriorating,"
    tkn "Details unheard of."
    tkn "Tried to persuade her into performing abroad, she declined."
    tkn "Clearly she wants to spend the last few days performing in her homecity before retiring."
    show tsukino speak
    tkn "We can not let this happens."
    show tsukino default
    show bailey pant
    b "Argghhh"
    show bailey pant at slide_out_right
    show tsukino default at slide_to_right
    show snowie sad at slide_in_left
    sn "Why is it going this way?"
    show tsukino speak
    tkn "That's why It's being asked."
    extend " If any of you Nekomins have any ideas."
    tkn "I believe only her biggest fans will get a grasp of her problems and solve them."
    show tsukino default
    sn "Mhhhmm"
    show snowie huh
    sn "Surely if we can promote her more, maybe more people will motivate her?"
    show tsukino default at slide_out_right
    show bailey mad at slide_in_right
    b "No the problem is what made her like that,"
    b "What is the source of the mental draining"
    show bailey pant
    b "Ugh not this again"
    show bailey mad
    b "Could be family, or sickness, or stress, can be anything."
    show snowie huh at slide_out_left
    show tsukino speak at slide_in_left
    tkn "She doesn't want to disclose that information, it's up to us to guess."
    tkn "Any more ideas?"
    menu:
        "How about letting her retire as she wanted?":
            show bailey mad at slide_out_right
            show watta default at slide_in_right
            w "What if we just let her retires as she wants to?"
            show tsukino angry
            tkn "Are you crazy? Are you even a Nekomin?"
            tkn "We needs to support her career, we are here to get her to the top of the idols."
            tkn "Surely this is just a temporary decision on impulse."
            tkn "There is no space for that, we have to knock the sense back to her mind."
            tkn "This is her biggest dream after all."
            $ meeting_choice_retire = True
            show tsukino speak
            tkn "This will need to be discussed on a more private manner."
            tkn "The chosen people will receive a message on their mail."
            tkn "The meeting concludes here for now."
            $ bailey_hall_presence = False
            scene bg black with fade
            "The meeting concluded"
            scene bg hall with fade
            play music "bgm_hall.mp3" fadein 1.0 if_changed
            show snowie jealous at left
            sn "Seems like I wasn't selected"
            show watta default at slide_in_right
            pause 0.8
            show snowie jealous2
            sn "Oh it's you"
            sn "You know, what you suggested?"
            show watta deter
            w "Huh?"
            sn "I know you cared about her mental health."
            sn "We all do"
            show snowie huh2 at bounced
            sn "But Neko is like that, she sometimes make decisions on impulse."
            sn "I don't want her to stop performing, but I also don't think she will ever quit"
            sn "As because it's something really important to her"
            show snowie sad
            sn "I believe time will tell."
            $ actions_locked = False
            $ neko_second_end = True
            $ action_done()
            $ action_done()
            $ action_done()
            jump hall
        "How about spying on her?":
            show bailey mad at slide_out_right
            show watta default at slide_in_right
            w "What if we spy on her to figure out the problem?"
            show tsukino angry
            tkn "Spying? Really?"
            show watta default at slide_out_right
            show snowie surprised at slide_in_right
            sn "That's so morally wrong"
            show tsukino close at bounced
            tkn "Uhhh... I think that's a good option for the last resort if it comes to this case."
            tkn "But who will spy on her?"
            show snowie surprised at bounce
            sn "OH NOT ME I WOULD NEVER DO THAT!."
            show snowie surprised at slide_out_right
            show bailey mad at slide_in_right
            b "I really don't support this but..."
            b "Can we really think of a better plan?"
            tkn "We really wish."
            show tsukino speak
            tkn "How about you blonde sheep?"
            show bailey mad at slide_out_right
            show watta default at slide_in_right
            show watta deter
            w "ME???"
            tkn "Ye, I saw you talking to her yesterday, and you are new also."
            tkn "Perfect for an expendable."
            show watta upset
            w "Maybe that's not the word but, "
            extend "I can try?"
            tkn "It's settled then, the meeting concludes"
            $ meeting_choice_spy = True
            $ bailey_hall_presence = False
            scene bg black with fade
            "The meeting concluded"
            scene bg hall with fade
            play music "bgm_hall.mp3" fadein 1.0 if_changed
            show snowie jealous at left
            sn "My opinion wasn't heard"
            show watta default at slide_in_right
            pause 0.8
            show snowie jealous2
            sn "Oh it's you"
            sn "You know, what you suggested?"
            show watta deter
            w "Huh?"
            sn "Nvm"
            sn "Good luck on it, I have to go now."
            show snowie jealous2 at slide_out_left
            $ snowie_hall_presence = False
            $ neko_second_end = True
            $ actions_locked = False
            $ action_done()
            $ action_done()
            $ action_done()
            jump hall

