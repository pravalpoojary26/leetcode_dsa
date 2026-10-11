
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and 
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
'''

def maxprofit(prices):
    minimum_price=prices[0]
    maximum_profit=0
    for price in prices:
        if price<minimum_price:
            minimum_price=price

        current_profit=price-minimum_price

        if current_profit>maximum_profit:
            maximum_profit=current_profit

    return maximum_profit


'''
by using kadanes algorithm approach 
'''
def kadanesprofit(prices):
    for i in range(len(prices)-1):
        prices[i]=prices[i+1]-prices[i]

    current_sum = 0
    maximum_profit=0
    for i in range(len(prices)-1):
        current_sum+=prices[i]
        if current_sum>maximum_profit:
            maximum_profit=current_sum
        elif current_sum<0:
            current_sum=0

    return maximum_profit

print(kadanesprofit([7,1,5,3,6,4]))

        
