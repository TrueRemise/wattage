default player_hand = []
default dealer_hand = []
default game_phase = "idle"
default whose_turn = "player"
default player_stood = False
default dealer_stood = False
default win_in_a_row = 0
default max_bet = 50

default tries_before_costing_action = 3

init python:
    import random

    def depleting_bj_tries():
        global tries_before_costing_action
        if bet != 0:
            tries_before_costing_action -= 1
            if tries_before_costing_action <=0:
                tries_before_costing_action = 3
                action_done()
        else:
            pass

    # Draw a card (1–10)
    def draw_card():
        return random.randint(1, 10)


    # Sum the hand
    def hand_value(hand):
        return sum(hand)

    # Start a new round
    def start_round():
        global player_hand, dealer_hand, whose_turn, player_stood, dealer_stood, game_phase
        player_hand = [draw_card(), draw_card()]
        dealer_hand = [draw_card(), draw_card()]
        whose_turn = "player"
        player_stood = False
        dealer_stood = False
        game_phase = "player_turn"

    # Player hits
    def player_hit():
        global whose_turn, player_stood

        if whose_turn != "player" or player_stood:
            return
        player_hand.append(draw_card())
        renpy.play("sfx/card_swipe.mp3", channel="sound")

        if hand_value(player_hand) > 21:
            player_stood = True
        whose_turn = "dealer"

    # Player stands
    def player_stand():
        global whose_turn, player_stood
        player_stood = True
        whose_turn = "dealer"

    def dealer_draw_card(total):
        card = draw_card()

        # If total > 10, avoid drawing deadly cards
        if total > 10 and total <= 14:
            safe_cards = [1,2,3,4,5,6,7,8,9]
            return random.choice(safe_cards)
        elif total > 14 and total <17:
            safe_cards = [1,2,3,4,5,6]
            return random.choice(safe_cards)
        elif total >= 17 and total <19:
            safe_cards = [1,2,3,4]
            return random.choice(safe_cards)
        else:
            return card

    def dealer_hit_once():
        global whose_turn, dealer_stood
        if dealer_stood:
            return

        total = hand_value(dealer_hand)

        # Dealer stands on 17–21
        if total >= 19:
            dealer_stood = True
            whose_turn = "player"
            return
        # Otherwise, draw a card
        else:
            new_card = dealer_draw_card(total)
            dealer_hand.append(new_card)
            total = hand_value(dealer_hand)

        # If bust, mark stood
        if player_stood == True:
            dealer_hit_once()
        # Switch back to player if needed
        whose_turn = "player"


    # Dealer stands
    def dealer_stand():
        global dealer_stood, whose_turn
        dealer_stood = True
        whose_turn = "player"


transform slide_left_deck(xpos_final, ypos_final, duration=0.8):
    # Start off-screen, slightly below, rotated
    xpos -300
    ypos ypos_final - 300
    rotate 90
    xanchor 0.5
    yanchor 0.5
    parallel:
        ease_cubic duration xpos xpos_final ypos ypos_final rotate 0

transform slide_right_deck(xpos_final, ypos_final, duration=0.8):
    # Start off-screen, slightly below, rotated
    xpos 1800
    ypos ypos_final + 350
    rotate -90
    xanchor 0.5
    yanchor 0.5
    parallel:
        ease_cubic duration xpos xpos_final ypos ypos_final rotate 0


transform flip_card:
    ease_cubic 0.25 xzoom 0
    ease_cubic 0.25 xzoom 1

    
screen card_down(x=0.5, y=0.5):
    frame:
        background "misc/card_down.png"
        xsize 200
        ysize 280
        xpos x
        ypos y
        
