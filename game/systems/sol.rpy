default sol = 0
default job_upgrade = 0

# base values
define work = 100
define work_remote = 25

init python:
    def sol_add(amount):
        global sol, job_upgrade

        # Check if this is a "work" type job
        if job_upgrade >= 1 and amount in (work, work_remote):
            amount *= 2

        sol += amount


    def sol_lose(amount):
        global sol
        sol = max(0, sol - amount)  # prevent negative money

    def sol_set(amount):
        global sol
        sol = max(0, amount)