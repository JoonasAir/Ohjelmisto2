"use strict";

let sides = +prompt("Syötä nopan suurin mahdollinen silmäluku")



function rollthedice(sides) {
    let dice = Math.floor(Math.random() * sides ) + 1;
    return dice;
}

let result = rollthedice(sides);

while (result != sides) {
    result = rollthedice(sides)
    document.querySelector("#tag").innerHTML += "<li>" + result + "</li>";
}

