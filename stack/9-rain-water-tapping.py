from runner import runner
""""
https://www.youtube.com/watch?v=FbGG2qpNp4U&ab_channel=AdityaVerma

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Examples:  

Input: arr[]   = {2, 0, 2}
Output: 2


Solution:
    water[i]  = min(maxL, maxR)(#find max height) - arr[i](#height)  # width is 1unit. so can be ignored

    arr =  [i i i]
    maxr = [x x x]
    maxl = [y y y]
    water= [min(x,y) -i  ]  => sum = answer

"""

def watercollected(arr:list[int]) -> int:

    maxr = [arr[-1]] * len(arr)
    maxl = [arr[0]] * len(arr)
    water = [0] * len(arr)

    for i in range(1, len(arr)):
        print(i)
        maxl[i] = max(maxl[i-1], arr[i])

    for i in range(len(arr)-2, -1):
        maxr[i] = max(maxl[i+1], arr[i])
    
    for i in range(len(arr)):
        water[i] = min(maxl[i], maxr[i]) - arr[i]
    
    return sum(water)



testcases = {
    10:([3, 0,0,2,0,4],),
    2: ([2,0,2],)
}

runner(watercollected, testcases)