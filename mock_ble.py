import random
from datetime import datetime
import json
import time as t
import pandas as pd

MESSAGE = {
  "deviceType": "BLE_GW",
  "payload": {
    "adv": [
    ]
  }
}

# get current datetime
today = datetime.now()
# print('Today Datetime:', today)

df_gw = pd.read_csv("gateway_list_250K.csv")
df_ble =  pd.read_csv("ble_tag_100K.csv")

import json
import requests

try:
    for i in range(10001):
      print(i)
      gw_id = df_gw.loc[i, "DEVICE_ID"]
      print(gw_id)
      MESSAGE["payload"]["adv"] = []
      for j in range(i*10,i*10+10):
          adv_data = {
                        "type": 0,
                        "count": 3,
                      }
          adv_data["ts"] = int(datetime.now().timestamp()* 1000) 
          adv_data["src"] = df_ble.loc[j, "DEVICE_ID"]
          adv_data["addr"] = df_ble.loc[j, "DEVICE_ID"]
          adv_data["tm"] = round(random.uniform(0.00, 30.00), 2)
          adv_data["vbat"] = random.randint(2700,3300)
          adv_data["rssi"] = random.randint(-100,-70)
          MESSAGE["payload"]["adv"].append(adv_data)
      print(MESSAGE)
      url = "https://api.staging.tagntrac.io/device/"+str(gw_id)+"/data"
      # print(url)
      payload = json.dumps(MESSAGE)
      headers = {
          'Content-Type': 'application/json'
      }
      # response = requests.request("POST", url, headers=headers, data=payload)
      # print(response.text)
      t.sleep(1)
    t.sleep(3600)
      
except:
    pass
    


