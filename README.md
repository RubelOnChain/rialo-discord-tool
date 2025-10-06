# 🛠️ Rialo Discord Tool  

A community-built **Discord tool written in Python** for the **Rialo ecosystem** — designed to automate roles, add engagement features, and make the community more interactive.  

---

## ✨ Features
- 🎮 Mini commands & games (quiz, reactions, XP)
- 🧩 Automatic role assignment
- 💬 Message listener for engagement tracking
- 🔔 Event and announcement notifier
- 🔐 Secure token-based authentication

---

## 🧠 Built With
- **Python 3.10+**
- **discord.py** library
- **Rialo theme styling**
- JSON / SQLite (for small data storage)

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/RubelOnChain/rialo-discord-tool.git
cd rialo-discord-tool

# 2. Install dependencies
pip install -r requirements.txt

# 3. Add your Discord bot token
# Create a file named `.env` and add this line:
DISCORD_TOKEN=your_bot_token_here

# 4. Run the bot
python main.py
