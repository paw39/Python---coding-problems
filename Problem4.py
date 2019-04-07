# Given an array of integers, find the first missing positive integer in linear time and constant space.
# In other words, find the lowest positive integer that does not exist in the array.
# The array can contain duplicates and negative numbers as well.
#
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
#
# You can modify the input array in-place.

arr = list(map(int, input().split()))
# arr = sorted([i for i in arr if i > 0])
# temp = 1
s = set()
for i in arr:
    if i > 0:
        s.add(i)
for i in range(1, max(arr)):
    if i not in s:
        print(i)
        break




