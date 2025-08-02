from collections import Counter
from typing import List


def getMaxTotalArea(stick_lengths: List[int]) -> int:
    if len(stick_lengths) < 4:
        return 0

    MODULUS = 1_000_000_007
    length_count = Counter(stick_lengths)
    distinct_sorted_lengths = sorted(length_count.keys(), reverse=True)

    total_area = 0
    last_side = 0

    for current_length in distinct_sorted_lengths:
        count = length_count[current_length]
        pairs = count // 2

        if pairs > 0:
            if last_side > 0:
                total_area += current_length * last_side
                pairs -= 1
                if pairs > 0:
                    total_area += current_length * current_length * pairs
                    last_side = 0
                else:
                    total_area += current_length * current_length * (pairs - 1)
                    last_side = current_length
                length_count[current_length] = count % 2

        if (
            length_count[current_length] == 1
            and length_count.get(current_length - 1, 0) > 0
        ):
            if last_side > 0:
                total_area += (current_length - 1) * last_side
                last_side = 0
            else:
                last_side = current_length - 1
            length_count[current_length] = 0
            length_count[current_length - 1] -= 1

    return int(total_area % MODULUS)


"""
Max Total Area of Rectangles
FULLTIME
You will be given n sticks and the player is required to form rectangles from those sticks.

Formally, given an array of n integers representing the lengths of the sticks, you are required to create rectangles using those sticks. Note that a particular stick can be used in at most one rectangle and in order to create a rectangle we must have exactly two pairs of sticks with the same lengths. For example, you can create a rectangle using sticks of lengths [2, 2, 5, 5] and [4, 4, 4, 4] but not with [3, 3, 5, 8] . The goal of the game is to maximize the total sum of areas of all the rectangles formed.

In order to make the game more interesting, we are allowed to reduce any integer by at most 1. Given the array sideLengths , representing the length of the sticks, find the maximum sum of areas of rectangles that can be formed such that each element of the array can be used as length or breadth of at most one rectangle and you are allowed to decrease any integer by at most 1. Since this number can be quite large, return the answer modulo 10^9+7 .

Note: It is not a requirement that all side lengths be used. Also, a modulo b here represents the remainder obtained when an integer a is divided by an integer b .


Function Description

Complete the function getMaxTotalArea in the editor.

getMaxTotalArea has the following parameter(s):

int sideLengths[n] : the side lengths that can be used to form rectangles

Returns

int : the maximum total area of the rectangles that can be formed, modulo (109 +7) .


Example 1 :

Input: sideLengths = [2, 6, 2, 6, 3, 5]
Output: 12
Explanation: The lengths 2, 2, 6, and 6 can be used to form a rectangle of area 2*6=12. No other rectangles can be formed with the remaining lengths. The answer is 12 modulo (109+7)=12.


Example 2 :

Input: sideLengths = [2, 3, 3, 4, 6, 8, 8, 6]
Output: 54
Explanation: Two rectangles can be formed. One has sides of 6 and 8, and the other by reducing 4 and one of the 3s by 1 has sides of 2 and 3. The total area of these rectangles is (6*8+2*3) mod (109+7) = 54.


Example 3 :

Input: sideLengths = [3, 4, 5, 5, 6]
Output: 20
Explanation: The rectangle can have either sides of 5 and 3 (reduce 4 by 1), or sides of 5 and 4 (reduce 6 and one 5 by 1). The second option has a greater area, so 5*4 > 3*5.


Constraints:

1 ≤ n ≤ 105
2 ≤ sideLengths[i] ≤ 104 where 0 ≤ i < n


solution:
Time Complexity
Counting stick lengths: O(n), where n is the number of sticks.
Creating and sorting unique lengths: O(k log k), where k is the number of unique lengths.
Overall time complexity: O(n + k log k), where n is the total number of sticks and k is the number of unique lengths. In the worst case where all lengths are unique, this becomes O(n log n).

Space Complexity
O(k), where k is the number of unique lengths. In the worst case, this could be O(n) if all lengths are unique.
"""
