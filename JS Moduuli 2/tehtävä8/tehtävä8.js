"use strict";

let lista = ["Johnny", "DeeDee", "Joey", "Marky"];

function concat(array){
    let result = "";
    for (let i = 0; i < array.length; i++){
        result += array[i];
    }
    return result;
}

let result = concat(lista)

document.querySelector("#tag").innerHTML = result;

