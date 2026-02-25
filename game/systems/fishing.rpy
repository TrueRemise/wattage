# ====================================================
# FISHING SYSTEM CORE — Rod Stats, Rarity, Upgrading
# ====================================================

default rod = {
    "size": 0,        # Width of player bar
    "luck": 0,         # Affects rare fish chance
    "resilience": 0,    # Reduces fish toughness
    "maxweight": 0     # Weight limit for fish
}
default rarity_names = {
    1: "Common",
    2: "Insane",
    3: "Extreme",
    4: "Grandpa"
}

default manhake_attempt_counter = 0
# ====================================================
#   RARITY CHANCES (BASE)
# ====================================================
# Total = 100, but luck modifies the higher tiers.
#
# COMMON:     70%
# RARE:       20%
# EPIC:       8%
# LEGENDARY:  2%
# ====================================================

init python:
    def notify_rarity_simple(rarity_prob, chosen_rarity):
        """Show a simple rarity table: C/R/E/L and the picked rarity."""

        # Convert probability → percentage numbers
        c = round(rarity_prob[1] * 100)
        r = round(rarity_prob[2] * 100)
        e = round(rarity_prob[3] * 100)
        l = round(rarity_prob[4] * 100)

        rarity_name = {
            1: "COMMON",
            2: "RARE",
            3: "EPIC",
            4: "LEGENDARY",
        }[chosen_rarity]

        # One-line compact popup
        renpy.notify(f"{c}/{r}/{e}/{l}  →  {rarity_name}")

    def _lerp(a, b, t):
        return a + (b - a) * t

    def get_rarity_chances():

        # read luck and clamp
        luck = rod.get("luck", 0)
        luck = max(0, min(250, luck))

        # Anchor points (luck_value : [common, rare, epic, legendary])
        anchors = [
            (0,    [80, 20, 0, 0]),
            (60,   [40, 45, 13, 2]),
            (100,  [15, 45, 35, 5]),
            (175,  [8, 17, 55, 20]),
            (250,  [3, 6, 25, 66])
        ]

        # Find which two anchors the current luck lies between
        low = anchors[0]
        high = anchors[-1]
        for i in range(len(anchors)-1):
            if anchors[i][0] <= luck <= anchors[i+1][0]:
                low = anchors[i]
                high = anchors[i+1]
                break

        low_val, low_vec = low
        high_val, high_vec = high

        # interpolation factor between low and high
        span = (high_val - low_val)
        t = 0.0 if span == 0 else (luck - low_val) / float(span)

        # interpolate each component
        interp = [
            _lerp(low_vec[i], high_vec[i], t)
            for i in range(4)
        ]

        # safety clamps (no negatives)
        interp = [max(0.0001, x) for x in interp]

        # normalize to probabilities
        total = sum(interp)
        probs = [x / total for x in interp]

        return {
            1: probs[0],   # common
            2: probs[1],   # rare
            3: probs[2],   # epic
            4: probs[3],   # legendary
        }



    # ====================================================
    # PICK A RANDOM FISH
    # ====================================================
    import random

    def _pick_weighted_fish(candidates):
        """Weighted fish pick to reduce streaks within the same rarity tier."""
        if not candidates:
            return None

        total_weight = 0.0
        weighted_candidates = []

        for fish in candidates:
            caught_count = fish_catch_counts.get(fish["name"], 0)
            # Lower chance for fish that have already been caught many times.
            # sqrt keeps this soft so randomness is still present.
            catch_balance_weight = 1.0 / ((caught_count + 1) ** 0.5)
            weighted_candidates.append((fish, catch_balance_weight))
            total_weight += catch_balance_weight

        roll = random.random() * total_weight
        cumulative = 0.0
        for fish, weight in weighted_candidates:
            cumulative += weight
            if roll <= cumulative:
                return fish

        return weighted_candidates[-1][0]

    def pick_fish():
        global manhake_attempt_counter

        rarity_prob = get_rarity_chances()

        # --- FIX: Normalize again (avoid rounding drift problems) ---
        total = sum(rarity_prob.values())
        normalized = {k: v / total for k, v in rarity_prob.items()}

        # Random roll
        r = random.random()
        cumulative = 0.0
        chosen_rarity = 1

        for rarity in [1, 2, 3, 4]:
            cumulative += normalized[rarity]
            if r <= cumulative:
                chosen_rarity = rarity
                break

        # 🔥 new notify
        notify_rarity_simple(rarity_prob, chosen_rarity)

        # Get fish that match rarity AND rod can lift
        candidates = [
            f for f in fish_list
            if f["rarity"] == chosen_rarity and f["weight"] <= (rod["maxweight"]+20)
        ]
        
        # Soft pity for ManHake after Nemu's third talk.
        if nemu_third_talk_done and not nemu_manhake:
            manhake_attempt_counter += 1

            manhake_fish = next((f for f in fish_list if f["name"] == "ManHake"), None)
            if manhake_fish and manhake_fish["weight"] <= (rod["maxweight"] + 20):
                # Hard guarantee at 20 attempts.
                if manhake_attempt_counter >= 5:
                    manhake_attempt_counter = 0
                    notify_rarity_simple(rarity_prob, manhake_fish["rarity"])
                    return manhake_fish

                # Soft pity: increasing chance from attempt 8 onward.
                if chosen_rarity == 2 and manhake_fish in candidates and manhake_attempt_counter >= 3:
                    pity_progress = (manhake_attempt_counter - 8) / 12.0
                    pity_chance = min(0.75, max(0.05, pity_progress * 0.75))
                    if random.random() < pity_chance:
                        return manhake_fish

        # If none fit weight, fallback to ANY fish the rod can handle
        if not candidates:
            candidates = [f for f in fish_list if f["weight"] <= (rod["maxweight"]+20)]

        # If STILL none → your rod is too weak
        if not candidates:
            return None

        # Final weighted pick within the chosen tier.
        return _pick_weighted_fish(candidates)



    # ====================================================
    # ROD UPGRADING
    # ====================================================

    def upgrade_rod(stat, amount):
        if stat in rod:
            rod[stat] += amount
            if rod[stat] < 0:
                rod[stat] = 0
                
