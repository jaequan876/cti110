# CTI - 110
# P2HW2 - List and Sets
# Jae'Quan Perrin
# March 10, 2021
#
# Prompt user to enter a series of ten numbers
# Display the lowest number in the list
# Display the highest number in the list
# Display the total of all the numbers in the list
# Display the average of the numbers in the list
# Convert the list into a set
# Display the set content

mylist = []
print('Please enter a number:')
num1 = float(input())
print('Please enter a second number:')
num2 = float(input())
print('Please enter a third number:')
num3 = float(input())
print('Please enter a fourth number:')
num4 = float(input())
print('Please enter a fifth number:')
num5 = float(input())
print('Please enter a sixth number:')
num6 = float(input())
print('Please enter a seventh number:')
num7 = float(input())
print('Please enter an eight number:')
num8 = float(input())
print('Please enter a ninth number:')
num9 = float(input())
print('Please enter a tenth number:')
num10 = float(input())
mylist.append(num1)
mylist.append(num2)
mylist.append(num3)
mylist.append(num4)
mylist.append(num5)
mylist.append(num6)
mylist.append(num7)
mylist.append(num8)
mylist.append(num9)
mylist.append(num10)
average = sum(mylist) / len(mylist)
print('Lowest number:', min(mylist))
print('Highest number:', max(mylist))
print('Total of numbers:', sum(mylist))
print('The average of the numbers is:', average)
mylist = str(mylist)
print('The list converted to a string is:', mylist)












