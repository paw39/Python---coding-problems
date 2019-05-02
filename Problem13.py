# This problem was asked by Amazon.
#
# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a single count and character.
# For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
#
# Implement run-length encoding and decoding. You can assume the string to be encoded have
# no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
from collections import OrderedDict


def encoding(message):
    count = 1
    results = []
    for i in range(1, len(message)):
        if message[i] == message[i-1]:
            count += 1
        else:
            results.append((count, message[i-1]))
            count = 1
        if i == len(message) - 1:
            results.append((count, message[i]))
    for result in results:
        print(result[0], result[1], sep="", end="")


def decoding(message):
    results = []
    for i in range(len(message) - 1):
        if message[i].isdigit():
            results.append(int(message[i]) * str(message[i+1]))
        else:
            i += 1
    print(*results, sep="")


if encoding("AAAABBBCCDAA") == decoding("4A3B2C1D2A"):
    print("Decoding and encoding works!")
