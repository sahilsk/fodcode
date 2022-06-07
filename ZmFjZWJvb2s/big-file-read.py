import chunk
from tkinter import E

from time import sleep


def chunkify(fd, chunksize):
    while True:
        content = fd.readline(chunksize)
        if not content:
            break
        sleep(1)
        yield content


with open("dataset1.csv") as fd:
    for chunk in chunkify(fd, 1):
        print(chunk, sep="")
