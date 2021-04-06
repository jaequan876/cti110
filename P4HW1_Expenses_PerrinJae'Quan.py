# CTI - 110
# P$HW1 - Expenses
# Jae'Quan Perrin
# April 5, 2021
#
# Prompt user to starting amount in account
# Prompt user to enter first expense
# Subtract expense from account
# Ask user if they want to enter another expense
# If user not to enter new expense, display info

account = int(input('Enter starting amount in account $'))
exp1 = int(input('Enter expense 1:'))
newacc = account - exp1
ques = input('Do you want to enter another expense?(y/n)')
count = 1
if ques == "n":
    print('Amount in account before expenses subtracted $', account)
    print('Number of expenses entered:', count)
    print('Amount in account after expenses subtracted is $', newacc)
else:
    exp2 = int(input('Enter expense 2:'))
    newacc = newacc - exp2
    count += 1
    print("Amount in account before expenses subtracted $", account)
    print("Number of expenses entered:", count)
    print("Amount in account after expenses subtracted is $", newacc)
    

    
