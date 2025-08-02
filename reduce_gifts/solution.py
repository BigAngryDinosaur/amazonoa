def reduceGifts(prices, k, threshold):
    if len(prices) < k:
        return 0

    prices.sort()

    sums = []

    for i in range(0, prices.len):
        sums[i] += prices[i]
        if i >= k:
            sums[i] -= prices[i - k]

    if sums[len(sums) - 1] <= threshold:
        return 0

    if sums[k] > threshold:
        return len(prices) - (k - 1)

    result = 0

    while local_sum > threshold and len(prices) > k:
        last = prices.pop()
        local_sum -= last
        local_sum += prices[len(prices) - k]
        result += 1

    return result


"""
Reduce Gifts
New Year's Day is around the corner and Amazon is having a sale. They have a list of items they are considering but they may need to remove some of them. Determine the minimum number of items to remove from an array of prices so that the sum of prices of any k items does not exceed a threshold.

Note : If the number of items in the list is less than k , then there is no need to remove any more items.


Function Description

Complete the function reduceGifts in the editor.

reduceGifts has the following parameters:

int prices[n] : the prices of each item
int k : the number of items to sum
int threshold : the maximum price of k items

Returns

int : the minimum number of items to remove


Examples and Constraints:

Solution
1, sort the whole array
2, start from the end of the array, calculate the sum K
3, maintain a rolling window of the size K, to avoid the duplicate sum K computations
4, keep iterating through the array until the sum K <= threshold.

Concerns for this approact:
when the most of the array has a sum K > threshold, in the worst case, we need to scan the full array. This is acceptable considering we already have a sort function as the maximum time complexity.

Time complexity:
O(N log N), where N is the length of the prices array.
"""
