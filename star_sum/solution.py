def fiveStarReviews(productRatings, ratingsThreshold):
    avgTotal = 0
    for first, second in productRatings:
        average = first / second * 100
        avgTotal += average
    counter = 0
    currMaxIndex = None
    currMaxAvgTotal = avgTotal

    while avgTotal / len(productRatings) < ratingsThreshold:
        for index, value in enumerate(productRatings):
            first, second = value
            average = first / second * 100
            avgTotal -= average
            newAverageTotal = ((first + 1) / (second + 1) * 100) + avgTotal
            if newAverageTotal > currMaxAvgTotal:
                currMaxAvgTotal = newAverageTotal
                currMaxIndex = index
            avgTotal += average

        if currMaxIndex is not None:
            productRatings[currMaxIndex][0] += 1
            productRatings[currMaxIndex][1] += 1
            avgTotal = currMaxAvgTotal
            currMaxIndex = None

        counter += 1

    return counter


"""
Problem Statement: (Star sum / five star reviews)
Given a graph where each node is a city and each edge is the connection between two cities [from_city, to_city], you are going to build a power plant in a city. The power plant supplies power to the city where it's built, and no more than K cities directly connected to the city. Any city with power will be able to produce value. The value produced by city i is value[i] (1-based index).
Please determine which city is the optimal place for the power plant. You goal is to maximize the total value from the producing cities. Return the maximum total value.
Example
Input:

cities = 7
connections = 8
from_city = [2, 3, 4, 4, 5, 5, 6, 1]
to_city = [5, 6, 5, 1, 6, 7, 7, 7]
values = [-30, -20, 15, 30, -10, 5, 20]
k = 3

Output:
45
Explanation:
Place the power plant in city 5, so that up to k = 3 adjacent cities to node 5 can get power. Power supplies to nodes 5, 4, 6 and 7, producing a total value of 45.
Example of another suboptimal option:
Place power plant in city 6. Power supplies to node 6, 3 and 7 (do not supply to city 5 since it has a negative value). In this case, the total value is 40. Therefore it's suboptimal.
Function:
int maximumTotalValue(int cities, int connections, int[] from_city, int[] to_city, int[] values, int k)
Diagram Description:
The diagram shows a graph with 7 nodes (cities) numbered 1-7, with their corresponding values:

Node 1: value -30
Node 2: value -20
Node 3: value 15
Node 4: value 30
Node 5: value -10
Node 6: value 5
Node 7: value 20

Connections (edges):

Node 2 connects to Node 5
Node 3 connects to Node 6
Node 4 connects to Node 5
Node 4 connects to Node 1
Node 5 connects to Node 6
Node 5 connects to Node 7
Node 6 connects to Node 7
Node 1 connects to Node 7

The optimal solution places the power plant at city 5 (highlighted in the explanation), which can supply power to itself and up to k=3 adjacent cities, selecting cities 4, 6, and 7 for maximum total value of 45.
"""
