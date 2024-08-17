document.addEventListener('DOMContentLoaded', function() {
    
    let currentYear = new Date().getFullYear();
    document.getElementById('currentYear').textContent = currentYear;

    console.log('scripts.js loaded');

    let selectBox = document.getElementById("bank");
    let otherBankInput = document.getElementById("otherBank");

    let expenseCategory = document.getElementById("expenseCategory");
    let otherCategory = document.getElementById("otherCategory");
    
    selectBox.addEventListener("change", function() {
        console.log(selectBox.value);
        let otherBankDiv = document.getElementById("otherBankDiv");
        if (selectBox.value === "other") {
            otherBankDiv.classList.remove("hidden");
            otherBankInput.focus();
        } else {
            otherBankDiv.classList.add("hidden");
        }
    });

    expenseCategory.addEventListener("change", function() {
        console.log(expenseCategory.value);
        if (expenseCategory.value === "other") {
            otherCategoryDiv.classList.remove("hidden");
            otherCategory.focus();
        } else {
            otherCategoryDiv.classList.add("hidden");
        }
    });

    const closeIcon = document.getElementById('close-icon');

    closeIcon.addEventListener('click', function() {
        const alertBox = document.getElementById('alert-box');
        alertBox.style.display = 'none';
    });
})
