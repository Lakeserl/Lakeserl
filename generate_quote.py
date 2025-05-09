
import random
import datetime

with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

quote = random.choice(quotes)

today = datetime.datetime.now().strftime("%d/%m/%Y")

readme_content = f"""\ 
<h1 align="center">🌀 Daily Herta Quote</h1>

<p align="center"><i>"{quote}"</i></p>

<p align="center"><small>Quote updated: {today}</small></p>

---

> ✨ This quote refreshes automatically every day. Spin on! 🌀
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("✅ README.md updated with a new quote!")