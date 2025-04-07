"use strict";

let lista = [2, 7, 4]

function even(array){
    let evens = [];
    for (let i = 0; i < array.length; i++) {
        if (array[i] % 2 === 0) {
            evens.push(array[i])
        }
    }return evens;
}
let result = even(lista)

console.log(lista)
console.log(result)