"use strict";

const form = document.getElementById("searchForm")
const results = document.getElementById("results")

form.addEventListener("submit", async function (evt) {
  evt.preventDefault()
  results.innerHTML = ""

  const search = document.querySelector("input[name=q]").value

  try {
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${search}`)
    const data = await response.json();

    for(const joke of data.result) {
    const article = document.createElement("article")
    const p = document.createElement("p")
    p.innerText = joke.value;

    article.appendChild(p)
    results.appendChild(article)
      }
    

  } catch (error) {
    console.error("Error fetching jokes:", error)
    results.innerHTML = "<p>Something went wrong while fetching jokes.</p>"
  }
});