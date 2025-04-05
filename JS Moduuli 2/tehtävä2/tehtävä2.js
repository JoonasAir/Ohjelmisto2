"use strict";

const participants = []

let number = +prompt("Tell me how many participants we have?");

while (number > 0) {
    let names = prompt("Give me a participants name: ")
    participants.push(names);
    number -= 1;
}


for (let i in participants) {
    const participantname = participants[i]
    document.querySelector("#tag").innerHTML += "<li>" + participantname + "</li>";
}


