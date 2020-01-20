items = ['a', 'b', 'c','d']

print(f'Original list: {items}')
print('')
print('1. Find on the List')


def find_item(List, item):
    try:
        index_number = List.index(item)
        print(f'"{letter}" is in index {index_number}.')
    except ValueError:
        print(f'"{letter}" is not on the list.')


letter = '1'
find_item(items, letter)
print('')
print('2. Append the List')


def append_list(List, item):

        List.append(item)
        print(f'"{item}" is appended on {List}.')


to_append = 'e'
append_list(items,to_append)

print('')
print('3. Extend the List')


def extend_list(List, item):

        List.extend(item)
        print(f'"{item}" is extended on {List}.')


to_extend = ['x','y','z']
extend_list(items, to_extend)
print('')
print('4. Insert on the List')


def insert_on_list(List, index_number, item):
        List.insert(index_number, item)
        print(f'"{item}" is inserted on index: {index_number} {List}.')


to_insert = 'w'
at_index = 5
insert_on_list(items, at_index, to_insert)


def count_number_of_instance_on_list(List, item):
        count = List.count(item)
        if not count ==0:
            print(f'"{item}" is repeated {count} times on {List}.')
        else:
            print(f'"{item}" not on the list.')


to_find = 'r'
count_number_of_instance_on_list(items,to_find)


def reverse_list(List):
    List.reverse()
    print(f'List Reversed {List}')

reverse_list(items)


def sort_list(List):
    List.sort()
    print(f'List Sorted {List}')

sort_list(items)


def pop_item(List):
    List.pop()
    print(f'One item popped {List}')

pop_item(items)

def copy_entire_list(List):
    newlist = List.copy()
    List.append(newlist)
    print(f'List copied and appended {List}')

copy_entire_list(items)

def clear_list(List):
    List.clear()
    print(f'The list has been cleared. {List}')

clear_list(items)