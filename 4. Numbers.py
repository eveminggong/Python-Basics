import random
import math


def select(a):
    print(random.choice(a))


choices = ['2', '3', '6', '1']
select(choices)


def logarithmic_ten(x):
    return math.log10(x)


print(logarithmic_ten(50))


def sine(a):
    return math.sin(a)


print(sine(180))


def cosine(a):
    return math.cos(a)


print(cosine(180))


def tangent(a):
    return math.tan(a)


print(tangent(180))


def divide_by_pi(a):
    return a/math.pi


print(divide_by_pi(60))


def shuffle_list(a):
    random.shuffle(a)


choices = ['2', '3', '6', '1']
shuffle_list(choices)
print(choices)


def natural_logarithm(x):
    return math.log(x)


answer = natural_logarithm(50)
print(answer)


def round_number(x):
    return round(x)


rounded = round_number(answer)
print(rounded)


def square_root(x):
    return math.sqrt(x)


print(square_root(rounded))