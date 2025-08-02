import heapq


def getItems(entries):
    """
    :type entries: List[str]
    :rtype: List[str]
    """
    mn = []
    heapq.heapify(mn)

    mx = []
    heapq.heapify(mx)

    res = []

    for action, name, price in entries:
        if action == "INSERT":
            heapq.heappush(mx, (-int(price), name))
            p, n = heapq.heappop(mx)
            heapq.heappush(mn, (-p, n))
        else:
            p, n = heapq.heappop(mn)
            heapq.heappush(mx, (-p, n))
            res.append(n)

    return res


"""

"""
