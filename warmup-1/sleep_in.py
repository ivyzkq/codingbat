def sleep_in(weekday, vacation):
    """
    The parameter weekday is True if it is a weekday, and the parameter
    vacation is True if we are on vacation. We sleep in if it is not a
    weekday or we're on vacation.

    Return True if we sleep in.
    """
    if not weekday or vacation:
        return('We sleep in!')
    else:
        return('We cannot sleep in!')

print(sleep_in(False, False))
print(sleep_in(True, False))
print(sleep_in(False, True))




















# return not weekday or vacation