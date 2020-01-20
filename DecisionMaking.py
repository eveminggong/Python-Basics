def is_equal(a,b):
    if a==b:
        return 'equal'
    else:
        return 'not equal'
print(f'{is_equal(4,4)}')


def is_lesser(a,b):
    if a<b:
        return 'lesser'
    else:
        return 'not lesser'
print(f'{is_lesser(4,5)}')

def is_greater(a,b):
    if a>b:
        return 'greater'
    else:
        return 'not greater'
print(f'{is_greater(4,5)}')

def is_lesser_or_equal(a,b):
    if a <= b:
        return 'lesser or equal'
    else:
        return 'not lesser or not equal'


print(f'{is_lesser_or_equal(5, 5)}')

def odd_even(a):
    result= a/2
    if result ==1:
        return 'even'
    else:
        return 'odd'

print(f'odd or even = {odd_even(4)}')


def more_than_100(a):
    if a>=100:
        return 'More than 100'
    else:
        return 'Less than 100'

print(f'Number is = {more_than_100(101)}')

def is_zero_balance(a):
    if a==0:
        return 'Your balance is zero.'
    else:
        return 'Your balance is not zero'

print(is_zero_balance(0))

def is_heavy(a):
    if a > 500 :
        return 'This weighs more than 500kg.'
    else:
        return 'This weighs lesser than 500kg.'
print(is_heavy(502))

def is_overtime(hours_worked_weekly):
    if hours_worked_weekly>40:
        return 'Due for overtime pay.'
    else:
        return 'Not due for overtime pay.'
print(is_overtime(45))

def temperature_celsius(temperature):
    if temperature> 27:
        return "It's a hot day"
    else:
        return "It's not a hot day"

print(temperature_celsius(32))