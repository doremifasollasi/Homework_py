def enough(cap, on, wait):
    """Simple program telling him if he will be able to fit all the passengers.
    a function that accepts three parameters:
    cap is the amount of people the bus can hold excluding the driver.
    on is the number of people on the bus.
    wait is the number of people waiting to get on to the bus.
    If there is enough space, return 0, and if there isn't, return the number of passengers he can't take."""
    if cap < on + wait:
        return wait-(cap-on)
        # return "You can not fit {} out of {} waiting".format(wait-(cap-on), wait)
    else:
        return 0

        # cap >= on + wait:
        # return "You can fit all {} passengers".format(cap-on)
        