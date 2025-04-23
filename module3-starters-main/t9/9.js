"use strict";

const start = document.getElementById("start")

start.addEventListener('click', function(evt){
    const input = document.getElementById("calculation").value
    const p = document.getElementById("result")
    const split = input.split(/([+\-*/])/)
    let num1 = parseInt(split[0])
    let value = split[1]
    let num2 = parseInt(split[2])
    let result;

    switch(value){
        case "+":
            result = num1 + num2
            break
        case "-":
            result = num1 - num2
            break
        case "/":
            result = num1 / num2
            break
        case "*":
            result = num1 * num2
            break
        default:
            p.innerHTML = "Väärä syöte"
    }
    p.innerHTML = result

})