
def a_very_big_sum(arr: list) -> int:
    """
    Calculates the sum of all the elements in the given list.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The sum of all the elements in the list.
    """
    result = 0
    for i, num in enumerate(arr):
        result += num
    return result
print(a_very_big_sum([1,2,3,4]))
