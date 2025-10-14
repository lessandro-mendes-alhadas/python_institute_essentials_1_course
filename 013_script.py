'''
Basic list methods
'''
# Creating an empty list
my_list = [] 
print('Empty List: ', my_list,end='\n\n')

# Adding a new member to the end of the list
for i in range(5):
    print('Appending: ', i + 1)
    my_list.append(i + 1)

# The length of the list
print('\nList Lenght: ', len(my_list))
print('List: ', my_list)

# Insert a new member into a specific position
print('\nInsert 6 on a 4 position')
my_list.insert(4,6)
print('List Lenght: ', len(my_list))
print('List: ', my_list)

# Delete a member in a specific position
print('\nDelete the 4 position')
del my_list[4]

print('List Lenght: ', len(my_list))
print('List: ', my_list)

# Nested list
my_list = [1, 'a', ["list", 64, [0, 78], False]]
print('\nNested List: ', my_list)

# Accessing a member of a nested list
print('\nSecond member of a second nested list:',my_list[2][2][1])

# Delete can delete whole list
del my_list
print('\nList was deleted')

# New list
my_list = [8, 10, 6, 2, 4]
print('\nMy new List:',my_list)

# Sorting the list
my_list.sort()
print('\nSorted List:',my_list)