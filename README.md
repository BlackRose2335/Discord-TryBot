# 🎲 Discord TryBot

A lightweight Discord bot for communities, providing simple and fun slash commands like `/try`, `/roll`, and `/coin`.

---

## ✨ Features

- `/try` → Randomly returns **"YES"** or **"NO"** for decisions  
- `/roll` → Rolls a random number between **1 and 20**  
- `/coin` → Flips a coin: **Heads** or **Tails**

---

## 🚀 Complete Setup Guide

### **1. Clone the repository**

```bash
git clone https://github.com/your-username/discord-trybot.git
cd discord-trybot
```

### **2. Install Python**

Make sure you have **Python 3.10** or **newer** installed.

Check your version:

```bash
python --version
```
If not installed, download it from [*python.org*](https://python.org).

---

### **3. Install dependencies**

Use pip to install required Python libraries:

```bash
python -m pip install -r requirements.txt
```

---

### **4. Create a .env file**

In the root project folder, create a file named .env with this content:

```bash
DISCORD_TOKEN=your_bot_token_here
```
Replace **your_bot_token_here** with your actual Discord bot token from the Discord Developer Portal.

#### **Keep this token secret!**

---

### **5. Run the bot**

Start your bot with:

```bash
python bot.py
```
Note: Without specifying a **guild ID**, slash commands will be registered **globally**.
It can take up to **1 hour** for commands to appear in **all servers your bot is in**.

---

### 🧾 Files included

- ***bot.py*** — main bot source code
- ***.env*** — environment variables (your bot token)
- ***requirements.txt*** — dependencies (discord.py, python-dotenv)
- ***.gitignore*** — ignores .env and Python cache files
- ***LICENSE*** — MIT License

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.