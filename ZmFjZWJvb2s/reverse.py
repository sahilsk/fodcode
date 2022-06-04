"""
Given a vector/ array and 2 numbers, eg 2 and 5. Between those 2 positions in the vector (2 and 5) reverse the order of the elements
"""


def reverseArr(arr, i , j):

    while i < j:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
