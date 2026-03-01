# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define unknown = Character("???", color="#000000", what_size=50, what_ypos = 15, what_xpos =340,)
define w = Character("Watta", what_font="fonts/Watta.ttf",who_font="fonts/Watta.ttf", size = 50, what_size=50, what_xpos =350, color="#fcba03", callback=watta_talk_callback)
define r = Character("Remi", what_font="fonts/Remi.ttf", who_font="fonts/Remi.ttf", size = 55, who_xpos = 10, who_ypos = 30, what_size=50, what_ypos = 15, what_xpos =350, color="#656565", callback=remi_talk_callback)
define sr = Character("Sari", what_font="fonts/Sari.ttf", who_font="fonts/Sari.ttf", size = 55, who_xpos = 20, who_ypos = 30, what_size=55, color="#1cb8c6", callback=sari_talk_callback)
define lan = Character("Flan", what_font="fonts/Lan.ttf", who_font="fonts/Lan.ttf", size = 55, who_xpos = 15, who_ypos = 29, what_size=47, what_ypos = 0, what_xpos =350, color="#583ddd")
define c = Character("Chii", what_font="fonts/Chiko.ttf", who_font="fonts/Chiko.ttf", size = 75, who_xpos = 10, who_ypos = 25, what_size=75, what_ypos = -5, what_xpos =350, color="#4dc31f")
define n = Character("Nemu", what_font="fonts/Nemu.ttf", who_font="fonts/Nemu.ttf", size = 55, who_xpos = 10, who_ypos = 25, what_size=55, what_ypos = 5, what_xpos =350, color="#8c8c8c", callback=nemu_talk_callback)
define ts = Character("Tsuyu", what_font="fonts/Tsuyu.ttf", who_font="fonts/Tsuyu.ttf", size = 48, who_xpos = 10, who_ypos = 20, what_size=45, what_ypos = -20, what_xpos =340, color="#ddba21")
define iog = Character("Iog", what_font="fonts/Iog.ttf", who_font="fonts/Iog.ttf", size = 45, who_xpos = 12, who_ypos = 25, color="#000000")
define john = Character("John", what_font="fonts/Iog.ttf", who_font="fonts/Terraria.ttf", size = 45, who_xpos = 12, who_ypos = 25, color="#000000")
define rn = Character("Renia", what_font="fonts/Reni.ttf", who_font="fonts/Reni.ttf", size = 48, who_xpos = 25, who_ypos = 24, what_size=55, what_ypos = -0, what_xpos =350, color="#f94886")
define nk = Character("Neko", what_font="fonts/Reni.ttf", who_font="fonts/Reni.ttf", size = 48, who_xpos = 25, who_ypos = 24, what_size=55, what_ypos = -0, what_xpos =350, color="#f49e4d")
define sc = Character("Sanco", what_font="fonts/Sanco.ttf", who_font="fonts/Sanco.ttf", size = 55, who_xpos = 10, who_ypos = 25, what_size=55, what_ypos = -11, what_xpos =350, color="#c6892d")
define tt = Character("Tato", what_font="fonts/Tato.ttf", who_font="fonts/Tato.ttf", size = 74, who_xpos = 25, who_ypos = 27, what_size=75, what_ypos = -0, what_xpos =350, color="#48ca37")
define kr = Character("Kuro", what_font="fonts/Kuro.ttf", who_font="fonts/Kuro.ttf", size = 65, who_xpos = 10, who_ypos = 25, what_size=65, what_ypos = -11, what_xpos =350, color="#c62d2d")
define wo = Character("Woogie", what_font="fonts/Woogie.ttf", who_font="fonts/Woogie.ttf", size = 45, who_xpos = -5, who_ypos = 25, what_size=45, what_ypos = 15, what_xpos =350, color="#2db4c6", callback=woogie_talk_callback)
define tk = Character("Toko", what_font="fonts/Toko.ttf", who_font="fonts/Toko.ttf", size =60, who_xpos = 13, who_ypos = 30, what_size=55, what_ypos = 10, what_xpos =380, color="#c7c757")
define i = Character("Iskra", what_font="fonts/Iskra.ttf", who_font="fonts/Iskra.ttf", size = 85, who_xpos = -5, who_ypos = 25, what_size=45, what_ypos = 15, what_xpos =380, color="#c770b8")
define b = Character("Bailey", what_font="fonts/Bailey.ttf", who_font="fonts/Bailey.ttf", size = 75, who_xpos = 0, who_ypos = 25, what_size=65, what_ypos = 10, what_xpos =350, color="#57bcc7")
define o = Character("Owl", what_font="fonts/Owl.ttf", who_font="fonts/Owl.ttf", size = 55, who_xpos = 15, who_ypos = 35, what_size=40, what_ypos = 25, what_xpos =355, color="#908c53")
define tkn = Character("Tsukino", what_font="fonts/Tsukino.ttf", who_font="fonts/Tsukino.ttf", size = 45, who_xpos = -10, who_ypos = 30, what_size=45, what_ypos = 10, what_xpos =350, color="#a75028")
define sn = Character("Snowie", what_font="fonts/Snowie.ttf", who_font="fonts/Snowie.ttf", size = 50, who_xpos = -10, who_ypos = 25, what_size=50, what_ypos = 15, what_xpos =340, color="#212d7b")
define vv = Character("Vivi", what_font="fonts/Vivi.ttf", who_font="fonts/Vivi.ttf", size = 65, who_xpos = 5, who_ypos = 35, what_size=50, what_ypos = 15, what_xpos =340, color="#23899d")
define al = Character("Aloy", what_font="fonts/Aloy.ttf", who_font="fonts/Aloy.ttf", size = 45, who_xpos = 10, who_ypos = 30, what_size=38, what_ypos = 15, what_xpos =340, color="#8a1313")
default inv_check = False
default current_location = "home"
default food_prepared = False
# The game starts here.
default persistent.horror_crash = False
label start:
    $ preferences.text_cps = 50
    if persistent.horror_crash:
        show screen horror_timer
    stop music fadeout 1.0
    pause 1.0
    w "Festival?"
    pause 0.5
    r "Yes, the festival of Sidurina."
    r "You moved in at the right time, it will start in just a week."
    r "Anyways"
    show screen phone_toggle
    scene bg intro1 with Fade(0.5,0,1.0)
    r "The festival is a pretty special event here to people of this land."
    r "As a celebration to the new nation's creation, most people will be more active and social than usual in preparation for it."
    r "Which is good for this seemingly quiet city..."
    r "7 days from now,"
    show screen console_toggle
    r "The blood of the queen will drop."
    r "The unruled land will come back to life."
    w "What are you talking about?"
    scene bg intro2 with Fade(1.0,0,1.0)
    r "Well it's not really that important..."
    r "I will be heading to your place tomorrow at around your working time,"
    r "Come greet me won't ya"
    w "Whatever."
    scene bg black with Fade(1.0,0,1.0)
    "...{w=0.5}{nw}"
    "The festival..."
    "After it's done, I likely won't have much chance to talk to my friends irl."
    "Gonna make it counts..."
    scene bg bedroom with Fade(1.0,0,1.0)
    show watta ahh at right
    w "*yawn*"
    play music "bgm_apartment.mp3" fadein 1.0
    show watta sleepy at right
    w "Another work day..."
    w "Should get myself prepared."
    w "And prolly visit some of my friends."

    window hide
    hide watta
    jump bedroomskip
