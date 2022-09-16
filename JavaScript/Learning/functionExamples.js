const example1 = () => "a string";

const example2 = () => {
    let blah = 123;

    return "a string 2";
}

function example3() {
    return "a string 3";
}

//console.log(example1());
//console.log(example2());
//console.log(example3());

function example4() {
    let blah = 2;
    console.log(blah);
    console.log("test2");

    return blah;
}

//console.log(example4());

//example4();

let variable3 = example4;
variable3();

let variable2 = example4();
console.log("test3");
console.log(variable2);

function function2() {
    
};

let variable4 = function2();
console.log(variable4);

let variable5 = function2;
console.log(variable5);
