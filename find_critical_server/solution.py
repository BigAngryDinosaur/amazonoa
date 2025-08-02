import collections


def findCriticalNodes(n, edges):
    nums = [None] * n
    lows = [0] * n
    parent = [-1] * n
    counter = 0
    articulation_points = [False] * n

    def dfs(u):
        nonlocal counter
        nums[u] = lows[u] = counter
        children = 0
        counter += 1

        for v in graph[u]:
            if nums[v] is None:
                parent[v] = u
                children += 1
                dfs(v)

                if (parent[u] == -1 and children > 1) or (
                    parent[u] != -1 and lows[v] >= nums[u]
                ):
                    articulation_points[u] = True

                lows[u] = min(lows[u], lows[v])
            elif parent[u] != v:
                lows[u] = min(lows[u], nums[v])

    graph = collections.defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    for u in range(n):
        if nums[u] is None:
            dfs(u)

    return [i for i in range(n) if articulation_points[i]]


if __name__ == "__main__":
    # n = 7
    # edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
    n = 8
    edges = [[0, 1], [1, 2], [3, 2], [3, 4], [4, 6], [5, 6], [6, 7]]
    res = findCriticalNodes(n, edges)
    print(res)

"""
Find Critical Nodes
Given an undirected graph, find out all the vertices when removed will make the graph disconnected.  Initially the graph is connected.

For example given the graph below:


Return [3, 6]. Because we can make the graph disconnected by removing either vertex 3 or vertex 6.

Input:

nodeNum, the total count of vertices in the graph. Each vertex has an unique id in the range from 0 to nodeNum - 1 inclusive.

edges, a list of integer pairs representing all the edges on the graph.

output:

A list of integers representing the ids of the articulation points.

example:

Input:

nodeNum = 7

edges = [[0,1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3,4]]

Output:

[2,3,5]


"""
