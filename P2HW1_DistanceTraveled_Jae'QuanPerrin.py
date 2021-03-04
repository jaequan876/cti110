# The aim of this program is to calculate the total distance traveled by a car
# March 4, 2021
# CTI - 110  P2HW1 - DistanceTraveled
# Jae'Quan Perrin
#
# Prompt user to enter speed of their car
# Prompt user to enter time traveled
# Calculate the total distance traveled
# Print the value entered for speed
# Print time traveled
# Print total distance traveled

print("Enter car's speed:")      
carspeed = float(input())      
print('Enter time traveled:')
time = float(input())
      
distance_trav = carspeed * time
      
print('Speed entered:', carspeed)
print('Time entered:', time)
      
print("Distance Traveled is", distance_trav)
      
