from typing import List


def getMinimumBoxes(boxes: List[int], capacity: int) -> int:
    boxes.sort()
    start = 0
    mx = 0

    for end in range(len(boxes)):
        while boxes[end] > capacity * boxes[start]:
            start += 1

        if end - start + 1 > mx:
            mx = end - start + 1

    return len(boxes) - mx


"""
Get Minimum Boxes
Alex is shipping the last container of the day, trying to load all n boxes into the container with their sizes represented in the array boxes . The container may not have enough capacity for all the boxes. So some of the boxes may have to be removed. The boxes in the container must satisfy the condition max(boxes) ≤ capacity * min(boxes) .

Given the array, boxes , and capacity , find the minimum number of boxes that need to be removed.


Function Description

Complete the function getMinimumBoxes in the editor.

getMinimumBoxes has the following parameters:

int[] boxes : an array of integers representing the sizes of the boxes
int capacity : the capacity index of the container

Returns

int: the minimum number of boxes that need to be unloaded


Example 1 :

Input: boxes = [1, 4, 3, 2], capacity = 2
Output: 1
Explanation:

This satisfies the required condition. Hence the answer is 1.


Example 2 :

Input: boxes = [3000, 1, 6, 40, 210], capacity = 5
Output: 4
Explanation:
Only 1 of the boxes can be loaded into the container.
"""
