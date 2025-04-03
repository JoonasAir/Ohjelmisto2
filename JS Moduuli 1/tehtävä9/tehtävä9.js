"use strict";

let num = +prompt("Give me a number, i'll check is it a prime number or not.")

if (num < 2) {
    document.querySelector("#answer").innerHTML = "Given number " + num + " is not a prime number." 
} else {
    let isPrime = true;
    for (let jakaja = 2; jakaja <= Math.sqrt(num); jakaja++) { //Math.sqrt laskee ohjelman laskentatehoa, ei tarvitse käydä niin monta lukua läpi.
        if (num % jakaja === 0) {
        isPrime = false;
        break;
        }
    }

if (isPrime) {
    document.querySelector("#answer").innerHTML = "Given number " +num + " is a prime number." 
} else {
    document.querySelector("#answer").innerHTML = "Given number " +num + " is not a prime number."
}
}