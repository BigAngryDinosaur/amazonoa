def countDecodedLetters(input):
    """
    :type input: String
    :rtype: int[]
    """

    cnts = [0] * 26

    right = len(input) - 1
    mult = 1
    while right >= 0:
        if input[right] == "x":
            index = int(input[right - 2 : right])
            cnts[index - 1] += 1 * mult
            right -= 3
            mult = 1
        elif input[right] == "]":
            left = right
            while input[left] != "[":
                left -= 1
            mult = int(input[left + 1 : right])
            right = left - 1
        else:
            index = int(input[right])
            cnts[index - 1] += 1 * mult
            right -= 1
            mult = 1

    return cnts


"""
Decoding String
A message containing uppercase letters from A–Z can be encoded using the following mapping:

A - 1
B - 2
C - 3
D - 4
E - 5
F - 6
G - 7
H - 8
I - 9
J - 10x
K - 11x
L - 12x
M - 13x
N - 14x
O - 15x
P - 16x
Q - 17x
R - 18x
S - 19x
T - 20x
U - 21x
V - 22x
W - 23x
X - 24x
Y - 25x
Z - 26x

Consecutive occurrences of any letter is encode it as letterCode[count].
For instance,
"HELLO" is encoded as "8512x[2]15x"
"AABBBB" is encoded as "1[2]2[4]"
Given an encoded message, find the count of each letter in the decoded message.
Return an array of size 26, where array[0] is the count of A, array[1] is the count of B, ...
array[25] is the count of Z
Example 1
Input
"8512x[2]15x"
Output
{0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
The decoded message is "HELLO"
Example 2
Input
18x14x18x[2]11x18x11x[3]
Output
{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 1, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0}
The decoded message is "RNRRKRKKK"
Example 3
Input
1212x12323x23123
Output
{3, 4, 3, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0}
The decoded message is "ABLABCWBCABC"
Function
int[] countDecodedLetters(String message)
"""
