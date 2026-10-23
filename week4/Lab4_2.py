# lab4_2.py - Geometric Calculations (Tuples & Immutability)

import math

print("--- Lab 4.2: Geometric Calculations ---")
print("\n")
fx = int(input("Please set first point's X value : "))
fy = int(input("Please set first point's Y value : "))
sx = int(input("Please set Second point's X value : "))
sy = int(input("Please set Second point's Y value : "))
point1 = (fx,fy) 
point2 = (sx,sy) 

print("\n[1] Access Coordinates")
print(f"Point 1: x = {point1[0]}, y = {point1[1]}")
print(f"Point 2: x = {point2[0]}, y = {point2[1]}")

print("\n[2] Attempt Modification (Immutability Demonstration)")
try:
    point1[0] = 5
except TypeError as e:
    print(f"Error trying to modify tuple: {e}")

print("\n[3] Calculate Distance")
distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) #เติมเลขตำแหน่งในลิส 0 และ 1 ใน [] ให้ถูกต้อง 👈ต้องทำ
print(f"Distance between point1 {point1} and point2 {point2}: {distance}")