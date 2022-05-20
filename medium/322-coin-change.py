"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Example 3:

Input: coins = [1], amount = 0
Output: 0
"""
import sys
def coinChangeDp(coins, amount, n, count) -> int :
    if amount == 0:
        return 0
    if n == 0:
        return sys.maxsize
    
    # if amount - coins[n-1] >= 0:
    if amount >= coins[n-1] :
       return min(1 + coinChangeDp(coins, amount-coins[n-1], n, count+1), 
                    coinChangeDp(coins, amount, n-1, count))
    else:
        return coinChangeDp(coins, amount, n-1, count)
        
sys.setrecursionlimit(999999999)
coins = [3, 7, 405,436]
amount = 8839
    
answer =  coinChangeDp(coins, amount, len(coins), 0)
print("printing answer", answer)