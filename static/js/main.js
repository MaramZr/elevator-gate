const navToggle = document.querySelector(".site-nav-toggle");
const siteNav = document.querySelector(".site-nav");

if (navToggle && siteNav) {
    navToggle.addEventListener("click", () => {
        const isOpen = siteNav.classList.toggle("site-nav--open");

        navToggle.setAttribute("aria-expanded", isOpen);
    });
}
/* =========================================
   FAQ SEARCH + FILTERS + ACCORDION
   ========================================= */

const faqSearchInput = document.querySelector("#faq-search-input");
const faqFilterButtons = document.querySelectorAll(".faq-filter");
const faqItems = document.querySelectorAll(".faq-item");

let activeFaqCategory = "all";

function updateFaqVisibility() {
    const searchTerm = faqSearchInput
        ? faqSearchInput.value.trim().toLowerCase()
        : "";

    faqItems.forEach((item) => {
        const question =
            item.querySelector(".faq-item__question")?.textContent.toLowerCase() || "";

        const answer =
            item.querySelector(".faq-item__answer")?.textContent.toLowerCase() || "";

        const itemCategory = item.dataset.category || "";

        const matchesSearch =
            question.includes(searchTerm) ||
            answer.includes(searchTerm);

        const matchesCategory =
            activeFaqCategory === "all" ||
            itemCategory === activeFaqCategory;

        const shouldShow = matchesSearch && matchesCategory;

        item.style.display = shouldShow ? "" : "none";

        if (!shouldShow) {
            item.open = false;
        }
    });
}


/* Search */

if (faqSearchInput) {
    faqSearchInput.addEventListener("input", updateFaqVisibility);
}


/* Filters */

faqFilterButtons.forEach((button) => {
    button.addEventListener("click", () => {
        activeFaqCategory = button.dataset.category;

        faqFilterButtons.forEach((btn) => {
            btn.classList.remove("faq-filter--active");
        });

        button.classList.add("faq-filter--active");

        updateFaqVisibility();
    });
});


/* Accordion */

faqItems.forEach((item) => {
    item.addEventListener("toggle", () => {
        if (!item.open) return;

        faqItems.forEach((otherItem) => {
            if (otherItem !== item) {
                otherItem.open = false;
            }
        });
    });
});