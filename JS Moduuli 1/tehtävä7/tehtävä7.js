"use strict";


let calculator = 0
let sum = 0

let  dice_rolls = +prompt("How many times do you want to roll the dice?");


do {
    let dice = Math.floor(Math.random()*6)+1;
    sum += dice
    calculator += 1
    
} while (calculator < dice_rolls);

document.querySelector("#answer").innerHTML = `Rolled dice ${calculator} times, total sum is ${sum}.`

