
prices = [1, 25, 24, 23, 12, 36, 14, 40, 31, 41, 5]


def maxProfitWithKTransactions(n, k, hold):
    # Base case
    if k == 0:
        return 0
    if n == len(prices) - 1:
        return prices[len(prices)-1] if hold == True else 0
    # 90
    if hold == False:
        # buy = stock - maxProfitWithKTransactions(prices, k, True)
        # nothing = maxProfitWithKTransactions(prices, k, hold)
        return max(maxProfitWithKTransactions(n+1, k, False),
                     maxProfitWithKTransactions(n+1, k, True) - prices[n])
    elif hold == True:
        # sell = stock + maxProfitWithKTransactions(prices, k-1, False)
        # nothing = maxProfitWithKTransactions(prices, k, hold)
        return max(maxProfitWithKTransactions(n+1, k, True),
                     maxProfitWithKTransactions(n+1, k-1, False) + prices[n])

if __name__ == "__main__":
    print(maxProfitWithKTransactions(0, 4, False))



def maxProfitWithKTransactions(prices, k):
    # Base case
    if k == 0 or len(prices) == 0:
        return 0
    
	if len(prices) == 1:
		return -prices[0] if k%1 != 0 else 0
	
	if k%1 != 0:
		return max(maxProfitWithKTransactions([i for i in prices[:len(prices)-1]], k), maxProfitWithKTransactions([i for i in prices[:len(prices)-1]], k-0.5) - prices[len(prices)-1])
	else:
		return max(maxProfitWithKTransactions([i for i in prices[:len(prices)-1]], k), maxProfitWithKTransactions([i for i in prices[:len(prices)-1]], k-0.5) + prices[len(prices)-1])