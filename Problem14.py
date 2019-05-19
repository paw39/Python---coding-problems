# This problem was asked by Facebook.
#
# Given a array of numbers representing the stock prices of a company in chronological order,
# write a function that calculates the maximum profit you could have made from buying and selling that stock once.
# You must buy before you can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could buy the stock
# at 5 dollars and sell it at 10 dollars.


arr = [9, 11, 8, 5, 7, 10]




def calculate(prices):
    buy = arr[0]
    maximum = 0
    for i in range(1, len(arr)):
        if arr[i] < buy:
            buy = arr[i]
        else:
            profit = arr[i] - buy
            if profit > maximum:
                maximum = profit
    if maximum:
        return maximum
    else:
        return -1


print(calculate(arr))




