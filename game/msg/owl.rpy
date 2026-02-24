
default owl_first_talk_done_stage = 0
default owl_quest_acquired = False
default owl_bad_end = False
default owl_about_remi = False
default owl_quest_done = False

label owl_test:
    if the_knower == 2 and not owl_about_remi:
        $ option_add("owl", "Remi", "owl_about_remi", pos=0)
    if owl_first_talk_done_stage == 0:
        jump owl_first_talk
    elif owl_first_talk_done_stage == 1 and not owl_quest_done:
        jump owl_first_talk_2
    elif owl_quest_done:
        jump owl_second_talk

default image_counter = 0
default image_beach = False
default image_monument = False
default image_spira = False
default image_skyward = False
label owl_first_talk:
    show bg owlnest at whiten_lesser
    show owl default at left
    show watta default at right
    w "Hello?"
    show owl speak
    o "Hello"
    show owl default
    show watta deter
    w "..."
    w "Are you not gonna question anything or..."
    show owl speak
    o "No I already knew you would come"
    show owl default
    show watta huh
    w "Oh okay."
    w "Uhh..."
    w "So do you know the reason as well?"
    show owl speak
    o "Ye, Remi told me."
    show owl default
    show watta upset
    w "{i}why didn't he also tell everyone else?"
    show watta deter
    w "Oh right, uhh"
    extend " so what should I do?"
    show owl speak
    o "Before starting the actual thing..."
    o "Do you mind if I ask for something?"
    show owl default
    show watta smile
    w "Oh sure of course!"
    show owl speak
    show watta huh
    o "I miss the outside world."
    show watta happy
    o "I want you to capture the outside world for me."
    o "Take this camera, it has 3 uses."
    $ item_add("Image Capturer")
    extend " But it's fine, you only need to take a picture of 3 things."
    o "The beach with the mountains, the big monument on the mountain, and the capital's academy."
    o "Gather them and I will help you with what you want."
    show screen task_aquired("OWL'S QUEST ACQUIRED", "CAPTURE 3 PICTURES", "images/task/taskowl.png")
    $ renpy.pause(11, hard=True)
    hide screen task_aquired
    $ quest_add("owl")
    $ owl_quest_acquired = True
    $ owl_first_talk_done_stage = 1
    hide owl
    hide watta
    jump owlnestskip

label owl_first_talk_2:
    show owl default at left
    show watta default at right
    if not len(set(image_taken_list)) == 0:
        jump owl_quest_check
    show owl speak
    o "Have you finished collecting yet?"
    show owl default
    show watta huh
    w "Not yet."
    show owl speak
    o "Hope it's not too troublesome."
    show owl default
    show watta smile
    w "It's fine"
    hide watta
    hide owl
    jump owlnestskip

label owl_bridge:
    show watta deter
    o "Hey don't touch that"
    show watta ahh
    w "Ahh!"
    o "Don't touch other people's stuffs."
    show watta sad
    w "Sorry."
    hide watta
    jump balconyskip

label owl_lake_night:
    show bg owlnestn at whiten_lesser
    show owl default at left
    show watta default at right
    show owl default
    o "Hey, don't get outside at this hour."
    show owl default
    show watta huh
    w "Huh? Why?"
    show owl speak
    o "It's not safe out there."
    o "You can get out once the clock chimes midnight."
    hide watta
    hide owl
    jump owlnest

label owl_quest_check:
    if len(image_taken_list) == 1:
        show owl speak
        o "Oh you got one. Great."
        o "Two to go."
        hide owl
        hide watta
        jump owlnest
    elif len(image_taken_list) == 2:
        show owl speak
        o "Oh you got two of them, that's nice."
        if len(set(image_taken_list)) == 1:
            show owl speak
            o "But why are they all the same place?"
            show owl default
            show watta sweat
            w "Erm..."
            jump owl_quest_restart
    elif len(image_taken_list) == 3:
        show owl speak
        o "Oh you got all of them, let's see."
        if len(set(image_taken_list)) == 1:
            show owl speak
            o "But why are they all the same place?"
            show owl default
            show watta deter
            w "...To enjoy it from all angles?"
            jump owl_quest_restart
        if len(set(image_taken_list)) == 2:
            show owl speak
            o "But why are 2 of them the same place?"
            show owl default
            show watta upset
            w "Double tapped..."
            jump owl_quest_restart
        if len(set(image_taken_list)) == 3:
            o "Good."
            o "Good."
            o "Good."
            o "I can replicate the outside world once more, thanks to you."
            o "I think you are trustworthy enough to be told the information."
            show screen task_aquired("OWL'S QUEST COMPLETED", "QUALITY: GOOD", "images/task/taskowl.png")
            pause 3.0
            $ owl_quest_done = True
            o "Now go ahead, ask me any question."
            $ quest_end("owl")
            $ option_add("owl","Swan Lake","owl_about_swan_lake", pos=0)
            $ option_add("owl","Soulbearer", "owl_about_soulbearer", pos=0)
            $ option_add("owl","Ability", "owl_about_ability", pos=0)
            $ option_remove("owl","Cooking")
            $ option_remove("owl","Sanco")
            $ option_remove("owl","Quest")
            $ option_remove("owl","owlnest")
            $ option_remove("owl","Spiralia")
            show owl default
            hide watta
            call screen owl_screen
        o "Only one left."
        hide owl
        hide watta
        jump owlnest


