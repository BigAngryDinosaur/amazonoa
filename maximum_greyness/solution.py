def maxAcutance(image):
    """
    :type image: List[String]
    :rtype: int
    """
    m, n = len(image), len(image[0])
    row_counts = [[0, 0] for _ in range(m)]
    col_counts = [[0, 0] for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if image[i][j] == "0":
                row_counts[i][0] += 1
                col_counts[j][0] += 1

            else:
                row_counts[i][1] += 1
                col_counts[j][1] += 1

    mx = -(m + n)
    for i in range(m):
        for j in range(n):
            ac = (row_counts[i][1] + col_counts[j][1]) - (
                row_counts[i][0] + col_counts[j][0]
            )
            mx = max(mx, ac)

    return mx


"""

"""
