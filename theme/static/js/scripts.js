document.addEventListener('DOMContentLoaded', function() {

    let currentYear = new Date().getFullYear();
    document.getElementById('currentYear').textContent = currentYear;

    let selectBox = document.getElementById("bank");
    let otherBankInput = document.getElementById("otherBank");

    selectBox.addEventListener("change", function() {
        let otherBankDiv = document.getElementById("otherBankDiv");
        if (selectBox.value === "other") {
            otherBankDiv.classList.remove("hidden");
            otherBankInput.focus();
        } else {
            otherBankDiv.classList.add("hidden");
        }
    });

    let expenseCategory = document.getElementById("expenseCategory");
    let otherCategoryDiv = document.getElementById("otherCategoryDiv")
    let otherCategoryInput = document.getElementById("otherCategoryInput")
    let form = document.querySelector('form');

    expenseCategory.addEventListener("change", function() {
        if (expenseCategory.value === "other") {
            otherCategoryDiv.classList.remove("hidden");
            otherCategoryInput.focus();
        } else {
            otherCategoryDiv.classList.add("hidden");
        }
    });

    form.addEventListener('submit', function(event) {
        if (expenseCategory.value === "other" && otherCategoryInput.value.trim() !== "") {
            expenseCategory.value = otherCategoryInput.value.trim();
        }
    });


    let toastAlert = document.getElementById("toast-alert");
    if (toastAlert) {
        setTimeout(function() {
            toastAlert.classList.add("hidden");
        }, 5000);
    }

    function setupPaginationLinks() {
        const paginationLinks = document.querySelectorAll('.pagination-link');

        paginationLinks.forEach(link => {
            link.addEventListener('click', function (e) {
                e.preventDefault();

                const url = this.href;

                fetch(url, {
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                })
                .then(response => response.json())
                .then(data => {
                    const tableContainer = document.querySelector('#table-container');
                    tableContainer.innerHTML = data.html;

                    const paginationContainer = document.querySelector('#pagination-container');
                    paginationContainer.innerHTML = data.pagination_html;

                    history.pushState(null, '', url);

                    setupPaginationLinks();
                })
                .catch(error => console.error('Error:', error));
            });
        });
    }

    setupPaginationLinks();

    window.addEventListener('popstate', function () {
        const url = window.location.href;

        fetch(url, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
            }
        })
        .then(response => response.json())
        .then(data => {
            const tableContainer = document.querySelector('#table-container');
            tableContainer.innerHTML = data.html;

            const paginationContainer = document.querySelector('#pagination-container');
            paginationContainer.innerHTML = data.pagination_html;

            setupPaginationLinks();
        })
        .catch(error => console.error('Error:', error));
    });

});

document.querySelectorAll('.btn-danger').forEach(button => {
    button.addEventListener('click', function(e) {
        e.preventDefault();
        const accountId = this.getAttribute('data-account-id');
        const accountIdField = document.getElementById('account-id-field');
        accountIdField.value = parseInt(accountId);

        const form = document.getElementById('delete-account-form');
        form.setAttribute('action', `/banking/accounts/${accountId}/`);
    });
});

document.addEventListener('DOMContentLoaded', function () {
    let budgetInputFields = document.querySelectorAll(".budget-input");
    let resetBtn = document.getElementById("resetBudget");

    resetBtn.addEventListener('click', (event) => {
        event.preventDefault();
        budgetInputFields.forEach((input) => {
            input.value = "0.00";
        });
    });
});
