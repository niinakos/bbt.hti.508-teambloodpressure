class DataService:

    def __init__(self, repository):
        self.repository = repository
        self.patient_json = self.repository.load()
        # self.id_list = self.repository.save(self.patient_json)

    @staticmethod
    def get_patient_data(patient_json, patient_id, fullUrl):
        requesturl = fullUrl + "/Patient/" + patient_id
        for patient in patient_json:
            if patient[0]['fullUrl'] == requesturl:
                patient_info = patient  # ['resource']

                return patient_info

    @staticmethod
    def get_patient_name(patient_json, patient_id, fullUrl):
        requesturl = fullUrl + "/Patient/" + patient_id
        for patient in patient_json:
            if patient[0]['fullUrl'] == requesturl:
                resource_patient = patient[0]['resource']
                given = resource_patient['name'][0]['given'][0]
                surname = resource_patient['name'][0]['family'][0]

                return given, surname