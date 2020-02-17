def double_char(str):
    """
    Given a string, return a string where for every 
    char in the original, there are two chars.
    """
    word = ''
    for i in str:
        letter = i*2
        word = word + letter
    return (word)

print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi, there'))


























    # new_str = ''
    # for letter in str:
    #     new_str += letter * 2
    # return new_str