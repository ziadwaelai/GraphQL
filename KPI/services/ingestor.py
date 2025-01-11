import time
import json

class DataIngestor:
    def __init__(self, file_path, frequency=5):
        self.file_path = file_path
        self.frequency = frequency 

    def read_messages(self):
        """Read messages from a text file at the specified frequency."""
        with open(self.file_path, 'r') as file:
            for line in file:
                message = json.loads(line.strip())
                yield message
                time.sleep(self.frequency) 
