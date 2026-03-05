class DataController:

    def __init__(self, service):
        self.service = service

    def get_patient_data(self):
        self.service.get_patient_data()

    def get_patient_name(self):
        return self.service.get_patient_name(self.service.patient_json, '665677', "http://tutsgnfhir.com")
