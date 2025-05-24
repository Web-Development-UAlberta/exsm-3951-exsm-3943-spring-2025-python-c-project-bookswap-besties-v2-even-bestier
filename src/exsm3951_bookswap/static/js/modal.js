function openModal() {
  document.getElementById("searchModal")?.classList.remove("hidden");
}

function closeModal() {
  document.getElementById("searchModal")?.classList.add("hidden");
}

// ESC key closes modal
document.addEventListener("keydown", function (event) {
  if (event.key === "Escape") {
    closeModal();
  }
});

// Click backdrop to close
function closeModalOnBackdrop(event) {
  if (event.target.id === "searchModal") {
    closeModal();
  }
}
