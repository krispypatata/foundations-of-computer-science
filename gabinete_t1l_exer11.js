// EXER 11
// Keith Ginoel Gabinete
// 2020-03670
// BS CS

/*
Create a script that does the following:

Create a randomizer function that will be called with a 
click of a button that if asked where to eat,it will output 
a randomized or fast-food chain restaurant and a randomized 
food from that restaurant or fast-food chain. There should 
be only one data dictionary / array that should be used.
*/


// Create an object that holds the list of the food restaurants with their offered meals
const foodMenu = {
	'Jollibee': 'Jolly Hot Dog|Big Yum Burger|Ice Cream Sundae|Jolly Spaghetti|Chickenjoy',
	"McDonald's": 'Spicy McNuggets|Cheeseburger with Fries|McCafe Coffee Float|Spicy Chicken McDo|Chicken Fillet Ala King',
	'GreenWich': 'Hawaiian Overload|Pepperoni Overload|Bacon Overload|All-Beef Overload|Ham & Cheese Classic',
	'Mang Inasal': 'Chicken Inasal|Pork Bbq|Pork Sisig|Pinoy Halo-halo|Palabok',
	'Chowking': 'Sweet & Sour Fish Lauriat|Pork Choa Fan|Chinese-style Fried Chicken|Regular Meaty Wonton Mami|Chunky Asado Siopao'
}


// Create a button element in the html file with the createElement method in javascript
// We store this created button element in a variable so we can manipulate the behavior of this button easily
const eatButton = document.createElement('button');

// Add text inside our created Button
eatButton.innerText = 'Where To Eat?';

// Display the created button in the website
document.body.appendChild(eatButton);

// If the button is clicked, we'll execute a program that will output the randomized fastfood chain and its meal
eatButton.onclick = function () {
	// Get a random entry from our object/dictionary foodMenu and store it in the variable randomFoodChain
	const randomFoodChain = Object.entries(foodMenu)[Math.floor(Math.random()*Object.entries(foodMenu).length)];

	// Now, we'll split the contents of the second element in the array randomFoodChain and store the resulting split elements to the variable foodList so that we can choose a random meal from that food restaurant
	const foodList = randomFoodChain[1].split('|')

	// Get a random element from the resulting foodList array and store that random element to the variable randomFood
	randomFood = foodList[Math.floor(Math.random() * foodList.length)];
	
	// Now we have already successfully extracted a random food chain with its random meal from our foodMenu object/dictionary

	// We should always clear the console first before displaying the results in the console
	console.clear()

	// Display the results in our console when the button is clicked
	console.log(randomFoodChain[0], randomFood)

	// Display the results in the web site with the alert message when the button is clicked
	alert(`We should eat ${randomFood} in ${randomFoodChain[0]}.`)
}


