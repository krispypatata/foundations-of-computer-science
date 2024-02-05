# Write a program that a student can use to compute their general weighted average (GWA) for 1semester (5 subjects). 
# The program should ask for user input, then print the resulting GWA.
# GWA = (grade*units)/units

name = input("What's your name?")
print('''
	Welcome''', name, '''! This program lets you compute your GWA in 5 subjects.
''')

print('''
For reference, UP uses the following grading scale:''')

print('''1.00		1.25		1.50		1.75		2.00 		
2.25		2.50		2.75		3.00		5.00
''')

print('''The weights (units) of these grades can be:
1.0		2.0		3.0		5.0
''')

grade1 = float(input("Grade in 1st subject:	"))
units1 = float(input("No. of Units Taken:	"))

grade2 = float(input('''
Grade in 2nd subject:	'''))
units2 = float(input("No. of Units Taken:	"))

grade3 = float(input('''
Grade in 3rd subject:	'''))
units3 = float(input("No. of Units Taken:	"))

grade4 = float(input('''
Grade in 4th subject:	'''))
units4 = float(input("No. of Units Taken:	"))

grade5 = float(input('''
Grade in 5th subject:	'''))
units5 = float(input("No. of Units Taken:	"))

gwa = float((grade1*units1 + grade2*units2 + grade3*units3 + grade4*units4 + grade5*units5)/(units1+units2+units3+units4+units5))

print('''
	Your resulting GWA is''', gwa, "Keep up the good work", name, "!")