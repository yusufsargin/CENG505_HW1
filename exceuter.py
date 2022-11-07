#!/usr/bin/env python3
from datetime import *
import subprocess


matrix_arrays = [
      16, # 16x16
    32, # 32x32
    64, # 16x64
    128, # 128x128
    512, # 512x512
]
threadCount = [
    4,
    8,
    16,
    32,
    64,
]
mod = len(matrix_arrays)
timeArray = []

print(datetime.now().second)

for therad in threadCount:
    for matrix in matrix_arrays:
        startTime = datetime.now()
        #subprocess.run(["./hw_parallel", str(therad), str()])
        subprocess.run(["ls"])
        endTime = datetime.now()
        diff = endTime - startTime
        timeArray.append(diff)

times = 0

with open("output.txt", "w") as txt_file:
    for index, timeItem in enumerate(timeArray):
        if(index %5 == 0 and index > 0):
            times = times +1
        text ="Execution time in " + str(threadCount[times])+" tread " + "for "+ str(matrix_arrays[index%mod])+ "x", str(matrix_arrays[index%mod])+ " "+ str(timeItem.microseconds)+ " microseconds" 
        print(text)
        txt_file.write(" ".join(text) + "\n") # works with any number of elements in a line
