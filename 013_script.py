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

# Sorting in a reverse order
my_list.reverse()
print('\nList sorted in reverse order:',my_list)

'''
If you have a list l1, then the following assignment: l2 = l1 does not make a copy of the l1 list, but makes the variables l1 and l2 point to one and the same list in memory
'''
my_list2 = my_list
print('\nmy_list2 receives my_list:',my_list2)

del my_list2[0]
print('\nDeleting my_list2[0], my_list:',my_list)

'''
If you want to copy a list or part of the list, you can do it by performing slicing
'''
colors = ['red', 'green', 'orange']
print('\ncolors: ', colors)
copy_whole_colors = colors[:]  # copy the entire list
print('\ncopy_whole_colors: ', copy_whole_colors)
copy_part_colors = colors[0:2]  # copy part of the list
print('\ncop_part_colors: ', copy_part_colors)

'''
You can use negative indices to perform slices, too
'''
sample_list = ["A", "B", "C", "D", "E"]
print('\nsample_list: n',sample_list)
new_list = sample_list[2:-1]
print('\ncopying sample_list[2:-1]: ',new_list)

'''
Copying elements from a list
'''
new_list = sample_list[2:]
print('\ncopying sample_list[2:]: ',new_list)

new_list = sample_list[ :2]
print('\ncopying sample_list[:2]: ',new_list)

new_list = sample_list[-2:]
print('\ncopying sample_list[-2:]: ',new_list)

'''
Deleting elements from a list and deleting a list
'''
del sample_list[1:3]
print('\n"del sample_list[1:3]" deleting elements from the list: ',sample_list)

del sample_list
print('\n"del sample_list" deleted the sample_list variable')

'''
Existence of an element in the list.
'''
my_list = ["A", "B", 1, 2]
print('\nOther list: ', my_list)
print('\nA in my_list?: ',"A" in my_list) 
print('\nC not in my_list?: ',"C" not in my_list) 
print('\n2 not in my_list?: ',2 not in my_list)