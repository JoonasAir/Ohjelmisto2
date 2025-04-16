const button = document.getElementById("start");

button.addEventListener("click", (event) =>{
    const input = document.getElementById("calculation").value;
    const result = document.getElementById("result");
    
    if(input.includes("+")) {
        let parts = input.split("+");
        number1 = parseInt(parts[0]);
        number2 = parseInt(parts[1])
        answer = number1 + number2;
        return answer
        
    } else if (input.includes("-")) {
        let parts = input.split("-");
        number1 = parseInt(parts[0]);
        number2 = parseInt(parts[1])
        answer = number1 - number2;

    } else if (input.includes("/")) {
        let parts = input.split("/");
        number1 = parseInt(parts[0]);
        number2 = parseInt(parts[1]);
        answer = number1 / number2;

    } else if (input.includes("*")) {
        let parts = input.split("*");
        number1 = parseInt(parts[0]);
        number2 = parseInt(parts[1])
        answer = number1 * number2
    } else {
        answer = "Väärä syöte";
    }

    result.innerHTML = answer;

});

