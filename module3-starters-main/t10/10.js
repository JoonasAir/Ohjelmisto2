const target = document.getElementById("target")
const form = document.getElementById("source")

form.addEventListener('submit', function(evt){
    evt.preventDefault()
    const fname = document.querySelector("input[name=firstname]").value
    const lname = document.querySelector("input[name=lastname]").value

    target.innerHTML = `Terve ${fname} ${lname}!`

})