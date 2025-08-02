from typing import List


def getServerIds(num_servers: int, requests: List[int]) -> List[int]:
    server = [0] * num_servers
    result = []
    for request in requests:
        if request == 0:
            server[0] += 1
            result.append(0)
            continue
        index_of_minimum, minimum_value = 0, server[0]
        for i in range(request):
            if minimum_value > server[i]:
                minimum_value = server[i]
                index_of_minimum = i
        server[index_of_minimum] += 1
        result.append(index_of_minimum)
    return result


"""
Find Minimum Load Index
Given an array of integers and a maximum capacity, assign each number to the index with the minimum load among available indices.
Input:
An integer n (representing total available indices from 0 to n-1)
An array nums where each value nums[i] represents the maximum index that can be considered for assignment (exclusive)

For each number in nums, find the index to assign it based on these rules:
1, You can only consider indices from 0 to nums[i]-1
2, Among these indices, choose the one with the minimum current load
3, If multiple indices have the same minimum load, choose the smallest index
4, After assigning a number, increment the load at that index by 1

Return an array containing the chosen index for each number.

Example 1:
Input: n = 5, nums = [1, 2, 3]
Output: [0, 1, 2]
Explanation: Each number is assigned to the first available index with load 0

Example 2:
Input: n = 3, nums = [3, 0, 2, 1]
Output: [0, 0, 1, 1]
Explanation:
- For 3: consider indices [0,1,2], all have load 0, choose 0
- For 0: no indices to consider, default to 0
- For 2: consider indices [0,1], 0 has load 2, 1 has load 0, choose 1
- For 1: consider indices [0,1], 0 has load 2, 1 has load 1, choose 1

"""
