example_list = []

example_list.append(1)  # add an object
example_list.insert(0, 2)  # insert object before index
example_list.remove(1)  # remove first occurrence of value.
example_list.pop()  # remove and returns, default is first

example_tuple = (0, 1, 2)  # immutable

example_dict = {
    'name': 'example',
    'email': 'example@ex.com'
}

caught = example_dict.get('name')  # get a value from key
example_dict.update({'email': 'new@new.com', 'age': 0})  # merge dict

...  # ellipsis (like NOP 0x90)
