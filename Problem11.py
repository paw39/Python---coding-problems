# This problem was asked by Facebook.
#
# Implement regular expression matching with the following special characters:
#
# . (period) which matches any single character
# * (asterisk) which matches zero or more of the preceding element
# That is, implement a function that takes in a string and a valid regular expression and returns whether or not
# the string matches the regular expression.
#
# For example, given the regular expression "ra." and the string "ray", your function should return true.
# The same regular expression on the string "raymond" should return false.
#
# Given the regular expression ".*at" and the string "chat", your function should return true.
# The same regular expression on the string "chats" should return false.


def match(string, pattern):

    if '*' not in pattern:  # period case only
        if len(string) != len(pattern):
            return False
        else:
            for index, character in enumerate(string):
                if pattern[index] == character or pattern[index] == '.':
                    continue
                else:
                    return False
            return True
    else:   # asterisk case
        tmp = list(string)
        for index, character in enumerate(string):
            if character == pattern[index] or pattern[index] == '.':
                continue
            elif pattern[index] == '*':
                string.index(pattern[index+1])



print(match('mleko', 'm.e.o'))
