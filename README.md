# PythonReadCardDllServer
## 說明  
1. 透過晶片經融卡機器讀取健保卡卡面資料(無法讀取完整醫令資料)
2. 透過hl7apy 轉換為hl7 v2 格式
3. 將hl7 message send 給 DCM4CHEE workitem 做開單

# module
```python
certifi==2022.12.7
charset-normalizer==3.0.1
click==8.1.3
colorama==0.4.6
distlib==0.3.6
filelock==3.9.0
gTTS==2.3.1
idna==3.4
keyboard==0.13.5
platformdirs==3.0.0
playsound==1.3.0
requests==2.28.2
urllib3==1.26.14
virtualenv==20.20.0
```

![image](https://user-images.githubusercontent.com/81738019/222977087-8ec65a6f-9179-4bf9-a01e-53b12f85c997.png)




