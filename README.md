# NhiCardReader_to_HL7_PythonGUI
## 說明  
https://beaded-wood-268.notion.site/HL7-v2-3-1-d3680fccba354efb8bb06d3cd1cbf6d4  
根据HL7标准，ORM_O01消息类型必须包含至少以下几个段：MSH、PID和ORC。此外，具体取决于实际情况和用例，ORM_O01还可能需要包含其他的段和字段。  
1. 透過晶片經融卡機器讀取健保卡卡面資料(無法讀取完整醫令資料)
2. 透過hl7apy 轉換為hl7 v2 格式
3. 將hl7 message send 給 DCM4CHEE workitem 做開單


## 範例

```abap
MSH|^~\&|HMIS|DUHS|PACS|KIWITEAM|20181016115248||OMI^O23^OMI_O23|20181016115248|P|2.5.1||||||UNICODE UTF-8
PID|||E125945087^^^^TW||楊嘉翔||20010412|M||||||||||E12594508720230308|E12594508720230308
ORC|NW|E12594508720230308^^^TW|||SC||||||20230308213110|||E125945087^Yang^Jiaxiang
OBR|1|||||||||||||||||||||||US
```

## 驗證

[HL7 Validator (Health Level 7) - Free Online](https://freeonlineformatter.com/hl7-validator/run)

## C4 Model

https://drive.google.com/file/d/1UVbRzK9L6xuYpIszsKAZ2sThBERAIB07/view?usp=share_link

    

## 欄位說明

- MSH段，包含消息控制信息和元数据，如消息类型、发送者、接收者、日期/时间等等。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/MSH)
    
- PID段，包含患者的识别信息和相关的人口统计学数据。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/PID)
    
- ORC段，包含医嘱或指示的控制信息，如医嘱号码、医嘱状态、医嘱类型等等。
    
    [Caristix HL7-Definition V2](https://hl7-definition.caristix.com/v2/HL7v2.3.1/Segments/ORC)

![image](https://user-images.githubusercontent.com/81738019/222977087-8ec65a6f-9179-4bf9-a01e-53b12f85c997.png)




