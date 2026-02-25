# File: game/systems/remi.rpy
default chii_settled = False
default chii_first_talk_done_stage = 0

label chii_intro:
    $ cutscene_on = True
    stop music fadeout 0.5
    play music "bgm_chiko1.mp3" fadein 1.0
    scene bg chiko1 with Fade(0.5, 0, 1.0)
    $ renpy.pause(1.0, hard=True)
    w "So this is the centre area of the city"
    w "Despite the advancement, it still needs a great barrier... Which I guess serves no purpose now"
    w "Still... they won't take it down"
    w "I do wonder, what threatened it...?"
    if not day == 1:
        $ chii_settled = True
        jump centre_day_2_skip
    scene bg chiko2 with Fade(0.5, 0, 0.5)
    $ renpy.pause(1.0, hard=True)
    w "Argh...!"
    w "{i}the winds here are super strong!"
    show bg chiko3 at shake
    "!!!"
    "*fwoomp*"
    stop music fadeout 1.5
    unknown "{size=33}h{w=0.2}e{w=0.2}l{w=0.2}p"
    w "Huh???"
    show bg chiko4 at shake
    unknown "{size=34}h{w=0.2}e{w=0.2}l{w=0.2}p"
    show watta wtf at slide_in_right
    w "{size=60}HOLD ON!! I'M RIGHT HERE!!!"
    hide watta
    show bg chiko5 at shake
    $ renpy.pause(0.3, hard=True)
    show bg chiko5 at shake
    $ renpy.pause(1.0, hard=True)
    show bg chiko5 at shake
    $ renpy.pause(1.0, hard=True)
    show bg chiko5 at shake
    $ renpy.pause(1.0, hard=True)
    show bg chiko6 at shaker
    $ renpy.pause(1.0, hard=True)
    scene bg chiko7 with Fade(0.5, 0, 0.5)
    c "Thank god..."
    play music "bgm_chiko2.mp3" fadein 2.5
#SWITCH
    show screen action_display
    scene bg centrepath with Fade(1, 0, 1)
    show bg centrepath at whiten
    show chii cry at right
    show watta sweat at left
    pause 0.3
    show chii cry at bounce
    c "I thought i'd be stuck down there for ages..."
    show chii default
    show watta delighted
    c "Well thanks for your help... uh..."
    w "Watta"
    show chii smile
    c "Thanks for your help, Watta!"
    show chii default
    c "Call me Chii, I was trying to move into the centre before all my luggage tumbled onto me."
    show chii pout
    show watta sweat
    c "These roads are NOT stable at all"
    show chii default
    show watta default
    c "Uh, do you mind helping me one more time? We can talk more once we arrive at my shop."
    show watta deter
    w "S-sure... (That's a lot of luggage...)"
    scene bg centrel with Fade(0.5, 0, 0.5)
    scene bg centrel at whiten
    show chii default at right
    show watta sweat at left
    pause 0.3
    show chii default at bounce
    c "Here we are! Just give me a moment to unpack a bit..."
    show chii smile
    c "Oh and one last thing!"
    show watta default at bounced
    w "Ye?"
    c "I'm opening a shop here as well! I'll be selling some stuff that will hopefully help people"
    c "One girl's trash is another's treasure, yknow?"
    c "Hope you swing around at some point!"
    show watta delighted
    w "Oh yes of course!"
    show chii wink at bounced
    c "Glad to hear!"
    label centre_day_2_skip:
    show screen action_display
    $ chii_settled = True
    $ centre_first = True
    $ cutscene_on = False
    jump centre

image chii_mouth_talk:
    "char_int/chii_mouth.png"
    pause 0.20
    "char_int/chii_mouth2.png"
    pause 0.20
    repeat

image mouth_rest = "chii_mouth"
image chii_shop:
    Composite(
        (749, 1241),
        (340, 365), "chii_mouth_talk",
    )

