from typing import List


def getTimes(numCustomers: int, time: List[int], direction: List[int]) -> List[int]:
    en, ex = [], []
    res = [0] * len(time)
    for i, t in enumerate(time):
        if direction[i] == 1:
            ex.append([time[i], i])
        else:
            en.append([time[i], i])

    timeCounter, lastTurn = 0, -1  # time is 0 at the beginning and -1
    # indicates nothing happened at prior time
    while ex or en:
        # Process the exit queue if and only if following conditions are satisfied
        # If exit queue is not empty and the person at the front of the queue can go out based on his time stamp
        # and ( Nothing happened at last time stamp i.e. nobody moved in or out so lastTurn will be -1 in this case
        # or, somebody moved out at last time stamp, in this case lastTurn will be 1
        # or, nobody is there in the entrance queue
        # or, at last time stamp somebody got in but the person at the front of the queue can't go in due to their timestamp
        if (
            ex
            and ex[0][0] <= timeCounter
            and (
                lastTurn == -1
                or lastTurn == 1
                or not en
                or (lastTurn == 0 and en[0][0] > timeCounter)
            )
        ):
            res[ex[0][1]] = timeCounter
            lastTurn = 1
            ex.pop(0)
        elif en and en[0][0] <= timeCounter:
            res[en[0][1]] = timeCounter
            lastTurn = 0
            en.pop(0)
        else:
            lastTurn = -1

        timeCounter += 1

    return res


"""
Turnstile
A warehouse has one loading dock that workers use to load and unload goods.
Warehouse workers carrying the goods arrive at the loading dock at different times. They form two queues, a "loading" queue and an "unloading" queue. Within each queue, the workers are ordered by the time they arrive at the dock.
The arrival time (in minutes) array stores the minute the worker arrives at the loading dock. The direction array stores whether the worker is "loading" or "unloading", a value of 0 means loading and 1 means unloading. Loading/unloading takes 1 minute.
When a worker arrives at the loading dock, if no other worker is at the dock at the same time, then the worker can use the dock.
If a "loading" worker and an "unloading" worker arrive at the dock at the same time, then we decide who can use the dock with these rules:
1,if the loading dock was not in use in the previous minute, then the unloading worker can use the dock.
2,if the loading dock was just used by another unloading worker, then the unloading worker can use the dock.
3,if the loading dock was just used by another loading worker, then the loading worker can use the dock.
Return an array of the time (in minute) each worker uses the dock.

Example:
Input:
time = [0, 0, 1, 6] direction = [0, 1, 1, 0]

Output:
[2, 0, 1, 6]

Explanation:
At time 0, worker 0 and 1 want to use the dock. Worker 0 wants to load and worker 1 wants to unload. The dock was not used in the previous minute, so worker 1 unload first.
At time 1, workers 0 and 2 want to use the rock. Worker 2 wants to unload, and at the previous minute the dock was used to unload, so worker 2 uses the dock.
At time 2, worker 0 is the only worker at the dock, so he uses the dock.
At time 6, worker 3 arrives at the empty dock and uses the dock.
We return [2, 0, 1, 6].


"""
