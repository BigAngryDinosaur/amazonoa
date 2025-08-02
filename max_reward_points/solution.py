import heapq


def calculate_maximum_reward_points(reward_values):
    accumulated_points = 0
    item_count = 0
    reward_heap = [-value for value in reward_values]
    heapq.heapify(reward_heap)

    ## when the next top of the heap value smaller than the items Purchased, we know all the rewards are below zero
    while reward_heap and -reward_heap[0] > item_count:
        top_reward = -heapq.heappop(reward_heap)
        adjusted_reward = top_reward - item_count
        accumulated_points += adjusted_reward
        item_count += 1

    return accumulated_points


"""
Max Reward Points
INTERN
An online shopping website periodically has offers to attract more customer.

It recently launched an offer for n items in its inventory, where the ith item offered reward[i] reward points to the customer purchasing the item. Every time an offer-bearing item is purchased, the customer gains the reward points associated with that item. Then the reward points of the remaining items are reduced by 1 unless it will reduce the points below 0 .

Note

Each item can be purchased at most once, in other words, reward[i] becomes 0 after the ith item is purchased.


Function Description

Complete the function getMaxRewardPoints in the editor.

getMaxRewardPoints has the following parameter(s):

int reward[n] : the reward points of each item

Returns

long_int : the maximum reward points which can be collected


Example 1 :



Input: reward = [5, 2, 2, 3, 1]
Output: 7
Explanation: Considering 0-based indexing, the items can be purchased in the following order:
1. First, purchase item 2, points earned = reward[2] = 2. Points of remaining items after this purchase reward = [4, 1, 0, 2, 0].
2. Next, purchase item 3, points earned = reward[3]= 2. Points of remaining items after this purchase reward = [3, 0, 0, 0, 0].
3. Finally, purchase item 0, points earned = reward[0] = 3. Points of remainig items after this purchase reward = [0, 0, 0, 0, 0]
At this point, no items have reward points left. The maximum reward points is 2 + 2 + 3 = 7.


Example 2 :

Input: reward = [5 ,5 ,5]
Output: 12
Explanation: Using 0-based indexing, the items can be purchased in the following order:
1. First, purchase item 0, points earned = reward[0] = 5. Points of remaining items after this purchase reward = [0, 4, 4].
2. Next, purchase item 1, points earned to = reward [1] = 4. and reward = [0, 0, 3].
3. Finally, purchase item 2, points earned = reward[2] = 3 and reward = [0, 0, 0].
The maximum reward points is (5 + 4 + 3 = 12).


Constraints:

1 <= n <= 105
0 <= reward[i] <= 106

Solution
1. Create a heap with the maximum reward at the top.
2. Keep polling from the heap. Subtract the number of items purchased from each polled value.
3. Stop when all the remaining items' values fall below zero. We know this when peeking at the heap and the top value is smaller than the number of items purchased.

Time Complexity
Average: O(n)
Worst: O(n logn)
- The heapify is O(n). This is important because using a heap here will be faster than directly sorting, in general. So don't sort directly.
- The worst case is still O(n log n), when we have to go through the entire heap to get the final answer.

"""
