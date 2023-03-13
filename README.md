# NhiCardReader_to_DCM4CHEE_PythonGUI
## 說明  
### HL7 詳細筆記
https://beaded-wood-268.notion.site/HL7-v2-3-1-d3680fccba354efb8bb06d3cd1cbf6d4  

根據HL7標準，ORM_O01消息類型必須包含至少以下幾個段：MSH、PID和ORC。此外，具體取決於實際情況和用例，ORM_O01還可能需要包含其他的段和字段。
1. 透過晶片經融卡機器讀取健保卡卡面資料(無法讀取完整醫令資料)
2. 透過hl7apy 轉換為hl7 v2 格式
3. 將hl7 message send 給 DCM4CHEE workitem 做開單

## 安裝
### Python版本需大於3.8
1. 將本專案下載為Zip或git clone到本地端
2. 在專案根目錄執行以下指令
  ```
  pip install -r requirements.txt
  ```
  **如果安裝過程遇到問題，請嘗試以 系統管理員權限執行 命令提示字元**

3. 執行程式
```
python main.py
```

## 產出之HL7 message範例

```abap
MSH|^~\&|HMIS|DUHS|PACS|KIWITEAM|20181016115248||OMI^O23^OMI_O23|20181016115248|P|2.5.1||||||UNICODE UTF-8
PID|||E125945087^^^^TW||楊嘉翔||20010412|M||||||||||E12594508720230308|E12594508720230308
ORC|NW|E12594508720230308^^^TW|||SC||||||20230308213110|||E125945087^Yang^Jiaxiang
OBR|1|||||||||||||||||||||||US
```

## HL7格式驗證器

[HL7 Validator (Health Level 7) - Free Online](https://freeonlineformatter.com/hl7-validator/run)

## C4 Model

https://drive.google.com/file/d/1UVbRzK9L6xuYpIszsKAZ2sThBERAIB07/view?usp=share_link

![NhiCardReader_To_DCM4CHEE_python-第 4 页 drawio](https://user-images.githubusercontent.com/81738019/224273100-ffef4005-4658-4817-918e-b7f913f3b9c3.png)

    

## HL7欄位說明

- MSH段，包含消息控制信息和元數據，如消息類型、發送者、接收者、日期/時間等等。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/MSH)
    
- PID段，包含患者的識別信息和相關的人口統計學數據。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/PID)
    
- ORC段，包含醫囑或指示的控制信息，如醫囑號碼、醫囑狀態、醫囑類型等等。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/ORC)

## 介面展示
![image](https://user-images.githubusercontent.com/81738019/222977087-8ec65a6f-9179-4bf9-a01e-53b12f85c997.png)




