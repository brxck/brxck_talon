from talon import Context, Module, actions, cron, scope

mod = Module()

_speech_was_enabled = False
_speech_fallback_job = None


def _speech_fallback_disable():
    global _speech_fallback_job
    _speech_fallback_job = None
    if actions.speech.enabled() and not _speech_was_enabled:
        actions.speech.disable()


@mod.action_class
class MacroPadActions:
    def wispr_toggle_down():
        """Disable speech for wispr if it was enabled, tracking state for re-enable on up"""
        global _speech_was_enabled
        actions.key("alt-shift-w:down")
        _speech_was_enabled = actions.speech.enabled()
        if _speech_was_enabled:
            actions.speech.disable()

    def wispr_toggle_up():
        """Re-enable speech after wispr if it was enabled before"""
        actions.key("alt-shift-w:up")
        global _speech_was_enabled
        if _speech_was_enabled:
            actions.speech.enable()

    def speech_toggle_down():
        """Toggle speech on and off"""
        global _speech_was_enabled, _speech_fallback_job
        if _speech_fallback_job:
            cron.cancel(_speech_fallback_job)
            _speech_fallback_job = None
        _speech_was_enabled = actions.speech.enabled()
        if actions.speech.enabled():
            actions.speech.disable()
        else:
            actions.user.delayed_speech_on()

    def speech_toggle_up():
        """Toggle speech on and off"""
        global _speech_was_enabled, _speech_fallback_job
        if actions.user.is_delayed_enabled():
            actions.user.delayed_speech_off()
            _speech_fallback_job = cron.after("1s", _speech_fallback_disable)
        elif _speech_was_enabled:
            actions.speech.enable()
        elif actions.speech.enabled():
            _speech_fallback_job = cron.after("1s", _speech_fallback_disable)

    def mode_toggle():
        """Toggle between command, dictation, and mixed mode"""
        mode = scope.get("mode")
        if {"command", "dictation"}.issubset(mode):
            actions.app.notify("Command mode")
            actions.mode.enable("command")
            actions.mode.disable("dictation")
        elif "command" in mode:
            actions.app.notify("Dictation mode")
            actions.mode.enable("dictation")
            actions.mode.disable("command")
        elif "dictation" in mode:
            actions.app.notify("Mixed mode")
            actions.mode.enable("command")
            actions.mode.enable("dictation")
