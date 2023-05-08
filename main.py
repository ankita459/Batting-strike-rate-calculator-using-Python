# Prompt the user to input the number of runs scored and balls faced
runs_scored = int(input("Enter runs scored: "))
balls_faced = int(input("Enter balls faced: "))

# Calculate the batting strike rate
strike_rate = (runs_scored / balls_faced) * 100

# Display the batting strike rate
print("Batting strike rate: {:.2f}".format(strike_rate))
