default aloy_first_talk_done_stage = 0
default aloy_about_remi = False

label aloy_test:
    if the_knower == 2 and not aloy_about_remi:
        $ option_add("aloy", "Remi", "aloy_about_remi", pos=0)
    if aloy_first_talk_done_stage == 0:
        jump aloy_first_talk
    elif aloy_first_talk_done_stage == 1:
        jump aloy_second_talk

label aloy_first_talk:
    $ cutscene_on = True
    show bg dustwynd at whiten
    show aloy default at left
    show watta default at right
    al "Yo Watta my brotherman welcome"
    show aloy noy
    al "The day finally arrived, although it coulda been earlier if it wasn't due to my business Wahaha!."
    show watta deter
    w "You sure do own a lot of guns..."
    show watta sweat
    show aloy deter
    al "They are not for sale tho, I plan to move out of here soon to open the store somewhere else. This city is doomed"
    show watta smile
    al "But I think i'll at least see the festival through first."
    w "I see"
    al "For these final days tho, I want to do something else." 
    show aloy close
    show watta delighted
    extent "I want to host a party, a farewell party, with all of our friends."
    w "A party huh?"
    show aloy default
    al "I can totally invite them via texts but here's the thing"
    show watta default
    show aloy speak
    al "This festival is a rare chance for you Watta, it's not everyday you can talk to people freely like this,"
    al "I want you to make full use of this opportunity, talk to people and bond with them before it's too late"
    show watta smile
    w "I can work with that"
    show aloy default
    al "So this is what I'm going to do, I will give you these invitations. You will then directly hand them to people."
    al "Make sure to verbally invite them as well."
    show aloy close
    al "It will be hosted at my house at around the time the festival takes place, so see you there!"
    show watta delighted
    w "See you soon!"
    $ aloy_first_talk_done_stage = 1
    $ cutscene_on = False
    hide watta
    hide aloy
    jump dustwynd

label aloy_second_talk:
    show bg dustwynd
    show aloy default
    al "Also say hello to people for me"
    w "Aight"
    show aloy noy
    al "Thanks, Wahahaha!"
    hide aloy
    jump dustwyndskip

