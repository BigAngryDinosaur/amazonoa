from typing import List


def fortunetelling(m: int, a: List[int], b: List[int]) -> int:
    idxMax, maxValue = 0, a[0]
    idxMin, minValue = 0, a[0]
    for i, val in enumerate(a):
        if maxValue < val:
            idxMax, maxValue = i, val
        if minValue >= val:
            idxMin, minValue = i, val

    result = maxValue - minValue
    if m == 0:
        return result

    if a[idxMax] > b[idxMax]:
        x, y = a[idxMax], b[idxMax]
        a[idxMax], b[idxMax] = y, y  # avoid future flips
        result = min(result, fortunetelling(m - 1, a, b))
        a[idxMax], b[idxMax] = x, y

    if a[idxMin] < b[idxMin]:
        p, q = a[idxMin], b[idxMin]
        a[idxMin], b[idxMin] = q, q  # avoid future flips
        result = min(result, fortunetelling(m - 1, a, b))
        a[idxMin], b[idxMin] = p, q

    return result


"""
Fortune Telling
Given a collection of n cards. The i-th card (1 ≤ i ≤ n) has a number Ai on its front and a number Bi on its back. At the start, all the cards are facing upwards. He wants to minimize the range of numbers (i.e. the difference between the maximum and minimum values) on the face-up side. He is allowed to flip a maximum of m cards. Flipping a card will transition Bi to the face up side and Ai to the back. Help him find the minimum possible range after using at most m flips.

Input

The first line of the input consists of 2 integers n and m . The next line contains n integers, i-th of which denotes Ai . The next line contains n integers, i-th of which denotes Bi .

Output

Output a single integer, the minimum possible range.


Example 1 :

Input: n = 5, m = 2, A = [1, 2, 17, 16, 9], B = [3, 4, 5, 6, 11]
Output: 8
Explanation: By flipping card 3 and 4, we get the face up numbers {1, 2, 5, 6, 9}. This makes range=9-1=8.


Constraints:
1 <= m <= n
1 <= Ai, Bi <= 107
"""
