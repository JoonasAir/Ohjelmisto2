"use strict";

const form = document.getElementById("searchForm")

form.addEventListener('submit', async function(evt){
    evt.preventDefault()

    const search = document.querySelector("input[name=q]").value
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${search}`)
        const jsondata = await response.json()
        console.log(jsondata)
    } catch(error) {
        console.log(error.message)
    }
}
)