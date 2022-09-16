// Template Literals allow embeded expressions ${expression}
let name = "Jayden"
console.log`Hello, ${name}`);
// Prints: Hello, Jayden
console.log(name.length);
// Prints: 6 (number of characters)

/*
Math.random() returns a random floating point number in the range from 0 (inclusive) up to,
but not including, 1.

Math.floor() returns the largest integer less than or equal to
*/

// Declaring Variables
var = preES6Version
let = reassignable
const = constant

if (false) {
    console.log('The code in this block will not run.');
  } else {
    console.log('But the code in this block will!');
  }
// Prints: But the code in this block will!

/*
<   Less than
>   Greater than
<=  Less than or equal to
>=  Greater than or equal to
=== Is equal to
!== Is not equal to
&&  The and operator
||  The or operator
!   The not operator, otherwise known as the bang operator
*/

function greeting (name = 'stranger') {
  console.log(`Hello, ${name}!`)
}
 
greeting('Nick') // Output: Hello, Nick!
greeting() // Output: Hello, stranger!

/* Scope refers to where variables can be accessed throughout the program, and is determined by where and how they are declared.
Blocks are statements that exist within curly braces {}.
Global scope refers to the context within which variables are accessible to every part of the program.
Global variables are variables that exist within global scope.
Block scope refers to the context within which variables are accessible only within the block they are defined.
Local variables are variables that exist within block scope.
Global namespace is the space in our code that contains globally scoped information.
Scope pollution is when too many variables exist in a namespace or variable names are reused. 

An array is represented by the square brackets [] and the content inside.
Each content item inside an array is called an element.
There are three different elements inside the array.
Each element inside the array is a different data type.

Arrays are lists that store data in JavaScript.
Arrays are created with brackets [].
Each item inside of an array is at a numbered position, or index, starting at 0.
We can access one item in an array using its index, with syntax like: myArray[0].
We can also change an item in an array using its index, with syntax like myArray[0] = 'new string';
Arrays have a length property, which allows you to see how many items are in an array.
Arrays have their own methods, including .push() and .pop(), which add and remove items from an array, respectively.
Arrays have many methods that perform different tasks, such as .slice() and .shift(), you can find documentation at the Mozilla Developer Network website.
Some built-in methods are mutating, meaning the method will change the array, while others are not mutating. You can always check the documentation.
Variables that contain arrays can be declared with let or const. Even when declared with const, arrays are still mutable. However, a variable declared with const cannot be reassigned.
Arrays mutated inside of a function will keep that change even outside the function.
Arrays can be nested inside other arrays.
To access elements in nested arrays chain indices using bracket notation.*/