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

button {
  margin-top: 40px;
  padding: 12px 32px;
  font-size: 18px;
  border: none;
  border-radius: 30px;
  background: #ff4d6d;
  color: white;
  cursor: pointer;
}

button:hover {
  background: #ff2e55;
}
</style>
</head>

<body>
  <div class="container">
    <div id="line" class="line"></div>
    <button onclick="nextLine()">Next 👉</button>
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
  "So… will you be my Valentine? 🌹💍"
];

let index = 0;
const lineDiv = document.getElementById("line");

function nextLine() {
  lineDiv.style.opacity = 0;
  setTimeout(() => {
    lineDiv.innerHTML = lines[index];
    lineDiv.style.opacity = 1;
    index++;
    if (index >= lines.length) index = lines.length - 1;
  }, 300);
}

nextLine();
</script>
</body>
</html>
"""

components.html(html_code, height=420)
