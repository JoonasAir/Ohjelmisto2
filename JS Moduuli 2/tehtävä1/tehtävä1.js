"use strict";

const lista = []

while (lista.length < 5) {
    let numero = +prompt("Give me a number between 1-10:")
    lista.push(numero)   
}

console.log(lista)


for (let i in lista) {
    lista.sort((a,b) => b-a)
    let list = lista[i]
    console.log(list)
}