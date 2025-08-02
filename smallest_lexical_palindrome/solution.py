def getKeyIdentifier(key: str) -> str:
    n = len(key)
    mid = n // 2
    mid_char = key[mid] if n % 2 == 1 else ""

    counts = [0] * 26
    for i in range(mid):
        counts[ord(key[i]) - ord("a")] += 1

    half = []
    for i in range(26):
        if counts[i] > 0:
            s = chr(i + ord("a"))
            half.append(s * counts[i])

    return "".join(half) + mid_char + "".join(reversed(half))


"""
Smallest Lexical Palindrome | Compute Encoded Product Name

You team is building a keychain utility to group access keys.

Every access key is a palindromic string. A palindrome is a string that reads the same forward and backward.
The common identifier for a group of keys is obtained by rearranging the characters in one of the keys in the group into a palindrome of the smallest lexicographical order possible.
Build a function that accepts a key as the input, and finds the identifier of the group which the key belongs to.

Note that the group identifier could match the original key if it's already in the smallest lexicographical order.


Function Description

Complete the function getKeyIdentifier in the editor.

getKeyIdentifier has the following parameter:

string key : the initial key.

Returns

string : the group identifier for key


Example 1 :

Input: key = "baab"
Output: "abba"
Explanation:
Rearrange the original key to generate "abba",
which is a palindrome and also the smallest possible.


Example 2 :

Input: key = "pop"
Output: "pop"
Explanation:
The original key "pop" is already the smallest lexicographical palindrome possible, so it remains unchanged.


Example 3 :

Input: key = "zyxxxyz"
Output: "xyzxzyx"


Constraints:
1 ≤ |key| ≤ 10^5
key consists of lowercase English letters only.
key is a palindrome.


"""
