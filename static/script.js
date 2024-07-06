document.getElementById("new-quote").addEventListener("click", function() {
    fetch("/quote")
        .then(response => response.json())
        .then(data => {
            document.getElementById("quote").innerText = data.quote;
        });
});
