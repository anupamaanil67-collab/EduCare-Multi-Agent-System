import json

class SaveTool:
    def save(self, data):
        with open("latest_output.json", "w") as f:
            json.dump(data, f, indent=2)
