from collections import Counter
from typing import List


def getSequence(dna: List[List[str]]) -> List[bool]:
    def isAnagramByLetterRemoval(s: str, t: str) -> bool:
        extraCharInT = None
        sCharCount = Counter(s)

        for char in t:
            if char in sCharCount:
                sCharCount[char] -= 1
                if sCharCount[char] == 0:
                    del sCharCount[char]
            elif extraCharInT and char != extraCharInT:
                return False
            else:
                extraCharInT = char

        return len(sCharCount) <= 1

    return [isAnagramByLetterRemoval(s, t) for s, t in dna]


if __name__ == "__main__":
    res = getSequence([["safddadfs", "famafmss"]])
    print(res)

"""
Similar DNA Pairs
FULLTIME
A DNA sequence is represented by a string of lowercase letters. Given a pair of DNA sequences, if the scientist is able to remove any number of a letter in sequence1 and any number of a letter in sequence2 to make the strings anagrams, then the sequences are similar.

Given n pairs of DNA sequences, for each pair, attempt to find if they are similar. Return a list of boolean values where boolean[i] indicates for the i'th pair.


Function Description

Complete the function getSequence in the editor below.

getSequence has the following parameter(s):

String dna[n][2] : the pairs of DNA sequences.

Returns

boolean[n] : 'true' if the pair is special, and 'false' otherwise


Example 1 :

Input: dna = [["safddadfs", "famafmss"]]
Output: [true]
Explanation:
The strings are anagrams after removing all the occurrences of character 'd' from s and character 'm' from t. Return [True].
Note: It is not required that all instances of a character be removed. For example, given 'aab' and 'ba', one 'a' can be removed from 'aab' to leave 'ab'.


Example 2 :

Input: dna = [["abcee", "acdeedb"], ["sljffsajej", "sljsje"]]
Output: [true, false]
Explanation:
For pair 1, remove 'b' from the second string and leave the first string untouched.
For pair 2, dna1 contains 'f' and 'a' which are not in dna2. They cannot be anagrams after removing only a character from dna1.


Constraints:

1 <= n <= 10
1 <= length of dna[i][0], dna[i][1] <= 10000.
The strings in dna1 and dna2 consist of lowercase English letters only.
"""
