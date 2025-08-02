def minTotalSum(bulb, k):
    """
    :type bulb: List[Integer]
    :type k: Integer
    :rtype: Integer
    """
    total = sum(bulb)
    current_total = 0
    mn = total if total > 0 else 0

    for end in range(len(bulb)):
        current_total += bulb[end]
        if end >= k:
            current_total -= bulb[end - k]
        if end >= k - 1:
            mn = min(mn, total - current_total)

    return mn


if __name__ == "__main__":
    bulb = [3, 3, 3, 2, 2, 1, 4, 4]
    k = 5
    bulb = [4, 9, 2, 10, 3, 5, 3]
    k = 3
    bulb = [-1, -2, -3]
    k = 1
    res = minTotalSum(bulb, k)
    print(res)
