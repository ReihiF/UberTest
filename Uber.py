#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


st.title('Uber Pickups in NYC')


# In[3]:


DATE_COLUMN='date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')


# In[4]:


@st.cache_data
def load_data(nrows):
    data=pd.read_csv(DATA_URL, nrows=nrows)
    lowercase=lambda x:str(x).lower()
    data.rename(lowercase, axis="columns", inplace = True)
    data[DATE_COLUMN]=pd.to_datetime(data[DATE_COLUMN])
    return data


# In[5]:


data_load_state=st.text("Loading Data...")
data=load_data(10000)
data_load_state.text("Loading Data...Done! using cache_data")


# In[7]:


if st.checkbox("Show Raw Data"):
    st.subheader("Raw Data")
    st.write(data)


# In[8]:


st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


# In[9]:


hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)

