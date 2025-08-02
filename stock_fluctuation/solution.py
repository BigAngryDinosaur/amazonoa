def sumOfFluctuation(prices):
    n = len(prices)
    maxSt, maxArrR, maxArrL = [0], [n] * n, [-1] * n
    minSt, minArrR, minArrL = [0], [n] * n, [-1] * n

    for i in range(1, n):
        cur = prices[i]
        while maxSt and prices[maxSt[-1]] < cur:
            stPop = maxSt.pop()
            maxArrR[stPop] = i
        maxSt.append(i)

    maxSt = [n - 1]
    for i in range(n - 2, -1, -1):
        cur = prices[i]
        while maxSt and prices[maxSt[-1]] <= cur:
            stPop = maxSt.pop()
            maxArrL[stPop] = i
        maxSt.append(i)

    for i in range(1, n):
        cur = prices[i]
        while minSt and prices[minSt[-1]] > cur:
            stPop = minSt.pop()
            minArrR[stPop] = i
        minSt.append(i)

    minSt = [n - 1]
    for i in range(n - 2, -1, -1):
        cur = prices[i]
        while minSt and prices[minSt[-1]] >= cur:
            stPop = minSt.pop()
            minArrL[stPop] = i
        minSt.append(i)

    totSum = 0

    for i in range(n):
        cur = prices[i]
        totSum += cur * ((maxArrR[i] - i) * (i - maxArrL[i]))

    for i in range(n):
        cur = prices[i]
        totSum -= cur * ((minArrR[i] - i) * (i - minArrL[i]))

    return totSum


"""
Stock Fluctuation
Stock prices are given in an array. price[i] is the price of day i.
For any period of time from day i to day j (i < j), the stock's fluctuation is
(maximum stock price from i to j) - (minimum stock price from i to j)
Can you find the sum of fluctuations for the stock in any contiguous periods of time?
Example 1
Input
price = [7, 10, 5, 3]
Output
29
day0 to day1: fluctuation = 10 - 7 = 3
day1 to day2: fluctuation = 10 - 5 = 5
day2 to day3: fluctuation = 5 - 3 = 2
day0 to day2: fluctuation = 10 - 5 = 5
day1 to day3: fluctuation = 10 - 3 = 7
day0 to day3: fluctuation = 10 - 3 = 7
The sum of fluctuations is 29.
Example 2
Input
price = [1, 1, 1, 2, 2, 3, 3]
Output
22
"""
