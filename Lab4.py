# ECOR 1041 Fall 2022 Lab 4

__author__ = "Sabeen Rafiq"
__student_number__ = "101258923"

# ======================================================
# Exercise 1

def tip(cost_meal: float, customer_satisfaction: int) -> float:
    """
    Return the tip, given the cost of meal and customer satisfaction
    Precondition -> customer_satisfaction = 1, 2 or 3
                 -> cost_meal >= 0
    tip(100, 3)
    5.0
    tip(50, 1)
    10.0
    tip(50, 3)
    2.5
    """
    
    if customer_satisfaction == 1:
        return cost_meal * 0.20
    elif customer_satisfaction == 2:
        return cost_meal * 0.15
    else:
        return cost_meal * 0.05


#======================================================
# Exercise 2

def coupon(amount_spent_groceries: float) -> float:
    """
    Return coupon amount, given amount spent on groceries
    Precondtion: amount_spent_groceries >= 0
    coupon(100)
    10.0
    coupon(500)
    70.0
    coupon(5)
    0.0
    """
    
    if amount_spent_groceries < 10:
        coupon_amount = 0
    elif 10 <= amount_spent_groceries <= 60:
        coupon_amount = amount_spent_groceries * 0.08
    elif 60 < amount_spent_groceries <= 150:
        coupon_amount = amount_spent_groceries * 0.10
    elif 150 < amount_spent_groceries <= 210:
        coupon_amount = amount_spent_groceries * 0.12
    else:
        coupon_amount = amount_spent_groceries * 0.14
    return coupon_amount

# ======================================================
# Exercise 3

def bakers_party(weekend_tf: bool, number_pastries: int) -> bool:
    """
    Return if baker's party was sucessful (True) or not (False), given if it
    was a weekend (True) or a weekday (False) and the number of pastries
    Preconditon: weekend_tf = True or False, number_pastries >= 0
    bakers_party(True, 30)
    False
    bakers_party(True, 100)
    True
    bakers_party(False, 50)
    True
    """

    if weekend_tf and number_pastries >= 40:
        party_success = True
    elif not weekend_tf and 40 <= number_pastries <= 60:
        party_success = True
    else:
        party_success = False
    return party_success

#======================================================
# Exercise 4

def squirrel_play(summer_tf: bool, temperature_f: int) -> bool:
    """
    Return if the squirrels are playing (True or False), given if it is the 
    summer or not and the temperature_f
    Precondition: summer_tf == True or False
    squirrel_play(True,60)
    True
    squirrel_play(True,100)
    True
    squirrel_play(False,60)
    True
    squirrel_play(False,90)
    True
    """
    if summer_tf:
        if 60 <= temperature_f <= 100:
            squirrel_play_tf = True
        else:
            squirrel_play_tf = False
    else:
        if 60 <= temperature_f <= 90:
            squirrel_play_tf = True
        else:
            squirrel_play_tf = False
    return squirrel_play_tf

# ======================================================
# Exercise 5

def great_42(a: int, b: int) -> int:
    """
    Return if value is 42, sum is 42, or absolute value of diffrence is 42, 
    given values a and b
    great_42(42,0)
    True
    great_42(21,21)
    True
    great_42(50,8)
    True
    """
    if a == 42 or b == 42 or a + b == 42 or abs(a - b) == 42:
        great_42_tf = True
    else:
        great_42_tf = False
    return great_42_tf

# ======================================================
# Exercise 6

def multiply_uniques(a: int, b: int, c: int) -> int:
    """
    Return product of 3 intergers a, b and c, if two values are the same they
    are not used in the product
    multiply_uniques(3,3,3)
    1
    multiply_uniques(3,2,3)
    2
    multiply_uniques(1,2,3)
    6
    """
    if a != b and b != c and a != c:
        return a * b * c
    else:
        a_product = a
        b_product = b
        c_product = c
        if a == b:
            a_product = 1
            b_product = 1
        if b == c:
            b_product = 1
            c_product = 1
        if a == c:
            a_product = 1
            c_product = 1
        return a_product * b_product * c_product

