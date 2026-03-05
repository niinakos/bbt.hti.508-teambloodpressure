import json
from pathlib import Path

class JsonRepository:

    def __init__(self, file_path):
        self.file_path = Path(file_path)

    def load(self):
        with open(self.file_path, 'rb') as json_file:
            return json.load(json_file)

    @staticmethod
    def save(patient_json):
        id_list = []
        for patient in patient_json:
            if patient[0]['resource']['resourceType'] == 'Patient':
                id = patient[0]['resource']['id']
            id_list.append(id)
        return id_list

    # TODO: Adding patient data to the repository



