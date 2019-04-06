# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

arr = [10, 15, 3, 7]  # OK
arr2 = [1, 5, 50, 46]   # NOT
arr3 = [-5, 5, 0, 10]
k = 17

for i in arr:
    if i > 0:
        if k - i in arr:
            print("True!")
            break

