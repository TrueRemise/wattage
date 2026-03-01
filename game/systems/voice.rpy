init -5 python:
    TALK_VOICE_SFX = {
        "watta": "sfx/voice/watta.mp3",
        "remi": "sfx/voice/remi.mp3",
        "woogie": "sfx/voice/woogie.mp3",
        "sari": "sfx/voice/sari.mp3",
        "nemu": "sfx/voice/nemu.mp3",
    }

    # Seconds between beepings
    TALK_VOICE_INTERVAL = {
        "watta": 0.045,
        "remi": 0.05,
        "woogie": 0.05,
        "sari": 0.05,
        "nemu": 0.05,
    }
    DEFAULT_TALK_VOICE_INTERVAL = 0.05

    _active_talk_voice = {}

    def _talk_voice_periodic_callback():
        import time
        now = renpy.display.core.get_time()

        for character_key, state in list(_active_talk_voice.items()):
            if now < state["next_play"]:
                continue

            renpy.sound.play(state["sfx_path"], channel=state["channel_name"], loop=False)
            state["next_play"] = now + state["interval"]

    _existing_periodic_callback = config.periodic_callback

    def _combined_periodic_callback():
        if _existing_periodic_callback is not None:
            _existing_periodic_callback()

        _talk_voice_periodic_callback()

    config.periodic_callback = _combined_periodic_callback

    def register_talk_voice(character_key, sfx_path):
        channel_name = "{0}_voice".format(character_key)

        renpy.music.register_channel(
            channel_name,
            mixer="voice",
            loop=False,
            stop_on_mute=True,
            tight=True,
        )

        interval = TALK_VOICE_INTERVAL.get(character_key, DEFAULT_TALK_VOICE_INTERVAL)

        def talk_callback(event, **kwargs):
            if event == "show":
                # Allow missing files in dev so voice assets can be dropped in later.
                if renpy.loadable(sfx_path):
                    _active_talk_voice[character_key] = {
                        "channel_name": channel_name,
                        "sfx_path": sfx_path,
                        "interval": interval,
                        "next_play": 0.0,
                    }
            elif event in ("slow_done", "end"):
                if character_key in _active_talk_voice:
                    del _active_talk_voice[character_key]

                renpy.sound.stop(channel=channel_name)

        setattr(store, "{0}_talk_callback".format(character_key), talk_callback)

    for character_key, sfx_path in TALK_VOICE_SFX.items():
        register_talk_voice(character_key, sfx_path)