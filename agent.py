import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class AIPrepAgent:
    def __init__(self):
        # We assume GROQ_API_KEY is available in the environment
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set in the environment variables.")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile" # Default high-performance groq model

    def generate_prep(self, contact_name: str, past_memories: list) -> dict:
        """
        Takes past meeting notes for a contact and generates a structured meeting prep brief.
        """
        
        if not past_memories:
            return {
                "summary": f"No past meetings found with {contact_name}.",
                "pending_tasks": "None",
                "missed_follow_ups": "None",
                "advice": "This seems to be your first meeting (or first logged meeting). Keep it introductory and establish baseline expectations."
            }
            
        memory_text = ""
        for idx, m in enumerate(past_memories, 1):
            memory_text += f"\n--- Meeting {idx} ({m.get('timestamp')}) ---\n{m.get('notes')}\n"

        system_prompt = """You are an AI Meeting Prep Agent.
Your job is to read the past meeting notes between the user and a specific contact, and generate a brief for their upcoming meeting.
You must return your output strictly in JSON format with the following keys:
{
    "summary": "Brief summary of the relationship and past discussions",
    "pending_tasks": "Bullet points of any tasks the user or contact committed to doing",
    "missed_follow_ups": "Identify tasks or promises from past meetings that have NOT been marked as done or seem delayed/forgotten",
    "advice": "Actionable advice on how the user should approach the upcoming meeting based on past context (e.g., 'Address the missed deadline first')."
}
Ensure the response is valid JSON and contains NO markdown wrapping like ```json.
"""

        user_prompt = f"Contact Name: {contact_name}\n\nHere are the notes from our past meetings:\n{memory_text}\n\nPlease generate the preparation brief."

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3,
            max_tokens=1024,
            response_format={"type": "json_object"}
        )

        try:
            content = response.choices[0].message.content
            return json.loads(content)
        except Exception as e:
            # Fallback in case of parse error
            return {
                "summary": "Failed to parse AI response.",
                "pending_tasks": "",
                "missed_follow_ups": "",
                "advice": str(e)
            }
