"use strict";

let dicecount = +prompt("Give a dice amount")

let eyesum = +prompt("For what eye numbers you want to calculate probability?")

let eyesumtotal = 0

for (let i = dicecount; i <= 1000000; i+= dicecount) {
    let dice = Math.floor(Math.random() * 6) +1;
    let dicesum = dice * dicecount
    if (dicesum === eyesum){
        eyesumtotal += 1
    }

}
let probability = (eyesumtotal / 1000000 * 100).toFixed(2);


document.querySelector("#answer").innerHTML = probability