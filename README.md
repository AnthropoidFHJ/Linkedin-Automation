## LinkedIn Engagement Bot 🤖

**Project Overview**

The **LinkedIn Engagement Bot** is an intelligent automation tool designed to manage your LinkedIn presence effortlessly. It logs into your LinkedIn account, auto-generates meaningful posts, engages with connections by liking, commenting, and replying. All powered by **LLaMA3-70B** through the **Groq API**. Perfect for individuals or businesses aiming to stay active and build a professional audience without manual effort.

---

🔍 **How It Works**

1. **Login Automation**
   * Logs into LinkedIn using secure credentials.
   * Bypasses UI automation flags using stealth techniques.

2. **Post Creation with LLaMA3 (via Groq API)**
   * Reads a topic from `Topics.txt`.
   * Sends it to Groq LLM for a professional post generation.
   * Posts it automatically on your feed.

3. **Engagement Automation**
   * Likes recent posts in your feed.
   * Comments thoughtfully on connections’ posts using LLM.
   * Likes comments and replies on your own posts.
   * Uses Groq to reply naturally and professionally.

4. **Scheduling**
   * Uses `schedule` library to run automatically daily at 2 AM.

---

🔧 **Key Technologies**

* **Automation**: Python + Selenium + WebDriver Manager
* **LLM Integration**: Groq API (LLaMA3-70B)
* **Data Handling**: dotenv for secure credential storage
* **Scheduler**: `schedule` library for daily engagement
* **Logging**: Python `logging` module for tracking actions

---

📦 **Setup Instructions**

1. **Clone the Repository**

```bash
git clone https://github.com/AnthropoidFHJ/Linkedin-Automation
```

2. **Create and Activate a Conda Environment**

```bash
conda create -n linkedinBot python=3.10 -y
conda activate linkedinBot
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file:

```env
LINKEDIN_USERNAME="Email Address"
LINKEDIN_PASSWORD="Password"
GROQ_API_KEY="Groq-API Key"
```

5. **Prepare Your Topics**

Edit the `Topics.txt` file with one topic per line:

```
The role of AI in hiring
Remote work culture
Leadership in tech
```

6. **Run the Bot Manually**

```bash
python main.py
```

7. **(Optional) Run in Background Continuously**

Use `screen`, `tmux`, or Windows Task Scheduler to keep the bot running 24/7.

---

⚙️ **Workflow Summary**

```
Topics.txt → Groq API → Cleaned Content → LinkedIn Post
                                              ↓
                                            Feed → Like / Comment / Reply
```

---

🌟 **Future Enhancements**

* Smart sentiment detection for replies
* Scheduled posting with timezone support
* GUI-based dashboard for non-tech users
* Logging dashboard with metrics

---

🧪 **Deployment History**

* **Prototype**: Built locally and tested on test LinkedIn accounts
* **Logging**: Added logging support for troubleshooting
* **Scheduling**: Introduced `schedule` for time-based automation

---

**This project was created to help marketers, founders, and professionals automate consistent, high-quality engagement on LinkedIn without spending hours online.**

---

**Author:** Ferdous Hasan  
**Date:** 6 July 2025
