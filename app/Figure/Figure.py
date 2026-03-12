from operator import truediv


def graph(patient, start_date, end_date):
    #get data from patient_json by patientID
    #POTILASID PITÄISI VALIKOITUA AUTOMAATTISESTI KUN OLLAAN POTILASSIVULLA
    requesturl = fullUrl + "/Patient/" + patient_id
    date_list = []
    sys_bp_list = []
    dia_bp_list = []
    hr_list = []

    for patient in patient_json:
        if patient[0]['fullUrl'] == requesturl:
            resource_patient = patient[0]['resource']
            date_list.append(patient[0]['EffectiveDateTime'][0])
            sys_bp_list.append(resource_patient['component'][0]['valueQuantity'][0]['value'][0])
            dia_bp_list.append(resource_patient['component'][0]['valueQuantity'][0]['value'][1])
            #EN VIELÄ LÖYTÄNYT SYKETTÄ SAMALLA AIKALEIMALLA
            #hr_list.appened(resource_patient[''][0]['heartRate'][0]) #KESKEN


    #figure
    fig = plt.figure(figsize=(12, 6))

    #MITEN PVM SÄÄDETÄÄN?
    #blood pressure
    plt.scatter(date_list, sys_bp_list, label="Systolic blood pressure")
    plt.scatter(date_list, dia_bp_list, label="Diastolic blood pressure")

    #heart rate fitted line
    #plt.plot(date_list, hr_list, label="Heart rate") #KESKEN

    # Axis
    plt.xlabel("Date")
    plt.ylabel("mmHg/bpm")
    plt.xlim(pd.to_datetime(start_date), pd.to_datetime(end_date))

    plt.legend()
    plt.grid(True)

    sys_bp = max(sys_bp_list)
    dia_bp = max(dia_bp_list)
    if critical_state(sys_bp, dia_bp)==True:
        print("Critical condition")

    return fig

def critical_state(sys_bp, dia_bp):
    #critical state alert
    personal_max_sys = None
    personal_max_dia = None

    # the user should be able to modify this
    if personal_max_sys is None:
        max_sys_bp = 140
    else:
        max_sys_bp = personal_max_sys

    if personal_max_dia is None:
        max_dia_bp = 90
    else:
        max_dia_bp = personal_max_dia

    # check if the value is above the max limit value
    if sys_bp > max_sys_bp or dia_bp > max_dia_bp:
        return True
    else:
        return False