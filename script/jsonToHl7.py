import requests
from hl7apy.core import Message, Segment, Field

def jsonToHl7(json_data):
    # 創建HL7消息
    msg = Message("ADT_A01")
    data = json_data

    # 創建PID段
    pid = msg.add_segment("PID")
    pid.pid_1 = "1"
    pid.pid_3.cx_1 = data['id']
    pid.pid_3.cx_5 = 'TW'
    pid.pid_5.xpn_1 = data['name']
    pid.pid_7.ts_1=str(int(data['birthday'][0:2])+1911)+str(data['birthday'][2:6])
    pid.pid_8 = data["sex"]

    # 轉換為HL7字符串
    hl7_message = msg.to_er7()
    return hl7_message
