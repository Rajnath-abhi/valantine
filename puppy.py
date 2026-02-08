import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="For Puppy", layout="centered")

html_code = """
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
  color: #f2f2f2;
  font-family: 'Segoe UI', sans-serif;
  margin: 0;
}

.container {
  height: 90vh;
  overflow-y: auto;
  padding: 40px 30px;
}

.text {
  max-width: 650px;
  margin: auto;
  font-size: 20px;
  line-height: 1.9;
  animation: fade 1.5s ease;
}

.name {
  text-align: center;
  font-size: 26px;
  margin-bottom: 30px;
  color: #ffb6c1;
}

@keyframes fade {
  from { opacity: 0; transform: translateY(15px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>
</head>

<body>
  <div class="container">
    <div class="text">

      <div class="name">Puppy 🤍</div>

      Nuv vellipoyav.<br>
      Kaani nenu ninnu blame cheyyaledu.<br><br>

      Endukante nuv chesindi bhayam tho chesina decision ani naaku telusu.<br><br>

      Nenu ninnu hurt cheyyaledu.<br>
      Nenu ninnu force cheyyaledu.<br>
      Nenu na 100% try chesanu — kalisi undham ani.<br><br>

      Love fail avvadam tappu valla kaadu.<br>
      Bhayam valla.<br><br>

      Nenu aa bhayam ni ardham chesukuni silent ayya.<br>
      Ee silence weakness kaadu.<br>
      Idi self-respect.<br><br>

      Ee breakup nannu break cheyyaledu.<br>
      It changed me.<br><br>

      Ivvala nenu better unna.<br>
      Stronger unna.<br>
      Clear unna.<br><br>

      Ninnu impress cheyyadaniki kaadu —<br>
      nenu na life ni build chesukuntunna.<br><br>

      Oka roju nuv aalochiste —<br>
      “Vaadu em tappu cheyyaledu” ani,<br>
      adi regret kaadu.<br><br>

      Adi truth ki late ga vachina clarity.<br><br>

      Nuv vaste — clarity tho vastaanu.<br>
      Raakapoyina — respect tho vadilesthanu.<br><br>

      Because real love<br>
      doesn’t beg.<br>
      It just stays honest.

    </div>
  </div>
</body>
</html>
"""

components.html(html_code, height=600, scrolling=True)
