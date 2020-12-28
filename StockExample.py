#TheSam command

import plotly.graph_objects as go
import pandas as pd
import ssl
from datetime import datetime
#if your data is in JSON format uncomment the following
'''import requests, json
#handeling SSL err
ssl._create_default_https_context = ssl._create_unverified_context
#generate token from API
url = ""
payload = {}
headers = {
  'Authorization': ''
}
response = requests.request("GET", url, headers=headers, data = payload)
getJson = json.loads(response.text)
toStr = json.dumps(getJson)
toCsv = pd.read_json(toStr)
toCsv.to_csv('tocsv.csv')
#Create chart usign Plotly
'''
df = pd.read_csv('', parse_dates=['']) #first is your CSV dir & second is your date format in your csv file
#print(df.head())
df['Date'] = pd.to_datetime(df[''], format='%Y%m%d') #format is your wishes alignment date format

#newdf = pd.to_datetime(df['<DTYYYYMMDD>'], format="%Y%m%d")
def candlestick(value):
    fig = go.Figure(data=[go.Candlestick(
      x=df['Date'],
      open=df['<OPEN>'],
      high=df['<HIGH>'],
      low=df['<LOW>'],
      close=df['<CLOSE>'],
      increasing_line_color   =  '#3CB371',
      decreasing_line_color  =  '#FF4500'
  )])
    return{'data':[fig]}


#print(json.dumps(j, indent=4))
