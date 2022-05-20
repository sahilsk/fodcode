"""
Given an infinite sorted array consisting 0s and 1s. The problem is to find the index of first ‘1’ in that array. As the array is infinite, therefore it is guaranteed that number ‘1’ will be present in the array.

Example:

Input : arr[] = {0, 0, 1, 1, 1, 1} 
Output : 2
"""


"""
NOTE: infinite array
"""
def findfirstone(arr):
    start = 0
    end = start + 1

    while arr[end] < 1:
        start = end
        end = end * 2

    # found start, end index

    l = start
    r = end

    lastres = -1
    while l <= r:
        mid = l + (r-l)//2

        if arr[mid]  >= 1:
            lastres = mid
            r = mid - 1
        elif arr[mid] < 1:
            l = mid + 1

    return lastres



arr = [0,0, 1,1,1,1]
print(findfirstone(arr))