screen blackjack_board():

    add "bg/bg bj.png"

    # ----------------------
    # Dealer cards
    # ----------------------
    for i, card in enumerate(dealer_hand):
        $ rank = 0 if i == 1 else (1 if i == 0 else i)
        $ final_x = 1384 - rank * 200
        $ final_y = 90

        if game_phase == "player_turn" and i == 1:
            add "misc/card_down.png" at slide_left_deck(final_x+71, final_y+130)
        elif i == 1 and game_phase == "dealer_turn":
            # Reveal the face-down card with flip
            add "misc/card_[card].png" at flip_card xpos final_x ypos final_y
        else:
            # All other cards slide from left normally
            add "misc/card_[card].png" at slide_left_deck(final_x+71, final_y+130)
            


    # ----------------------
    # Player cards
    # ----------------------
    for i, card in enumerate(player_hand):
        $ final_x = 513 + i*200
        $ final_y = 850
        add "misc/card_[card].png" at slide_right_deck(final_x, final_y)


    # ----------------------
    # Player buttons
    # ----------------------
    if game_phase == "player_turn" and whose_turn == "player" and not player_stood:
        $ player_total = hand_value(player_hand)
        $ dealer_total = hand_value(dealer_hand)

        if player_total > 21:
            $ player_stood = True  # end player's turn
            $ whose_turn = "dealer"
        else:
            vbox:
                spacing 50
                xalign 0.53
                yalign 0.5

                for name, function in [("HIT", Function(player_hit)), ("STAND", Function(player_stand))]:
                    button:
                        xsize 820
                        ysize 70
                        xalign 0
                        background Solid("#FFFFFF00")
                        hover_background Solid("#FFFFFF00")
                        action function

                        text name:
                            size 120
                            xalign 0.5
                            yalign 0.5
                            color "#ffffff"
                            hover_color "#BA5AC8"
                            outlines [(10, "#000000", 0, 0)]
                            font "BJ.ttf"

    # ----------------------
    # Score display
    # ----------------------
    frame:
        background "#ffffff00"
        xalign 0.27
        yalign 0.52
        xsize 400
        ysize 200

        vbox:
            xalign 0.5
            yalign 0.5
            $ player_total = hand_value(player_hand)
            text "[player_total]/21":
                size 130
                color "#FFFFFF"
                font "Bar.ttf"
                outlines [(6, "#000000", 0, 0)]
    frame:
        background "#22222200"
        xalign 0.77
        yalign 0.52
        xsize 400
        ysize 200
        vbox:
            xalign 0.5
            yalign 0.5
            if game_phase == "player_turn":
                $ dealer_total = hand_value(dealer_hand)
                text "??/21":
                    size 130
                    color "#FFFFFF"
                    font "Bar.ttf"
                    outlines [(6, "#000000", 0, 0)]
            else:
                $ dealer_total = hand_value(dealer_hand)
                text "[dealer_total]/21":
                    size 120
                    color "#FFFFFF"
                    font "Bar.ttf"
                    outlines [(6, "#000000", 0, 0)]
    frame:
        background Solid("#FFFFFF00")
        xalign 0.98
        yalign 0.95
        xsize 400
        ysize 200
        vbox:
            spacing 50
            xalign 0.9
            yalign 0.9
            button:
                xsize 170
                ysize 70
                xalign 0.9
                yalign 0.9
                background Solid("#FFFFFF00")
                hover_background Solid("#FFFFFF00")
                action [SetVariable("sol", max(0, sol - 20)), Jump("blackjack_bet")]
                text "Renew":
                    size 120
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#BA5AC8"
                    outlines [(10, "#000000", 0, 0)]
                    font "BJ.ttf"
            button:
                xsize 170
                ysize 70
                xalign 0.9
                yalign 0.9
                background Solid("#FFFFFF00")
                hover_background Solid("#FFFFFF00")
                action [SetVariable("sol", max(0, sol - 20)), Jump("blackjack_quit")]
                text "Quit":
                    size 120
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#BA5AC8"
                    outlines [(10, "#000000", 0, 0)]
                    font "BJ.ttf"

label blackjack_bet:
    $ bet = 10
    scene bg bj at whiten_lesser
    call screen bet_selector
    jump blackjack_start

label blackjack_start:
    if sol < 10:
        jump blackjack_broke  # leave before entering loop
    elif sol < bet:
        jump blackjack_broke_lesser
    $ loop_counter = 0 
    $ start_round()
    $ depleting_bj_tries()
    $ renpy.play("sfx/card_swipe.mp3", channel="sound")
    $ game_phase = "player_turn"
    hide screen blackjack_result
    hide screen blackjack_board
    show screen blackjack_board
    if hand_value(dealer_hand) >= 19:
        $ dealer_stood = True

    while True:# Check for busts
        $ loop_counter += 1

        if whose_turn == "dealer" and not dealer_stood:
            $ renpy.pause(0.5)  # small delay for animation
            $ renpy.play("sfx/card_swipe.mp3", channel="sound")
            $ dealer_hit_once()
            if hand_value(dealer_hand) >= 19:
                $ dealer_stood = True
        
        if whose_turn == "dealer" and hand_value(dealer_hand) >= 19:
            $ dealer_stood = True
            $ whose_turn = "player"
        #If dealer stood but player did not
        if whose_turn == "dealer" and dealer_stood:
            $ whose_turn = "player"
        # If both stood or bust, go to dealer resolution
        if player_stood and dealer_stood:
            jump dealer_turn

        $ renpy.pause(0.1)  # allow screen to update

