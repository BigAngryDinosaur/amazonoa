def makeSubsequence(searchWord, resultWord):
    """
    :type searchWord: String
    :type resultWord: String
    :rtype: int
    """
    if not resultWord:
        return 0

    i, j = 0, 0

    while i < len(searchWord):
        if searchWord[i] == resultWord[j]:
            j += 1
        if j == len(resultWord):
            break
        i += 1

    return len(resultWord) - j


"""
Given two Strings, append minimum letters to the second String to make it a subsequence of the first String...

"""
