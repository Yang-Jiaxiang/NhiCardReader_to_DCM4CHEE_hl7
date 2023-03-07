import requests
import json
import os
import socket
from dotenv import load_dotenv

load_dotenv()
dcm4cheeAPI=os.getenv("DCM4CHEE_API")
dcm4cheePORT=os.getenv("PORT")


def apiGetWorkList():
    try:
        response=requests.get(dcm4cheeAPI+"/WORKLIST/rs/workitems")
        if(response.status_code>=200 and response.status_code<=300):
            return {"status_code":200,"datas":response}
        else:
            return {"status_code":500}
    except requests.exceptions.RequestException as e:
        return {"status_code":500}

def apiPostWorkList(hl7_msg):
    dcm4cheeAPI
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((dcm4cheeAPI, dcm4cheePORT))
    client_socket.sendall(hl7_msg)
    client_socket.close()