from hl7apy.parser import Message
import json

# 創建HL7消息
msg = Message("ADT_A01")

def jsonToHl7(json_data):
    data = json.loads(json_data)

    # 創建PID段
    pid = msg.add_segment("PID")
    pid.pid_3.cx_1 = data['id']
    pid.pid_5.xpn_1 = data['name']

    # 轉換為HL7字符串
    hl7_message = msg.to_er7()
    return hl7_message