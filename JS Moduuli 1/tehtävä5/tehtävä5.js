"use strict";

let byear = +prompt("Tell me your year of birth:")

if (byear % 4 === 0 && (byear % 100 !== 0 || byear % 400 === 0)){
    document.querySelector("#answer").innerHTML = byear + " is a leap year."
} else {
    document.querySelector("#answer").innerHTML = byear + " is not a leap year."
}
 