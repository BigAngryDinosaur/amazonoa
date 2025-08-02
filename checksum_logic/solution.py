def find_hash(n, param):
    count = [0] * (n + 2)
    for p in param:
        if p <= n:
            count[p] += 1
        else:
            count[n + 1] += 1

    max_over = 0
    prefix_sum = 0
    for i in range(1, n + 1):
        prefix_sum += count[i]
        if prefix_sum > i:
            max_over = max(max_over, prefix_sum - i)

    return n - max_over


"""
Checksum Logic
The developers are designing a new checksum logic for an authentication module. The checksum is calculated as an array hash, where:
hash[i] = secretKey[i] % param[i]

There are n parameters for the checksum, represented by param[i]. The secret key also has n values, and a good secret key produces more distinct values in the hash array.

Task
Given an array param of size n, determine the maximum number of distinct values possible in the hash array by choosing an appropriate secretKey.

Example
Input:
n = 3
param = [1, 2, 4]

Possible secretKey = [1, 3, 2].
Then hash = [0, 1, 2] -> 3 distinct values

Function Signature
int findHash(int param[n])

Returns
Maximum number of distinct elements in hash.

Constraints
1 ≤ n ≤ 2 × 10⁵
"""
