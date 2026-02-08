import streamlit as st
import streamlit.components.v1 as components

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: linear-gradient(135deg, #000000, #1a1a2e);
  color: white;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
  overflow: hidden;
}

.container {
  margin-top: 70px;
  padding: 20px;
}

.line {
  font-size: 26px;
  opacity: 0;
  transition: opacity 0.6s ease;
}

.buttons {
  margin-top: 30px;
  display: none;
}

button {
  padding: 12px 32px;
  font-size: 18px;
  border: none;
  border-radius: 30px;
  cursor: pointer;
}

#yesBtn {
  background: #2ecc71;
  color: white;
  margin-right: 20px;
}

#noBtn {
  background: #e74c3c;
  color: white;
  position: absolute;
}
</style>
</head>

<body>
  <div class="container">
    <div id="line" class="line"></div>

    <div class="buttons" id="buttons">
      <button id="yesBtn" onclick="yesClicked()">YES 💕</button>
      <button id="noBtn">NO 😅</button>
    </div>

    <button id="nextBtn" onclick="nextLine()">Next 👉</button>
  </div>

<script>
const lines = [
  "Nenu scientist kaadu… kani nee smile chuste heart automatic ga react avtundi 😂❤️",
  "Cinema lo hero laaga dialogues raavu… kani feeling maatram full clarity 😌",
  "Nee msg vasthe chaalu… mood automatic ga happy mode lo ki velthadi 😄",
  "Arey idi love aa crush aa telidu… kani skip cheyyalekapothunna 😜",
  "Nuvvu navvutunte background lo music play avvali anipistundi 🎶😂",
  "Life lo logic miss ayina parledhu… nuvvu maatram miss avvakudadhu 😌❤️",
  "Ee Proposal Day roju cheppali anipinchindi…",
  "Cinema ending la kaadu idi… real life start avvali 💫",
  "Vani ❤️ … will you be my Valentine? 🌹💍"
];

let index = 0;
const lineDiv = document.getElementById("line");
const buttonsDiv = document.getElementById("buttons");
const nextBtn = document.getElementById("nextBtn");
const noBtn = document.getElementById("noBtn");

function nextLine() {
  lineDiv.style.opacity = 0;

  setTimeout(() => {
    lineDiv.innerHTML = lines[index];
    lineDiv.style.opacity = 1;

    if (index === lines.length - 1) {
      nextBtn.style.display = "none";
      buttonsDiv.style.display = "block";
    }

    index++;
    if (index >= lines.length) index = lines.length - 1;
  }, 300);
}

// NO button runs away 😈
function moveNoButton() {
  const maxX = window.innerWidth - noBtn.offsetWidth;
  const maxY = window.innerHeight - noBtn.offsetHeight;

  const x = Math.random() * maxX;
  const y = Math.random() * maxY;

  noBtn.style.left = x + "px";
  noBtn.style.top = y + "px";
}

noBtn.addEventListener("mouseenter", moveNoButton);

// YES clicked ❤️
function yesClicked() {
  document.body.innerHTML = `
    <div style="margin-top:120px; font-size:34px; color:white;">
      Vani ❤️ 😍<br><br>
      Naku telusu nuv YES antav ani 😌<br><br>
      From today… nuv naa Valentine 🌹💍
    </div>
  `;
}

nextLine();
</script>
</body>
</html>
"""

components.html(html_code, height=520)
