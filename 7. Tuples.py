tuple1 = (1,2,3)
tuple2 = (5,6,7)
tuple3 = ('Red', 'Blue', 'Black')

print(f'Tuple1: {tuple1}')
print(f'Tuple2: {tuple2}')
print(f'Tuple3: {tuple3}')

def add_tuple(Tuple1, Tuple2):

    FinalTuple = Tuple1 + Tuple2
    print(f'The tuples are added {FinalTuple}')


add_tuple(tuple1,tuple2)


def duplicate_tuple(Tuple1, Tuple2):
    FinalTuple = Tuple1 * 4
    print(f'The tuples are multiplied. {FinalTuple}')


LargeTuple = duplicate_tuple(tuple1, tuple2)


def count_item(Tuple1, item):
    counts = Tuple1.count(item)
    print(f'The count of {item} on the Tuple 1 is {counts}')

items = 1
count_item(tuple1, items)


def index_of_item(Tuple, item):
    index = Tuple.index(item)
    print(f'The index of {item} on the Tuple 2 is {index}')


item_to_index = 6
index_of_item(tuple2, item_to_index)


def reiterate_tuple(Tuple3):
    for color in (Tuple3):
        print(f'The color is {color}')

reiterate_tuple(tuple3)
