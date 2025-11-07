#Author:Rinat.R
#Date:10.26.25
"""This program prints numbers 1-50 with messages for divisible by 3 or 5"""

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by three")
    elif i % 5 == 0:
        print("Divisible by five")
    else:
        print(i)