label home:
    play music "bgm_apartment.mp3" fadein 1.0
    if home_from_outhome == True:
        jump mainhall
        $ home_from_outhome = False
    else:
        pass
label homeskip:
label bedroom:
    $ current_location = "bedroom"
    scene bg bedroom with Fade(0.1, 0, 0.1)
label bedroomskip:
    call screen bedroom

screen bedroom:
    imagebutton:
        xpos 0
        ypos 282
        auto "images/int/bed_%s.png"
        action Jump("bed")
    imagebutton:
        xpos 1175
        ypos 636
        auto "images/int/alarm_%s.png"
        action Jump("alarm")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("diningroom")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("workspace")
        
label diningroom:
    $ current_location = "diningroom"
    scene bg diningroom with Fade(0.1, 0, 0.1)
label diningroomskip:
    default knife_vis = 1
    call screen diningroom

screen diningroom:
    imagebutton:
        xpos 165
        ypos 91
        auto "images/int/wc_%s.png"
        action Jump("wc")
    imagebutton:
        xpos 605
        ypos 0
        auto "images/int/fridge_%s.png"
        action Jump("fridge")
    imagebutton:
        xpos 1185
        ypos 463
        auto "images/int/counter_%s.png"
        action Jump("counter")
    imagebutton:
        xpos 1521
        ypos 628
        auto "images/int/drawer_%s.png"
        action Jump("drawer")
    if knife_vis == 1:
        imagebutton:
            xpos 1844
            ypos 373
            auto "images/int/knife_%s.png"
            action Jump("knife")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("mainhall")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("bedroom")
