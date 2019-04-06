# Given an array of integers, return a new array such that each element 
# at index i of the new array is the product of all the numbers in the original array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].

arr = [3, 2, 1]
new = []
for i, v in enumerate(arr):
    temp = list([x for x in arr if x != arr[i]])
    res = 1
    for k in temp:
        res *= k
    new.append(res)
    print(temp)
print(new)
