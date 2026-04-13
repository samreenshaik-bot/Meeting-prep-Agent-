import json
import os
from datetime import datetime


    
from hindsight_client import Hindsight

class HindsightMemory:
    def __init__(self):
        self.client = Hindsight(base_url="https://api.hindsight.vectorize.io")

    def add(self, contact_name, notes):
        self.client.add(
            content=notes,
            metadata={"contact": contact_name}
        )    

    def get(self, contact_name):
        return self.client.search(
            query=contact_name
        )

class ScheduleMemory:
    """
    A simple file-based JSON store for calendar events.
    """
    def __init__(self, db_path="schedules.json"):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            with open(self.db_path, 'w') as f:
                json.dump([], f)

    def _load(self):
        with open(self.db_path, 'r') as f:
            return json.load(f)

    def _save(self, data):
        with open(self.db_path, 'w') as f:
            json.dump(data, f, indent=4)

    def get_all(self):
        return self._load()

    def add(self, title, start, end=None):
        data = self._load()
        event = {
            "id": str(len(data) + 1),
            "title": title,
            "start": start
        }
        if end:
            event["end"] = end
        data.append(event)
        self._save(data)
        return event
