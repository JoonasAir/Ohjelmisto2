"use strict";

const username = prompt("Let's see which house of Hogwarts School of Witchcraft and Wizardry you belong to?");

const housenumber = Math.floor(Math.random()*4);

if (housenumber < 1) {
    document.querySelector('#answer').innerHTML = username + ", you are a Gryffindor!";
} else if (housenumber < 2) {
    document.querySelector('#answer').innerHTML = username + ", you are a Slytherin!";
} else if (housenumber < 3) {
    document.querySelector('#answer').innerHTML = username + ", you are a Hufflepuff!";
} else if (housenumber < 4) {
    document.querySelector('#answer').innerHTML = username + ", you are a Ravenclaw!";
}   
