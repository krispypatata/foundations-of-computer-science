'''
Keith Ginoel Gabinete
2020-03670
BS CS
'''
'''
Create a python application that can hold records of products sold in a pet shop.
Each product record should contain
Product Number
Brand
Type of product
Weight
Number of items in stock

There should be options to:
Add a product
View a product
View all products
Delete a product
Delete all products
Exit

The following are sample entries:
1. (P001) Feline Fresh cat litter 5 kg (25 pcs)
2. (P002) Whiskas canned cat food 400g (25 pcs)
3. (P003) Vitality puppy food 5kg (30 pcs)
4. (P004) NutriChunks puppy food 5kg (30 pcs)
5. (P005) Holistic puppy food 5 kg (30 pcs)
6. (P006) Special Cat cat food 5kg (30 pcs)
'''

def options():  	# define a function for our options/main menu
					# print all the available choices in our main menu
	print("\nOptions:")
	print("\t[1] Add a product")
	print("\t[2] View a product")
	print("\t[3] View all products")
	print("\t[4] Delete a product")
	print("\t[5] Delete all products")
	print("\t[6] Save to file")
	print("\t[7] Load from file")
	print("\t[0] Exit")

	choice = int(input("\nChoice: ")) 		# ask the User what option number does he/she want to choose; typecast it into an integer

	print("")								# just print an empty string so there would be an empty line below the choice input

	return choice 							# return the input


def addProduct(productdictionary):			# define a function that will add a product in our Petshop dictionary
	productID = input("Enter Product ID: ") # ask a product ID from the user

	print("")								# just print an empty string so there would be an empty line below the choice input

	productoverallinfo = ""  				# assign an empty string that will store all the info of our product; this will then be added as a value to our Petshop dictionary along with its key

	if productID.upper() in productdictionary.keys(): # if the productID is already stored in our Petshop Dictionary, inform the user about it
		print("\nSorry, the product already exists!")

	else:
		# if the productID does not found in our Petshop dictionary then ask the user the product's info
		productBrand = input("Product brand: ")
		productType = input("Product type: ")
		productWeight = input("Product weight: ")
		productStock = input("Items in stock: ")

		# update our string variable productoverallinfo and add it to our Petshop dictionary as a dicitonary value along with the productID as a dictionary key
		# also add a delimiter pipe(|) that will separate our input values in the string (as we can use the split function() in strings for future purposes)
		productoverallinfo = productoverallinfo + productID.upper() + "|" + productBrand + "|" + productType + "|" + productWeight + "|" + productStock
		productdictionary[productID.upper()] = productoverallinfo

	return productdictionary  				# return the updated Petshop dictionary


def viewProduct(productdictionary): 		# define a function that will view all the info about a specific product given its productID
	productID = input("Enter Product ID: ") # ask the user for the product ID

	print("")								# just print an empty string so there would be an empty line below the productID input

	if productID.upper() in productdictionary.keys(): 	# if the productID is determined as key in our dictionary, then its value will be accessed
		productInfo = productdictionary[productID.upper()]

		# use the split function for strings to remove our delimiter pipe(|) in the corresponding value of our product ID
		newproductInfo = productInfo.split("|")
		
		# remove the product ID in the returned list newproductInfo
		newproductInfo.pop(0)

		# print all the elements in our list newproductInfo 
		# use the print function separately so each element in the list will always be printed in a new line
		print("PRODUCT INFO:")
		print("Product brand:", newproductInfo[0])
		print("Product type:", newproductInfo[1])
		print("Product weight:", newproductInfo[2])
		print("Items in stock:", newproductInfo[3])

	# if the productID does not found in our Petshop dicitionary, tell the user that the product does not exist
	else:
		print("Sorry, the product does not exist!")


def viewAllProducts(productdictionary):  	# define a function that will view all the products stored in our Petshop dictionary
	
	if len(productdictionary) == 0: 		# inform the user if the productdictionary is still empty
		print("NO STORED PRODUCTS YET!")

	# Else, proceed to view all the products stored in the dictionary
	else:
		print("ALL STORED PRODUCTS:") 					# just a print function for the heading of this definition function

		# express our Petshop dictionary as a secquence to print only the values stored in it
		for product in productdictionary.values():
			# use the split function for strings to remove our delitmiter pipe(|)
			productInfo = product.split("|")

			# add all the necessary characters that will make our output data more presentable
			productInfo.insert(0, "(")
			productInfo.insert(2, ")")
			productInfo.insert(-1, "(")
			productInfo.append(" pcs")
			productInfo.append(")")

			# insert spaces between each element of the list
			productInfo.insert(6, " ")
			productInfo.insert(5, " ")
			productInfo.insert(4, " ")
			productInfo.insert(3, " ")


			# express our list productInfo as a sequence in for loop for us to convert the data stored in it into immutable data type strings
			newproductInfo = ""
			for info in productInfo:
				newproductInfo = newproductInfo + info


			# print the resulting newproductInfo string
			print(newproductInfo)


