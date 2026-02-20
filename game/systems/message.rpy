default unlocked_msg = ["Remi", "Sanco", "Toko", "Sari"]
default msg_active_context = False
default phone_number = ""     
default msg_data = {
    "Remi": {"phase": "0", "surprises": []},
    "Sanco": {"phase": "0", "surprises": []},
    "Toko": {"phase": "0", "surprises": []},
    "Sari": {"phase": "0", "surprises": []},
    "Aloy": {"phase": "0", "surprises": []},
    "Reni": {"phase": "0", "surprises": []},
}
default number_to_name = {
    "9171434321": "Reni",
    "9504371562": "John Phone Number",
    "93127548": "Jamal",
    "9359490308": "Aloy",
    "9785183": "HRLAF",
    "190015158": "Aquarina Corp",
    "1389008009": "RM corp",
}

init python:
    def get_msg_phase(name):
        """Return the current phase for a character."""
        info = msg_data.get(name)
        if not info:
            return "0"
        if info["surprises"]:
            s = info["surprises"][-1]
            return s
        return info["phase"]

    def update_msg_phase(name, new_phase):
        """Update story/surprise phase for a person."""
        if name in msg_data:
            msg_data[name]["phase"] = str(new_phase)
        else:
            msg_data[name] = {"phase": str(new_phase), "surprises": []}

    def add_surprise(name, tag):
        """Add a surprise phase (prioritized)."""
        if name in msg_data:
            msg_data[name]["surprises"].append(tag)
        else:
            msg_data[name] = {"phase": "0", "surprises": [tag]}

    def msg_unlock(name):
        """Unlock new person for messaging."""
        if name not in unlocked_msg:
            unlocked_msg.append(name)
            renpy.notify(f"New contact unlocked: {name}")

    def open_message_convo(name):
        """Open a character’s message conversation."""
        phase = get_msg_phase(name)
        label_name = f"msg_{name.lower()}_{phase}"
        if renpy.has_label(label_name):
            renpy.call(label_name)
            # After message, reopen the message list automatically
            renpy.call_screen("message_screen")
        else:
            renpy.notify(f"No messages for {name}")

# ============================================================
# Labels
# ============================================================

init python:
    msg_last_screen = None
    msg_last_bg = None

label open_messages:
    # Store what screen and background were active
    $ scr = renpy.current_screen()
    $ msg_last_screen = scr.screen_name if scr else None
    $ msg_last_bg = renpy.scene_lists().get_displayable_by_tag("master", "master")

    # Hide any overlaying UIs
    hide screen map_screen
    hide screen phone_screen

    scene bg phone with fade
    if already_write_reni_number and not "Reni" in unlocked_msg:
        call already_write_reni_number from _call_already_write_reni_number
        
    w "Who should I check today?"
    call screen message_screen

    # After returning, restore background and screen
    if msg_last_bg:
        scene expression msg_last_bg
    else:
        scene bg black  # fallback


    $ renpy.restart_interaction()
    return

# ============================================================
# Screens
# ============================================================


# message screen snippet
screen message_screen():
    tag phone_sub
    modal True
    zorder 95
    add "bg/bg phone.png" xalign 0.5 yalign 0.5

    vbox:
        spacing 18
        xalign 0.2
        yalign 0.25

        if unlocked_msg:
            $ shift = 0
            for name in unlocked_msg:

                button:
                    at hover_fade
                    xsize 520
                    ysize 70
                    xalign 0.5
                    xoffset -shift
                    background Solid("#FFFFFF30")
                    hover_background Solid("#FFFFFFCC")
                    action Function(open_message_convo, name)

                    text name:
                        size 60
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#0055FF"
            
                $ shift += 30
            null height 100
            button:
                at hover_fade
                xsize 520
                ysize 70
                xalign 0.5
                xoffset -shift
                background Solid("#FFFFFF40")
                hover_background Solid("#FFFFFFAA")
                action Show("add_contact_screen")
                text "Add contact":
                    size 60
                    xalign 0.5
                    yalign 0.5
                    color "#000000"
                    hover_color "#0055FF"

            button:
                at hover_fade
                xsize 520
                ysize 70
                xalign 0.5
                xoffset -shift
                background Solid("#FFFFFF40")
                hover_background Solid("#FFFFFFAA")
                action Return("exit")

                text "Return":
                    size 60
                    color "#000000"
                    hover_color "#0055FF"
                    xalign 0.5
                    yalign 0.5
        else:
            text "No contacts yet." size 40 xalign 0.5 color "#000000"


