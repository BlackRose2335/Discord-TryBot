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
- ***privacy.html*** — Privacy Policy page (needed for Discord app verification)
- ***terms.html*** — Terms of Service page (needed for Discord app verification)

---

## 🌐 Why the web server in ```bot.py```?

When deploying on free hosting services like Render, your bot needs to keep an open web port to avoid being shut down for inactivity.
The included minimal web server listens on port 8000, responding with a simple "TryBot is running!" message. 

This satisfies [*Render’s*](https://render.com) requirement and keeps the bot alive **24/7**.

---

## 📑 Discord App Verification

Discord requires public bots to have Privacy Policy and Terms of Service links for verification if they request certain permissions or are in many servers.

This repository includes simple privacy.html and terms.html files you can host on your domain or your Render app’s web server, and provide their URLs in your Discord Developer Portal application settings.

---

## 🔐 Security Policy

Please refer to our [Security Policy](./SECURITY.md) for details on how to report vulnerabilities.

We encourage responsible disclosure of security vulnerabilities. If you discover any, please contact us directly via Discord. You can find the full guidelines for reporting in the [Security Policy](./SECURITY.md).

---

## 🐞 Issue Reporting and Feature Requests

We welcome contributions and suggestions! If you encounter a bug or have a feature request, please use the provided templates for submitting your issues:

- [Bug Report](.github/ISSUE_TEMPLATE/bug_report.md)
- [Feature Request](.github/ISSUE_TEMPLATE/feature_request.md)

To submit a bug report or feature request, visit our [GitHub Issues](https://github.com/your-repo/issues) page and select the appropriate template.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.