default chii_reset = True
default chii_neko_bracelet_repeat = False
default chii_meet_sanco_timer = 4
default chii_go_to_lake_timer = 0
label chii_test:
    $ actions_locked = True
    if is_unlocked("lake") and chii_go_to_lake_timer < 2:
        $ chii_go_to_lake_timer = 1
        jump chii_go_to_lake_talk
    if chii_first_talk_done_stage == 0:
        jump chii_first_talk
    elif chii_meet_sanco_timer == 5 and chii_after_sanco_talk_done == False:
        jump chii_after_sanco_talk
    elif is_item_get("Neko's Bracelet") and not chii_neko_bracelet_repeat:
        jump chii_neko_bracelet
    elif chii_first_talk_done_stage == 1 and chii_reset == True:
        stop music fadeout 0.5
        play music "bgm_floral.mp3" fadein 1.0 volume 0.5
        jump chii_second_talk
    else:
        stop music fadeout 0.5
        play music "bgm_floral.mp3" fadein 1.0 volume 0.5
        call screen shop_screen


label chii_first_talk:
    scene bg floral respitel
    stop music fadeout 0.5
    play music "bgm_chiko2.mp3" fadein 1.0
    show chii happy at right
    show watta smile at left
    if not day == 1:
        jump chii_day_2_skip
    pause 0.3
    show chii happy at bounce
    c "Thank you again Watta, I don't think I could have carried all that alone"
    show watta sweat
    w "No problem..."
    show chii default
    c "Here, take this as a gift"
    show watta deter at bounced
    w "Hmm!?"
    show chii sweat
    c "It's nothing special really, just a rock I had with me for a long time."
    c "I was about to sell anyways so... You can take it!"
    w "Wao! Thank you for t-"
    stop music
    show bg floral respitel at shaker
    show watta shocked at shake
    show chii what at shake
    pause 2.0
    show chii what at bounce
    c "Watta, what's wrong?"
    play music "bgm_lighthouse.mp3" fadein 1.0
    c "Wait, the rock-"
    show watta frown
    c "It {w=0.5}glows?"
    hide screen action_display
    scene bg stone with Fade(0.5, 0, 0.5)
    pause 0.5
    w "This thing... "
    extend "reacts to me???"
    w "I can feel a lot of energy from it,"
    extend " almost like"
    w "it's flowing into me..."
    c "Interesting... {w=0.5}I've never seen it do that before"
    c "I can even feel its energy from here."
    w "I'm not sure but... I think..."
    w "I think it's trying to grant me something?"
    stop music fadeout 0.5
    show screen stone_aquired()
    $ renpy.pause(11, hard=True)

    $ stone_add()
    
    hide screen task_aquired
    $ key_item_add("Twisted Stone","Mystery stone found across Spiralia, having them in my bag boosts my energy for some reasons.", "twisted stone")
    $ key_items_add("Twisted Stone")
    c "Wait really? How can you tell?"
    show screen action_display
    play music "bgm_floral.mp3" fadein 1.0 volume 0.5
    scene bg floral respitel with Fade(0.2, 0, 0.2)
    show chii what at right
    show watta huh at left
    c "Do you feel any different Watta?"
    w "I don't know, it's like-"
    w "Everything feels a bit {w=0.2}slower-"
    show watta default
    w "Maybe it's nothing but-"
    w "I feel pretty awake now"
    show chii wink at bounced
    c "Well... that's a good thing regardless!"
    c "Keep it, it seems to be in better hands with you"
    c "But let me know if anything else happens! {nw}{size=*.5}Kinda jealous it didn't do that for me too{/size}"
    show watta happy
    w "Sure do, thanks for the gift, but may I ask..."
    show watta sweat
    w "Where did you get this rock from?"
    show chii what
    c "Huh? I don't really know its origins."
    c "It was one of my mom's artifacts from long ago, I never knew what it did."
    c "When she passed it on to me I figured I should give it to someone who could use it instead of letting dust gather."
    show chii wink at bounce
    c "And guess I gave it to the correct person!"
    w "Strange..."
    c "Well I do sell many others artifacts here if you wanna check out, mixed in some random stuffs as well"
    c "They're not cursed or deadly, at worst they do nothing. But who knows, maybe another will resonate with you?"
    show chii smile at bounce
    c "I'll put them upfront for you to look at!"
    $ shop_item_remove("Twisted Stone")
    hide watta
    hide chii
    scene bg floral respite with Fade(0.2, 0, 0.2)
    $ chii_first_talk_done_stage = 1
    $ chii_settled = True
    call screen shop_screen
    jump centre

