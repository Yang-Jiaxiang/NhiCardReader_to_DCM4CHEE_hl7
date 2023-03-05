# PythonReadCardDllServer
簡易flask api server ，監聽健保卡讀取。  
將python 打包為exe檔案，透過系統開機設定自動啟動post:5051，功能為讀取健保卡卡面資料，name需再前端轉譯。

# #API
ＧET：```http://localhost:5051/readNHICard``` 

# pip install 
```python
pip install flask pyscard swig requests
```

