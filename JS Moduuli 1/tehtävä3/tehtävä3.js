let number1 = +prompt("Insert first numbers")
let number2 = +prompt("Insert second numbers")
let number3 = +prompt("Insert third numbers")

sum = number1 + number2 + number3
product = number1 * number2 * number3
average = sum / 3

document.querySelector("#sum").innerHTML = ("Sum of given numbers is: " +sum);
document.querySelector("#product").innerHTML = ("Product of given numbers is: " +product);
document.querySelector("#average").innerHTML = ("Average of given numbers is: " +average);
