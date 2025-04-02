"use strict";

question = confirm("Should I calculate the square root?");

if (question === true){
    question2 = +prompt("Enter the number")
    if (question2 < 0){
        document.querySelector("#answer").innerHTML = "The square root of a negative number is not defined."
    } else {
        document.querySelector("#answer").innerHTML = `Square root of number ${question2}  is ${Math.sqrt(question2)}.`
    }
} else {
    document.querySelector("#answer").innerHTML = "The square root is not calculated."
}

