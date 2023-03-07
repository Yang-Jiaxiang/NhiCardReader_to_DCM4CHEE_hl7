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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((dcm4cheeAPI, dcm4cheePORT))
    client_socket.sendall(hl7_msg)

    # 讀取 server 回傳的 response
    response = b''
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        response += data

    # 關閉 socket 連線
    client_socket.close()

    # 將回傳的 response 轉換成字串，並印出來
    print(response.decode())

    # 處理可能的錯誤
    try:
        response_code = int(response.split(b' ')[1])
        if response_code == 404:
            print('404 Not Found')
        elif response_code == 500:
            print('500 Internal Server Error')
        # 其他錯誤處理...
    except Exception as e:
        print(e)
