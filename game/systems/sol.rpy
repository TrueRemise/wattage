default sol = 0
default job_upgrade = 0

# base values
define work = 200
define work_remote = 50

init python:
    def _sync_lan_currency_on_sol_change():
        sync_fn = getattr(renpy.store, "lan_sync_currency_last_save", None)
        if sync_fn is not None:
            sync_fn()

    def sol_add(amount):
        global sol, job_upgrade

        # Check if this is a "work" type job
        if job_upgrade >= 1 and amount in (work, work_remote):
            amount *= 2

        sol += amount
        _sync_lan_currency_on_sol_change()


    def sol_lose(amount):
        global sol
        sol = max(0, sol - amount)  # prevent negative money
        _sync_lan_currency_on_sol_change()

    def sol_set(amount):
        global sol
        sol = max(0, amount)
        _sync_lan_currency_on_sol_change()
