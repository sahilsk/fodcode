"""
source: https://leetcode.com/discuss/interview-question/391865/facebook-software-engineer-phone-screen-interview-questions-reject
Question 1:
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. 
The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.
"""


from os import path


dino = dict()
curdir = "c:\\Users\\sonuk\\Documents\\wkspce\\fodcode\\ZmFjZWJvb2s"

with open(path.join(curdir, "dataset1.csv")) as f:
    # discard first record
    f.readline()
    for record in f.readlines():
        record_arr = record.lower().strip().split(",")
        dino[record_arr[0]] = [float(record_arr[1])]


with open(path.join(curdir, "dataset2.csv")) as f:
    for record in f.readlines():
        f.readline()
        record_arr = record.lower().strip().split(",")
        if record_arr[0] in dino and record_arr[2] == "bipedal":
            dino[record_arr[0]].append(float(record_arr[1]))


dino = {k: v for k, v in dino.items() if len(v) == 2}


from math import sqrt

dino_sorted = sorted(
    dino.items(), key=lambda x: ((x[1][1] / x[1][0]) - 1) * sqrt(x[1][0] * 9.8)
)
print(dino_sorted)
