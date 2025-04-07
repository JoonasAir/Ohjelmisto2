"use strict";

let ehdokasmäärä = +prompt("Enter how many candidates we have:");
let ehdokkaat =[];

let kierros = 1;


while (ehdokasmäärä > 0){
    let ehdokasnimi = prompt("Name for candidate " +kierros +".");

    ehdokkaat.push({
        name: ehdokasnimi,
        vote: 0
    });

    kierros += 1
    ehdokasmäärä -=1
}


let äänestäjät = +prompt("Enter how many voters we have:");

while (äänestäjät > 0){
    let äänestettävä = prompt("Who would you like to vote? Enter the name: ");

    let ehdokas = null;

    for (let i = 0; i < ehdokkaat.length; i++) {
        if (ehdokkaat[i].name === äänestettävä) {
            ehdokas = ehdokkaat[i];
            break;
        }
    }
    if (ehdokas !== null) {
        ehdokas.vote += 1;
    } 
    äänestäjät -= 1;
}

ehdokkaat.sort((a, b) => {
    return b.vote - a.vote;
});


console.log(`The winner is ${ehdokkaat[0].name} with ${ehdokkaat[0].vote} votes.`);

console.log("Results:");
for (let i = 0; i < ehdokkaat.length; i++) {
    console.log(`${ehdokkaat[i].name}: ${ehdokkaat[i].vote} votes`);
}