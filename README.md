
# Meeting-prep-Agent

🧠 AI Meeting Prep Agent with Hindsight Memory

An intelligent full-stack application that acts as your personal meeting assistant, using semantic memory to store, recall, and synthesize insights from past interactions — so you never walk into a meeting unprepared again.

🚀 Overview

The AI Meeting Prep Agent is a Flask-based application that leverages a memory system (simulating Hindsight) and an LLM (Groq/OpenAI) to:

Store meeting notes with context

Retrieve relevant past interactions

Generate AI-powered meeting preparation summaries

Instead of manually reviewing notes, the system provides context-aware insights instantly.
=================================================================================================================================================================================================================================
🎯 Key Features

🧠 Persistent Memory System

Stores meeting notes and retrieves them using contact-based queries.

⚡ AI-Powered Insights

Generates summaries, action items, and recommendations using LLMs.

📅 Meeting Dashboard UI

Clean interface to manage schedules, notes, and preparation.

🔄 Continuous Learning Loop

The more you use it, the smarter your meeting preparation becomes.

🌐 Full-Stack Implementation

Built using Flask, HTML/CSS/JS, and AI APIs.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
🏗️ Project Architecture

AI-Meeting-Prep-Agent/
│
├── app.py                  # Main Flask server

├── agent.py               # AI logic (LLM integration)

├── memory.py              # Simulated Hindsight memory layer

├── memory_store.json      # Local memory storage

├── requirements.txt       # Dependencies

├── .env.example           # API key template
│
├── templates/
│   └── index.html         # Frontend UI
│
└── static/                # (Optional) CSS/JS assets

🧩 How It Works

1️⃣ Add Meeting Notes

Users store interaction details:

Preferences
Discussions
Action items

Stored in:

{
  "contact": "Rahul",
  
  "notes": "Discussed project deadline, report pending"
}

2️⃣ Memory Storage

The system uses a local simulated Hindsight layer:

Stores data in memory_store.json

Mimics real API behavior (.add() and .search())

3️⃣ Generate Meeting Preparation

When preparing for a meeting:

Past notes are retrieved

Sent to AI (Groq/OpenAI)

AI returns structured insights

4️⃣ AI Output Example
{
  "summary": "Previously discussed project deadlines.",
  "pending_tasks": ["Send report"],
  "missed_followups": ["Report not submitted"],
  "advice": "Follow up on pending deliverables before meeting."
}

----------------------------------------------------------------------------------------------------------------------------
🛠️ Tech Stack

Backend

Python

Flask

Flask-CORS

AI / LLM

Groq API (Primary)

OpenAI (Fallback)

Memory Layer

Simulated Hindsight Memory

JSON-based persistence

Frontend

HTML

CSS (Dark UI + Glassmorphism)

JavaScript

=====================================================================================================================================================================================================================================================
⚙️ Setup Instructions

1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-meeting-prep-agent.git

cd ai-meeting-prep-agent

2️⃣ Create Virtual Environment

python -m venv venv

venv\Scripts\activate   # Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Setup Environment Variables

Create .env file:

GROQ_API_KEY=your_groq_api_key

OPENAI_API_KEY=your_openai_key (optional)'

5️⃣ Run the Application

python app.py

Open in browser:


<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/6d5661dc-8e46-495a-83c5-1fd8b19fbf5b" />


====================================================================================================================================================================================================================================================

Contributions are welcome! Feel free to fork and improve the project.

📄 License

This project is for educational and hackathon purposes.
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/13bb220f-3f85-4c57-8c54-a65cce5c4413" />
