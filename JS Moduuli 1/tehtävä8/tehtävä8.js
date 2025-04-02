"use strict";

let start_year = +prompt("Give the starting year.");

let end_year = +prompt("Give the ending year.");

for (let i = start_year; i <= end_year; i++) {
   if (i % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)){
   document.querySelector("#answer").innerHTML += "<li>" + i + "</li>";
}
}