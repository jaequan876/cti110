# CTI - 110
# P3HW2 - Distance Traveled
# Jae'Quan Perrin
# March 24, 2021
#
# Prompt user to enter speed of car
# Prompt user to enter time traveled
# Display error if user enters 0 or a negative number
# Calculate distance traveled for one hour
# Calculate distance traveled when accurate time is entered
# Print calculated amounts

print("Enter car's speed:")
speed = float(input())
print("Enter time traveled:")
time = float(input())
if time <= 0:
    print("Error! time entered should be >0")
    traveled = speed * 1
else:
    traveled = speed * time

print('Speed entered:', speed)
print('Time:', time)
print('Distance traveled:', traveled)

