'''
Keith Ginoel Gabinete
2020-03670
BS CS
'''
'''
Write recursive functions for the following:
a) Multiplication using repeated addition
b) Integer Division using repeated subtraction
'''

def menu(): 							# define a function for our main menu
	print("\nOptions:")
	print("[1] Multiplication")
	print("[2] Division")
	print("[0] Exit")

	choice = int(input("\nChoice: "))  	# ask an input from the user for the choice

	return choice 						# terminate our definition function menu() by returning the value of the choice input


def getProduct(x, y):  					# define a recursive function that gets the product of the two numbers(x and y) using repeated addition
	
	if y == 1:							# if y's value is already equal to 1 (due to the recursive function), return the final value of x
		return x

	elif y == 0:						# if the input value for y is 0, then the product of the two numbers is automatically equal to y which is 0
		return y

	return x + getProduct(x, y-1)   	# decrement the value of y by 1 every time the funcion recurs


def getQuotient(x, y, quotient):   		# define a function that gets the quotient of the two numbers(x and y) using repeated subtraction
										# the third parameter is allotted for the resulting quotient of the two numbers
										# note that the intial value of our quotient is zero (as specified in the call function in our while loop below)
	
	if x<y:								# if the value x is already lower than the input value for y, terminate the recursion and return the final value of quotient
		return quotient

	return getQuotient(x-y, y, quotient + 1) 	# increment the value of the parameter quotient by 1 every time the function recurs


def firstnumber(): 						# define a function that asks the value of the first number from the user
	x = int(input("Enter number: "))

	return x


def secondnumber():						# define a function that asks the value of the second number from the user
	y = int(input("Enter number: "))

	return y


# The print function below is just a quick info about our program
print("\nThis program uses recursive functions to perform multiplication or division operations between two given numbers.", end="\n")


# write an infinite loop for our program that will only terminate when a break statement is encountered
while True:
	choice = menu()  	# invoke the defintion function for our main menu

	if choice == 1:  	# if the user chooses option number 1, invoke our definition funtion for the multiplication operation
		print("Product:", getProduct(firstnumber(), secondnumber()))

	elif choice == 2:	# if the user chooses option number 2, invoke our definition funtion for the division operation
		print("Quotient:", getQuotient(firstnumber(), secondnumber(), 0))  # set the third paramater of the getQuotient function to 0

	elif choice == 0:	# if the user chooses option number 0, exit the program
		print("\nThank you for using this program!\n")
		break

	else:				# inform the user if he/she enters an option number unavailable in our menu
		print("\nInvalid Choice!")