"""
Separate Pages
Users of an online e-book store can choose a book from a wide range of categories.
An e-book also provides bookmark pages for the user to return to later.
A book is represented as a binary string having two types of pages:
'0': an ordinary page
'1': a bookmarked page
Find the number of ways to select 3 pages in ascending index order such that no two adjacent selected pages are of the same type.
Example 1
book = '01001'
The following sequences of pages match the criterion:
[1, 2 ,3], that is, 01001 → 010.
[1, 2 ,4], that is, 01001 → 010.
[2, 3 ,5], that is, 01001 → 101.
[2, 4 ,5], that is, 01001 → 101.
The answer is 4.
Function
long numberOfWays(String book)
Returns
long int: the total number of ways to select 3 pages that meet the criterion
Example 2
Input
0001 → book = "0001"
Output
0
It is not possible to pick a sequence of 3 pages that satisfies the conditions.
"""


def numberOfWays(book):
    """
    Find number of ways to select 3 pages in ascending order
    such that no two adjacent selected pages are of the same type.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(book)
    if n < 3:
        return 0

    # dp[i][j][k] represents:
    # i = number of pages selected so far (1, 2, or 3)
    # j = type of last selected page (0 or 1)
    # k = current position in book

    # Since we only need previous states, we can optimize space
    # prev[pages_selected][last_type] = count
    prev = [[0, 0], [0, 0], [0, 0], [0, 0]]  # 0-3 pages selected, last type 0 or 1
    curr = [[0, 0], [0, 0], [0, 0], [0, 0]]

    # Initialize: select first page
    if book[0] == "0":
        prev[1][0] = 1
    else:
        prev[1][1] = 1

    # Process each subsequent page
    for i in range(1, n):
        # Reset current state
        for j in range(4):
            curr[j][0] = curr[j][1] = 0

        # Copy previous states (not selecting current page)
        for pages in range(4):
            curr[pages][0] = prev[pages][0]
            curr[pages][1] = prev[pages][1]

        # Try selecting current page
        page_type = int(book[i])

        # Select as first page
        curr[1][page_type] += 1

        # Select as second page (if first page was different type)
        if prev[1][1 - page_type] > 0:
            curr[2][page_type] += prev[1][1 - page_type]

        # Select as third page (if second page was different type)
        if prev[2][1 - page_type] > 0:
            curr[3][page_type] += prev[2][1 - page_type]

        # Swap prev and curr
        prev, curr = curr, prev

    # Return total ways to select exactly 3 pages
    return prev[3][0] + prev[3][1]


def numberOfWays_optimized(book):
    """
    Even more space-optimized version using only necessary variables.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    n = len(book)
    if n < 3:
        return 0

    # Track states: [count_with_1_page_ending_0, count_with_1_page_ending_1,
    #                count_with_2_pages_ending_0, count_with_2_pages_ending_1]
    one_page_0, one_page_1 = 0, 0
    two_pages_0, two_pages_1 = 0, 0
    three_pages = 0

    for i in range(n):
        page_type = int(book[i])

        if page_type == 0:
            # Can form 3-page sequence if we had 2 pages ending with 1
            three_pages += two_pages_1
            # Can form 2-page sequence if we had 1 page ending with 1
            new_two_pages_0 = two_pages_0 + one_page_1
            # Always can start new 1-page sequence
            new_one_page_0 = one_page_0 + 1

            two_pages_0 = new_two_pages_0
            one_page_0 = new_one_page_0
        else:  # page_type == 1
            # Can form 3-page sequence if we had 2 pages ending with 0
            three_pages += two_pages_0
            # Can form 2-page sequence if we had 1 page ending with 0
            new_two_pages_1 = two_pages_1 + one_page_0
            # Always can start new 1-page sequence
            new_one_page_1 = one_page_1 + 1

            two_pages_1 = new_two_pages_1
            one_page_1 = new_one_page_1

    return three_pages


# Test with provided examples
def test_solution():
    # Example 1
    book1 = "01001"
    result1 = numberOfWays_optimized(book1)
    print(f"Book: {book1}")
    print(f"Result: {result1}")
    print(f"Expected: 4")
    print()

    # Example 2
    book2 = "0001"
    result2 = numberOfWays_optimized(book2)
    print(f"Book: {book2}")
    print(f"Result: {result2}")
    print(f"Expected: 0")
    print()

    # Additional test cases
    test_cases = [
        ("010", 1),  # Only one way: select all 3
        ("101", 1),  # Only one way: select all 3
        ("000", 0),  # All same type
        ("111", 0),  # All same type
        ("0101", 2),  # [0,1,3] and [1,2,3] -> 010 and 101
    ]

    for book, expected in test_cases:
        result = numberOfWays_optimized(book)
        print(f"Book: {book}, Result: {result}, Expected: {expected}")


if __name__ == "__main__":
    test_solution()
