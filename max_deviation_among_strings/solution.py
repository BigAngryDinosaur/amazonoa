import collections


def maxDeviation(input):
    """
    :type input: String
    :rtype: int
    """
    mn, mx = 0, 0
    counts = collections.defaultdict(int)
    dev = 0

    for c in input:
        idx = ord(c) - ord("a")
        counts[idx] += 1
        mn = min(counts.values())
        mx = max(counts.values())
        dev = max(dev, mx - mn)

    if len(counts) == 1:
        return mx
    else:
        return dev


"""
Given a string of lowercase letters, return the max deviation from any substring of the input string...


"""
