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
