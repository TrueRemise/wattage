# Top of save_blocker.rpy

# ✅ This is global, outside python
default save_lock = False   

init python early:
    # Helper function
    def is_save_locked():
        return renpy.store.save_lock

    # Wrapper for actions we want to block
    class BlockIfLocked(Action):
        def __init__(self, wrapped):
            self.wrapped = wrapped

        def __call__(self):
            if is_save_locked():
                renpy.notify("Saving/Loading disabled during gameplay.")
                return
            return self.wrapped()

        def get_sensitive(self):
            return not is_save_locked()

init python early:

    # Dummy action to replace QuickSave/QuickLoad
    class DisabledAction(renpy.Displayable):
        def __call__(self):
            renpy.notify("Quicksave/Quickload is disabled!")