label owl_quest_restart:
    show owl speak
    show watta default
    o "No this isn't right, you must get 3 different ones."
    o "I'll give you another 3 blank sheets, take the proper pictures."
    $ image_taken_list = []
    $ image_taken = 0
    hide owl
    hide watta
    jump owlnest




label owl_second_talk:
    show bg owlnest at whiten_lesser
    show owl default at fade_in_left
    show owl speak
    o "What is up?"
    show owl default
label owl_talk_skip:
    call screen owl_screen

default owl_options = {
    "Swan Lake": "owl_about_swan_lake",
    "Soulbearer": "owl_about_soulbearer",
    "Ability": "owl_about_ability",
    "Festival": "owl_about_festival",
    "Leave": "owl_byebye",
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
screen owl_screen():
    tag owl_sub
    modal True
    zorder 95

    vbox:
        spacing 60
        xalign 0.7
        yalign 0.25

        if owl_options:
            $ shift = 0
            for name, target_label in owl_options.items():

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
                        size 90
                        xalign 0
                        yalign 0.5
                        color "#ffffff"
                        hover_color hover_color
                        outlines [(13, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "Owl.ttf"

                $ shift += 0

label owl_byebye:
    o "Okie."
    hide owl
    scene bg owlnest
    jump owlnestskip

label owl_about_swan_lake:
    show owl speak
    o "The swan lake."
    o "Decades ago, there was an area filled with life and swamps."
    o "Gorgeous landscape, stunning tropical climate, exotic resources."
    o "We claimed the lands and built stuffs on it, while trying to keep the natural vibe intact."
    o "One day, for some reason, a corruption outbreak occured."
    o "The unused swan boats got infected and started to move on their own."
    o "During the daylight they would be immobile swanboats like the usual, but when night comes they start acting wild."
    o "The queen realized this problem... so for the sake of people's livelyhood she locked the area away."
    o "And I volunteered to be the guardian of this place looking out for the swans."
    o "This building was built in the center of the area. On high elevation with view to all sides."
    o "It's also where I draw and store the paintings."
    show owl default
    jump owl_talk_skip
label owl_about_soulbearer:
    show owl speak
    o "The soulbearers, the big 7, you should know all of them by now."
    o "They inherited the 7 broken pieces of the Soul of Art."
    o "With the duty of keeping them safe, while the queen is in a coma."
    o "However the purpose of it was unclear for a reason I cannot disclose."
    o "They did their best before, but it has been a long while now, it's unclear they still prioritize it beyond all things."
    o "Rather than being idle, they should all be searching for a solution."
    show owl default
    jump owl_talk_skip
label owl_about_ability:
    show owl speak
    o "Magic is something that should have been forgotten long time ago."
    o "Due to the magnitude of its power, people swore an oath to not use it during the modern days."
    o "But recently, someone used it to cause disasters across the city, this caught everyone offguard because many don't even understand the concept of magic."
    o "Likely due to the work of the monarch, which was also used to drain the queen's lifeforce. Unfortunately she's the only other person who can use magic."
    o "I was given a part of time soul when I moved here, which give me the power related to time."
    o "While not powerful, it still lets me see briefly into the future."
    o "It can't go past 12 hours and I can't see my own future."
    show owl default
    jump owl_talk_skip
label owl_about_festival:
    show owl speak
    o "I can't enjoy it but I hope you will"
    show owl default
    jump owl_talk_skip
label owl_about_remi:
    show owl speak
    o "He's a good one, he knows many things."
    o "He's just too shy to be comfortable around people, at least for long."
    o "I am one of the few he would seek when he's in trouble."
    o "Now I might be the only one in such position."
    o "But I can't physically help him so, look after him won't ya?"
    show owl default
    $ owl_about_remi = True
    $ remi_opinion += 1
    $ option_remove("owl","Remi")
    jump owl_talk_skip
