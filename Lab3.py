# ECOR 1041 Fall 2022 Lab 3

__author__ = "Sabeen Rafiq"
__student_number__ = "101258923"

import math

# =====================================================
# Exercise 1

def area_of_disk(radius):
    return math.pi * radius ** 2

# =======================================================
# Exercise 2

LITRES_PER_GALLON = 4.54609
KMS_PER_MILE = 1.60934

def convert_to_litres_per_100_km(mpg):
    return (mpg / LITRES_PER_GALLON * KMS_PER_MILE) ** -1 * 100

# =======================================================
# Exercise 3

def accumulated_amount(principal, rate, n, time):
    return principal * (1 + rate / n) ** (n * time)

# =======================================================
# Exercise 4

def area_of_cone(height, radius):
    return math.pi * radius * math.sqrt(radius ** 2 + height ** 2)

# =======================================================
# Exercise 5

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def area_of_circle(xc, yc, xr, yr):
    return area_of_disk(distance(xc, yc, xr, yr))

