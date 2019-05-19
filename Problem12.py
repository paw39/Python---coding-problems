# This problem was asked by Facebook.
#
# Given a string of round, curly, and square open and closing brackets, return whether
# the brackets are balanced (well-formed).
#
# For example, given the string "([])[]({})", you should return true.
#
# Given the string "([)]" or "((()", you should return false.


def isBalanced(s):
    openers = "{[("
    closers = {
        "}": "{",
        "]": "[",
        ")": "("
    }
    stack = []
    for l in s:
        if l in openers:
            stack.append(l)
        elif l in closers.keys():
            if not stack or closers[l] != stack.pop():
                return "NO"
    if stack:
        return "NO"

    return "YES"


print(isBalanced("((()"))