label workspace:
    $ current_location = "workspace"
    scene bg workspace with Fade(0.1, 0, 0.1)
label workspaceskip:
    default sus_vis =1
    default phone_vis =1
    call screen workspace

screen workspace:
    imagebutton:
        xpos 52
        ypos 590
        auto "images/int/rocko_%s.png"
        action Jump("rocko")
    imagebutton:
        xpos 847
        ypos 362
        auto "images/int/pc_%s.png"
        action Jump("pc")
    imagebutton:
        xpos 534
        ypos 56
        auto "images/int/clock_%s.png"
        action Jump("clock")
    if sus_vis == 1:
        imagebutton:
            xpos 500
            ypos 170
            auto "images/int/sus_%s.png"
            action Jump("sus")
    if phone_vis == 1:
        imagebutton:
            xpos 934
            ypos 545
            auto "images/int/phone_%s.png"
            action Jump("phone")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("bedroom")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("mainhall")
label mainhall:
    $ current_location = "mainhall"
    scene bg mainhall with Fade(0.1, 0, 0.1)
label mainhallskip:
    call screen mainhall

screen mainhall:
    imagebutton:
        xpos 729
        ypos 192
        auto "images/int/out_%s.png"
        action Jump("out")
    imagebutton:
        xpos 1354
        ypos 372
        auto "images/int/pig_%s.png"
        action Jump("pig")
    imagebutton:
        xpos 27
        ypos 400
        auto "images/int/left_%s.png"
        action Jump("workspace")
    imagebutton:
        xpos 1752
        ypos 400
        auto "images/int/right_%s.png"
        action Jump("diningroom")

label bed:
    default bed=0
    if phases[phase] == "Midn":
        show watta sweat at right
        w "Well, time to sleep"
        $ action_done()
        hide watta
    elif first_work == True:
        if bed==0:
            show watta upset at right
            w "Maybe after work is done."
            $ bed += 1
            hide watta
            jump bedroomskip
        else:
            show watta upset at right
            w "Must resist..."
            hide watta
            jump bedroomskip
    else:
        show watta default at right
        w "I can finally sleep now, but do I really need to sleep?"
        menu:
            "Sleep til next phase":
                hide watta
                $next_phase()
                jump bedroom
            "Sleep til next day":
                show watta sweat at right
                w "Well, time to sleep"
                $ action_done()
                hide watta
                if phase == 0:
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                if phase == 1:
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                if phase == 2:
                    $ next_phase()
                    $ next_phase()
                    $ next_phase()
                if phase == 3:
                    $ next_phase()
                    $ next_phase()
            "Let's not be lazy":
                hide watta
                jump bedroomskip
label alarm:
    show watta sweat at right
    w "I always wake up way before the alarm goes off."
    hide watta
    jump bedroomskip
label pc:
    default pc=0
    if pc==0:
        show watta happy at right
        w "My PC..."
        w "I wish I had energy after work to play games..."
        $ pc += 1
        hide watta
    else:
        show watta sweat at right
        w "Someday..."
        hide watta
    jump workspaceskip
label rocko:
    show watta happy at right
    w "He's sleeping peacefully, I shouldn't bother him."
    hide watta
    jump workspaceskip
