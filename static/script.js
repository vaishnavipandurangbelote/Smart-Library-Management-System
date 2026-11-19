// Load books automatically when page opens
window.onload = loadBooks;

// Display all books
function loadBooks() {
    fetch("/books")
        .then(response => response.json())
        .then(data => {
            let table = document.getElementById("bookTable");
            table.innerHTML = "";

            data.forEach(book => {

                let actionButtons = "";

                if (book.status === "Available") {
                    actionButtons += `<button class="issue-btn" onclick="updateStatus(${book.id}, 'Issued')">Issue</button>`;
                } else {
                    actionButtons += `<button class="return-btn" onclick="updateStatus(${book.id}, 'Available')">Return</button>`;
                }

                actionButtons += `<button class="delete-btn" onclick="deleteBook(${book.id})">Delete</button>`;

                table.innerHTML += `
                    <tr>
                        <td>${book.id}</td>
                        <td>${book.title}</td>
                        <td>${book.author}</td>
                        <td>${book.category}</td>
                        <td>${book.status}</td>
                        <td>${actionButtons}</td>
                    </tr>
                `;
            });
        });
}

// Add new book
function addBook() {

    const title = document.getElementById("title").value.trim();
    const author = document.getElementById("author").value.trim();
    const category = document.getElementById("category").value.trim();

    if (title === "" || author === "" || category === "") {
        alert("Please fill all fields.");
        return;
    }

    fetch("/books", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            author: author,
            category: category
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);

        document.getElementById("title").value = "";
        document.getElementById("author").value = "";
        document.getElementById("category").value = "";

        loadBooks();
    });
}

// Change book status
function updateStatus(bookId, status) {

    fetch("/books/" + bookId, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            status: status
        })
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadBooks();
    });
}

// Delete book
function deleteBook(bookId) {

    if (!confirm("Are you sure you want to delete this book?")) {
        return;
    }

    fetch("/books/" + bookId, {
        method: "DELETE"
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
        loadBooks();
    });
}