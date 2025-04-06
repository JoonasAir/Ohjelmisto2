"use strict";

let doglist = [];
let num = 6;


while (num > 0){
    let dogname = prompt("Give me another dog name:");
    doglist.push(dogname)
    num -= 1
}

doglist.sort().reverse();

for (let i in doglist){
    let dname = doglist[i]
    document.querySelector("#tag").innerHTML += "<li>" + dname + "</li>" 
}