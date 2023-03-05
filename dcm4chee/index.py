import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
dcm4cheeAPI=os.getenv("DCM4CHEE_API")

def apiGetWorkList():
    try:
        response=requests.get(dcm4cheeAPI+"/WORKLIST/rs/workitems")
        if(response.status_code>=200 and response.status_code<=300):
            return {"status_code":200,"datas":response}
        else:
            return {"status_code":500}
    except requests.exceptions.RequestException as e:
        return {"status_code":500}

def apiPostWorkList():
    url = "http://dcm4chee.luckypig.net:8080/dcm4chee-arc/aets/WORKLIST/rs/workitems"
    headers = {'Content-type': 'application/json'}
    data = {
        "ScheduledProcedureStepSequence": [
            {
                "ScheduledStationAETitle": "DCM4CHEE",
                "ScheduledProcedureStepStartDate": "20220306",
                "ScheduledProcedureStepStartTime": "100000",
                "Modality": "MR",
                "ScheduledPerformingPhysicianName": {
                    "Alphabetic": "Doe^John"
                },
                "ScheduledProcedureStepDescription": "Brain",
                "ScheduledProcedureStepID": "SPS_001",
                "ScheduledProcedureStepLocation": "Room1",
                "ScheduledStationName": "DCM4CHEE",
                "ScheduledProcedureStepStatus": "SCHEDULED",
                "PatientName": {
                    "Alphabetic": "健保測"
                },
                "PatientID": "A123457815",
                "PatientBirthDate": "19600127",
                "PatientSex": "M"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Work item created successfully.")
    else:
        print("Error creating work item:", response.status_code, response.text)