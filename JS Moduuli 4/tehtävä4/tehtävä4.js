"use strict";

const result = document.getElementById("results")
const form = document.getElementById("searchForm")

form.addEventListener('submit', async function(evt){
    evt.preventDefault()
    result.innerHTML = ""
    const search = document.querySelector("input[name=q]").value
    try {
        const response = await fetch(`https://api.tvmaze.com/search/shows?q=${search}`)
        const jsondata = await response.json()


        for(const data of jsondata){
            const h2 = document.createElement("h2")
            h2.innerText = data.show.name

            const figure = document.createElement("figure")
            const figcap = document.createElement("figcaption")

            
            const url = document.createElement("a")
            url.href = data.show.url
            url.target = "_blank"
            url.innerText = data.show.name
        
        
            const img = document.createElement("img")
            img.src = data.show.image?.medium || "https://via.placeholder.com/210x295?text=Not%20Found";
            img.alt = data.show.name

            const article = document.createElement("article")
            
            figcap.appendChild(url);        
            figure.appendChild(img);      
            figure.appendChild(figcap);    
            
            article.appendChild(h2);
            article.appendChild(figure);
            result.appendChild(article);
            
        }




    } catch(error) {
        console.log(error.message)
    }
}
)