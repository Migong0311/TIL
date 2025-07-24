document.addEventListener("DOMContentLoaded", () => {
  const input = document.getElementById("user-input");
  const button = document.getElementById("send-btn");

  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      button.click();
    }
  });

  button.addEventListener("click", sendMessage);

  // ✅ 추천 질문 랜덤 출력
  const box = document.querySelector(".suggestion-buttons");
  const shuffled = ssafyData.suggestions.sort(() => 0.5 - Math.random());
  const pickCount = 5;
  shuffled.slice(0, pickCount).forEach(text => {
    const btn = document.createElement("button");
    btn.textContent = text;
    btn.addEventListener("click", () => {
      input.value = text;
      button.click();
    });
    box.appendChild(btn);
  });
});

let loadingInterval;
let loadingElement;

async function sendMessage() {
  const input = document.getElementById("user-input");
  const message = input.value.trim();
  if (!message) return;

  displayMessage("user", message);
  input.value = "";

  startLoadingMessage();

  // ✅ 살짝 딜레이 주기 (DOM에 로딩 메시지 붙을 시간 확보)
  await new Promise(resolve => setTimeout(resolve, 500));

  try {
    const autoReply = getAutoReply(message);
    if (autoReply) {
      stopLoadingMessage();
      displayMessage("bot", autoReply);
    } else {
      const reply = await getGptReply(message);
      stopLoadingMessage();
      displayMessage("bot", reply);
    }
  } catch (error) {
    stopLoadingMessage();
    displayMessage("bot", "(답변을 불러오는 중 오류가 발생했습니다)");
    console.error(error);
  }
}


function displayMessage(sender, text) {
  const container = document.getElementById("chat-container");
  const msg = document.createElement("div");
  msg.className = `message ${sender}`;

  if (sender === "bot" && typeof marked !== "undefined") {
    msg.innerHTML = marked.parse(text);
  } else {
    msg.textContent = text;
  }

  container.appendChild(msg);
  container.scrollTop = container.scrollHeight;
}

function startLoadingMessage() {
  const container = document.getElementById("chat-container");

  loadingElement = document.createElement("div");
  loadingElement.className = "message bot";
  loadingElement.textContent = "ChatSAFY가 생각중입니다";
  container.appendChild(loadingElement);
  container.scrollTop = container.scrollHeight;

  let dotCount = 0;
  loadingInterval = setInterval(() => {
    dotCount = (dotCount + 1) % 4;
    loadingElement.textContent = "ChatSAFY가 생각중입니다" + ".".repeat(dotCount);
  }, 100);
}

function stopLoadingMessage() {
  if (loadingInterval) clearInterval(loadingInterval);
  if (loadingElement) loadingElement.remove();
  loadingElement = null;
}

async function getGptReply(prompt) {
  const res = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer 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",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: prompt }]
    })
  });

  const data = await res.json();
  return data.choices?.[0]?.message?.content || "(답변을 불러오지 못했습니다)";
}

// ✅ "오늘의 점심" 자동 응답 (요일 기반 식단 샘플)
function getTodayLunchMenu() {
  const menuMap = {
    0: "🌞 일요일: 급식 없음",
    1: "🍚 월요일 메뉴: 김치볶음밥, 계란후라이, 미소된장국",
    2: "🍜 화요일 메뉴: 제육덮밥, 콩나물국, 배추김치",
    3: "🍛 수요일 메뉴: 돈까스, 양배추샐러드, 우동국물",
    4: "🍲 목요일 메뉴: 부대찌개, 소시지볶음, 쌀밥",
    5: "🍝 금요일 메뉴: 크림파스타, 마늘빵, 오렌지주스",
    6: "🍱 토요일: 급식 없음"
  };
  const today = new Date().getDay();
  return `**[오늘의 점심메뉴]**\n\n${menuMap[today] || "급식 정보 없음"}`;
}

// ✅ 자동 응답 매칭 함수
function getAutoReply(question) {
  const lowerQ = question.toLowerCase().replace(/\s/g, "");

  if (lowerQ.includes("점심") || lowerQ.includes("메뉴")) {
    return getTodayLunchMenu();
  }

  // ssafyData.info 대응
  for (const [title, obj] of Object.entries(ssafyData.info || {})) {
    if (lowerQ.includes(title.replace(/\s/g, "").toLowerCase())) {
      return `**[${title}]**\n\n${obj.description}`;
    }
  }

  return null;
}
