"""
An array consisting of N integers is given. There are several Right Circular Rotations of range[L..R] that we perform. After performing these rotations, we need to find element at a given index.
Examples : 
 

Input : arr[] : {1, 2, 3, 4, 5}
        ranges[] = { {0, 2}, {0, 3} }
        index : 1
Output : 3
Explanation : After first given rotation {0, 2}
                arr[] = {3, 1, 2, 4, 5}
              After second rotation {0, 3} 
                arr[] = {4, 3, 1, 2, 5}
After all rotations we have element 3 at given
index 1. 

"""


def findIndex(arr, ranges, idx):

    for i in range(len(ranges)-1, -1, -1):
        rng = ranges[i]

        if rng[0] < idx <= rng[1]:
            idx = idx - 1
        elif idx == rng[0]:
            idx = rng[1]

    print(arr[idx])    
    return arr[idx]



findIndex([1,2,3,4,5], [[0,2], [0,3]], 1)
findIndex([3,1,2,4,5], [[0,3], [0,3]], 1)


