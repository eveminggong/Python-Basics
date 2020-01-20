def add(a,b):
    return a + b


print(f'1.sum = {add(4,5)}')


def subtraction(a,b):
    return a-b


print(f'2.difference = {subtraction(4,5)}')


def multiplication(a,b):
    return a * b


print(f'3.product = {multiplication(4,5)}')


def division(a,b):
    return a / b


print(f'4.quotient = {division(4,5)}')


def modulus(a,b):
    return a%b


print(f'5.remainder = {modulus(4,5)}')


def exponent(a,b):
    return a**b


print(f'6.exponent = {exponent(4,5)}')


def floor_division(a,b):
    return a//b


print(f'7.floordivision = {floor_division(10,5)}')


def square(a):
    return a*a


print(f'8.square = {square(2)}')


def power_of_ten(a):
    return 10**a


print(f'9.power of ten = {power_of_ten(2)}')


def odd_even(a):
    result= a/2
    if result ==1:
        return 'even'
    else:
        return 'odd'


print(f'10.odd or even = {odd_even(4)}')