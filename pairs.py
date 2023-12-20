"""
Given an array of integers and a value, determine if there are any two integers
in the array whose sum is equal to the given value.
"""

def find_pairing_sum(arr: list[int], x: int) -> int:
    """
    Find the number of pairs in an array that sum to x
    :param arr: list of integers
    :param x: integer
    :return: integer  - number of pairs
    """
    count = 0

    if len(arr) <= 1:
        return 0

    if x in arr:
        count += 1
        arr.remove(0)
        arr.remove(x)

    for i in range(len(arr)):
        rem = abs(x - arr[i])
        if rem in arr[i+1:]:
            count += 1
            arr.remove(rem)
            arr.remove(arr[i])
        else:
            arr.remove(arr[i])
        break
    return count + find_pairing_sum(arr, x) if len(arr) > 1 else count


