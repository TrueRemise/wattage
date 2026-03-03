default sol = 0
default job_upgrade = 0

# base values
define work = 200
define work_remote = 50

init python:
    def _sync_lan_currency_on_sol_change(previous_sol, current_sol):
        sync_fn = getattr(renpy.store, "lan_sync_currency_last_save", None)
        if sync_fn is not None:
            sync_fn()

        sol_change_fn = getattr(renpy.store, "lan_on_sol_changed", None)
        if sol_change_fn is not None:
            sol_change_fn(previous_sol, current_sol)

    def sol_add(amount):
        global sol, job_upgrade

        # Check if this is a "work" type job
        if job_upgrade >= 1 and amount in (work, work_remote):
            amount *= 2

        previous_sol = sol
        sol += amount
        _sync_lan_currency_on_sol_change(previous_sol, sol)


    def sol_lose(amount):
        global sol
        previous_sol = sol
        sol = max(0, sol - amount)  # prevent negative money
        _sync_lan_currency_on_sol_change(previous_sol, sol)

    def sol_set(amount):
        global sol
        previous_sol = sol
        sol = max(0, amount)
        _sync_lan_currency_on_sol_change(previous_sol, sol)
