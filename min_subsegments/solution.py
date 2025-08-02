def get_min_segments(frames):
    frame_count = len(frames)

    # Track minimum flips and segments for first 'i' characters
    min_flips = [float("inf")] * (frame_count + 1)
    min_segments = [float("inf")] * (frame_count + 1)

    # Base case: empty string
    min_flips[0] = 0
    min_segments[0] = 0

    # Try all possible ending positions (step by 2 for even lengths)
    for end_pos in range(2, frame_count + 1, 2):
        for start_pos in range(0, end_pos - 1, 2):
            segment_length = end_pos - start_pos

            if segment_length % 2 != 0:
                continue

            current_segment = frames[start_pos:end_pos]

            # Count flips needed to make segment uniform
            flips_to_zero = 0
            flips_to_one = 0
            for char in current_segment:
                if char == "0":
                    flips_to_one += 1
                else:
                    flips_to_zero += 1

            segment_cost = min(flips_to_zero, flips_to_one)

            total_flips = min_flips[start_pos] + segment_cost
            total_segments = min_segments[start_pos] + 1

            # Update DP: minimize flips first, then segments
            if total_flips < min_flips[end_pos]:
                min_flips[end_pos] = total_flips
                min_segments[end_pos] = total_segments
            elif total_flips == min_flips[end_pos]:
                min_segments[end_pos] = min(min_segments[end_pos], total_segments)

    return min_segments[frame_count]


"""
Min Subsegments
Your team is developing a new feature called "Segmentify." This feature applies to a video with n (even) visual frames, where each frame is represented by a binary character in the array frames. In this format, a "0" represents a black pixel, and a "1" represents a white pixel.

Due to factors like lighting and camera angles, some frames may need horizontal or vertical flips (changing "0"s to "1"s and vice versa) to create consistent visuals. The objective is to divide the video into subsegments so that all frames in a subsegment are visually identical (i.e., the frames in a subsegment are either all "0"s or all "1"s). Additionally, each subsegment should have an even length.

The goal is to accomplish this segmentation with two criteria in mind:

1. Minimize the number of flips required to form valid segments, let this be denoted by B.
2. Among all configurations requiring B flips, minimize the total number of subsegments.

Given the binary string frames, determine the minimum number of even-length subsegments that can be created while utilising the least number of flips.

Note: A subsegment is a segment that can be derived from another segment by deleting some elements without changing the order of the remaining elements.

Example
Given frames = "1110011000", one set of optimal moves is as follows -

Flip the first 0 to 1 (1110011000) → 1111011000
Flip the first 0 to 1 (1111011000) → 1111111000
At last, again flip the first 0 to 1 (1111111000) → 1111111100

Hence, the length of all subsegments - (11111111 and 00) is even.
So, the minimum number of subsegments that frames can be divided into to make it "Segmentify-compliant" is 2 with minimum flips of 3.
Hence, the answer is 2.
"""
