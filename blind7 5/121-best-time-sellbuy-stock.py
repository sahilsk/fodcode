from runner import runner
"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Solution:
Trick is to look forward when you find the dip as you pass  through the array


"""


"""
7 6 4 3 1

"""


def maximizeprofit(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0

    i, j = 0, 1
    maxprofit = 0
    while j < len(prices):

        if prices[i] < prices[j]:
            maxprofit = max(maxprofit, prices[j] - prices[i])
            j += 1
        else:
            i = j
            j += 1

    return maxprofit


testcases = {5: ([7, 1, 5, 3, 6, 4], ), 0: ([7, 6, 4, 3, 1], )}

runner(maximizeprofit, testcases)