transform hover_fade:
    on hover:
        linear 0.2 zoom 1.1
    on idle:
        linear 0.2 zoom 1.0
# ============================================================
# Add Contact Scren
# ============================================================

# Screen: shows placeholder image + numeric input + Confirm/Cancel
screen add_contact_screen():
    tag add_contact
    modal True
    zorder 210

    # semi-transparent backdrop
    add Solid("#ffffff29") xalign 0.5 yalign 0.5
    add "gui/ui_watta.png" xalign 0.5 yalign 0.5
    frame:
        xalign 0.5
        yalign 0.51
        xsize 900
        ysize 420
        background None
        vbox:
            spacing 20
            xalign 0.5
            yalign 0.5  
            text "Input phone number:" size 70 color "#000000" xalign 0.5
            hbox:
                spacing 12
                xalign 0.5
                yalign 0.5  

                # Input element:
                # - value point to the store variable phone_number
                # - length limits number of characters
                # - allow restricts characters to digits only
                input:
                    value VariableInputValue("phone_number")
                    length 15
                    allow "0123456789"
                    color "#000000ff"
                    size 85
                    copypaste True
        

            # small hint
            text "Digits Only, Max 15" size 28 color "#aaa" xalign 0.5
            null height 20

            # Confirm / Cancel
            hbox:
                spacing 50
                xalign 0.5

                button:
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), Hide("add_contact_screen"), Function(try_add_contact_from_number)]

                    text "Confirm":
                        size 60
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#c0af19"

                button:
                    xsize 180
                    ysize 80
                    xalign 0.5
                    yalign 0.9
                    background Solid("#00000000")
                    hover_background Solid("#FFFFFF00")
                    action [Play("sound", "sfx/bet_select.mp3"), SetVariable("phone_number", ""), Hide("add_contact_screen")]

                    text "Cancel":
                        size 60
                        xalign 0.5
                        yalign 0.5
                        color "#000000"
                        hover_color "#8da417"
init python:
    def try_add_contact_from_number():
        """
        Called when the user presses Confirm on the add contact screen.
        Returns an action-friendly value (None), but performs the unlock / notify.
        """
        global phone_number

        # sanitize: strip spaces
        num = phone_number.strip()

        # basic validation
        if not num:
            renpy.notify("Please enter a number.")
            return None
        if num == "911":
            renpy.hide("message_screen")
            renpy.call("whats_your_emergency")

        # lookup name
        name = number_to_name.get(num)
        if name:
            if name in unlocked_msg:
                renpy.notify(f"{name} is already in your contacts.")
            else:
                msg_unlock(name)
                renpy.notify(f"{name} added to contacts.")

            phone_number = ""
            renpy.hide_screen("add_contact_screen")

        else:
            renpy.notify("Number not found.")
            # keep screen open so player can edit the number
        return None

label whats_your_emergency:
    show bg phone
    unknown "911, what's your emergency?"
    show bg phone what
    w "Wait what?"
    unknown "What? What's your trouble?"
    w "Errr, I called by acci-"
    unknown "FU- This shit again, Jeff this is the 3rd times this week already."
    "Jeff" "I got 5 Jeremy this job is not serious anymore Imma-"
    "Jeremy" "I might ta- Wha?"
    "Jeff" "What?"
    "Jeremy" "Oh continue I didnt mean to cut you off I was l-"
    "Jeff" "It's fine you can continue I don't mind"
    "Jeremy" "..."
    show bg phone mad
    "Jeff" "..."
    "Jeremy" "Wanna go hit Johnson next?"
    "Jeff" "Yeah yeah sure I'll do pepper this time."
    "Jeremy" "Cool- Oh wai-"
    "The call hung up"
    w "okay?"
    return
    