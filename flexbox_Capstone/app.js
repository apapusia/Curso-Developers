/* seleccionar los elementos */
const navToggle = document.querySelector(".nav-icon");
const links = document.querySelector(".menu-bar");

navToggle.addEventListener("click", function () {
   console.log(links.classList);
   if (links.classList.contains("show-menu-bar")) {
links.classList.remove("show-menu-bar");
  } else {
   links.classList.add("show-menu-bar");
  }
});