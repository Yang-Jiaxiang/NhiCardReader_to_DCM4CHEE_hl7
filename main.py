import requests
import tkinter as tk
import script.cardReader
import script.jsonToHl7
import dcm4chee.index as dcm4chee
import json

def checkConnection_button_event():
    status_code=dcm4chee.apiGetWorkList()["status_code"]
    if status_code==200:
        connectionStatusLabel['text']="連線成功"
        connectionStatusLabel['bg']="green"
    else:
        connectionStatusLabel['text'] = "連線失敗"

def readCard_button_event() :
    #清空cardReadTextBox
    cardReadTextBox.delete(1.0, 'end')
    cardContent = script.cardReader.readCard()
    carCode = str(cardContent)[9:12]
    if carCode == "500":
        readCardLabel['text'] = "尚未讀取到卡片"
        readCardLabel['bg'] = "#ff5757"
    if carCode =="200":
        hl7 = script.jsonToHl7.jsonToHl7(cardContent)
        readCardLabel['text'] = "讀取卡片成功"
        readCardLabel['bg'] = "green"
        print(hl7)
        #顯示結果
        for k in cardContent:
            cardReadTextBox.insert(tk.END, '{} = {}\n'.format(k, cardContent[k]))

    # alreadyPOST = False
    # while True:
    #     cardContent=script.cardReader.readCard()
    #     carCode = str(cardContent)[9:12]
    #     if carCode == "500":
    #         print("Card not inserted==========================")
    #         alreadyPOST = False
    #     if carCode == "200" and alreadyPOST == False:
    #         alreadyPOST = True
    #         hl7 = script.jsonToHl7.jsonToHl7(cardContent)
    #         print(hl7)

window = tk.Tk()
window.title('GUI')
window.geometry('300x400')
window.resizable(False, False)

#連線狀態顯示
connectionStatusLabel=tk.Label(window,text="請檢查連線", bg='#ff5757', font=('標楷體', 20))
connectionStatusLabel.pack(side="top",fill="x")

#檢查連線Button
mybutton = tk.Button(window, text='檢查連線',command=checkConnection_button_event)
mybutton.pack()

#讀取卡片狀太顯示
readCardLabel = tk.Label(window,text="尚未讀取到卡片",bg="#ff5757",font=('標楷體',14))
readCardLabel.pack(side="top",fill="x")

#讀取卡片
cardReadbutton = tk.Button(window, text='讀取卡片',command=readCard_button_event)
cardReadbutton.pack()

cardReadTextBox = tk.Text(window,height=12,width=40)
cardReadTextBox.pack()

postbutton=tk.Button(window,text="post",command=dcm4chee.apiPostWorkList)
postbutton.pack()

window.mainloop()





#url = 'http://localhost:3310/api/smartCard'
# def postToNodeJs(cardContent):
#     try:
#         postApi = requests.post(url, cardContent)
#         if  postApi.status_code == 200:
#             print("Pasted")
#         else:
#             print("Not Pasted")
#     except requests.exceptions.RequestException as e:
#         print(e)


