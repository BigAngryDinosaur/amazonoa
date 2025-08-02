from collections import defaultdict
from typing import List


def getMaxRacers(speed: List[int], k: int) -> int:
    occurrencesOfSpeed = defaultdict(lambda: [])
    for i, value in enumerate(speed):
        occurrencesOfSpeed[value].append(i)

    # find the maximum number of racers at this speed with at most k other racers removed
    def maxWindowAtMostKRacersRemoved(occurrences: List[int], k: int) -> int:
        if len(occurrences) == 1:
            return 1

        maxRacers, racers = 1, 1
        left = 0
        for right in range(1, len(occurrences)):
            racers += 1
            k -= (
                occurrences[right] - occurrences[right - 1] - 1
            )  # remove racers in between ccurrences[right] and occurrences[right - 1]

            if k < 0:
                left += 1
                k += occurrences[left] - occurrences[left - 1] - 1
                racers -= 1
            else:
                maxRacers = max(maxRacers, racers)

        return maxRacers

    maxRacers = 1
    for sp in occurrencesOfSpeed:
        maxRacers = max(
            maxRacers, maxWindowAtMostKRacersRemoved(occurrencesOfSpeed[sp], k)
        )

    return maxRacers


"""
Get Max Racers
FULLTIME
HackerLand Sports Club wants to send a team for a relay race. There are n racers in the group indexed from 0 to n - 1 . The ith racer has a speed of speed[i] units.

The coach decided to send some contiguous subsegments of racers for the race i.e. racers with index i , i + 1 , i + 2 ..., j such that each racer has the same speed in the group to ensure smooth baton transfer. To achieve the goal, the coach decided to remove some racers from the group such that the number of racers with the same speed in some contiguous segment is maximum.

Given the array, racers , and an integer k , find the maximum possible number of racers in some contiguous segment of racers with the same speed after at most k racers are removed.


Function Description

Complete the function getMaxRacers in the editor.

getMaxRacers has the following parameter(s):

int speed[n] : the speeds of the racers
int k : the maximum number of racers that can be removed

Returns

int : the maximum number of racers that can be sent after removing at most k racers


Example 1 :

Input: speed = [1, 4, 4, 2, 2, 4], k = 2
Output: 3
Explanation:

It is optimal to remove the two racers with speed 2 to get the racers [1, 4, 4, 4]. Each racer with speed 4 can now be sent as they are in a contiguous segment. A maximum of 3 racers can be sent for the relay race.


Constraints:
1 ≤ n ≤ 3 * 10^5
1 ≤ k ≤ n
"""
