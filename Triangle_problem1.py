# Finding an Angle of a triangle in a Right Angled Triangle
# https://www.hackerrank.com/challenges/find-angle/problem

import math
AB = int(input())
BC = int(input())

AC = math.sqrt((AB*AB) + (BC*BC))
MC = AC/2
MB = MC


MBC = round(math.degrees(math.acos((math.pow(MB,2) + math.pow(BC,2) - math.pow(MC,2)) / (2*MB*BC))))


degree = "\u00b0"
print(f"{MBC}{degree}")