def deleteProduct(productdictionary):  		# define a function that will delete a certain product given its productID
	productID = input("Enter Product ID: ") # ask the ID of the product the User wish to delete

	print("")								# just print an empty string so there would be an empty line below the productID input

	if productID.upper() in productdictionary.keys():  # if the productID exists in our Petshop Dictionary, delete that product's key:value pair in the dictionary
		del productdictionary[productID.upper()]
		print("Product", productID, "has been successfully deleted.")

	else:  									# if the productID does not found in our Petshop dictionary, tell the user that the product does not exist
		print("Sorry, the product does not exist!")

	return productdictionary 				# return the updated dictionary


def deleteAllProducts(productdictionary):  	# define a function that will delete all the products in our PetShop dictionary
	productdictionary.clear()
	print("All entries have been succesfully deleted!") # inform the user that all products are deleted successfully

	return productdictionary 				# return the updated dictionary


def savetoFile(productdictionary): 			# define a function that will save the current data of our program to a file named "Petshop_dictionary.txt"

	# open a file for writing
	fileHandle = open("Petshop_dictionary.txt", "w")

	# access each item in the dictionary by expressing the dicitonary as a sequence in for loop
	# store every item in our dictionary as a line in the new file 
	# use comma to separate the key:value pair from our dictionary
	for productInfo in productdictionary.values():
		fileHandle.write(productInfo + "\n")

	# close our fileHandle
	fileHandle.close()

	# inform the user that data are successfully stored in the file
	print("Data in the Petshop Dictionary have been successfully saved to a file!")

def loadfromFile(productdictionary):	# define a function that will load the data stored in a file named "Petshop_dictionary.txt"

	# erase the current items stored in the Petshop dictionary before loading data from a file
	productdictionary.clear()

	# open the file "Petshop_dictionary.txt" for reading
	fileHandle = open("Petshop_dictionary.txt", "r")

	# access each line in the file by expressing the fileHandle as sequence in for loop
	for line in fileHandle:
		productoverallInfo = line[0:-1].split("|")  	# perform a split function to separate data stored in each line
														# use splice function to only retrieve strings before the string "\n" in each line of the file

		# assign a variable for the first element in the returned list productoverallInfo
		# this element is simply the ID of the product which will then be used as a key input in our dictionary
		productID = productoverallInfo[0]
		
		# the product's info is just the data stored in each line ("\n" string is not included)
		# this will then be used as a value input in our dicitionary
		productInfo = line[0:-1]

		# add the 2 retrieved data (productID and productInfo) as key:value pair into the Petshop dictionary
		productdictionary[productID] = productInfo

	# close our fileHandle
	fileHandle.close()

	# inform the user that data are successfully loaded from a file
	print("Data have been successfully loaded from a file!")


productsPetShop = {}  	# the empty PetShop dictionary mentioned on above definition functions (this empty dictionary will store all the info about our products)

print("\nWelcome to Animalaya Pet Shop!") # Greetings

while True: 			# create a loop that will only terminate when a break statement is encountered
	
	choice = options()  # invoke our options definition function
	
	if choice == 1:  	# if the User chooses option number 1, invoke our addProduct definition function
		addProduct(productsPetShop)


	elif choice == 2: 	# if the User chooses option number 2, invoke our viewProduct definition function
		viewProduct(productsPetShop)


	elif choice == 3: 	# if the User chooses option number 3, invoke our viewallProducts definition function
		viewAllProducts(productsPetShop)


	elif choice == 4:  	# if the User chooses option number 4, invoke our deleteProduct definition function
		deleteProduct(productsPetShop)


	elif choice == 5:  	# if the User chooses option number 5, invoke our deleteAllProducts definition function
		deleteAllProducts(productsPetShop)


	elif choice == 6:	# if the User chooses option number 6, invoke our savetoFile definition function
		savetoFile(productsPetShop)


	elif choice == 7:	# if the User chooses option number 7, invoke our loadfromFile definition function
		loadfromFile(productsPetShop)


	elif choice == 0: 	# if the User chooses option number 0, terminate our program
		print("Thank You for using this program!\n")
		break


	else: # inform the user if he/she entered an invalid choice
		print("Invalid choice!")






