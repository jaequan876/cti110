# Define your function here 
def miles_to_laps(user_miles):
    num_laps = user_miles * 4
    return num_laps
    

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    user_miles = float(input())
    print('{:.2f}'.format(miles_to_laps(user_miles)))
    