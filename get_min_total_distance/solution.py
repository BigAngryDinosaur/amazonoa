import math
from typing import List


def getMinTotalDistance(dist_centers: List[int]) -> int:
    dist_centers.sort()
    mn = math.inf
    n = len(dist_centers)

    for pivot in range(1, n):
        w1 = (pivot - 1) // 2
        w2 = (pivot + n - 1) // 2
        # w2 = pivot + (n-1 - pivot) // 2

        dist = 0

        for i in range(pivot):
            dist += abs(dist_centers[w1] - dist_centers[i])

        for i in range(pivot, n):
            dist += abs(dist_centers[w2] - dist_centers[i])

        mn = min(mn, dist)

    return int(mn)


"""
Get Minimum Total Distance
FULLTIME
There are n distribution centers, all built along a straight line. They plan to build two warehouses to serve the distribution centers. A distribution center has its demands met by the warehouse that is closest to it. Position the warehouses optimally, such that the sum of distances from the distribution centers to their closest warehouse is minimized.

Given an array dist_centers, that represent the positions of the distribution centers, return the minimum sum of distances to their closest warehouses if the warehouses are positioned optimally.


Function Description

Complete the function getMinTotalDistance in the editor.

getMinTotalDistance has the following parameter:

int dist_centers[n] : the locations of the distribution centers

Returns

int: the minimum sum of distances


Example 1 :

Input: dist_centers = [4, 1, 5, 99, 100]
Output: 5
Explanation: One optimal solution is to position warehouse at w1 = 4, w2 = 99.


Example 2 :

Input: dist_centers = [1, 2, 3]
Output: 1
Explanation: One optimal solution is to position the warehouses at w1 = 1 and w2 = 2.

The minimum sum of the distances between distribution centers and the warehouses closest to them is 0 + 0 + 1 = 1.

"""
