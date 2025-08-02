def packaging(numGroups, arr):
    """
    :type numGroups: int
    :type arr: List[int]
    :rtype: int
    """
    maxItems = 0
    if not arr or not numGroups:
        return 0
    for a in sorted(arr):
        if a > maxItems:
            maxItems += 1
        elif a == maxItems:
            continue
        else:
            return maxItems
    return maxItems


"""
Packaging Automation
The Fulfillment Center consists of a packaging bay where orders are automatically packaged in groups(n). The first group can only have 1 item and all the subsequent groups can have one item more than the previous group. Given a list of items on groups, perform certain operations in order to satisfy the constraints required by packaging automation.
The conditions are as follows:
-The first group must contain 1 item only.
-For all other groups, the difference between the number of items in adjacent groups must not be greater than 1. In other words, for 1<=i<n, arr[i]-arr[i-1]<=1

To accomplish this, the following operations are available:
- Rearrange the groups in any way.
- Reduce any group to any number that is at least 1
Write an algorithm to find the maximum number of items that can be packaged in the last group with the conditions in place.

Input
The function/method consists of two arguments:
numGroups, an integer representing the number of groups(n);
arr, a list of integers representing the number of items in each group

Output
Return an integer representing the maximum items that can be packaged for the final group of the list given the conditions above.

Example1:
Input:
[3,1,3,4]
Output:
4
Explanation:
Subtract 1 from the first group making the list [2, 1, 3, 4]. Rearrange the list into [1, 2, 3, 4]. The final maximum of items that can be packaged in the last group is 4.
Example2:
Input:
[1,3,2,2]
Output:
3
Example3:
Input:
[1,1,1,1]
Output:
1
Example4:
Input:
[3,2,3,5]
Output:
4




"""
