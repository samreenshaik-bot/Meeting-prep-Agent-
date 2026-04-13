import os
import json
from datetime import datetime


# =========================
# 🧠 LOCAL MEMORY (REPLACES HINDSIGHT)
# =========================
class HindsightMemory:
    def __init__(self, file_path="memory.json"):
        self.file_path = file_path

        # Create file if not exists
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.file_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=4)

    def add(self, contact_name, notes):
        """
        Store meeting notes locally
        """
        try:
            data = self._load()

            new_entry = {
                "contact": contact_name.lower(),   # normalize
                "notes": notes,
                "timestamp": str(datetime.now())
            }

            data.append(new_entry)
            self._save(data)

            print("✅ SAVED:", new_entry)  # debug

            return {"status": "success"}

        except Exception as e:
            print("🔥 ADD ERROR:", e)
            return {"status": "failed", "error": str(e)}

    def get(self, contact_name):
        """
        Retrieve past meetings for a contact
        """
        try:
            data = self._load()

            memories = []

            for item in data:
                if item.get("contact") == contact_name.lower():
                    memories.append({
                        "notes": item.get("notes", ""),
                        "timestamp": item.get("timestamp", "")
                    })

            print("✅ FOUND MEMORIES:", memories)  # debug

            return memories

        except Exception as e:
            print("🔥 GET ERROR:", e)
            return []


# =========================
# 📅 SCHEDULE MEMORY (LOCAL JSON)
# =========================
class ScheduleMemory:
    def __init__(self, db_path="schedules.json"):
        self.db_path = db_path

        if not os.path.exists(self.db_path):
            with open(self.db_path, "w") as f:
                json.dump([], f)

    def _load(self):
        with open(self.db_path, "r") as f:
            return json.load(f)

    def _save(self, data):
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        return self._load()

    def add(self, title, start, end=None):
        data = self._load()

        event = {
            "id": str(len(data) + 1),
            "title": title,
            "start": start,
            "end": end
        }

        data.append(event)
        self._save(data)

        return event