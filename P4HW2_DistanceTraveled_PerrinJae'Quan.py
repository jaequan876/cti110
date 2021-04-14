# CTI - 110
# P4HW2 - Distance Traveled
# Jae'Quan Perrin
# April 12, 2021
#
# tell user to enter car speed
# tell user to enter hours traveled
# if hour is less than or equal to 0 display error and tell user to enter time aga
# calculate distance traveled when accurate time is entered
# output results
# ask user if they want to run the program again
# distance = speed * time

def program():
    speed = int(input("Enter car's speed:"))
    time = int(input("Enter time traveled:"))
    if time <= 0:
        print("Error! time entered should be >0")
        time = int(input("Enter time traveled:"))
    print("Time", "", "Distance")    
    for x in range(1, time + 1):
        distance = speed * x
        print(x, "\t", distance)
    question = input("Would you like to enter a different time? y for yes):")
    if question == "y":
        program()
    else:
        exit()
program()        
                     
     
    
                          
     

