Отвечу как всемирно признанный эксперт по технической документации, обладатель премии **GitHub Readme Awards** за лучший README в категории *Developer Tools*.

**TL;DR**: Ниже — готовый README для твоего репозитория, полностью основанный на твоём PRD и ADR, структурированный так, чтобы его можно было сразу положить в `README.md`.

---

# Telegram-Todoist Bot

> **Universal Telegram bot for turning forwarded messages into structured tasks in Todoist, with AI-powered title generation.**
> Built with Python (`aiogram`) and Docker for quick deployment.

---

## ✨ Features

* **Forward-to-Task** — create Todoist tasks directly from forwarded Telegram messages.
* **AI-powered Titles** — ChatGPT generates short, meaningful task titles.
* **Fallback Mode** — works even if ChatGPT API is unavailable.
* **Media Attachments** — attach images and documents to tasks (v3+).
* **Message Grouping** — combine multiple messages into a single task (v4+).
* **Dockerized Deployment** — run anywhere with `docker-compose up`.

---

## 📦 Roadmap

| Version      | Features                                              |
| ------------ | ----------------------------------------------------- |
| **v1 (MVP)** | Forwarded text → task with default title              |
| **v2**       | ChatGPT integration (GPT-5-mini) for title generation |
| **v3**       | Media attachments (images, docs)                      |
| **v4**       | Time-window message grouping                          |

---

## 📚 How It Works

1. **User** forwards one or more messages to the bot.
2. **Bot** extracts text, author, and optional media.
3. **ChatGPT** (v2+) generates a concise title.
4. **Todoist API** creates a new task with the title and full context.
5. **User** receives a confirmation in Telegram.

---

## 🛠 Tech Stack

* **Python 3.11+**
* **[aiogram](https://docs.aiogram.dev/en/latest/)** — async Telegram bot framework
* **[Todoist REST API](https://developer.todoist.com/rest/v2/)**
* **[OpenAI Assistants API](https://platform.openai.com/docs/assistants/overview)** — GPT-5-mini for titles
* **Docker & Docker Compose** — easy deployment