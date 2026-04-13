from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from flask_cors import CORS
from memory import HindsightMemory, ScheduleMemory
from agent import AIPrepAgent
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "hackathon_super_secret")
CORS(app)

# Initialize components
memory_client = HindsightMemory()
schedule_client = ScheduleMemory()

# Try to initialize the agent (will fail if GROQ_API_KEY is missing)
try:
    agent = AIPrepAgent()
except ValueError as e:
    print(f"Warning: {e}")
    agent = None

@app.route('/')
def index():
    if 'logged_in' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Dummy authentication for hackathon
    username = request.form.get('username')
    if username:
        session['logged_in'] = True
        session['username'] = username
    return redirect(url_for('dashboard'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('index'))
    return render_template('dashboard.html', username=session.get('username', 'Agent'))

@app.route('/api/schedules', methods=['GET', 'POST'])
def schedules():
    if request.method == 'GET':
        return jsonify(schedule_client.get_all())
    elif request.method == 'POST':
        data = request.json
        title = data.get('title')
        start = data.get('start')
        
        if not title or not start:
            return jsonify({"error": "title and start date are required"}), 400
            
        event = schedule_client.add(title, start)
        return jsonify({"status": "success", "event": event})

@app.route('/add', methods=['POST'])
def add_meeting():
    data = request.json
    contact_name = data.get('contact_name')
    notes = data.get('notes')

    if not contact_name or not notes:
        return jsonify({"error": "contact_name and notes are required"}), 400

    result = memory_client.add(contact_name, notes)
    return jsonify(result)
@app.route('/prepare', methods=['POST'])
def prepare_meeting():
    try:
        data = request.json
        contact_name = data.get('contact_name')

        if not contact_name:
            return jsonify({"error": "contact_name is required"}), 400

        # 👇 If agent is missing → fallback instead of crash
        if not agent:
            return jsonify({
                "status": "success",
                "insights": {
                    "summary": "No AI agent available.",
                    "pending_tasks": "N/A",
                    "missed_follow_ups": "N/A",
                    "advice": "Set GROQ_API_KEY to enable AI."
                }
            })

        past_memories = memory_client.get(contact_name)
        insights = agent.generate_prep(contact_name, past_memories)

        return jsonify({
            "status": "success",
            "insights": insights
        })

    except Exception as e:
        print("🔥 PREP ERROR:", e)
        return jsonify({"error": str(e)}), 500





if __name__ == "__main__":
    app.run(debug=True)    

