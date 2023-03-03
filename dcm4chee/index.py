import requests
import json
def apiGetWorkList():
    try:
        response=requests.get('https://www.google.com.tw/')
        if(response.status_code>=200 and response.status_code<=300):
            return {"status_code":200,"datas":response}
        else:
            return {"status_code":500}
    except requests.exceptions.RequestException as e:
        return {"status_code":500}