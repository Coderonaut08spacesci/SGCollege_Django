const menuToggle = document.getElementById("menu-toggle");
const mainNav = document.getElementById("main-nav");

menuToggle.addEventListener("click", function () {

    mainNav.classList.toggle("active");

    const isOpen = mainNav.classList.contains("active");

    menuToggle.setAttribute("aria-expanded", isOpen);

    if (isOpen) {
        menuToggle.innerHTML = "✕";
        menuToggle.setAttribute("aria-label", "Close navigation menu");
    } else {
        menuToggle.innerHTML = "☰";
        menuToggle.setAttribute("aria-label", "Open navigation menu");
    }

});