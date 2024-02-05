'''
Keith Ginoel Gabinete
2020-03670
BS CS
'''
'''
# Create a program that asks the user for two positive integers, x and y, and performs the following operations on those integers:
1. Addition (x+y)
2. Subtraction (x-y)
3. Multiplication (using repeated addition)
4. Integer Division (using repeated subtraction)
5. Exponentiation (using repeated multiplication)
'''

def menu(): 				# define a function for our main menu
	print("\n1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("5. Exponentiation")
	print("0. Exit\n")

	choice = int(input("Enter your choice: ")) # asks for an input from the user (the input asked is the user's choice among the options in our menu)
	
	print("")				# just print an empty string so there would be an empty line below the choice input

	return choice 			# use a return command to terminate the definition function and return the value of choice


def firstNum(): 			# define a function that asks an input from from the user for the value of the first number
	firstNum = int(input("Enter first number: "))

	return firstNum			# return the value of the first number


def secondNum(): 			# define a function that asks an input from from the user for the value of the second number
	secondNum = int(input("Enter second number: "))

	return secondNum 		# return the value of the second number


def addition(x, y):			# define a function that adds our two integer inputs (x and y)
	Sum = x+y

	return Sum 				# return the value of the resulting sum


def subtraction(x, y):		# define a function that subtracts y from our integer x
	Difference = x-y
	
	return Difference 		# return the value of the resulting difference


def multiplication(x, y):	# define a function that multiplies x to y times

	# use for loop to get the product of x and y using repeated addition
	Sum = 0					# set an initial value for the sum of x and y in our repeated addition
	for addend in range(0,y):
		Sum = Sum+x 		# increment the value of our sum every time the addend in the range of our for loop is executed 
	
	return Sum 				# return the final value of Sum which is also the product of x and y


def division(x, y):			# define a function that divides x by y
	
	# get the quotient of x and y using repeated subtraction
	
	# We'll use while loop since we do not know the exact no. of times we need to be subtract y from our integer x to get their quotient
	Difference = x 					# assign a variable for the difference in our repeated subtraction that has an initial value equal to x
	quotient = 0 					# set an inital value for our quotient
	while Difference>=y: 			# perform the repeated subtraction
		Difference = Difference-y 	# update the value of our variable Difference
		quotient +=1 				# increment the value of quotient every time y is subtracted to the changing value x
					 				# The final value of the variable quotient is also our quotient/answer when x is divided by y
	
	remainder = Difference%y 		# solve for the remainder using the modulo operation
	
	return quotient, remainder 		# return the values of the quotient and the remainder


def exponentiation(x, y):	# define a function that multiplies x to itself y times
	
	# Use repeated multiplication to compute for the final value of x when it is multiplied to itself y times
	Product = 1	 							# initialize a value for our product
	for multiplier in range(0, y):			# write a for loop statement that performs repeated multiplication
		Product = Product*x 				# increment the value of 
	
	return Product 			# return the value of Product which is the answer when x is multiplied to itself y times



# invoke our firstNum and secondNum definition functions
x = firstNum()
y = secondNum()

while True:				# We'll use an infinite loop for our program since we don't want to terminate it until the user chooses to exit it(/until the program encounters a break statement) 

	choice = menu()		# invoke our menu function

	if choice==1:		# if the user chooses option 1 on our menu, the program will invoke our addition function to print the sum of x and y
		print("The sum of", x, "and", y, "is", addition(x, y))


	elif choice==2:		# if the user chooses option 2 on our menu, the program will invoke our subtraction function to print the difference between x and y
		print("The difference between", x, "and", y, "is", subtraction(x, y))


	elif choice==3:		# if the user chooses option 3 on our menu, the program will invoke our multiplication function to print the product of x and y
		print("The product of", x, "and", y, "is", multiplication(x, y))


	elif choice==4:		# if the user chooses option 4 on our menu, the program will invoke our division function to print the quotient of x and y and their remainder
		print("The quotient of", x, "and", y, "is", division(x, y)[0], "and the remainder is", division(x, y)[1])


	elif choice==5: 	# if the user chooses option 5 on our menu, the program will invoke our exponentiation function to print the product when x is muliplied to itself y times
		print(x, "raised to", y, "is", exponentiation(x, y))
	

	elif choice==0:		# if the user chooses 0 in our menu, the program will be terminated
		print("------------\n")
		break		
	

	else:				# if the user enters an invalid option number from our menu, the program will say that it is invalid and it'll continue the loop 
		print("\nNot a valid input!", end="\n\n")



