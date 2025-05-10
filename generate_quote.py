import random
import datetime
import re

# Load quotes
with open("quotes.txt", "r", encoding="utf-8") as f:
    quotes = [line.strip() for line in f if line.strip()]

quote = random.choice(quotes)
today = datetime.datetime.now().strftime("%d/%m/%Y")

new_quote_block = f'''<p align="center"><i>"{quote}"</i></p>
<p align="center"><small>Quote updated: {today}</small></p>'''

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Replace only the quote section
updated_content = re.sub(
    r'<!-- HERTA_QUOTE_START -->(.*?)<!-- HERTA_QUOTE_END -->',
    f'<!-- HERTA_QUOTE_START -->\n{new_quote_block}\n<!-- HERTA_QUOTE_END -->',
    content,
    flags=re.DOTALL
)

# Write updated README
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)

print("✅ Daily Herta quote updated successfully.")
