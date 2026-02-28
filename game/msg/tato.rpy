# File: game/systems/tato.rpy
default tato_first_talk_done_stage = 0

label tato_test:
    stop music fadeout 0.5
    play music "bgm_tato.mp3" fadein 1.0 
    if tato_first_talk_done_stage == 0:
        jump tato_first_talk
    elif tato_first_talk_done_stage == 2:
        jump tato_second_talk
    elif tato_first_talk_done_stage == 3:
        jump tato_second_talk_2

label tato_first_talk:
    show tato close at right
    tt "Oh hi, you found me."
    show watta default at left
    w "Hello?"
    show tato default at bounced
    tt "Do you think cards can decide our fate Watta?"
    show watta frown
    w "Wait how do you know my name?"
    tt "Do you think we all own no possession over our futures, they are all set like a Monocord track ready to play out the rest."
    show tato half
    tt "Nothing will happen if you do nothing though, but everything will happen if you do something."
    show tato close
    tt "But in a major scale, what they ultimately lead to is fixed."
    show tato default at bounced
    tt "Which I don't think cards can predict precisely, but a close future is totally within grasp."
    tt "Here I have prepared one for you"
    w "???"
    show tato close
    tt "Keep this card in hand and never flip it until the moon turns blue."
    tt "And your fate shall be revealed."
    $ item_add("Facedown Card")
    $ tato_first_talk_done_stage = 1
    w "What does this mean{nw}"
    $ notebook_unlock("Tato")
    jump beachskip


label tato_second_talk:
    show tato close at right
    tt "Oh hi, you found me."
    show watta default at left
    w "What are you doing here?"
    show tato default at bounced
    tt "What do you think defines the accuracy of a prophecy?"
    show watta frown
    w "What are you trying to do?"
    show tato close
    tt "I don't know either."
    tt "It's all dependent on the will of the greaters, and the cards don't represent them."
    show tato half
    tt "But would it hurt to try sometimes? To follow the forecast."
    tt "As long as it doesn't violate the nature's flow, there are open chances for us to be exposed to different approaches."
    show tato default
    show watta default
    tt "This case here specifically foretold about an extensive amount of oil hidden under a well beneath the sand in this area."
    tt "I'm in no need of wealth, but I believe many will be saved once this is discovered."
    tt "I just need to find a method to extract them."
    w "Wao that sound good to be honest, tho highly doubt this. If it's true it would be huge"
    w "Might as well give it a try."
    $ tato_first_talk_done_stage = 3
    jump beachskip

default oil_lake_cavern_found_talk = False
label tato_second_talk_2:
    show tato default at right
    tt "Any foundation?"
    if oil_lake_cavern_found and not oil_lake_cavern_found_talk:
        show watta default at left
        w "I found this really massive oil pool underground close to the monument. Do you want to..."
        tt "Maybe, but our main aim here isn't to extract oil."
        show watta smile
        show tato close
        tt "It's about proving the forecast, seeing if what predicted is correct."
        show tato half
        tt "If you want me to help extracting them, I would love to but unfortunately we are lacking the tools."
        show watta sweat
        show tato default
        tt "We can't gather them with only some buckets can we?"
        $ oil_lake_cavern_found_talk = True
        jump beachskip
    else:
        show watta default at left
        w "No idea"
        jump beachskip