# File: game/systems/reni.rpy

label msg_renia_aloy_back:
    show bg phone
    rn "Hello Watta"
    rn "Aloy got back to his house"
    rn "He might have something to tell you"
    w "I see, thank you"
    call screen message_screen
    return
    

label msg_renia_0:
    if phase == 0 or phase == 1:
        if not reni_phone_intro_done:
            call reni_calling_0 from _call_reni_calling_0
        else:
            call msg_renia_1
    else:
        "(voicemail) I am currently occupied, please avoid calling from 5pm to 10pm"
    call screen message_screen
    return

label already_write_reni_number:
    w "Let me type in Reni's number real quick!"
    w "Andddd... "
    $ msg_unlock("Renia")
    extend "Done!"
    w "So..."
    return

default timer_minutes = 0
default timer_seconds = 0
default reni_thought_it_was_a_scam_call = False
default reni_first_time_counter = 0
default reni_phone_intro_done = False

init python:
    def update_timer_counter():
        global timer_minutes, timer_seconds

        timer_seconds += 1
        if timer_seconds >= 60:
            timer_seconds = 0
            timer_minutes += 1

        if timer_minutes >= 100:  # reset at 99:59
            timer_minutes = 0
            timer_seconds = 0
screen running_timer():
    modal False
    zorder 100
    frame:
        xalign 0.482
        yalign 0.57
        background "#ffffff00"
        text "{:02d}:{:02d}".format(timer_minutes, timer_seconds) xalign 0.5 yalign 0.5 size 80 color "#000000" font "Nemu.ttf" outlines [(1, "#000000", 0, 0)]

    # Call the function every second
    timer 1.0 action Function(update_timer_counter) repeat True

label reni_calling_0:
    stop music fadeout 0.5
    scene bg ongoingcall with Fade(0.1,0,0.1)
    play sound "sfx/outgoing_call.mp3" loop
    "Calling Reniacc{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    "Calling Reniacc{fast}{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    "Calling Reniacc{fast}{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    play sound "sfx/join.mp3"
    $ timer_minutes =0
    $ timer_seconds=0
    show screen running_timer
    show bg call with Dissolve(0.5)
    show bg 
    play music "bgm_reni.mp3" fadein 3
    if reni_thought_it_was_a_scam_call == True:
        jump reni_thought_it_was_a_scam_call
    rn "Hello?"
    menu:
        "...":
            rn "Please don't call me if you just want to mess around, goodbye."
            stop music fadeout 0.5
            play sound "sfx/end_call.mp3"
            hide screen running_timer
            show bg endcall
            "They hang up." 
            w "Lmao..."
            $ reni_thought_it_was_a_scam_call = True
            return
        "It's me Watta":
            rn "Ohh good to see you Watta, I heard you just moved in last week, how are things going on there?"
    label reni_ask_1:
    w "Is nice, I met lots of nice people already"
    rn "That's great to hear, glad you enjoyed it, sadly I had to move out for a while..."
    rn "Wait..."
    w "Huh?"
    rn "Who gave you my number?"
    if already_write_reni_number or already_read_reni_number:
        w "Huh? Is on your home door."
        rn "Oh so you were in North Sidurina already? That's quick!"
        w "Well I was travelling around so..."
        rn "I see, well I'm free at the moment, so if you have anything to talk about you can ask me."
    else:
        w "Oh well... uhhh..."
        rn "Nevermind about that..."
        rn "I'm free at the moment, so if you have anything to talk about you can ask me."
    w "Of course!"
    $ reni_phone_intro_done = True
    $ update_msg_phase("Reni", "0")
    jump reni_talk_skip

label reni_thought_it_was_a_scam_call:
    rn "If you continue to call to mess with me I wil-"
    w "Hold on hold on It's me, Watta!"
    rn "Oh it's you I thought it was a.. sorry for hanging up on you earlier..."
    w "It's okay, I didn't respond in time."
    rn "It's fine, also I heard you just moved in last week, how are things going on there?"
    jump reni_ask_1


label msg_renia_1:
    stop music fadeout 0.5
    scene bg ongoingcall with Fade(0.1,0,0.1)
    play sound "sfx/outgoing_call.mp3" loop
    "Calling Reniacc{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    "Calling Reniacc{fast}{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    "Calling Reniacc{fast}{w=0.5}.{w=0.5}.{w=0.5}.{nw}"
    play sound "sfx/join.mp3"
    $ timer_minutes =0
    $ timer_seconds=0
    show screen running_timer
    show bg call with Dissolve(0.5)
    show bg 
    play music "bgm_reni.mp3" fadein 3
    rn "Hello Watta, what do you want to talk about?"
label reni_talk_skip:
    if neko_first_talk_done_stage >= 1:
        $option_add("reni", "About Neko", "reni_about_neko", pos=0) 
    call screen reni_screen
default reni_options = {
    "Why did you leave your house?": "reni_why_did_you_leave",
    "About Aloy": "reni_about_aloy",
    "About Toko": "reni_about_toko",
    "About Remi": "reni_about_remi",
    "About Sanco": "reni_about_sanco",
    "Leave Call": "reni_byebye" 
}
screen reni_screen():
    tag reni_sub
    modal True
    zorder 195

    vbox:
        spacing 20
        xalign 0.5
        yalign 0.5

        if reni_options:
            $ shift = 0
            for name, target_label in reni_options.items():

                # shift value normalized 0..1 (adjust divisor to control gradient)
                $ t = min(1.0, shift / 100.0)
                $ hover_color = lerp_color("#ff97bb", "#E35B97", t)
                button:
                    at hover_fade
                    xsize 1220
                    ysize 120
                    xalign 0.5
                    xoffset -shift
                    background Solid("#ffffff79")
                    hover_background Solid("#ffffffc8")
                    action Jump(target_label)

                    text name:
                        size 80
                        xalign 0.5
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(13, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Reni.ttf"

                $ shift += 0

label reni_about_neko:
    rn "Neko?"
    rn "You met her?"
    rn "Oh. She's totally my favorite, I really like her."
    rn "I do wish to one day be working for her, that would be really nice."
    $ option_remove("reni", "About Neko")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_why_did_you_leave:
    rn "Sorry, i can't talk about that in detail..."
    rn "Just know it's about the big things of this city,"
    rn "Government and stuff-"
    $ option_remove("reni", "Why did you leave your house?")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_about_aloy:
    if not prologue_done_4:
        rn "He left his house for the same reason as I, but I believe he will be back home sooner than I would be."
    else:
        rn "He left his house for the same reason as I, but he's back now."
    $ option_remove("reni", "About Aloy")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_about_remi:
    rn "Do not mention it"
    w "Huh???"
    rn "I'm sorry, just,{w=1} we move on.."
    $ option_remove("reni", "About Remi")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_about_toko:
    rn "If you meet him by chance please send him my thanks! He helped me a lot with my problem."
    $ option_remove("reni", "About Toko")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_about_sanco:
    rn "I feel kind of bad for the situation Sanco finds herself in, I do hope it gets better."
    w "What happened to Sanco?"
    rn "Not my business to talk about..."
    $ option_remove("reni", "About Sanco")
    $ reni_first_time_counter += 1
    jump reni_talk_skip
label reni_byebye:
    rn "Okay see ya Watta."
    stop music fadeout 0.5
    play sound "sfx/end_call.mp3"
    hide screen running_timer
    show bg endcall
    call screen message_screen