label dealer_turn:
    $ game_phase = "dealer_turn"
    show screen blackjack_board

    # Calculate result
    $ p_total = hand_value(player_hand)
    $ d_total = hand_value(dealer_hand)
    $ renpy.play("sfx/card_flip.mp3", channel="sound")

    if (p_total > 21 and d_total <= 21) or (p_total < d_total and d_total <= 21):
        $ result_str = "lose"
        play sound "sfx/lose.mp3"
        $ sol -= bet
        $ win_in_a_row = 0
    elif (p_total <= 21 and d_total > 21) or (p_total > d_total and p_total <= 21):
        $ result_str = "win"
        play sound "sfx/win.mp3"
        $ sol += bet
        $ win_in_a_row += 1
    else:
        $ result_str = "tie"
        play sound "sfx/tie.mp3"
        $ win_in_a_row = 0

    show screen blackjack_result(result_str, sol)

    $ renpy.pause(9999)  # Wait until player uses buttons

screen blackjack_result(result, sol):
    modal True

    # Determine text + color (needs 'bet' to exist as a variable!)
    $ bet_text = ("+" + str(bet)) if result == "win" else ("-" + str(bet)) if result == "lose" else "0"
    $ tries_left_text = ("0") if bet == 0 else ("-1")
    $ bet_color = "#0F0" if result == "win" else "#F00" if result == "lose" else "#FFF"
    $ tries_left_color = "#FFF" if bet == 0 else "#F00"

    # Top-right SOL display
    frame:
        background "#0000"
        xalign 0.94
        yalign 0.0
        padding (20, 20)
        vbox:
            xalign 1.0
            text "[sol]":
                size 80
                color "#FFF"
                outlines [(4, "#000", 0, 0)]
                font "Bar.ttf"

            # Floating +bet / -bet effect
            text bet_text:
                size 80
                color bet_color
                outlines [(3, "#000", 0, 0)]
                font "Bar.ttf"
                at bet_float
    frame:
        background "#0000"
        xalign 0.0
        yalign 0.0
        padding (20, 20)
        vbox:
            xalign 1.0
            text "[tries_before_costing_action]":
                size 80
                color "#FFF"
                outlines [(4, "#000", 0, 0)]
                font "Bar.ttf"

            # Floating +bet / -bet effect
            text tries_left_text:
                size 80
                color tries_left_color
                outlines [(3, "#000", 0, 0)]
                font "Bar.ttf"
                at bet_float

    # Main center result icon
    frame:
        background "#0000"
        xalign 0.45
        yalign 0.35
        at fade_in

        if result == "win":
            add "misc/win.png"
        elif result == "lose":
            add "misc/lose.png"
        else:
            add "misc/tie.png"

    hbox:
        spacing 60
        xalign 0.4
        yalign 0.9

        $ button_list = [
            ("Play Again", Jump("blackjack_before_start")),
            ("To HUB", Jump("blackjack_quit"))
        ]

        for name, act in button_list:
            button:
                at hover_fade_lesser
                xsize 820
                ysize 70
                xalign 0
                background Solid("#FFFFFF00")
                hover_background Solid("#FFFFFF00")
                action act

                text name:
                    size 80
                    xalign 0.5
                    yalign 0.5
                    color "#ffffff"
                    hover_color "#BA5AC8"
                    outlines [(10, "#000000", 0, 0)]
                    font "Bar.ttf"


default rng_from_bj = False
label blackjack_quit:
    hide screen blackjack_result
    hide screen blackjack_board
    $ rng_from_bj = True
    show screen action_display
    jump rng