# Simple hold-to-move bar example
label fishing_game:

    $ fish_caught_input_enabled = False
    scene bg fish1 with Fade(0.1,0,0.1)
    call screen fish_options
    return

init python:

    # --------------------------
    # STARTUP / DELAY
    # --------------------------
    startup_delay = 1.0       # Bars stay centered for 1 second
    startup_timer = 0.0
    fish_caught_input_enabled = False

    # --------------------------
    # CONTROL BAR / PLAYER BAR
    # --------------------------
    bar_x = 0.0               # normalized 0–1
    bar_up_speed = 0.0
    bar_down_speed = 0.0
    max_speed = 30.0
    accel = 1.0
    decel = 1.0
    holding = False

    # --------------------------
    # Apply rod stats
    # --------------------------    
    bar_size_scale = 1
    control_width = int(150 * bar_size_scale)        # bar width from rod
    resilience = 0       # reduces fish movement

    # --------------------------
    # Big bar layout
    # --------------------------
    big_bar_x = 535
    big_bar_width = 860

    # normalized bar length (so bar stays inside bounds)
    bar_length = control_width / big_bar_width
    
    def get_centered_bar_x():
        return max(0.0, (1.0 - bar_length) / 2.0)

    def get_toughness_width_scale(toughness):
        import math
        # fish.rpy currently ranges from toughness 1 (easiest) to 50 (hardest).
        t = max(1.0, min(50.0, float(toughness)))

        # Normalize toughness (1 → 0.0, 50 → 1.0)
        x = (t - 1.0) / 49.0
        x = max(0.0, min(1.0, x))  # safety clamp

        # Exponential ease-out curve
        reduction = 0.99 * (1 - math.exp(-6 * x))

        return 1.0 - reduction

    def reset_fishing_state():
        global startup_timer, holding, bar_up_speed, bar_down_speed
        global bar_x, fish_x, tension

        startup_timer = 0.0
        holding = False
        bar_up_speed = 0.0
        bar_down_speed = 0.0
        bar_x = get_centered_bar_x()
        fish_x = 0.5
        tension = 40.0

    # --------------------------
    # FISH POSITION & MOVEMENT
    # (this will be overwritten by picked fish)
    # --------------------------
    fish_x = 0.5       # normalized 0–1
    fish_toughness = 3 # default (will be replaced by fish)
    fish_direction = 1 # not used in your random shake version

    # --------------------------
    # TENSION SYSTEM
    # --------------------------
    tension = 50.0
    tension_up_speed = 20.0
    tension_down_speed = 40.0


    # Update function called by timer
    def update_bar():
        global startup_timer, startup_delay
        global bar_x, bar_down_speed, bar_up_speed, holding, bar_length, bar_right
        global fish_x, fish_toughness, fish_direction
        global tension

        dt = 0.016  # ~60 FPS

        # --------------------------
        # 1. STARTUP DELAY (freeze)
        # --------------------------
        if startup_timer < startup_delay:
            startup_timer += dt

            # Keep bars in the center during intro
            tension = 40
            holding = False
            bar_x = get_centered_bar_x()
            fish_x = 0.5
            bar_up_speed = 0.0
            bar_down_speed = 0.0
            return None

        # --------------------------
        # 2. PLAYER BAR MOVEMENT
        # --------------------------
        if holding:
            bar_down_speed = 0
            bar_up_speed += accel * dt
            bar_up_speed = min(bar_up_speed, max_speed)

            bar_x += bar_up_speed * dt
            if bar_x > 1.0 - bar_length:
                bar_x = 1.0 - bar_length

        else:
            bar_up_speed = 0
            bar_down_speed += decel * dt
            bar_down_speed = min(bar_down_speed, max_speed)

            bar_x -= bar_down_speed * dt
            if bar_x < 0.0:
                bar_x = 0.0
                bar_down_speed = 0

        # --------------------------
        # 3. FISH MOVEMENT
        # --------------------------
        jump = random.uniform(-fish_toughness, fish_toughness) / 200
        fish_x += jump

        # clamp
        fish_x = max(0.0, min(1.0, fish_x))

        # --------------------------
        # 4. TENSION CHECK
        # --------------------------
        bar_left = bar_x
        bar_right = bar_x + bar_length

        if bar_left <= fish_x <= bar_right:
            tension += tension_up_speed * dt
        else:
            tension -= tension_down_speed * dt

        # --------------------------
        # 5. Tension boundary → events
        # --------------------------
        if tension < 0.0:
            tension = 40.0
            update_tension(0)
        if tension > 100.0:
            tension = 100.0
            update_tension(100)

        return None

    def hold_on():
        global holding
        holding = True

    def hold_off():
        global holding
        holding = False

