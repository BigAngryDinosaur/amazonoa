def bestCombos(rating, k):
    n = len(rating)
    KArr = [rating[0]]
    for i in range(1, n):
        cur_KArr_len = len(KArr)
        for j in range(cur_KArr_len):
            KArr.append(KArr[j] + rating[i])
        KArr.append(rating[i])
    minIndex = k
    KArr.sort(reverse=True)
    for i in range(k):
        if KArr[i] <= 0:
            minIndex = i
            break
    KArr = KArr[:minIndex]
    return KArr if KArr else [0]


"""
Problem Statement:
N stocks are evaluated and a rating is assigned for each stock. rating[i] is the value of the ith stock. A rating may be negative.
The team wants to develop an algorithm that will suggest combinations of stocks, or combos for short, that investors might buy. A combo is defined as a subset of any number of stocks. The value of a combo is the sum of the ratings of all stocks in the combo.
Design an algorithm that can find the k combos with the highest values. Two combos are considered different if they have a different subset of stocks. Return an array of k integers where the ith integer denotes the value of the ith best combo.
Note: You can have an empty subset as a combo as well. The value for an empty subset is 0.
Constraints:

1<=n<=10³
-10⁶<=rating[i]<=10⁶
1<=k<=min(2000,2ⁿ)

Example 1:
Input:
n = 3
rating = [-1,7,-2]
k = 4
Output:
[7, 6, 5, 4]
The 4 best combos are [7], [-1,7], [7,-2], [-1,7,-2]
Example 2:
Input:
n = 5
rating = [2,-10,5,3,-1]
k = 10
Output:
[10,9,8,7,6,5,5,4,4]
The 10 best combos are [2, 5, 3], [2, 5, 3, -1], [5, 3], [5, 3, -1], [2, 5], [2, 5, -1], [5], [2, 3], [5, -1], [2, 3, -1]
Example 3:
Input:
n = 2
rating = [-2, -1]
k = 1
Output:
[0]
The best combo is []
Function:
int[] bestCombos(int[] rating, int k)
"""
