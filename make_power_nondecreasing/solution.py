from typing import List


def makePowerNonDecreasing(power: List[int]) -> int:
    totalAdditionalPower = 0
    for i in range(1, len(power)):
        if power[i] < power[i - 1]:
            totalAdditionalPower += power[i - 1] - power[i]

    return totalAdditionalPower


if __name__ == "__main__":
    res = makePowerNonDecreasing([3, 4, 1, 6, 2])
    print(res)


"""
Make Power Nondecreasing
In a scalable system, a set of n servers are used for horizontally scaling an application.

The goal is to have the computational power of the servers in non-decreasing order. To do so, you can increase the computational power of each server in any contiguous segment by x. Choose the values of x such that after the computational powers are in non-decreasing order , the sum of the x values is minimum.


Example 1 :

Input: power = [3, 4, 1, 6, 2]
Output: 7
Explanation: Add 3 units to the subarray [2, 4] and 4 units to the subarray [4, 4,]. The final arrangement of the server is: [3, 4, 4, 9, 9]. The ans is 3 + 4 = 7. (As shown in the image)



Constraints:
1 <= n <= 105
1 <= power[i] <= 109
"""
