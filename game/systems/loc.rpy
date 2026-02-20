default travel_upgrade = 0   # 0 = normal, 1 = unrestricted, 2 = free travel
default unlocked_locations = ["outhome", "district", "park", "bridge", "monument", "centre", "beach"]
default locked_locations = ["field", "lake", "spira", "alley"]
default park_first = False
default bridge_first = False
default monument_first = False
default field_first = False
default centre_first = False
default beach_first = False
default spira_first = False
default alley_first = False
default lake_first = False
default cutscene_on = False

# Store world background (for global refresh)
default world_bg = "bg default"

define location_backgrounds = {
    "field": {
        "Dawn": "bg field",
        "Noon": "bg field",
        "Dusk": "bg field",
        "Night": "bg field",
    },
}

# adjacency map: where you can go from each location
define location_paths = {
    "home": ["outhome", "district"],
    "outhome": ["district", "home"],
    "district": ["outhome", "park"],
    "bridge": ["park", "monument", "field", "island"],
    "park": ["bridge", "district"],
    "field": ["bridge", "lake"],
    "monument": [ "bridge", "centre"],
    "centre": ["beach", "monument", "lake"],
    "lake": ["field"],
    "spira": ["alley"],
    "beach": ["centre", "d", "island"],
    "alley": ["spira"],
}
define sub_locations = {
    "outhome": ["mainhall", "diningroom", "workspace", "bedroom"],
    "bridge": ["underbridge", "northgate"],
    "park": ["van"],
    "field": ["floralia", "westgate", "eastgate"],
    "monument": ["dustwynd", "nekopia", "aloy", "reni", "garage"],
    "centre": ["flan", "floral respite", "big screen"],
    "beach": ["island"],
    "spira": ["archeste", "railwork", "fishing lane"],
    "district": ["ruins"],
    "lake": ["owlnest"],
}