screen fishing_demo():

    timer 0.016 repeat True action Function(update_bar)

    # Controls
    key "K_SPACE" action Function(hold_on)
    key "keyup_K_SPACE" action Function(hold_off)
    key "mousedown_1" action Function(hold_on)
    key "mouseup_1" action Function(hold_off)

    # Big bar background
    add "gui/fish_bar.png" xalign 0.5 yalign 0.9

    # Player control bar
    $ control_x = big_bar_x + int(bar_x * big_bar_width)
    add Solid("#2ecc71") xpos control_x ypos 820 xsize control_width ysize 50
    #$bar_left = bar_x
    #$bar_right = bar_x + bar_length

    #add Solid("#cc2e2e") xpos (bar_left) ypos 720 xsize 20 ysize 50
    #add Solid("#4e2ecc") xpos (bar_right) ypos 720 xsize 20 ysize 50

    # Fish pointer
    $ fish_screen_x = big_bar_x + int(fish_x * big_bar_width)
    add "gui/fish_pointer.png" xpos (fish_screen_x - 50) ypos 720
    #add Solid("#2ecc71") xpos (fish_x) ypos 720 xsize 20 ysize 50

    # Tension bar
    $ tension_left = 620
    $ tension_meter = int((tension / 25.0) * 169)
    add Solid("#e74c3c") xpos tension_left ypos 950 xsize tension_meter ysize 25
    

