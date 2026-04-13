class DataController:

    def __init__(self, service):
        self.service = service

    def get_patient_ids(self):
        return list(dict.fromkeys(self.service.get_patient_ids()))

    def get_patient_data(self):
        self.service.get_patient_data()

    def get_patient_name(self, patient_id):
        return self.service.get_patient_name(self.service.patient_json, patient_id, "http://tutsgnfhir.com")

    def get_patient_blood_pressure(self, patient_id):
        return self.service.get_patient_blood_pressure(patient_id)

    def is_patient_critical(self, patient_id):
        return self.service.is_patient_critical(patient_id)