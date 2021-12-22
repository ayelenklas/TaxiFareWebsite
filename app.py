import streamlit as st
import requests
import datetime
import pandas as pd



'''
# TaxiFareModel Interface
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')
'''
## Please select the following information:'''



pickup_date = st.date_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_time = st.time_input('pickup datetime',
                            value=datetime.datetime(2012, 10, 6, 12, 10, 20))
pickup_datetime = f'{pickup_date} {pickup_time}'

pickup_latitude = st.number_input('pickup latitude', value=-73.9798156)
pickup_longitude = st.number_input('pickup longitude', value=40.7614327)

dropoff_latitude = st.number_input('dropoff latitude', value=-73.7803331)
dropoff_longitude = st.number_input('dropoff longitude', value=40.6413111)
passenger_count = st.slider('passenger_count',
                                  1,
                                  8,
                                  1)


url = 'https://taxifare.lewagon.ai/predict'

params = dict(pickup_datetime=pickup_datetime,
              pickup_longitude=pickup_longitude,
              pickup_latitude=pickup_latitude,
              dropoff_longitude=dropoff_longitude,
              dropoff_latitude=dropoff_latitude,
              passenger_count=passenger_count)

response = requests.get(url, params=params)
prediction = response.json()
pred = round(prediction['prediction'],2)
st.write(f"## The estimated fare is ${pred}")

@st.cache
def get_map_data():
    return pd.DataFrame([[pickup_latitude,pickup_longitude ],
                         [ dropoff_latitude, dropoff_longitude]],
                        columns=['lat', 'lon'])


points = get_map_data()
st.map(points)

# @st.cache
# def get_map_data():

#     return pd.DataFrame(
#             np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#             columns=['lat', 'lon']
#         )

# df = get_map_data()

# st.map(df)
