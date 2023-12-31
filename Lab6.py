# ECOR 1041 Fall 2022 Lab 6

__author__ = "Sabeen Rafiq"
__student_number__ = "101258923"

#======================================================
# Exercise 1

def add_up(n: int) -> float:
    """
    Return the total of the sequence 1 / n + 2 / n - 1 + ... + n / 1
    Precondition: x > 0
    add_up(1)
    2.0
    add_up(3)
    7.3333333
    add_up(4)
    10.4166666
    """
    sum_total = 0
    x = 1
    for x in range(n + 1):
        sum_total += x / (n - (x - 1))
        x += 1
    return sum_total + n

# ======================================================
# Exercise 2

def fib(n: int) -> int:
    """
    Return the value from the fibonacci sequence depending on the 
    n value given
    Precondition: x > 0
    fib(5)
    5
    fib(0)
    0
    fib(8)
    21
    """
    num_1 = 0
    num_2 = 1
    sum_total = 0
    for x in range(n):
        num_1 = num_2
        num_2 = sum_total
        sum_total = num_1 + num_2
    return sum_total

# ======================================================
# Exercise 3

def years_to_double(initial: float, rate: float) -> int:
    """
    Return the number of years needed to double the intial amount 
    given the rate of intrest
    Precondition: inital > 0, rate > 0
    years_to_double(10000, 5)
    15
    years_to_double(100,2)
    4
    years_to_double(1500, 10)
    8
    """
    years = 0
    investment = initial
    while investment <= 2 * initial:
        investment += investment * (rate / 100)
        years += 1
    return years

# ======================================================
# Exercise 4

def replicate(characters: str) -> str:
    """
    Return a string with characters repeated by the number of characters 
    in the string
    replicate("five")
    'fivefivefivefive'
    replicate("hello")
    'hellohellohellohellohello'
    replicate("bye")
    'byebyebye'
    """
    return characters * len(characters)
    
# ======================================================
# Exercise 5

def repeat_separator(word: str, sep: str, n: int) -> str:
    """
    Return a string with a word seperated by sep n amount of times
    Precondition: n > 0,  word and sep must have at least 1 character
    repeat_separator("Hello", "Bob", 5)
    'HelloBobHelloBobHelloBobHelloBobHello'
    repeat_separator("Bye", "Bob", 1)
    'Bye'
    repeat_separator("Word", "File", 2)
    'WordFileWord'
    """
    counter = 0
    result = word
    for counter in range(1, n):
        result += sep + word
    return result

# ======================================================
# Exercise 6
def has_pair(s: str, ch: str) -> bool:
    """
    Return if ch repeats 2 or more times in the string s
    Precondition: s has at least two characters
                  ch has one character
    has_pair("abc", "c")
    False
    has_pair("aaaaaaaa", "a")
    True
    has_pair("helloo", "o")
    True
    """
    pair = 0
    for character in s:
        if character == ch:
            pair += 1
    return pair >= 2
    
