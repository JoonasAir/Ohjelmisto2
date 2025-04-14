'use strict';
const names = ['John', 'Paul', 'Jones'];
const doc = document.querySelector("#target")

for (let name of names) {
    doc.innerHTML += "<li>" + name + "</li>" 
}

