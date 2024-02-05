# CMSC 12 Lab #2: Selection Statements
# Write a program that prints the largest odd number given three numbers.

print("This program determines the largest odd number among three given integers.")

number1 = int(input("Enter a number:"))
number2 = int(input("Enter a number:"))
number3 = int(input("Enter a number:"))

if number1%2 != 0:
	if number1>=number2 and number1>=number3:
		print("The largest odd number is", number1, ".")
	elif number2%2 != 0:
		if number3%2 == 0:
			print("The largest odd number is", number2, ".")

		elif number3%2 != 0:
			if number2>=number3:
				print("The largest odd number is", number2, ".")
			else:
				print("The largest odd number is", number3, ".")
	
elif number2%2 != 0:
	if number3%2 == 0:
		print("The largest odd number is", number2, ".")
	elif number3%2 != 0:
		if number2>=number3:
			print("The largest odd number is", number2, ".")
		else:
			print("The largest odd number is", number3, ".")

elif number3%2 != 0:
			print("The largest odd number is", number3, ".")

else:
	print("There is no odd number given.")