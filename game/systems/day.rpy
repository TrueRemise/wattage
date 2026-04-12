# ============================================================
# Phase & Day Cycle System
# ============================================================

default day = 1
default phase = 0
default max_actions = 3
default actions_left = 3
default work_first_time = False
default first_work = True
default stone_own = 0

define phases = ["Dawn", "Noon", "Dusk", "Night", "Midn"]

# Optional: week cycle
define days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


init python:
    # ------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------
    def get_day(day):
        """Return weekday name from number."""
        return days[(day - 1) % 7]

    # ------------------------------------------------------------
    # Main Action System
    # ------------------------------------------------------------
    def action_done():
        global actions_left, first_work

        if bailey_following_oil:
            renpy.hide_screen("phone_screen")
            renpy.call_in_new_context("bailey_following_action_done")
            actions_left -= 1
            actions_left = max(actions_left, 0)  # safety
            if actions_left <= 0:
                next_phase()
            return
        if first_work:
            renpy.notify(f"You should do your morning shift.{cutscene_on}")
            return

        actions_left -= 1
        actions_left = max(actions_left, 0)  # safety

        if actions_left <= 0:
            renpy.notify(f"{phase}")
            next_phase()

    def action_fill():
        global actions_left, first_work

        actions_left = max_actions
    def action_add():
        global actions_left, first_work

        actions_left += 1
        if actions_left >= max_actions:
            actions_left = max_actions    # safety
    def stone_add():
        global stone_own, max_actions, actions_left

        # Stop if already capped
        if stone_own >= 7:
            renpy.notify("You can't carry more stones.")
            return

        if max_actions >= 10:
            renpy.notify("You can't gain more actions.")
            return

        # Apply upgrade
        stone_own += 1
        max_actions += 1
        actions_left += 1

        # Update UI instantly
        renpy.restart_interaction()

        renpy.notify("Stone added! Actions +1.")

    def stone_remove():
        global stone_own, max_actions, actions_left

        # Apply upgrade
        stone_own -= 1
        max_actions -= 1
        if actions_left > max_actions:
            actions_left -=1

        # Update UI instantly
        renpy.restart_interaction()

        renpy.notify("Stone removed! Actions -1.")


    # ------------------------------------------------------------
    # Phase Transition System
    # ------------------------------------------------------------
    def next_phase():
        global actions_left, phase, day, actions_locked, current_location
        if phase == 0:
            phase += 1
            actions_left = max_actions
        elif phase == 1:
            phase += 1
            actions_left = max_actions
        elif phase == 2:
            if current_location == "lake":
                renpy.hide_screen("phone_screen")
                renpy.jump("lake_at_night")
            phase += 1
            actions_left = max_actions
        elif phase == 3:
            phase += 1
            actions_left = min(1, max_actions)
            actions_locked = True
            hide_everything()
            if current_location not in ["mainhall", "diningroom", "workspace", "bedroom"]:
                renpy.jump("force_home_midn")
        elif phase == 4:
            # Optional: ensure player ends up home
            renpy.jump("sleep")
            phase = 0
            day += 1
            actions_left = max_actions
            renpy.jump("homeskip")

        
        # Update background each time phase changes
        update_world_bg()
        things_that_change_when_next_phase()
        # If it’s Midnight (end of cycle), optionally force home

        # Notify player for clarity

        # Visually refresh background if currently in a main area
        refresh_bg_visual()

    def things_that_change_when_next_phase():
        global sari_exam_timer, chii_meet_sanco_timer, bailey_give_sauce_normal, neko_backstage_close_next_phase, backstage_open, chii_go_to_lake_timer, bailey_refining_timer
        if sari_exam_timer >= 1:
            sari_exam_timer += 1
            sari_exam_timer = max(4,sari_exam_timer + 1)
        if chii_meet_sanco_timer <= 3:
            chii_meet_sanco_timer -= 1
            if chii_meet_sanco_timer == 0:
                chii_meet_sanco_timer = 5
        if chii_go_to_lake_timer > 3:
            chii_go_to_lake_timer += 1
            if chii_go_to_lake_timer >= 8:
                chii_go_to_lake_timer = 7
        if bailey_give_sauce_normal >= 1:
            bailey_give_sauce_normal += 1
            bailey_give_sauce_normal = max(4,bailey_give_sauce_normal + 1)
        if bailey_refining_timer > 1:
            bailey_refining_timer += 1
            bailey_refining_timer = max(4,bailey_refining_timer + 1)
        if neko_backstage_close_next_phase:
            backstage_open = False

# ============================================================
# Example use (not required but useful for context)
label force_home_midn:
    hide screen map_screen
    hide screen phone_screen
    scene black with dissolve
    "You head home to rest..."
    $ current_location = "home"
    $ save_lock = False
    jump home

default about_hunger_first = False
label sleep:
    hide screen map_screen
    hide screen phone_screen
    scene black with dissolve
    "You lie on your bed..."
    $ phase = 0
    $ day += 1
    $ actions_locked = False
    scene bg bedroom with dissolve
    "A new day begins..."
    if food_prepared == True:
        show watta delighted at right
        w "Let's go prepared for the new day"
        $ actions_left = max_actions
    else:
        show watta huh
        w "Oops I didn't buy any food yesterday now it's growling"
        $ actions_left = max_actions - 2
    if not about_hunger_first:
        "From this day on you won't have to prepare manually anymore."
        "You can leave home for work right at the start."
        $ about_hunger_first = True
    jump things_that_change_when_you_sleep

label things_that_change_when_you_sleep:
    $ first_work = True
    $ lan_reset = True
    $ chii_reset = True
    $ tries_before_costing_action = 3
    $ food_prepared = False


    if remi_first_talk_done_stage == 1:
        $ remi_first_talk_done_stage = 2
    elif remi_first_talk_done_stage == 3:
        $ remi_first_talk_done_stage = 4
    elif remi_first_talk_done_stage == 5:
        $ remi_first_talk_done_stage = 6
    if nemu_first_talk_done_stage == 2:
        $ nemu_first_talk_done_stage = 3
    if tato_first_talk_done_stage == 1:
        $ tato_first_talk_done_stage = 2


    if tsuyu_go_sane_at_two == 1:
        $ tsuyu_go_sane_at_two = 2
    if backyard_tomato_planted >= 1:
        $ backyard_tomato_planted = max(3,backyard_tomato_planted+1)
    if glass_daisy_timer == 1 and is_item_get("Glass Daisy"):
        $ glass_daisy_timer = 2
        $ item_remove("Glass Daisy")
        $ item_add("Exquisite Daisy")
    elif glass_daisy_timer == 2 and is_item_get("Exquisite Daisy"):
        $ glass_daisy_timer = 3
        $ item_remove("Exquisite Daisy")
        $ item_add("Normal Daisy")
    if bailey_body_returning:
        $ bailey_unavailable = False
        $ bailey_body_returning = False
        $ bailey_body_returned = True
    if chii_go_to_lake_timer == 2 or chii_go_to_lake_timer == 3:
        $ chii_go_to_lake_timer = 4
    jump homeskip


init python:
    def hide_everything():
        renpy.hide_screen("blackjack_board")
        renpy.hide_screen("blackjack_result")
        renpy.hide_screen("bet_selector")
        renpy.hide_screen("shop_screen")
        renpy.hide_screen("bar_screen")