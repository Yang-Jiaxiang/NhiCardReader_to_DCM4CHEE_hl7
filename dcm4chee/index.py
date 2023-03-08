import requests
import sys
import os
import socket
from dotenv import load_dotenv

load_dotenv()
dcm4cheeAPI=os.getenv("DCM4CHEE_API")
dcm4cheePORT=os.getenv("DCM4CHEE_POST")

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
    RECV_BUFFER = 4096
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((dcm4cheeAPI, int(dcm4cheePORT)))
            s.send(hl7_msg.encode())

            # 等待dcm4chee回應，並接收回應
            data = s.recv(RECV_BUFFER)

            # 檢查dcm4chee的回應是否有錯誤訊息
            if "ERR" in data.decode():
                # 若dcm4chee的回應包含 "ERR"，則印出錯誤訊息
                print(f"Error: {data.decode()}")
            else:
                # 若dcm4chee的回應不包含 "ERR"，則印出回應訊息
                print(f"Response: {data.decode()}")
    except socket.error as e:
        # 捕捉socket錯誤，並印出錯誤訊息
        print(f"Socket error: {e}")
        sys.exit(1)
    except Exception as e:
        # 捕捉其他錯誤，並印出錯誤訊息
        print(f"Error: {e}")
        sys.exit(1)
    s.close()
