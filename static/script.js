function sendGuess() {
    const number = document.getElementById("number").value;

    fetch("/guess", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ number: number })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.message;
    });
}

function resetGame() {
    fetch("/reset", { method: "POST" })
    .then(res => res.json())
    .then(data => {
        document.getElementById("result").innerText = data.message;
    });
}