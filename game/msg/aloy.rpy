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
    al "It's finally the day, cant help that I was busy with businesses wahhaha."
    w "You do... own a lot of guns here"
    al "They are not for sale tho, I planned to move out of here soon to open the store somewhere else, this city is doomed"
    al "Well not until the festival is over at least"
    w "I see"
    al "For these final days, I want to do something else tho, I want to host a party, a farewell party, with all of our friends."
    w "A party huh?"
    al "I can totally invite them by messaging, but here is the thing"
    al "This festival is a rare chance for you Watta, it's not everyday you can talk to people freely like this,"
    al "I want you to make full use of the opportunity, talk to people and understand them before its too late"
    w "I can work with that"
    al "So this is what I'm going to do, I will give you these invitation letters, you will give people those letters directly"
    al "And invite them to the party."
    al "It will be hosted at my house at the time the festival takes place, so see you there"
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
    hide aloy
    jump dustwyndskip

