from typing import List


def binary_search(array: List[int], target: int, find_right: bool = False) -> int:
    left, right = 0, len(array)

    while left < right:
        mid = (left + right) // 2
        if array[mid] < target or (find_right and array[mid] == target):
            left = mid + 1
        else:
            right = mid

    return left


def processExecution(
    values: List[int], min_thresholds: List[int], max_thresholds: List[int]
) -> List[List[int]]:
    values.sort()
    array_length = len(values)

    # Create prefix sum array to store cumulative sums
    prefix_sums = [0] * (array_length + 1)
    for i in range(1, array_length + 1):
        prefix_sums[i] = prefix_sums[i - 1] + values[i - 1]

    results = []
    for i in range(len(min_thresholds)):
        # Find leftmost value >= min_threshold
        left_bound = binary_search(values, min_thresholds[i])
        # Find rightmost value <= max_threshold
        right_bound = binary_search(values, max_thresholds[i], find_right=True)

        # Calculate count of values in range and their sum
        count = right_bound - left_bound
        range_sum = prefix_sums[right_bound] - prefix_sums[left_bound]

        results.append([count, range_sum])

    return results


"""
Execute Processes II
FULLTIME
There are n processes to be executed and m processors to execute them. The ith process requires power[i] for execution. A processor can provide power within its range minPower through maxPower[i]. Process i can be executed on processor j if minPower[j] ≤ power[i] ≤ maxPower[j].

Given the power consumption of n processes, the range of processor power in m processors, find:
the number of processes which can be executed on the processor
the sum of power consumed by the processes that it can serve

Function Description
Complete the function processExecution in the editor.

Input:
int power[n]: the power consumption of processes
int minPower[m]: the minimum bounds of the ranges of processor power
int maxPower[m]: the maximum bounds of the ranges of processor power

Returns
long_int[m][2]: the ith element of this array consists of 2 integers - the number of processes that lie within the range of the ith processor, and the sum of the power consumption of those processes.

Example 1 :



Input: power = [7, 6, 8, 10], minPower = [6, 3, 4], maxPower = [10, 7, 9]
Output: [[4, 31], [2, 13], [3, 21]]
Explanation:
The answer for each of the processors are [4, 31], [2, 13], [3, 21], where the first num represents the num of processes, and the second is the sum of power requirements. Return the 2-dimensional array, [[4, 31], [2, 13], [3, 21]]


Example 2 :

Input: power = [11, 11, 11], minPower = [8, 13], maxPower = [11, 100]
Output:[[3, 33], [0, 0]]
Explanation:
The first processor (minPower[0] = 8, maxPower[0] = 11) can execute all 2 processes, and sum of powers = (11 + 11 + 11) = 33.
The second processor (minPower[1] = 13, maxPower[1] = 100) cannot execute any of the processes since none of them lie in its range. Thus, its number of processes = 0 and power consumed = 0.


Solution
Time Complexity: O((m+n) * log(n))
"""
