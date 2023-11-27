import json

class MyData(object):
    def __init__(self, filename):
        self.filename = filename
        
    def load_data(self):
        with open(self.filename, 'r', encoding='CP866') as f:
            return json.load(f)
        
    def update_data(self, inserting_data):
        data = self.load_data()
        print(data)
        data.append(inserting_data)
        return data
    
    def save_data(self, data):
        with open(self.filename, 'w', encoding='CP866') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)