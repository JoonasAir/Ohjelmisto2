"use strict";

let numblist = [];

let asknum = +prompt("Give me a number:")
numblist.push(asknum)

while (asknum != 0) {
    asknum = +prompt("Give me an another number:")
    numblist.push(asknum)
    }

numblist.sort((a,b) => b-a)

for (let i in numblist) {
    let numero = numblist[i]
    console.log(numero)
}