init python:
    # --------------------------------------------------
    # Utility functions
    # --------------------------------------------------
    
    def get_bg(loc, phase_name):
        """
        Auto background generator:
            Dawn/Noon/Dusk -> bg <loc>
            Night          -> bg <loc>n
        Special cases are handled via location_backgrounds
        """

        # --- SPECIAL CASES ---
        if loc in location_backgrounds:
            table = location_backgrounds[loc]
            if phase_name in table:
                return table[phase_name]

        # --- DEFAULT RULE ---
        if phase_name == "Night" and current_location in unlocked_locations:
            return f"bg {loc}n"
        else:
            return f"bg {loc}"
        
    def is_unlocked(loc):
        """Check if a location is accessible."""
        return loc in unlocked_locations


    def loc_unlock(loc):
        """Unlocks a new location if not already unlocked."""
        global unlocked_locations
        if loc not in unlocked_locations:
            unlocked_locations.append(loc)
            locked_locations.remove(loc)
            renpy.notify("New area unlocked: " + loc.title())

    def adjacent_unlock(loc1, loc2):
        """Makes loc1 and loc2 adjacent (bidirectional)."""
        # Ensure loc1 has a list
        if loc1 not in location_paths:
            location_paths[loc1] = []
        if loc2 not in location_paths:
            location_paths[loc2] = []

        # Add loc2 into loc1’s path (no duplicates)
        if loc2 not in location_paths[loc1]:
            location_paths[loc1].append(loc2)
        if loc1 not in location_paths[loc2]:
            location_paths[loc2].append(loc1)

        renpy.notify(f"Unlocked adjacency: {loc1} <--> {loc2}")
    def get_parent_location(loc):
        """
        Returns the parent location if loc is a sub-location,
        otherwise returns loc unchanged.
        """
        for parent, subs in sub_locations.items():
            if loc in subs:
                return parent
        return loc

    def loc_lock(loc):
        """Lock a location again."""
        global unlocked_locations
        if loc in unlocked_locations:
            unlocked_locations.remove(loc)
            locked_locations.append(loc)
            renpy.notify("Area locked: " + loc.title())

    def get_parent_locations(loc):
        """Return all parent locations that contain this loc as a sub-location."""
        result = []
        for parent, subs in sub_locations.items():
            if loc in subs:
                result.append(parent)
        return result

    def is_here(loc):
        """Current loc OR parent of current sub-location."""
        if loc == current_location:
            return True
        if get_parent_location(current_location) == loc:
            return True
        return False

    def is_travel_allowed(dest):
        """
        New travel rule:
        - If travel upgrade = unrestricted → always allowed
        - Normal rule: dest must be adjacent to current_location
        - NEW: If current location is a sub-location, check parent adjacency
        """
        global travel_upgrade
        if travel_upgrade >= 1:
            return True

        # direct adjacency
        if dest in location_paths.get(current_location, []):
            return True

        # check parent locations of current_location
        parents = get_parent_locations(current_location)
        for p in parents:
            if dest in location_paths.get(p, []):
                return True

        return False

    # --------------------------------------------------
    # Global background update system
    # --------------------------------------------------

    def update_world_bg():
        """
        Refresh the global background value to match the
        current location and phase. Called on phase change.
        """
        global world_bg
        new_bg = get_bg(current_location, phases[phase])
        world_bg = new_bg
        return new_bg

    def refresh_bg_visual():
        """
        Refreshes the background visual.
        Only swaps to night version if player is currently on the main BG.
        """

        global world_bg,phase   # <-- This is the real current BG
        new_base = update_world_bg()  # e.g. "bg_beach"
        
        # Candidate night version — e.g. "bg_beachn"
        night_version = new_base + "n"
        # Check if a night bg image exists

        night_exists = renpy.has_image(night_version)
        # Check if currently showing the MAIN location only
        in_main_location = (world_bg == new_base)

        # Decide final background
        if in_main_location and night_exists and phase == 3:
            final_bg = night_version
        else:
            final_bg = world_bg  # keep current (sub-area safe)

        # Update world_bg to reflect what we show
        world_bg = final_bg

        if phase == 3:
            renpy.scene()
            renpy.show(final_bg)




    # --------------------------------------------------
    # Movement system
    # --------------------------------------------------

    def move_to(loc):
        global current_location, actions_left, map_open, travel_upgrade

        renpy.hide_screen("map_screen")
        renpy.hide_screen("phone_screen")
        phone_open = False
        map_open = False
        # --- check unlocks ---
        if bailey_following_oil:
            if loc in ["district"]:
                renpy.hide_screen("map_screen")
                renpy.call_in_new_context("bailey_following_thru_district")
                return
            elif loc not in ["monument"]:
                renpy.hide_screen("map_screen")
                renpy.call_in_new_context("bailey_following_going_elsewhere")
                return

        if not is_unlocked(loc):
            renpy.notify(loc.title() + " is locked.")
            return

        if cutscene_on:
            renpy.notify("Wait for the cutscene to be finished first.")
            return

        if current_location in ["balcony", "owlnest"] and phase == 3:
            renpy.notify("You can not leave.")
            return
        
        parent_here = get_parent_location(current_location)
        parent_dest = get_parent_location(loc)
        if current_location in ["mainhall", "diningroom", "workspace", "bedroom"] and loc in ["district"]:
            renpy.notify("Get out of your house first")
            return
            
        if travel_upgrade == 0 and parent_dest not in location_paths.get(parent_here, []):
            renpy.notify("Can't reach " + loc.title() + " from here.")
            return

        # --- morning shift restriction ---
        if first_work and loc not in ["district", "outhome", "home"]:
            renpy.notify("You should do your morning shift before going elsewhere.")
            return

        # --- travel cost ---
        if (travel_upgrade < 2
            and not (first_work and loc == "district" and loc == "outhome")):
            action_done()

        # update world state BEFORE jump
        current_location = loc
        # update global bg for next area
        update_world_bg()

        renpy.jump(loc)
