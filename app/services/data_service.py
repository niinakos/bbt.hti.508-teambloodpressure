from datetime import datetime
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

    # haetaan BMI
    def get_bmi(self, patient_id):
        bmi = None
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
                # bmi
                if code == "39156-5":
                    bmi = value


        return bmi

    # haetaan ikä


    def get_age(self, patient_id):
        for entry in self.patient_json:
            if isinstance(entry, list):
                items = entry
            elif isinstance(entry, dict):
                items = [entry]
            else:
                continue

            for item in items:
                resource = item.get("resource", {})

                # Etsitään Patient-resurssi
                if resource.get("resourceType") != "Patient":
                    continue

                # Match id (string vs int varmistus)
                if str(resource.get("id")) != str(patient_id):
                    continue

                birth_date_str = resource.get("birthDate")
                if not birth_date_str:
                    return None

                try:
                    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d").date()
                    today = datetime.today().date()

                    age = today.year - birth_date.year - (
                        (today.month, today.day) < (birth_date.month, birth_date.day)
                    )

                    return age

                except ValueError:
                    return None

        return None

    def get_gender(self, patient_id):
        for entry in self.patient_json:
            if isinstance(entry, list):
                items = entry
            elif isinstance(entry, dict):
                items = [entry]
            else:
                continue

            for item in items:
                resource = item.get("resource", {})

                # Etsitään Patient-resurssi
                if resource.get("resourceType") != "Patient":
                    continue
                if str(resource.get("id")) != str(patient_id):
                    continue
                gender = resource.get("gender")
                if not gender:
                    return None


                return gender
        return None


    # is_hypertension_risk
    def is_hypertension_risk(self, patient_id):
        age = self.get_age(patient_id)
        bmi = self.get_bmi(patient_id)
        systolic, diastolic = self.get_patient_blood_pressure(patient_id)
        if age is None or bmi is None or systolic is None or diastolic is None:
            return False
        if age > 65 and (systolic >= 130 or diastolic >= 80):
            return True

        if bmi > 27 and (systolic >= 130 or diastolic >= 80):
            return True
        if systolic >= 140 or diastolic >= 90:
            return True
        return False

    def get_patient_blood_pressure_history(self, patient_id):
        readings = {}

        for entry in self.patient_json:
            if isinstance(entry, list):
                items = entry
            elif isinstance(entry, dict):
                items= [entry]
            else:
                continue
            for item in items:
                resource= item.get("resource", {})
                if resource.get("resourceType") != "Observation":
                    continue
                subject_ref = resource.get("subject", {}).get("reference")
                if subject_ref != f"Patient/{patient_id}":
                    continue

                coding = resource.get("code", {}).get("coding", [])
                if not coding:
                    continue

                code = coding[0].get("code")
                if code not in ("8480-6", "8462-4"):
                    continue

                value= resource.get("valueQuantity", {}).get("value")
                date= resource.get("effectiveDateTime")

                if value is None or date is None:
                    continue

                if code not in ("8480-6", "8462-4"):
                    continue

                if date not in readings:
                    readings[date] = {
                        "date": date,
                        "systolic": None,
                        "diastolic": None,
                    }

                if code == "8480-6":
                    readings[date]["systolic"] = value
                elif code == "8462-4":
                    readings[date]["diastolic"] = value

        result = list(readings.values())
        result.sort(key=lambda x: x["date"])

        return result
