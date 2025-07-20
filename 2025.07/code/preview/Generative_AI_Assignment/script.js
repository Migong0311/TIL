document.addEventListener("DOMContentLoaded", () => {
  const goals = [
    "무사히 수료하기",
    "SW역량테스트 B형 취득",
    "26년도까지 취뽀",
    "남들에게 도움되는 서비스 개발"
  ];
  const centerCard = "14기 파이팅";
  let timerInterval;
  let startTime;
  let matchedCount = 0;
  let firstCard = null;
  let secondCard = null;
  let lockBoard = false;

  const gameBoard = document.getElementById("gameBoard");
  const timerDisplay = document.getElementById("timer");
  const modal = document.getElementById("modal");
  const resultTime = document.getElementById("result-time");
  const restartBtn = document.getElementById("restartBtn");

  restartBtn.addEventListener("click", resetGame);

  window.closeModal = function () {
    modal.classList.add("hidden");
    resetGame();
  };

  function shuffle(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
  }

  function startTimer() {
    startTime = new Date();
    clearInterval(timerInterval);
    timerInterval = setInterval(() => {
      const now = new Date();
      const diff = Math.floor((now - startTime) / 1000);
      const min = String(Math.floor(diff / 60)).padStart(2, '0');
      const sec = String(diff % 60).padStart(2, '0');
      timerDisplay.textContent = `${min}:${sec}`;
    }, 1000);
  }

  function showModal() {
    const now = new Date();
    const elapsed = timerDisplay.textContent;
    const timeStr = now.toLocaleTimeString();
    resultTime.textContent = `완료 시각: ${timeStr} / 경과 시간: ${elapsed}`;
    modal.classList.remove("hidden");
    clearInterval(timerInterval);
  }

  function createCard(text, index) {
    const div = document.createElement("div");
    div.classList.add("card");
    div.dataset.index = index;
    div.dataset.text = text;
    div.textContent = "";

    if (text === centerCard) {
      div.classList.add("flipped");
      div.textContent = centerCard;
    }

    div.addEventListener("click", () => {
      if (lockBoard || div.classList.contains("flipped") || text === centerCard) return;

      div.classList.add("flipped");
      div.textContent = text;

      if (!firstCard) {
        firstCard = div;
      } else {
        secondCard = div;
        lockBoard = true;

        setTimeout(() => {
          if (firstCard.dataset.text === secondCard.dataset.text) {
            firstCard.classList.add("matched");
            secondCard.classList.add("matched");
            matchedCount++;
            if (matchedCount === 4) {
              showModal();
            }
          } else {
            firstCard.classList.remove("flipped");
            secondCard.classList.remove("flipped");
            firstCard.textContent = "";
            secondCard.textContent = "";
          }
          firstCard = null;
          secondCard = null;
          lockBoard = false;
        }, 700);
      }
    });

    return div;
  }

  function renderBoard() {
    gameBoard.innerHTML = "";
    let cards = goals.flatMap(goal => [goal, goal]);
    shuffle(cards);
    const fullCards = [...cards.slice(0, 4), centerCard, ...cards.slice(4)];

    fullCards.forEach((text, index) => {
      const card = createCard(text, index);
      gameBoard.appendChild(card);
    });
  }

  function resetGame() {
    matchedCount = 0;
    firstCard = null;
    secondCard = null;
    lockBoard = false;
    timerDisplay.textContent = "00:00";
    modal.classList.add("hidden");
    renderBoard();
    startTimer();
  }

  // 최초 게임 시작
  resetGame();
});