label chii_talk:
    show chii_shop
    c "What's up Watta!"
    hide chii_shop
    hide screen shop_confirm_screen
    hide screen shop_not_enough_screen
    call screen shop_chat_screen
    jump centre

label chii_byebye:
    if chii_reset == True:
        hide screen shop_confirm_screen
        hide screen shop_not_enough_screen
        show chii_shop
        c "Hope to see you again soon!"
        hide chii_shop
        $ chii_reset = False
        $ actions_locked = False
        jump centre
    else:
        hide screen shop_confirm_screen
        hide screen shop_not_enough_screen
        $ actions_locked = False
        jump centre

label chii_second_talk:
    if chii_reset == True:
        show chii_shop
        c "Welcome back! Lookin' for something?"
        hide chii_shop
    else:  
        pass
    call screen shop_screen

default shop_chat_options = {                                                               #THIS IS THE OPTION PANEL
    "Home": "chii_talk1",
    "Grass": "chii_talk2",
    "Garland": "chii_talk3",
    "Back": "chii_skip_to_shop_screen",
    "Flirt": "chii_talk4",
}
transform hover_sway:
    on hover:
        easein_cubic 0.30 xoffset 12
        pause 2
        easeout_cubic 5 xoffset 0
        repeat
    on idle:
        linear 0.15 xoffset 0
screen shop_chat_screen():
    tag shop_sub
    modal True
    zorder 95

    # Outer horizontal box for left/right columns
    hbox:
        xalign 0.99
        yalign 0.99
        spacing 90

        # --- LEFT COLUMN ---
        vbox:
            spacing 15
            xalign 0.0
            # first 3 options
            $ left_options = list(shop_chat_options.items())[:4]
            for i, (name, target_label) in enumerate(left_options):
                $ t = min(1.0, i * 0.3)
                $ hover_color = lerp_color("#ff0000", "#3cff00", t)
                button:
                    at hover_sway
                    xsize 180
                    ysize 85
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)
                    text name:
                        size 90
                        xalign 0
                        yalign 0.5
                        color "#000000"
                        hover_color hover_color
                        outlines [(2, "#000000", 0, 0)]
                        font "Shop.ttf"

        # --- RIGHT COLUMN ---
        vbox:
            spacing 10
            xalign 1.0
            # remaining options
            $ right_options = list(shop_chat_options.items())[4:]
            for i, (name, target_label) in enumerate(right_options):
                $ t = min(1.0, i * 0.3)
                $ hover_color = lerp_color("#ff0000", "#3cff00", t)
                button:
                    at hover_sway
                    xsize 180
                    ysize 85
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action Jump(target_label)
                    text name:
                        size 90
                        xalign 0
                        yalign 0.5
                        color "#000000"
                        hover_color hover_color
                        outlines [(2, "#000000", 0, 0)]
                        font "Shop.ttf"

default chii_talked_about_bloomfield = False
label chii_talk1:
    show chii_shop
    c "Huh, where did it come from?"
    c "Ever heard of Bloomfield? You know, the indoor town with artificial lighting?"
    c "Yeah, that place. Probably the best place to grow plants."
    c "But that's the issue, EVERYONE and their grandmas grow plants"
    c "So making any real money there is difficult, not to mention no one's interessted in some random dinky artifacts given to a girl as heirlooms"
    c "Came over here in hopes of both making money and finding an owner for all these silly trinkets, especially given those in my family forgot what most even do."
    c "Who knows why some are useless now, maybe we're not worthy? Well whatever the case, i'm hoping people like you get a better use outta 'em!"
    $ chii_talked_about_bloomfield = True
    hide chii_shop
    jump chii_talk_skip
