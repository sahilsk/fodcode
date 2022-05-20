# Property of binary search

1. After end of binary search, `low` and `high` will point to neighbour of `target/key`
2. In a rotated array
    - search in unsorted segment and ignore the sorted one i.e 
        ```
        # Edge case
        if arr[l] < arr[r]:
            return l

        if arr[mid] >= arr[l]:
            # find in other unsorted part
            l = mid + 1
        elif arr[mid] <= arr[r]:
            # find in other unsorted part
            r = mid - 1
        ```

## Must do problems

8) Find in a rotated array
11) Find ceil of element
13) find target in an  infinite array
15)  Minimum difference element in a sorted array