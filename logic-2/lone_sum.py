import math

def lone_sum(a, b, c):
    """
    Given 3 int values, a b c, return their sum.
    However, if one of the values is the same as
    another of the values, it does not count towards the sum.
    """
    number_list = [a,b,c]
    for i in number_list:
        if number_list.count(i) == 1:
            return(a+b+c)
        else:
            pass
    if a == b and b != c:
        return(sum(a,b))
    elif b == c and c != a:
        return(sum(b,c))
    elif a == c and b != c:
        return(sum(a,c))
    else: 
        return('0')


print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))



















    # l = [a, b, c]
    # result = 0
    # for x in l:
    #     if l.count(x) == 1:
    #         result += x
    # return result