label chii_talk2:
    show chii_shop
    c "Huh? You want to nibble my hair?"
    c "Look I know it seems like grass but it is NOT for grazing! If you want grass maybe a visit to Bloomfield might do ya good!"
    c "Then again, I dunno if the people there would be happy about a sheep running wild in there"
    c "..."
    c "Stop staring at my ahoge! I don't care if it smells minty, it's not food!"
    hide chii_shop
    jump chii_talk_skip
label chii_talk3:
    show chii_shop
    c "My garland? Believe it or not but it's also an artifact!"
    c "It used to be all wilted, but once my mom gave it to me the flowers bloomed back to life and have stayed that way!"
    c "All I have to do is get enough sunlight, keeps me and the flowers healthy."
    c "If the garland stays healthy then supposively I should have better luck in life"
    c "Now whether or not that's true, I dunno. But hey, I stumbled upon you in my time of need AND one of my artifacts immediately worked."
    c "So despite everything I'd say this garland is pretty lucky."
    c "..."
    c "No! You can't eat it!"
    hide chii_shop
    jump chii_talk_skip
label chii_talk4:
    show chii_shop
    c "What about my eyes and the sky?"
    c "Don'tcha think that's a pretty generic compliment? My eyes are blue yeah, but i've heard that phrase so many times at this point"
    c "If anything, seeing you stumble your words did a way better job than the actual sentence"
    c "Maybe if you keep that up i'll actually fall for you"
    c "You can try your hand at flirting again if you want though, nothing wrong with getting more practice in~"
    hide chii_shop
    jump chii_talk_skip
label chii_about_sanco:
    show chii_shop
    if not chii_meet_sanco_timer == 5:
        if not chii_meet_sanco_timer == 3:
            c "Eh? Someone want to meet little ol' me?"
            c "Sa- what?"
            c "A SOULBEARER?"
            c "This is something... I-i never expected this..."
            c "No... no need for her contact number"
            c "I'll meet her in person."
            c "Be quick with your purchases, I gotta go ASAP! Let em know i'm coming over will ya?"
        c "If you want to buy anything, do it now. I'll be gone pretty soon!"
        $ chii_meet_sanco_timer = 3
    else:
        c "Oh! We had a pretty fun meeting!"
        c "Soulbearer Sanco is a super kind person, meeting someone like her is very rare. I enjoyed all the interactions we had."
        c "We even made a lot of stuff together..."
        c "In fact, I'm selling one of those things right now! Please buy it, hehe~"
    hide chii_shop
    jump chii_talk_skip
label chii_skip_to_shop_screen:
    call screen shop_screen
label chii_talk_skip:
    call screen shop_chat_screen

default chii_after_sanco_talk_done = False
label chii_after_sanco_talk:
    scene bg floral respitel at whiten
    stop music fadeout 0.5
    play music "bgm_chiko2.mp3" fadein 1.0
    show chii happy at right
    show watta smile at left
    pause 0.3
    show chii happy at bounce
    c "Thank you for telling Sanco about me Watta."
    show chii default
    c "It was... quite a pleasant meeting"
    show chii cry3
    c "It's shocking she found me interesting at all."
    show chii sweat
    c "The real reason I moved out is... well... money is still part of it but-"
    show watta default
    show chii happy
    c "I mainly wanted to introduce more of the Bloomfield's artifacts to the world."
    show chii smile
    c "Each one has its own charm don'tcha think?"
    show watta frown
    show chii frown
    c "Ever since those unfortunate events happened, Bloomfield has seen much less attention..."
    c "So much so that now outsiders don't even know these kinds of artifacts exist!"
    show chii happy
    c "Which reminds me!"
    show watta deter
    w "Huh?"
    show chii smile at bounce
    c "Sanco and I made this flower charm together, you can have it!"
    show watta sweat
    show chii tease
    c "Well... after you buy it, I don't want Sanco's efforts to be given out freely, hehe~"
    show watta smile
    show chii happy
    c "But with it, you'll have the aura of a true Bloomfield resident."
    c "It'll be sold only to you, so do buy it when ya can, alright?"
    show watta happy at bounced
    w "Will do!"
    hide watta
    hide chii
    scene bg floral respite with Fade(0.2, 0, 0.2)
    play music "bgm_floral.mp3" fadein 1.0 volume 0.5
    $shop_item_add("Flower Charm", "250", "An artifact Sanco and I made together! Not really an artifact but moreso a combination of every essence that makes someone a true Bloomfield resident. Having it would help you blend in and even convince people that you are an actual Bloomfieldian... But if you'd rather not be roleplaying as us, It won't be hurt if you take them off so don't worry!.", "charm")
    $ chii_after_sanco_talk_done = True
    call screen shop_screen


