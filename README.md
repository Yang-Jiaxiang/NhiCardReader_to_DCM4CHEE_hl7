# PythonReadCardDllServer
## 說明  
1. 透過晶片經融卡機器讀取健保卡卡面資料(無法讀取完整醫令資料)
2. 透過hl7apy 轉換為hl7 v2 格式
3. 將hl7 message send 給 DCM4CHEE workitem 做開單

# pip install 
```python
pip install flask pyscard swig requests
```

![image](https://user-images.githubusercontent.com/81738019/222977087-8ec65a6f-9179-4bf9-a01e-53b12f85c997.png)




