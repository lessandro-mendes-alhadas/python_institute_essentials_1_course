'''
Basic list methods
'''
my_list = []  # Creating an empty list.
print('Empty List: ', my_list,end='\n\n')


for i in range(5):
    print('Appending: ', i + 1)
    my_list.append(i + 1)

print('\nList Lenght: ', len(my_list))
print('List: ', my_list)

print('\nInsert 6 on a 4 position')
my_list.insert(4,6)
print('List Lenght: ', len(my_list))
print('List: ', my_list)

print('\nDelete the 4 position')
del my_list[4]
print('List Lenght: ', len(my_list))
print('List: ', my_list)