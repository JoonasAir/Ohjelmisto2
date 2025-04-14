const target = document.querySelector("#target");

const first = document.createElement('li');
first.innerHTML = "First item";

const second = document.createElement("li");
second.innerHTML = "Second item";

const third = document.createElement("li");
third.innerHTML = "Third item";

second.classList.add('my-item');

target.appendChild(first);
target.appendChild(second);
target.appendChild(third);
