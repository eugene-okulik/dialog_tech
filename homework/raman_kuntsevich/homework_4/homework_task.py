my_dict = {'tuple': '', 'list': '', 'set': '', 'dict': ''}
simple_dict = {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5}
simple_list = [1, 2, 3, 4, 5]
simple_tuple = ('One', 'Two', 'Three', 'Four', 'Five', 6, 7, 8, 9, 10)
simple_set = {666, "Purple", "Salmon", 15.5, "Finger", True}

my_dict['tuple'] = simple_tuple
my_dict['set'] = simple_set
my_dict['list'] = simple_list
my_dict['dict'] = simple_dict

last_tuple_element = my_dict.get('tuple')[-1]
print(f'Last tuple item: {last_tuple_element}')

my_dict.get('list').append(6)
del my_dict.get('list')[1]

my_dict.get('dict')[('I am a tuple',)] = False
del my_dict.get('dict')['One']

my_dict.get('set').add('New element')
my_dict.get('set').remove(666)

for key, value in my_dict.items():
    print(f'{key}: {value}')
