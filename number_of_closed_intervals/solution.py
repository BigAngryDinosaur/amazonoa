from typing import List


def number_of_items(s: str, ranges: List[List[int]]) -> List[int]:
    n = len(s)
    prefix_sums = {}
    cur_sum = 0
    for i in range(n):
        if s[i] == "|":
            prefix_sums[i] = cur_sum
        else:
            cur_sum += 1

    left_bounds = [-1] * n
    last = -1
    for i in range(n):
        if s[i] == "|":
            last = i
        left_bounds[i] = last

    right_bounds = [-1] * n
    last = -1
    for i in reversed(range(n)):
        if s[i] == "|":
            last = i
        right_bounds[i] = last

    res = []
    for start_i, end_i in ranges:
        start = right_bounds[start_i]
        end = left_bounds[end_i]
        if start != -1 and end != -1 and start < end:
            res.append(prefix_sums[end] - prefix_sums[start])
        else:
            res.append(0)

    return res


"""
Number Of Closed Intervals
A librarian would like to count the number of enclosed * in a row that are between two dividers of |. A row is represented by a string s of * and |. A list of range tuples are given that represent each substring to consider, and the number of enclosed items for each substring must be returned in a list.
* = ascii number 42
| = ascii number 124

Example 1:
Input: s = |**|*|*, ranges = [[0, 4], [1, 6]]
Output: [1, 2]
Explanation:
The first range to consider is [0, 4] which corresponds to |**|*. There are 2 items in the first enclosed part.
For the second range, [1, 6], the substring is **|*|*, which contain only one enclosed section with one item in it.
Both of the answers are returned in an array, ie. [2, 1].

Example 2:
Input: s = *|*|, ranges = [[1, 3]]
Output: [1]
Explanation:
The substring from index = 1 to index = 3 is |*|. There is only one item and it is surrounded by two dividers. Therefore, the output is [1].

Constraints:
There are no invalid characters, and each range is non-zero in size and always increasing. The ranges provided are always within the string bounds.


Solution
Brute force Solution:
To find the number of enclosed items in a given range, we can simple do a linear scan and start counting after we encounter any | (since we need a left boundary to start a container). If the last element in the range is not a | then move back to the last | while subtracting item count.None
This works but for each query, we would need a linear scan. For an array with M elements and N queries, the complexity is O(MN).


Prefix Sum Solution:
An item "*" has to be enclosed in "|"s to be counted as an enclosed item. A valid range has to include both boundaries to enclose the item. Therefore whether an item is enclosed within a given range is decided by the indices of its boundaries rather than its own index. Now the problem becomes how to find the number of enclosed items within a pair of "|" quickly. And we can do this with the prefix sum algorithm:
"""
