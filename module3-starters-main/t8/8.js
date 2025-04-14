const button = document.getElementById("start");

button.addEventListener("click", (event) =>{
    const selection = document.getElementById("operation").value;
    const result = document.getElementById("result");
    const num1 = document.getElementById("num1").value;
    const num2 = document.getElementById("num2").value;

    if (selection === "add"){
        sum = num1 + num2
        result.innerHTML = "Result is: " + sum
    } else if (selection === "sub") {
        sub = num1 - num2
        result.innerHTML = "Result is: " + sub
    } else if (selection === "multi") {
        multi = num1 * num2
        result.innerHTML = "Result is: " + multi
    } else if (selection === "div") {
        div = num1 / num2
        result.innerHTML = "Result is: " + div
}
})

