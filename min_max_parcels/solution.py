from typing import List


def minimize_maximum_parcels(parcels: List[int], extra_parcels: int) -> int:
    if not parcels:
        return extra_parcels

    mx = max(parcels)
    for val in parcels:
        extra_parcels -= mx - val
        if extra_parcels <= 0:
            return mx

    return (
        mx
        + extra_parcels // len(parcels)
        + (0 if extra_parcels % len(parcels) == 0 else 1)
    )


"""
Minimize Maximum Parcels
Distribute parcels among delivery agents in a way that minimizes the maximum number of parcels any single agent has to deliver. You're given:

An integer array parcels[i], where parcels[i] is the number of parcels currently assigned to the i-th agent.

An integer extra_parcels, which is the number of parcels that need to be distributed among the agents.

The goal is to find the minimum possible value of the maximum number of parcels any agent has after distributing the extra_parcels.


Example 1 :

Input: parcels = [6, 6, 5, 5], extra_parcels = 3
Output: 7


Example 2 :

Input: parcels = [7, 5, 1, 9, 1], extra_parcels = 25
Output: 10


Example 3 :

Input: parcels = [1], extra_parcels = 9
Output: 10
"""
