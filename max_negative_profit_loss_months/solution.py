from heapq import heappop, heappush


def maximizeNegativePnLMonths(monthly_profits):
    # max heap
    negative_values = []
    negative_month_count = 0
    running_total = 0

    for current_profit in monthly_profits:
        # Case 1: Check if making current month will create a negative sum
        if (running_total - current_profit) > 0:
            # We can make this month negative without affecting overall positivity
            running_total -= current_profit
            heappush(negative_values, -current_profit)  # Store negative for max heap
            negative_month_count += 1

        # Case 2: Check if we can swap with a previously inverted larger negative value
        elif negative_values and -negative_values[0] > current_profit:
            # Undo a previous larger negative and use this smaller one instead
            prev = -heappop(negative_values)  # Convert back to positive
            running_total += prev * 2 - current_profit
            heappush(negative_values, -current_profit)  # Store negative for max heap

        # Case 3: Can't make this month negative, keep it positive
        else:
            running_total += current_profit

    return negative_month_count


"""
Maximize Negative PnL Months
FULLTIME
You are analyzing the stock trends. There is a service model returned an array of integers, PnL (Profit and Loss) , for your portfolio representing that in the ith month, you will either gain or lose PnL[i] . All reported PnL values are positive, representing gains.

As part of the analysis, you will perform the following operation on the PnL array any number of times:

Choose any month (0 ≤ i < n) and multiply PnL[i] by -1
Find the maximum number of months you can afford to face a loss, i.e., have a negative PnL, such that the cumulative PnL for each of the n months remains strictly positive i.e. remains greater than 0.

Note : The cumulative PnL for the ith month is defined as the sum of PnL from the starting month up to the ith month. For example, the cumulative PnL for the PnL = [3, -2, 5, -6, 1] is [3, 1, 6, 0, 1].


Function Description

Complete the function maximizeNegativePnLMonths in the editor.

maximizeNegativePnLMonths has the following parameter:

int[] PnL : an array of integers representing the Profit and Loss for each month

Returns

int : the maximum number of months with a negative PnL such that the cumulative PnL remains positive


Example 1 :

Input: PnL = [5, 3, 1, 2]
Output: 2
Explanation: Some of the possible arrays after performing the given operation some number of times:

| Modified PnL | Cumulative PnL | Number of negatives | Is Valid | Comments |
|--------------|----------------|-------------------|----------|----------|
| [5, -3, -1, 2] | [5, 2, 1, 3] | 2 | Yes | • The operation was performed on the second and third months (in bold).<br>• All the cumulative PnL are positive |
| [5, -3, -1, -2] | [5, 2, 1, -1] | 3 | No | • The last cumulative PnL is negative, hence this is not valid |
| [5, -3, 1, -2] | [5, 2, 3, 1] | 2 | Yes | • All the cumulative PnL are positive |
| [-5, 3, 1, 2] | [-5, -2, -1, 1] | 1 | No | • The cumulative PnL for the first three months are negative |


Example 2 :

Input: PnL = [1, 1, 1, 1, 1]
Output: 2
Explanation: There are multiple possible PnLs such as [1, -1, -1, 1, 1], [-1, 1, -1, 1, -1], etc.
However, it is optional to modify the PnL to be [1, 1, -1, 1, -1] or [1, 1, 1, -1, -1].


Example 3 :

Input: PnL = [5, 2, 3, 5, 2, 3]
Output: 3
Explanation:
The possible PnLs such that all the cumulative PnLs are positive are:
[5, 2, -3, 5, 2, -3]
[5, 2, 3, 5, -2, -3]
[5, -2, 3, 5, -2, -3]
...
The max num of negatives we can have ensuring that all the culmulative PnLs are positive is 3 corresponding to the case [5, -2, 3, 5, -2, -3]
Note that [5, 2, 3, -5, -2, -3] is not a valid case as the culative PnLs are [5, 7, 10, 5, 2, 0] but they must be strictly positive.


Constraints:
1 <= n <= 10
1 <= PnL[i] <= 109


Solution
Go over the input array. For each PnL, there are two basic cases:
1, If it's smaller than the running total, we definitely invert it. This adds one to our count in the result, which is optimal - we cannot do better by skipping it.
2, If it's larger than the current running total, we cannot directly invert it. We then have two choices:
i) Look back through the heap, pick the largest item, and try to swap it with the current PnL, as this will give us a better running total
ii) If the current PnL is smaller than the largest item in the heap, there's no need to swap

Algorithm: Greedy Time Complexity: O(nlogn)
"""
