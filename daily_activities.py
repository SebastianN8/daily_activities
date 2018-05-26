############################################################################################
# Unit 6_05
# daily_activities.py
# 
# Created by: Sebastian Navas
# Created on: May 26
# 
# This program determines the main activities to do depending on age.
########################################################################################### 

# Function
def determine_activities(age, day):
	# Variable in function 
	the_statement = None 
	# If statement
	if (age >= 18) and (day in the_week):
		the_statement = 'Time to get some work done!!!'
	elif (age < 18) and (day in the_week):
		the_statement = 'Time to go to school!!!'
	elif (day in the_weekend):
		the_statement = 'Time to relax for the weekend!!!'
	else:
		the_statement = 'Invalid input!'

	return the_statement





# Variables
the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
the_weekend = ['Saturday', 'Sunday']
the_age = int(input('What is you age: '))
the_day = raw_input('What day of the week is it today: ')

# Call the function
the_result = determine_activities(the_age, the_day)
print the_result
