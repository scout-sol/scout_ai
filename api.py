import requests
import base64

class ScoutAgent:
    BASE_URL = "https://api.scout.onl/main.php"

    def __init__(self, api_key, agent_id=None, thread_id=None):
        self.api_key = api_key
        self.agent_id = agent_id
        self.thread_id = thread_id

    @classmethod
    def create(cls, api_key, name):
        params = {
            "action": "create-agent",
            "api_key": api_key,
            "name": name
        }
        response = requests.get(cls.BASE_URL, params=params)
        data = response.json()

        if data["status"] != "success":
            raise Exception("Failed to create agent:", data["message"])

        agent_data = data["data"]
        return cls(api_key, agent_data["agent_id"], agent_data["thread_id"])

    def query(self, message):
        if not self.agent_id:
            raise Exception("Agent ID is required to send a query")

        encoded_message = base64.b64encode(message.encode("utf-8")).decode("utf-8")

        params = {
            "action": "query-agent",
            "agent_id": self.agent_id,
            "message": encoded_message,
            "api_key": self.api_key
        }

        response = requests.get(self.BASE_URL, params=params)
        data = response.json()

        if data["status"] != "success":
            raise Exception("Query failed:", data["message"])

        return data["data"]["response"]
