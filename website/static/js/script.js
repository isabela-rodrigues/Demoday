let menuBarra = document.querySelector("div:nth-child(2)");
let nav = document.querySelector("nav");
let input = document.querySelector("input");
let botao = document.querySelector("button");
let h2 = document.querySelector("h2");

function mostrarMenu(){
    
    nav.classList.toggle("visivel");
    menuBarra.classList.toggle("ativo");
}

menuBarra.onclick = mostrarMenu;
