const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

trigger.addEventListener("mouseover", (event) =>  {
    target.src = "img/picB.jpg";
});

trigger.addEventListener("mouseout", (evet) => {
    target.src = "img/picA.jpg";
});
