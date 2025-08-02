from queue import PriorityQueue


def findPairs(arr, N):
    """
    :type arr: List[Integer]
    :type N: Integer
    :rtype: List[Integer]
    """

    pq = PriorityQueue()

    def helper(sub_list, index):
        if len(sub_list) == 2:
            diff = abs(sub_list[0] - sub_list[1])
            pq.put((diff, list(sub_list)))

        for i in range(index, len(N)):
            sub_list.append(N[i])
            helper(sub_list, i + 1)
            sub_list.pop()

    helper([], 0)

    result = []
    while not pq.empty() and arr > 0:
        result.append(pq.get()[0])
        arr -= 1
    return result


"""
Find Pairs
Given an integer array, we need to find the pairs from this array with the minimum delta. The delta of a pair is the difference between the two integers. Sort all the pairs by the delta and return the the first N pairs with the minimum delta.
Example1:
Input:
arr = [1, 5, 2]
N = 2
Pairs:
[1, 5], delta = 4
[1, 2], delta = 1
[5, 2], delta = 3
Output:
[1, 3]

Example2:
Input:
arr = [2, 5, 3, 2]
N = 3
Pairs:
[2, 5], delta = 3
[2, 3], delta = 1
[2, 2], delta = 0
[5, 3], delta = 2
[5, 2], delta = 3
[3, 2], delta = 1
Output:
[0, 1, 1]
Signature:
int[] FindPairs(int[] arr, int N)
"""
