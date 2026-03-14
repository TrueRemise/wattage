init -5 python:
    TALK_VOICE_SFX = {
        "unknown": "sfx/voice/unknown.mp3",
        "w": "sfx/voice/watta.mp3",
        "r": "sfx/voice/remi.mp3",
        "sr": "sfx/voice/sari.mp3",
        "lan": "sfx/voice/flan.mp3",
        "c": "sfx/voice/chii.mp3",
        "n": "sfx/voice/nemu.mp3",
        "ts": "sfx/voice/tsuyu.mp3",
        "iog": "sfx/voice/iog.mp3",
        "john": "sfx/voice/john.mp3",
        "rn": "sfx/voice/renia.mp3",
        "nk": "sfx/voice/neko.mp3",
        "sc": "sfx/voice/sanco.mp3",
        "tt": "sfx/voice/tato.mp3",
        "kr": "sfx/voice/kuro.mp3",
        "wo": "sfx/voice/woogie.mp3",
        "tk": "sfx/voice/toko.mp3",
        "ik": "sfx/voice/iskra.mp3",
        "b": "sfx/voice/bailey.mp3",
        "o": "sfx/voice/owl.mp3",
        "tkn": "sfx/voice/tsukino.mp3",
        "sn": "sfx/voice/snowie.mp3",
        "vv": "sfx/voice/vivi.mp3",
        "al": "sfx/voice/aloy.mp3",
        "dv": "sfx/voice/moff.mp3",
        "mk": "sfx/voice/mokka.mp3",
    }

    # Seconds between beeping
    TALK_VOICE_INTERVAL = {
        "w": 0.055,
        "n": 0.05,
        "wo": 0.08,
        "dv": 0.05,
        "al": 0.05,
        "nk": 0.06,
        "rn": 0.05,
        "c": 0.15,
        "sn": 0.05,
        "sc": 0.05,
        "r": 0.05,
        "kr": 0.05,
    }
    DEFAULT_TALK_VOICE_INTERVAL = 0.05

    _active_talk_voice = {}

    def _talk_voice_periodic_callback():
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
