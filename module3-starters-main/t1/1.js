const add = document.querySelector("#target")

add.classList.add("my-list");

const html = `<li>First item</li>
             <li>Second item</li>
             <li>Third item</li>`


add.innerHTML = html;
