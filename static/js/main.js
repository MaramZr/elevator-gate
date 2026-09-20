const navToggle = document.querySelector(".site-nav-toggle");
const siteNav = document.querySelector(".site-nav");

if (navToggle && siteNav) {
    navToggle.addEventListener("click", () => {
        const isOpen = siteNav.classList.toggle("site-nav--open");

        navToggle.setAttribute("aria-expanded", isOpen);
    });
}