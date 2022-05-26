from runner import runner

"""



Solution:
1. for every number, run twosum algo. Complexity: o(n2)
"""

def threesum(nums:list[int], target:int) -> tuple:
    
    numlen = len(nums)
    for i, num in enumerate(nums):
        newtarget = target - num

        chash = dict()
        j = i + 1
        k =  numlen - 1

        while j <= k:
            nexttarget = newtarget - nums[j]
            if chash.get(nexttarget, None) != None:
                return (i, chash[nexttarget], j)
            chash[nums[j]] = j
            j += 1
            
    return (-1, -1, -1)
                


testcases = {
    "(0,2,3)" : ([1,2,6,4,5], 11)
}

runner(threesum, testcases)
