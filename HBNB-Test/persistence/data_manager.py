import json
from persistence.ipersistence_manager import IPersistenceManager

class DataManager(IPersistenceManager):
    def __init__(self):
        self.data = {}
        self._read_from_file()

    def save(self, entity):
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity.id] = entity.to_dict()
        self._write_to_file()

    def get(self, entity_id, entity_type):
        return self.data.get(entity_type, {}).get(entity_id)

    def update(self, entity):
        entity_type = type(entity).__name__
        self.data[entity_type][entity.id] = entity.to_dict()
        self._write_to_file()

    def delete(self, entity_id, entity_type):
        del self.data[entity_type][entity_id]
        self._write_to_file()

    def _write_to_file(self):
        with open('storage.json', 'w') as file:
            json.dump(self.data, file)

    def _read_from_file(self):
        try:
            with open('storage.json', 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            self.data = {}
