# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

#Solution
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
if __name__ == '__main__':
    list =  ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    new_list = []
    for x in range(len(list)):
        if not x in (0,4,5):
            new_list.append(list[x])
    print(new_list)