label clock:
    show watta sweat at right
    w "It's been dead for a while, fixing it isn't urgent."
    hide watta
    jump workspaceskip
label sus:
    "*Click*"
    show watta frown at right
    w "What just happened?"
    $ sus_vis = 0
    hide watta
    jump workspaceskip
label pig:
    if sol <3000:
        show watta sweat at right
        w "I need to save enough to get a new laptop before the end of the year."
        hide watta
    else: 
        show watta upset at right
        w "OMG I'm so rich I'm a billionaire now, who cares about pigs anymore"
        hide watta
    jump mainhallskip
default shower = 0
label fridge:
    default fridge = 0
    if shower == 0:
        show watta sweat at right
        w "I should take a bath before eating."
        hide watta
        jump diningroomskip
    elif shower >= 1 and fridge == 0:
        show watta deter at right
        w "Let's see, I'll eat for now..."
        $ fridge += 1
        hide watta
        $ item_add("Canned Breakfast")
        jump diningroomskip
    elif shower >= 1 and fridge == 1:
        if sari_first_talk_done_stage == 0:
            show watta frown at right
            w "Huh, what is this?"
            $ item_add("Sari's Sauce")
            show watta happy at right
            w "I forgot, he gifted me this a long time ago."
            $ fridge += 1
            hide watta
            jump diningroomskip
        elif sari_first_talk_done_stage == 1:
            show watta upset
            w "Here is it, your {i}beloved{/i} expired sauce"
            $ item_add("Sari's Sauce")
            $ fridge += 1
            hide watta
            jump diningroomskip
    elif shower >= 1 and fridge == 2 and not sari_food_bought:
        show watta upset at right
        w "I'm running out of food..."
        hide watta
        jump diningroomskip
    elif food_prepared:
        show watta smile at right
        w "I already bought food from Sari's for today."
        hide watta
        jump diningroomskip
    else:
        show watta upset at right
        w "I'm running out of food... {w=0.5} should go buy more from Sari's"
        hide watta
        jump diningroomskip
label wc:
    if shower == 0:
        show watta hype at right
        w "Alright, bath time!"
        hide watta
        scene bg bath loading with Fade(0.5,0.1,0.5)
        $ renpy.pause(2, hard=True)
        $ renpy.pause()  
        scene bg diningroom with Fade(0.5,0.1,0.5)
        show watta hype at right
        w "Ahh! So refreshing!"
        $ shower += 1
        show watta delighted
        w "I should go eat now."
        hide watta
        jump diningroomskip
    elif shower >= 6 and ate == False:
        "secret ending 1/5"
        return
    elif ate == True and first_work == False:
        show watta ahh at right
        w "Not good to bathe on a full stomach!"
        hide watta
        jump diningroomskip
    else:
        show watta deter at right
        w "Do I really need to take another bath?"
        menu:
            "I'm stinky":
                show watta ahh
                w "I still smell like sheep."
                hide watta
                scene bg bath loading with Fade(0.5,0.1,0.5)
                $ renpy.pause(2, hard=True)
                $ renpy.pause()  
                scene bg diningroom with Fade(0.5,0.1,0.5)
                show watta hype at right
                w "Refreshing!"
                $ shower += 1
                hide watta
                jump diningroomskip
            "Nah I'm good":
                show watta deter
                w "Eh, this smell is natural."
                hide watta
                jump diningroomskip
default ate=False
label counter:
    if ate==False:
        if fridge == 0:
            show watta sweat at right
            w "I should grab something to cook first."
            hide watta
            jump diningroomskip
        elif fridge == 1:
            show watta default at right
            w "Time to heat this up to eat!"
            hide watta
            label continueeating:
            scene bg black with Dissolve(2)
            $ renpy.pause(1, hard=True)
            scene bg diningroom with Dissolve(2)
            show watta delighted at right
            w "Yummy!"
            $ ate = True
            $ item_remove("Canned Breakfast")
            hide watta
            jump diningroomskip
        elif fridge == 2:
            show watta default at right
            w "Before heating this up..."
            w "Should I put the sauce in?"
            menu:
                "Sure":
                    show watta upset at right
                    w "This sucks, I can't open it at all."
                    hide watta
                    jump continueeating
                "Absolutely not":
                    show watta frown at right
                    w "Alright then."
                    hide watta
                    jump continueeating
    elif ate==True:
        show watta delighted at right
        w "Yummy!"
        hide watta
        jump diningroomskip
    
