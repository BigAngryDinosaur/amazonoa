import collections


def splitString(S, K):
    """
    :type S: String
    :type K: Integer
    :rtype: Integer
    """
    right = collections.Counter(S)
    left = set()
    comm = set()
    res = 0
    for ch in S:
        right[ch] -= 1
        left.add(ch)
        if right[ch] >= 1 and ch in left:
            comm.add(ch)
        if right[ch] == 0 and ch in comm:
            comm.remove(ch)
        if len(comm) >= K:
            res += 1
    return res


"""
Split String
Given a string S and an integer K, split S into two substrings S1 and S2 where the number of their common characters >= K. Return the number of such splits in S.
Example:
input:
S = "abcca"
K = 2
output:
1
Explanation:
"abc", "ca"
Example2:
input:
S = "abcdea"
K = 1
output:
5
Explanation:
"a", "bcdea"
"ab", "cdea"
"abc", "dea"
"abcd", "ea"
"abcde", "a"
"""
