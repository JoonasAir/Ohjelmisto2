"use strict";

let dicecount = +prompt("Give a dice amount");

let eyesum = +prompt("For what eye numbers you want to calculate probability?");

let eyesumtotal = 0;
let mil = 1000000;
let sum;

for (let i = 1; i <= mil; i++) {
    sum = 0;

    for (let j = 1; j <= dicecount; j++){

    let dice = Math.floor(Math.random() * 6) +1;
    sum += dice;
    } if (sum === eyesum) {
        eyesumtotal += 1;
}  

}


let probability = (eyesumtotal / mil * 100).toFixed(2);


document.querySelector("#answer").innerHTML = `If you thwor ${dicecount} dices, probability to get total sum of ${eyesum} is ${probability}%.`