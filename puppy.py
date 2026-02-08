import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Puppy 🤍", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: linear-gradient(135deg, #0b0b12, #1a1a2e);
  color: #f2f2f2;
  font-family: 'Segoe UI', sans-serif;
  text-align: center;
}

.container {
  margin-top: 70px;
  padding: 30px;
}

.line {
  font-size: 23px;
  margin: 20px 0;
  opacity: 0;
  transition: opacity 1.4s ease;
}
</style>
</head>

<body>
  <div class="container" id="container"></div>

<script>
const lines = [
  "As a final act of love…",
  "",
  "Puppy 🤍",
  "",
  "Ee words nenu ninnu malli disturb cheyyadaniki kaadu.",
  "Cheppakapothe lopala unna nijam nannu baadha pedutondi ani cheppadaniki.",
  "",
  "Nenu ninnu chase cheyyaledu.",
  "Nenu ninnu force cheyyaledu.",
  "Nee silence ni, nee space ni respect chesa.",
  "",
  "Love ante daily matladadam kaadu ani ippudu ardham ayindi.",
  "Love ante oka vyakti ni vaalla space lo kuda safe ga feel cheyyadam.",
  "",
  "Na life lo oka time varaku nenu strong ga kanipinchaledu.",
  "But nenu build cheskuntunna —",
  "not to impress you, but to become a better human being.",
  "",
  "Nenu perfect kaadu.",
  "Neeku pain ichina moments unte, I genuinely regret that.",
  "",
  "Oka vishayam clarity ga cheppagalanu —",
  "ninnu love cheyyadam na biggest mistake kaadu.",
  "",
  "Nuvvu na life lo oka lesson.",
  "Oka meaning.",
  "Oka truth.",
  "",
  "Nenu ninnu marchipovadam kosam try cheyyadam kaadu.",
  "Ninnu marchipoyina act cheyyadam matrame nerchukuntunna.",
  "",
  "If life ever gives us a chance to talk again,",
  "I’ll come with patience, not expectations.",
  "",
  "And if that chance never comes…",
  "I’ll still wish you peace.",
  "I’ll still wish you happiness.",
  "",
  "Some people stay in our heart forever,",
  "even if they don’t stay in our life.",
  "",
  "Take care, Puppy 🤍"
];

const container = document.getElementById("container");

lines.forEach((text, i) => {
  setTimeout(() => {
    const div = document.createElement("div");
    div.className = "line";
    div.innerHTML = text;
    container.appendChild(div);
    setTimeout(() => { div.style.opacity = 1; }, 100);
  }, i * 1700);
});
</script>
</body>
</html>
"""

components.html(html_code, height=3000)


