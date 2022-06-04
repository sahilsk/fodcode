"""
Given an array of integers greater than zero, 
find if it is possible to split it in two subarrays 
(without reordering the elements), such that the sum
of the two subarrays is the same. Print the two subarrays.

Examples : 

Input : Arr[] = { 1 , 2 , 3 , 4 , 5 , 5  }
Output :  { 1 2 3 4 } 
          { 5 , 5 }

Input : Arr[] = { 4, 1, 2, 3 }
Output : {4 1}
         {2 3}

Input : Arr[] = { 4, 3, 2, 1}
Output : Not Possible
"""

from runner import runner

def splitArray(arr:list[int]) -> list[list]:
    '''
    sum  should be equal
    '''

    tsum = sum(arr)
    if tsum % 2 != 0:
        return []    
    target = tsum//2

    tmp = 0
    for i,v in enumerate(arr):
        tmp += v
        if tmp == target:
            return [arr[:i+1], arr[i+1:]]


testcases = {
    1: ([1,2,3,4,5,5],),
    2: ([4,1,2,3],),
    3: ([4,3,2,1],),

}


runner(splitArray, testcases)