label chii_day_2_skip:
    pause 0.3
    show chii happy at bounce
    c "Greeting customer, welcome to my shop!"
    w "Wao... what do you sell?"
    show chii default
    c "This is an artifact store, mainly sell mysterious artifacts made and found in Bloomfield"
    c "Trust me, all of them are worth your money!"
    show watta happy at bounced
    w "Nice!"
    c "Oh! Before buying anything, can I get your name first?"
    w "Watta, it's Watta"
    c "Oh okay, nice to meetcha Watta."
    c "So.."
    c "Here are today's deals."
    hide watta
    hide chii
    scene bg floral respite with Fade(0.2, 0, 0.2)
    play music "bgm_floral.mp3" fadein 1.0 volume 0.5
    $ chii_first_talk_done_stage = 1
    $ chii_settled = True
    call screen shop_screen
    jump centre
    
label chii_neko_bracelet:
    stop music fadeout 0.5
    play music "bgm_floral.mp3" fadein 1.0 volume 0.5
    show chii_shop
    c "Wait is that..."
    c "Is that Neko's bracelet?"
    c "THE NEKO???"
    c "Oh my god I LOVE her performances!"
    c "She performed in Bloomfield multiple times before and i'd say she's a FANTASTIC singer."
    c "Hell I even have a nice collecton of Neko merch and figurines at home! But not anything directly USED by her!"
    c "But... sadly as a merchant I can't take this."
    c "It's not an artifact, so I can't get much use out of it. I'm also not really in any position to spend..."
    c "So unless you want give it to me for free..."
    c "No? Figures, worth a shot at least. I recommend you show it off to Flan, she's likely to buy it at a good price."
    c "Just leave my store and walk straight across to her before I end up splurging on it myself."
    $ chii_neko_bracelet_repeat = True
    hide chii_shop
    call screen shop_screen


label chii_go_to_lake_talk:
    play music "bgm_floral.mp3" fadein 1.0 volume 0.5 if_changed
    show bg floral respitel at whiten_lesser
    show watta default at left
    show chii happy at right
    c "Welcome back Watta!"
    show chii what
    c "WHAT!?"
    c "You removed the binding on Swan Lake?"
    show chii cry
    c "Oh my god! I used to visit that area a lot as a kid."
    show chii cry2
    c "There used to be a HUGE amusement park there but I recall it got brought down for whatever reason."
    show chii smile
    c "I also remember seeing a TON of exotic flora I have yet to see anywhere else!"
    c "And now with it unlocked, it might be the perfect time for me to go visit!"
    show chii sweat
    c "Don't get me wrong... It's probably illegal to go there but-"
    c "You know its already unlocked and you're not in jail or hurt..."
    show chii tease
    extend "...So yeah just a quick trip and back should be fine!"
    show chii wink
    c "Alright, like last time buy everything you can before I go. I'll be here a little longer as i prepare."
    $ chii_go_to_lake_timer = 2
    hide chii
    hide watta
    scene bg floral respite with Fade(0.2, 0, 0.2)
    call screen shop_screen