screen bet_selector():
    modal True 
    frame:
        background "#0000"
        xalign 0.94
        yalign 0.0
        padding (20, 20)
        vbox:
            xalign 1.0
            text "[sol]":
                size 80
                color "#FFF"
                outlines [(4, "#000", 0, 0)]
                font "Bar.ttf"
    frame:
        xalign 0.5
        yalign 0.5
        background Solid("#00000000")
        vbox:
            xalign 0.5
            yalign 0.4
            
            add "gui/lan_bet.png":
                xalign 0.5
                yalign 0.3
        vbox:
            xalign 0.5
            yalign 0.58
            text "Place Bet Amount":
                xalign 0.5
                yalign 0.5
                font "BJ.ttf"       # ← your custom font
                size 140
                color "#ffffff"
            

            hbox:
                spacing 50
                xalign 0.5
                button:
                    xsize 40
                    ysize 40
                    xalign 0.9
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#ffffff00")
                    action [Play("sound", "sfx/bet_select.mp3"), SetVariable("bet", max(0, bet - 100))]
                    text "-":
                        size 140
                        xalign 0.5
                        yalign 0.7
                        color "#ffffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"
                null width -100
                button:
                    xsize 120
                    ysize 120
                    xalign 0.5
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), SetVariable("bet", max(0, bet - 10))]
                    text "-":
                        size 280
                        xalign 0.5
                        yalign 0.7
                        color "#ffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"

                text "[bet]":
                    font "BJ.ttf"     # ← your number font
                    size 200
                    color "#ffffff"

                button:
                    xsize 120
                    ysize 120
                    xalign 0.5
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#FFFFFF00")
                    action If(bet + 10 > 50,
                        [Play("sound", "sfx/bet_denied.mp3"), Function(renpy.notify, f"Max bet is {max_bet} for now!"), SetVariable("bet", max_bet)],
                        [Play("sound", "sfx/bet_select.mp3"), SetVariable("bet", bet + 10)]
                    )
                    text "+":
                        size 280
                        xalign 0.5
                        yalign 0.7
                        color "#ffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"
                
                null width -100
                button:
                    xsize 40
                    ysize 40
                    xalign 0.9
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#FFFFFF00")
                    action If(bet + 100 > 50,
                        [Play("sound", "sfx/bet_denied.mp3"), Function(renpy.notify, f"Max bet is {max_bet} for now!"), SetVariable("bet", max_bet)],
                        [Play("sound", "sfx/bet_select.mp3"), SetVariable("bet", bet + 100)]
                    )
                    text "+":
                        size 140
                        xalign 0.5
                        yalign 0.7
                        color "#ffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"
            null height 20
            hbox:
                spacing 150
                xalign 0.5

                button:
                    xsize 160
                    ysize 60
                    xalign 0.5
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), Jump("blackjack_start")]
                    text "Confirm":
                        size 80
                        xalign 0.5
                        yalign 0.5
                        color "#ffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"

                button:
                    xsize 160
                    ysize 60
                    xalign 0.5
                    yalign 0.5
                    background Solid("#ffffff00")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), Jump("blackjack_quit")]
                    text "Cancel":
                        size 80
                        xalign 0.5
                        yalign 0.5
                        color "#ffffff"
                        hover_color "#ff19fb"
                        outlines [(2, "#000000", 0, 0)]  # thickness, color, x-offset, y-offset
                        font "BJ.ttf"
transform bet_float:
    alpha 1.0
    yoffset -20
    linear 1.0 alpha 0 yoffset 40
 
label blackjack_broke:
    hide screen blackjack_result
    lan "mf who let you play again GET OUT!!!"
    hide screen blackjack_board
    jump centre
    
label blackjack_broke_lesser:
    hide screen blackjack_result
    lan "You have less cash than your bet now"
    lan "Place a different bet"
    hide screen blackjack_board
    jump blackjack_bet

label blackjack_before_start:
    hide screen blackjack_result
    hide screen blackjack_board
    show bg bj
    if win_in_a_row == 3:
        show flan smirk at slide_in_right
        lan "Damn!"
        lan "Three times in a row..."
        lan "Either you're lucky or you have SOME talent"
        show flan close
        lan "Regardless, keep up the works."
        hide flan
        jump blackjack_start
    if win_in_a_row == 5:
        show flan huh at slide_in_right
        lan "5 times in a row?"
        lan "That's lucky."
        lan "and rare..."
        if max_bet == 50:
            show flan malicious
            lan "Either way, as a reward for your luck and effort, I raised the max bet to 100 sol, hope you will have fun."
            hide flan
            $max_bet = 100
        jump blackjack_start
    if win_in_a_row == 10:
        show flan mad at slide_in_right
        lan "Are you..."
        extend "cheating?"
        lan "That luck is not real..."
        lan "It's "
        extend "0.0000005%%"
        lan "I hope we are {w=0.5}having a fair game here..."
        jump blackjack_start
    jump blackjack_start