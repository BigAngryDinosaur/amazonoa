def maxRain(rainFall, n):
    starts = [0] * (n + 1)
    ends = [0] * (n + 1)

    for start, end, amount in rainFall:
        starts[start] += amount
        ends[end] += amount

    current = 0
    mx = 0

    for i in range(1, n + 1):
        current += starts[i]
        mx = max(mx, current)
        current -= ends[i]

    return mx