default drawerend = False
label drawer:
    if ate==False:
        show watta happy at right
        w "Just a drawer, nothing inside for now."
        $ drawerend = True
        hide watta
        jump diningroomskip
    elif ate==True and drawerend ==False:
        show watta happy at right
        w "Still just a drawer, it sadly doesn't magically create items."
        hide watta
        jump diningroomskip
    elif ate==True and drawerend ==True and charged ==False:
        show watta deter at right
        w "WHAT?"
        show watta upset
        w "The charger was here all along?"
        w "But it wasn't here before when I checked it-"
        show watta default
        w "Whatever"
        w "I can instantly charge my phone now."
        if phone_found:
            "You charged your phone"
            $ update_msg_phase("Sanco", "early", notify=True)
        $ charged = True
        $ update_msg_phase("Remi", "early")
        hide watta
        jump diningroomskip
    elif charged ==True:
        show watta sweat at right
        w "I might have short-term memory..."
        hide watta
        jump diningroomskip
default knife = 0
label knife:
    if knife == 0 and fridge >= 1 and ate == False:
        show watta sweat at right
        w "I don't need a knife, I can open this can on my own."
        $ knife += 1
        hide watta
        jump diningroomskip
    elif knife >= 0 and knife <= 2:
        show watta upset at right
        w "The hell do i need a knife for?"
        $ knife += 1
        hide watta
        jump diningroomskip
    elif knife >= 3 and knife <= 7:
        show watta upset at right
        w "No"
        $ knife += 1
        hide watta
        jump diningroomskip
    elif knife >= 8 and knife <= 16:
        show watta upset at right
        w "Nuh"
        $ knife += 1
        hide watta
        jump diningroomskip
    elif knife >= 17 and knife <= 18:
        show watta upset at right
        w "Alright fine!"
        hide watta
        $ item_add("Knife")
        $ knife_vis = 0
        jump diningroomskip
default outcheck = False
label out:
    if actions_locked == True:
        show watta upset at right
        w "It's midnight"
        hide watta
        jump mainhallskip
    else:
        if shower == 0:
            show watta upset at right
            w "I don't wanna go outside smelling stinky."
            hide watta
            jump mainhallskip
        elif ate==False:
            show watta upset at right
            w "I need to eat first."
            hide watta
            jump mainhallskip
        elif ate==True and outcheck == False and phone_found == False:
            show watta upset at right
            w "Can't forget my phone before going to work."
            hide watta
            jump mainhallskip
        elif ate==True and outcheck == False and phone_found == True:
            show watta happy at right
            w "Time to leave!"
            hide watta
            $ outcheck = True
            jump outhome
        else: 
            jump outhome
            return
default phone_found = False
label phone:
    $ update_msg_phase("Toko", "map")
    if not charged:
        show watta huh at right
        w "It's not turning on?"
        show watta upset
        w "Oh yeah I lost my charger, should be around here somewhere..."
        w "Gotta find it when I'm back, for now I'll borrow my co-worker's charger..."
        hide watta
        scene bg phone
        w "Hmm{w=0.5}.{w=0.5}.{w=0.5}."
        show bg phone mad
        w "...10 percent, too low to do anything."
        show bg workspace
    else: 
        show watta happy at right
        w "I can charge my phone!"
        w "Aaand instantly full."
        hide watta
    "You have acquired your phone"
    "You can toggle it by pressing Q or clicking on the icon on the top right."
    if charged:
        $ update_msg_phase("Sanco", "early", notify=True)
    $ phone_found = True
    $ phone_vis = 0
    jump workspaceskip


label home_midn:
    $ today = get_day(day)

    if today == "Mon":
        "You collapse onto your bed."
        $ next_phase()
    elif today == "Tue":
        "It feels uncomfortable..."
        $ next_phase()
    else:
        "It's always quiet at midnight."
        $ next_phase()

    return
