

def hot_water(temperature):
    while temperature<100:
        print(temperature)
        temperature = temperature + 1


hot_water(90)
print('Water is Boiling.')


def add_to_sum(count):
    while count < 100:
        print(count)
        count += count


add_to_sum(3)


color_list = ['red', 'green', 'blue']


def repeat_list(List):

    for i in List:
        print(f'The color is {i}.')


repeat_list(color_list)



def sum_of_list(i, number):

    while i > number:
        sum = 0
        sum = sum + i
