/*
Your task is to create a function called getWeather that will have 2 parameters.
One called country and one called weatherType. Call the getWeather function with 2 arguments.
The first should be “Scotland”, the second should be “sunny”.
Your function should return the String “The weather in Scotland is sunny”.
Wrap the call to getWeather in a console.log() to print out the String.
Call the getWeather function two more times with countries and weatherTypes of your choice.
*/

const getWeather = (country, weatherType) =>
    `The weather in ${country} is ${weatherType}`;

console.log(getWeather('Scotland', 'sunny'));
console.log(getWeather('Antigua', 'bright and beautiful'));
console.log(getWeather('Kenya', 'raining lions'));

/*
I declared an arrow function with 2 parameters (country & weather type) which is stored in a const variable called getWeather
The function returns a template literal using string interpolation to insert the values of the parameters into a string
The function then returns the string
The function is wrapped in a call to console.log which takes the string value returned from the function and then passes it into
console.log as an argument
I then called the function 3 times with varying arguments
*/