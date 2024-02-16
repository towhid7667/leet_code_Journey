
#O(n2)
def maxProfit(prices):
    n = len(prices)
    b = []
    for i in range(n):
        for j in range(i+1, n):
            if prices[j] > prices[i]:
                b.append(prices[j]-prices[i])
    if not b:
        return 0  
    else:
        return max(b)
    
    
    
    
    
    #O(n)
def maxProfit(prices):
        if not prices:
            return 0

        min_num = prices[0]
        max_prof = 0

        for i in prices: 
            if i < min_num:
                min_num = i
            else:
                max_prof = max(max_prof , i - min_num)     
        return max_prof 
    #O(n)
def maxProfit(prices):
        l , r = 0 , 1
        max_profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit  
    
    
    