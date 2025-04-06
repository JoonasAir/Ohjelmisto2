"use strict";

function rollthedice() {
    let dice = Math.floor(Math.random() * 6 ) + 1;
    return dice;
}

let result = rollthedice();

while (result != 6) {
    result = rollthedice()
    document.querySelector("#tag").innerHTML += "<li>" + result + "</li>";
}
