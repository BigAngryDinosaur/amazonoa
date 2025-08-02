def maxPalette(colors, paletteSize, threshold):
    """
    :type colors: List[int]
    :type paletteSize: int
    :type threshold: int
    :rtype: int
    """
    colors.sort()
    res = 0
    start, end = 0, paletteSize - 1

    while end < len(colors):
        diff = colors[end] - colors[start]
        if diff <= threshold:
            res += 1
            start += paletteSize
            end += paletteSize
        else:
            start += 1
            end += 1

    return res


"""
Given a list of colors with their chromatic values, select exactly N colors for a palette so that the difference between the maximum chromatic value and minimum chromatic value is no more than a threshold.
Find the maximum number of palettes that can be made from the given colors.
No duplicate indices can be selected.


Example 1
Input
colors = [6, 2, 10, 2, 11, 1, 3, 2] paletteSize = 3
threshold = 4
A++

Output
2
At most 2 palettes can be made: [1, 2, 2], [2, 3, 6] with a difference (max - min) no more than 4.

----

Example 2
Input
colors = [10, 15, 9, 10, 9, 1, 3, 3]
paletteSize = 4
threshold = 2

Output
1
The only palette [9, 9, 10, 10] with max difference no more than 2.
"""
