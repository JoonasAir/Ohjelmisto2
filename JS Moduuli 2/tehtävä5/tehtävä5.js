"use strict";

let numblist = [];

let asknumb = +prompt("Give me a number:")

while (numblist.includes(asknumb) != true) {
    numblist.push(asknumb)
    asknumb = +prompt("Give me a number:")
}

console.log("Number allready added..")

numblist.sort((a, b) => a- b)
console.log("Printing all the given numbers in ascending order:")
for (let i of numblist){
    console.log(i)
}