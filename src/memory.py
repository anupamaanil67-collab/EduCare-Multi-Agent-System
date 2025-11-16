import json

class MemoryBank:
    FILE = "memory.json"

    def store(self, key, value):
        try:
            with open(self.FILE, "r") as f:
                data = json.load(f)
        except:
            data = {}

        data[key] = value

        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load(self, key):
        try:
            with open(self.FILE, "r") as f:
                data = json.load(f)
            return data.get(key)
        except:
            return None