transform slide_slow:
    # Start offscreen right
    yalign 0.5
    xalign 2.0
    easein 0.4 xalign 0.6
    # Slow down in middle (ease curve)
    # Continue left
    easeout 0.4 xalign -1.5  # or whatever "off-left" means
transform fade_gray:
    alpha 0.0
    linear 0.5 alpha 0.7
    linear 0.5 alpha 0.0
screen fish_intro_anim():
    # Gray backdrop fade in/out
    add Solid("#00000080"):
        at fade_gray

    # Your image sliding right → center → left (with slowdown)
    add "bg/fishing/fish_start.png":
        at slide_slow

# --- Example label to call the minigame with sample fish & rod ---


screen fish_options():
    modal True
    frame:
        background Solid("#ffffff00")
        xalign 0.5
        yalign 0.9
        xsize 800
        ysize 500
        vbox:
            spacing 50
            xalign 0.5
            yalign 0.99
            imagebutton:
                at hover_action
                xalign 0.5
                yalign 0.5
                action [SetVariable("save_lock", True), Jump("kuro_fish_cast")]
                auto "bg/fishing/fish_cast_%s.png"
        fixed:
            xalign 0.5
            yalign 0.99
            imagebutton:
                at hover_fade
                xalign 0.5
                yalign 0.5  
                idle "bg/fishing/fish_leave.png"
                action [SetVariable("_skipping", True), SetVariable("save_lock", False), Jump("island")]   
    key "K_SPACE" action [Jump("kuro_fish_cast")]

label kuro_fish_cast:
    $ _skipping = False
    hide screen fish_options
    show bg fish2 with dissolve
    $ renpy.pause(0.8, hard=True)
    show bg fish3 with dissolve
    $ renpy.pause(random_from_0_to(10), hard=True)
    show bg fish4
    $ renpy.pause(0.6, hard=True)
    show bg fish5 at shake_zoomed
    show screen fish_intro_anim
    $ renpy.pause(1, hard=True)
    hide screen fish_intro_anim
    $ current_fish = pick_fish()
    if current_fish is None:
        "Your rod is too weak to catch any fish here."
        return

    $ fish_toughness = current_fish["toughness"] - rod["resilience"] / 5
    if fish_toughness < 0.1:
        $ fish_toughness = 0.1

    $ base_control_width = int((150 + int(rod["size"]*1.5)) * bar_size_scale)
    $ control_width = max(40, int(base_control_width * get_toughness_width_scale(current_fish["toughness"])))
    $ bar_length = control_width / big_bar_width
    $ reset_fishing_state()
    #$ renpy.notify(f"{current_fish}")
    call screen fishing_demo

init python:
    def random_from_0_to(num):
        roll = random.randint(0, num*10)
        roll2 = roll/10
        return roll2
    def update_tension(amount):
        global tension

        tension = amount
        # If tension reaches 0 → fail
        if tension <= 0:
            update_tension(40)
            renpy.jump("tension_fail")

        # If tension reaches 100 → success
        if tension >= 100:
            update_tension(40)
            renpy.jump("tension_success")

label tension_fail:
    scene bg fishl
    $ reset_fishing_state()
    $ renpy.notify(f"You let {current_fish['name']} got away!")
    call screen fish_options
