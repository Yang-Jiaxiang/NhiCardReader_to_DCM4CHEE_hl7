import requests
import sys
import os
from dotenv import load_dotenv
import socket
from hl7.client import CR, EB, SB, MLLPClient, MLLPException, mllp_send

load_dotenv()
dcm4cheeAPI=os.getenv("DCM4CHEE_API")
dcm4cheePORT=os.getenv("DCM4CHEE_POST")

def apiGetWorkList():
    try:
        response=requests.get("http://"+dcm4cheeAPI+":8080/dcm4chee-arc/aets/WORKLIST/rs/workitems")
        if(response.status_code>=200 and response.status_code<=300):
            return {"status_code":200,"datas":response}
        else:
            return {"status_code":500}
    except requests.exceptions.RequestException as e:
        return {"status_code":500}


def apiPostWorkList(hl7_msg):
    client = MLLPClient(dcm4cheeAPI, int(dcm4cheePORT))
    result = client.send_message(hl7_msg)
    print(result)
