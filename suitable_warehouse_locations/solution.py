def suitableLocations(center, d):
    def distance(mid):
        total = 0
        for c in center:
            total += 2 * abs(c - mid)
        return total

    def binarySearch(floor, ceil, findUpperBound):
        bound = -1
        while floor <= ceil:
            mid = floor + (ceil - floor) >> 1
            dist_mid = distance(mid)
            dist_mid_next = distance(mid + 1)

            if dist_mid <= d:
                bound = mid
                if findUpperBound:
                    floor = mid + 1
                else:
                    ceil = mid - 1
            elif dist_mid < dist_mid_next:
                ceil = mid - 1
            else:
                floor = mid + 1
        return bound

    lowerBound = binarySearch(-1000000000, 1000000000, False)
    if lowerBound < 0:
        return 0

    upperBound = binarySearch(lowerBound, 1000000000, True)
    return upperBound - lowerBound + 1


"""
Problem:

Suitable Warehouse Locations
FULLTIME
The world is represented by a number line from -109 to 109. There are n delivery centers, the ith one at location center[i]. A location x is called a suitable location for a warehouse if it is possible to bring all the products to that point by traveling a distance of no more than d. At any one time, products can be brought from one delivery center and placed at point x. Given the positions of n delivery centers, calculate the number of suitable locations in the world. That is, calculate the number of points x on the number line (-109 ≤ x ≤ 109) where the travel distance required to bring all the products to that point is less than or equal to d.

Note: The distance between point x and center[i] is |x - center[i]|, their absolute difference.


Example 1:

Input: center = [-2, 1, 0], d = 8

Output: 3

Explanation:
Initially, delivery centers locate at -2, 1 and 0:
chart-trips
The various locations along with the distance traveled to bring all treasures at that point are -

Locate the warehouse at x = -3: First bring products from center[0] = -2 covering a distance of |-3 - (-2)| = 1 to reach the center and |-3 - (-2)| = 1 to return. Similarly we bring products from centers 1 and 2 to point -3 for total distance of 1 + 1 + 4 + 4 + 3 + 3 = 16 which is > d. This is not a suitable location.
chart-trips
Locate the warehouse at x = 0, total distance traveled is 2 * |0 - (-2)| + 2 * |0 - 1| + 2 * |0 - 0| = 6 ≤ d. This is a suitable location.
chart-trips
Locate the warehouse at x = -1, total distance traveled is 2 * |-1 - (-2)| + 2 * |-1 - 1| + 2 * |-1 - 0| = 8 ≤ d. This is a suitable location.
chart-trips
Locate the warehouse at x = 1, total distance traveled is 2 * |1 - (-2)| + 2 * |1 - 1| + 2 * |1 - 0| = 8 ≤ d. This is a suitable location.
chart-trips
The only suitable location are {-1, 0, 1}. So return 3.

Example 2:

Input: center = [2, 0, 3, -4], d = 22

Output: 5

Explanation:
There are 5 suitable locations i.e {-1, 0, 1, 2, 3}.

Place a warehouse at x = -1, total distance traveled is 2 * |-1 - 2| + 2 * |-1 - 0| + 2 * |-1 - 3| + 2 * |-1 - (-4)| = 22 ≤ d.
x = 0, total distance traveled is 2 * |0 - 2| + 2 * |0 - 0| + 2 * |0 - 3| + 2 * |0 - (-4)| = 18 ≤ d.
x = 1, total distance traveled is 2 * |1 - 2| + 2 * |1 - 0| + 2 * |1 - 3| + 2 * |1 - (-4)| = 18 ≤ d.
x = 2, total distance traveled is 2 * |2 - 2| + 2 * |2 - 0| + 2 * |2 - 3| + 2 * |2 - (-4)| = 18 ≤ d.
x = 3, total distance traveled is 2 * |3 - 2| + 2 * |3 - 0| + 2 * |3 - 3| + 2 * |3 - (-4)| = 22 ≤ d.

Example 3:

Input: center = [-3, 2, 2], d = 8

Output: 0

Explanation:
It can be shown that there are no suitable locations. For example, if a warehouse is placed at x = 2, then total distance traveled is 2 * |2 - (-3)| + 2 * |2 - 2| + 2 * |2 - 2| = 10 > d.


Function Description
Complete the function suitableLocations in the editor below.
suitableLocations has the following parameters:
int center[n]: the positions of delivery centers
long d: the maximum total travel distance for a suitable location


Returns
int: the number of suitable locations.


Constraints
1 ≤ n ≤ 105
-109 ≤ packageweight[i] ≤ 109
0 ≤ d ≤ 105


Solution
1, We use binary search to find the boundary of the target ranges.
2, Binary search makes the time complexity O(log N), faster than checking every possible position.
3, The first binary search starts with -10^9 and 10^9, because the question defines that center values are in this range.
4, After exiting the first binary search, we get the lower bound of the solution.
5, If no lower bound is found (lowerBound < 0), we return 0 as there are no suitable locations.
6, We then perform a second binary search to find the upper bound of the solution. This search starts from the lower bound we just found, as we know there are no solutions below it.
7, The upper bound search continues up to 10^9 to ensure we find the highest possible position that satisfies the condition.
8, Finally, we return the number of suitable locations, [lower bound, upper bound]

Time Complexity O(log N)

"""
