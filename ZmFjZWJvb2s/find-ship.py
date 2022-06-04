"""
Write a function that finds a ship and return its coordinates

https://leetcode.com/discuss/interview-question/980711/facebook-phone-counts-of-connected-islands

Given matrix with 0 as water and 1 as island, find the number of island in each distinct group of connected of island.
If any island has another island in its proximity (all 8 adjacent vertex), then they are connected.

[[0, 1, 0],
[0, 0, 0],
[0, 1, 0]]
Ans: [1, 1], there are 2 chain of island with 1 island each

[[0, 1, 0],
[1, 0, 0],
[0, 1, 0]]
Ans [3] 1 chain of island with 3 island on it

[[0, 1, 1],
[0, 0, 0],
[0, 1, 0]]
Ans [2, 1] 2 chain of island and 2 island on first and 1 island on another.
"""


def findNeighbours(arr,m, n, visited):
    
    dfs = [(m,n)]
    icount = 0
    while dfs:
        p = dfs.pop()
        i = p[0]
        j = p[1]

        if (0 <= i < len(arr)) and ( 0<= j < len(arr[0])) and arr[i][j] == 1 and (i,j) not in visited:
            icount += 1
            visited.add(p)
    
            dfs.append((i-1, j))
            dfs.append((i+1, j))
            dfs.append((i, j+1))
            dfs.append((i, j-1))
            dfs.append((i-1, j+1))
            dfs.append((i-1, j-1))
            dfs.append((i+1, j-1))
            dfs.append((i+1, j+1))

    print("Islands count: ", icount)
    return icount

def countIslands(arr) -> int:

    visited = set()
    total_ships = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                if findNeighbours(arr, i, j, visited) > 0:
                    total_ships += 1


    print("total ships: ", total_ships)


islandMatrix = [[0, 1, 0],
                [1, 0, 0],
                [0, 0, 1],
                [0, 0, 0],
                [0, 1, 0]]
countIslands(islandMatrix)