"""
 (*high frequency question) Generate a minesweeper grid (2x3) with 3 randomly-placed mines (solution)

"""

import random


def placeMines(m, n, total):

    arr = [[0] * n for i in range(m)]

    # place mines
    random.SystemRandom()

    tcount = 0
    while True:
        pos = random.randint(0, m * n)

        i = pos % m  #  Row
        j = pos // n  # col
        if arr[i][j] == 1:
            continue
        else:
            tcount += 1
            arr[i][j] = 1

        if tcount == total:
            break

    print(arr)


placeMines(2, 3, 3)
