const button = document.getElementById("source");
const result = document.getElementById("target")

button.addEventListener("submit", (event) =>{
    event.preventDefault();
    const first = document.querySelector("input[name='firstname']").value;
    const second = document.querySelector("input[name='lastname']").value;
    

    result.innerHTML = `Your name is ${first} ${second}.`
})

