class DataService:

    def __init__(self, repository):
        self.repository = repository
        self.patient_json = self.repository.load()
        self.patient_ids = self.repository.save(self.patient_json)
        # self.id_list = self.repository.save(self.patient_json)

    def get_patient_ids(self):
        return self.patient_ids

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

    def get_patient_blood_pressure(self, patient_id):
        systolic = None
        diastolic = None
        latest_date=None

        for entry in self.patient_json:
            if isinstance(entry, list):
                items = entry
            elif isinstance(entry, dict):
                items = [entry]
            else:
                continue

            for item in items:
                resource = item.get("resource", {})

                if resource.get("resourceType") != "Observation":
                    continue

                subject_ref = resource.get("subject", {}).get("reference")
                if subject_ref != f"Patient/{patient_id}":
                    continue

                coding = resource.get("code", {}).get("coding", [])
                if not coding:
                    continue

                code = coding[0].get("code")
                value = resource.get("valueQuantity", {}).get("value")
                date = resource.get("effectiveDateTime")

                if value is None or date is None:
                    continue
                if latest_date is None or date > latest_date:
                    latest_date = date
                # systolinen
                if code == "8480-6":
                    systolic = value

                # diastolinen
                elif code == "8462-4":
                    diastolic = value

        return systolic, diastolic

    def is_patient_critical(self, patient_id):
        systolic, diastolic = self.get_patient_blood_pressure(patient_id)

        if systolic is not None and systolic >= 180:
            return True

        if diastolic is not None and diastolic >= 120:
            return True

        return False
    # haetaan sys ja dia päivämäärien mukaan (syke?)

    # haetaan syke

    #