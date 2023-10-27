let currentPlayer = "X";
const squares = document.querySelectorAll('.square');

squares.forEach((square, index) => {
    square.addEventListener('click', () => {
        if (square.textContent === "" && currentPlayer === "X") {
            square.textContent = currentPlayer;
            square.classList.add(currentPlayer);
            makeMove(index);
        }
    });
});

function makeMove(index) {
    fetch(`/move/${index}`)
        .then(response => response.json())
        .then(data => {
            const botMove = data.bot_move;
            if (botMove !== null) {
                squares[botMove].textContent = "O";
                squares[botMove].classList.add("O");
                checkWinner("O");
            }
        })
        .catch(error => console.error(error));
}

function checkWinner(player) {
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]            // Diagonals
    ];

    for (const combo of winningCombos) {
        const [a, b, c] = combo;
        if (squares[a].classList.contains(player) &&
            squares[b].classList.contains(player) &&
            squares[c].classList.contains(player)) {
            document.getElementById('w').textContent = `${player} Wins!`;
            return;
        }
    }

    if (![...squares].some(square => square.textContent === "")) {
        document.getElementById('w').textContent = "It's a Draw!";
    }
}
