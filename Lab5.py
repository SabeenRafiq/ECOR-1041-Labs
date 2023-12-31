# ECOR 1041 Fall 2022 Lab 5

__author__ = "Sabeen Rafiq"
__student_number__ = "101258923"
import math
math.pow()
math.sqrt()
math.ceil()
math.floor()
mathround()
#======================================================
# Exercise 1

def parrot_trouble(talking: bool, hour: int) -> bool:
    """
    Return if in trouble given if parrort is talking and the hour. 
    Precondition: 0 <= hour <= 23
    parrot_trouble(True, 8)
    False
    parrot_trouble(False, 23)
    False
    parrot_trouble(True, 4)
    True
    """
    return talking and (hour < 7 or hour > 20)

# ======================================================
# Exercise 2

def alarm_clock(day: int, vacation: bool) -> str:
    """
    Return the time alarm clock will ring given the day and if it is a vacation.
    Preconditions: 0 <= day <= 6
    alarm_clock(1, False)
    "7:00"
    alarm_clock(0, True)
    "off"
    alarm_clock(6, False)
    "10:00"
    """
    if 1 <= day <= 5 and not vacation:
        return "7:00"
    elif (not 1 <= day <= 5 and not vacation) or (1 <= day <= 5 and vacation):
        return "10:00"
    else:
        return "off"

# ======================================================
# Exercise 3

def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if b or c are close (within a range of 1) to a and if the one that 
    is not close is far or is equal to or greater than 2 away.
    close_far(-1, -2, 10)
    True
    close_far(1, 2, 3)
    False
    close_far(20, 2, 21)
    True
    """
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    elif abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    return False

# ======================================================
# Exercise 4

def blackjack(a: int, b: int) -> int:
    """
    Return value closest to 21 without being over 21 given two values a and b
    Precondtion: a and b >= 0
    blackjack(50, 22)
    0
    blackjack(0,21)
    21
    blackjack(5, 6)
    6
    """
    if (a > 21 and b > 21) or a == b:
        return 0
    elif b > 21 or (21 - a) < (21 - b):
        return a
    elif a > 21 or (21 - a) > (21 - b):
        return b

# ======================================================
# Exercise 5

def assistance(income: float, children: int) -> float:
    """
    Return the financial assistance given the household income and number of 
    children
    Precondition: children >= 0, income >= 0
    assistance(35000, 5)
    7500
    assistance(15000, 3)
    6000
    assistance(25000, 4)
    4000
    """
    if 30000 <= income < 40000 and children >= 3:
        return 1500 * children
    elif 20000 <= income < 30000 and children >= 2:
        return 1000 * children
    elif income < 20000:
        return 2000 * children
    else:
        return 0