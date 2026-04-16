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

    def get_bmi(self, patient_id):
        return self.service.get_bmi(patient_id)

    def get_age(self, patient_id):
        return self.service.get_age(patient_id)
    def get_gender(self, patient_id):
        return self.service.get_gender(patient_id)

    def is_hypertension_risk(self, patient_id):
        return self.service.is_hypertension_risk(patient_id)

    def get_patient_blood_pressure_history(self, patient_id):
        return self.service.get_patient_blood_pressure_history(patient_id)