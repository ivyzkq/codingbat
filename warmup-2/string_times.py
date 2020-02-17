def string_times(str, n):
    """
    Given a string and a non-negative int n, 
    return a larger string that is n copies of the original string.
    """
    if n <= 0:
        return('n has to be non-negative')
    else:
        return(str * n)
print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))


























    # return str * n