label tension_success:
    scene bg fishw
    $ reset_fishing_state()
    $ apply_fish_effect(current_fish)
    call screen fish_caught


transform zoomer:
    # Start offscreen right
    zoom 0.1
    easein 0.4 zoom 1
screen fish_caught():
    tag fish
    modal True
    zorder 210

    # semi-transparent backdrop
    add Solid("#ffffff29") xalign 0.5 yalign 0.5
    add "bg/fishing/fish_caught.png":
        xalign 0.5
        yalign 0.5
        at zoomer
    frame:
        xalign 0.5
        yalign 0.51
        xsize 900
        ysize 420
        background ("#ffffff29")
        at zoomer
        vbox:
            spacing 10
            xalign 0.5
            yalign 0.4
            text "YOU CAUGHT A:":
                size 100
                color "#000000"
                xalign 0.5
            null height -40
            fixed:
                add "bg/fishing/fish_%s.png" % current_fish["name"]:
                    xalign 0.5
                    yalign 0.0
                # small hint
            null height -40
            text "[rarity_names[current_fish['rarity']].upper()]" size 30 color "#656565" xalign 0.5
            null height -30
            text "[current_fish['name'].upper()]" size 80 color "#000000" xalign 0.5
            null height -40
            text "[current_fish['desc'].upper()]" size 35 color "#000000" xalign 0.5
            null height -20
            text "[fish_effect]" size 25 color "#000000" xalign 0.5
            null height -20

            text "PRESS SPACE TO CONTINUE" size 22 color "#c1c1c1" xalign 0.5
    # Timer to enable input after 1 second
    timer 1.0 action SetVariable("fish_caught_input_enabled", True) repeat False

    # Only allow keys if input is enabled
    if fish_caught_input_enabled:
        key "K_SPACE" action [Hide("fish_caught"), Jump("fishing_game")]
        key "mousedown_1" action [Hide("fish_caught"), Jump("fishing_game")]

label fishing_game_tutorial:
    $ lan_talked_on_island = True
    stop music fadeout 0.5
    play music "bgm_tutorial.mp3" fadein 1.0  volume 0.4
    scene bg fish0 with Fade(1, 0, 1)
    show flan smirk at slide_in_right
    lan "Alright fellas!"
    lan "Before you begin..."
    show watta frown at slide_in_left
    show flan huh
    w "Wait wait wait!!!"
    if lan_first_talk_done_stage == 1:
        w "Why are you here?"
        show flan close
        lan "Why should I not be here fellas?"
        lan "I'm the leading figure of the entertainment industry in Sidurina"
        lan "Of course I would be here."
        w "But this is a desserted islet, how did you get here?"
        show flan close at bounced
        lan "Don't mind about that..."
        show flan default
        lan "Do you wanna hear the tutorial or not?"
        show watta frown
        w "Go on..."
        show flan smirk
    else:
        w "Who are you?"
        show flan close
        lan "Don't mind about that..."
        show flan default
        lan "Do you wanna hear the tutorial or not?"
        show watta frown
        w "Go on..."
        show flan smirk
    lan "The rule of this game is simple"
    lan "You just press space or the \"Cast\" button to cast your rod."
    show watta default
    hide watta
    show kuro happy at left
    kr "Cast the rot yay yay!"
    lan "The fish will falls for the bait automatically."
    show flan close
    hide kuro
    show watta frown at left
    lan "Afterwards there will be 2 bars, hold space or mouse1 to move the green bar, try to overlap it with the fish pointer."
    lan "If done correctly the bottom bar will rise, and once it's full you will get the fish."
    lan "The fishes are pretty useless for now this is the beta test so..."
    show flan default
    lan "Have fun playing..."
    $ fish_tutorial_done = True
    stop music fadeout 0.5
    play music "bgm_island.mp3" fadein 1.0 volume 0.4
    jump fishing_game
