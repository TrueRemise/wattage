init -5 python:
    # Keep these clips very short for the Undertale-like speech tick effect.
    TALK_VOICE_SFX = {
        "watta": "sfx/voice/watta.mp3",
        "remi": "sfx/voice/remi.mp3",
        "woogie": "sfx/voice/woogie.mp3",
        "sari": "sfx/voice/sari.mp3",
        "nemu": "sfx/voice/nemu.mp3",
    }

    def register_talk_voice(character_key, sfx_path):
        channel_name = "{0}_voice".format(character_key)

        renpy.music.register_channel(
            channel_name,
            mixer="voice",
            loop=True,
            stop_on_mute=True,
            tight=True,
        )

        def talk_callback(event, **kwargs):
            if event == "show":
                # Allow missing files in dev so voice assets can be dropped in later.
                if renpy.loadable(sfx_path):
                    renpy.sound.play(sfx_path, channel=channel_name, loop=True)
            elif event in ("slow_done", "end"):
                renpy.sound.stop(channel=channel_name)

        setattr(store, "{0}_talk_callback".format(character_key), talk_callback)

    for character_key, sfx_path in TALK_VOICE_SFX.items():
        register_talk_voice(character_key, sfx_path)
