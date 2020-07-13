import json
import requests
import pandas as pd
import time
import numpy as np

# input string, split the string into a list
searchstring = input("Enter your search item : ")
input_list  = searchstring.split()

# call the market api to get a list of all items, create a dataframe with just item information
api_url = 'https://api.warframe.market/v1/items'
headers = {'Content-Type': 'application/json'}
response = requests.get(api_url, headers=headers)
response_dict = json.loads(response.text)
item_list = response_dict['payload']['items']
df = pd.json_normalize(item_list)

# defining a function which checks the dataframe of item names for the input string
def search_function(df, input_list):  #1
    df=df[np.logical_and.reduce([df['url_name'].str.contains(word) for word in input_list])]
    return df['url_name']

# calling the search_function and creating a list from the dataframe created
df3= search_function(df, input_list)
inputs = df3.values.tolist()

# defining a function which calls the warframe market api, this time with an item name to obtain stats for 90 day average sales per day and plot a simple line chart
def warframe_market(item_name):
    api_url_base = 'https://api.warframe.market/v1'
    headers = {'Content-Type': 'application/json'}
    item_name2= " ".join(item_name.split())
    item = item_name2.lower().replace(" ", "_")
    api_url = api_url_base + '/items/' + item + '/statistics'
    response = requests.get(api_url, headers=headers)
    response_dict = json.loads(response.text)
    historic = response_dict['payload']['statistics_closed']['90days']
    df = pd.json_normalize(historic)
    df2 = df[['datetime','avg_price']]
    df2['datetime'] = pd.to_datetime(df2['datetime'])
    df2.plot(x='datetime', y='avg_price', label=item)

# for each item we found from our search string, create a graph for average sales in the last 90 days, wait a second between calls
for input in inputs:
    warframe_market(input)
    time.sleep(1)
