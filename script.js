const faqCards = [...document.querySelectorAll(".faq-card")];

document.querySelector("[data-action='expand']")?.addEventListener("click", () => {
  faqCards.forEach((card) => {
    card.open = true;
  });
});

document.querySelector("[data-action='collapse']")?.addEventListener("click", () => {
  faqCards.forEach((card) => {
    card.open = false;
  });
});

const currentYear = document.querySelector("#current-year");
if (currentYear) {
  currentYear.textContent = String(new Date().getFullYear());
}
