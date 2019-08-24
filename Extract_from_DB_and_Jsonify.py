#!/usr/bin/env python
# coding: utf-8

# In[72]:


##dependencies
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template
import json
import sqlalchemy as db


# In[73]:


#create db connection to each table and bring it in as a pandas df
engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h15 = db.Table('h15',metadata, autoload=True,autoload_with=engine)
query = db.select([h15])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
h15 = pd.DataFrame(ResultSet)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h16 = db.Table('h16',metadata, autoload=True,autoload_with=engine)
query = db.select([h16])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
h16 = pd.DataFrame(ResultSet)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h17 = db.Table('h17',metadata, autoload=True,autoload_with=engine)
query = db.select([h17])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
h17 = pd.DataFrame(ResultSet)

engine = db.create_engine('sqlite:///static/health_plans.sqlite')
connection = engine.connect()
metadata = db.MetaData()
h18 = db.Table('h18',metadata, autoload=True,autoload_with=engine)
query = db.select([h18])
ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()
h18 = pd.DataFrame(ResultSet)


# In[74]:


#name columns
h15.columns = ['State','County','Metal','Issuer','Type','FIPS']
h16.columns = ['State','County','Metal','Issuer','Type','FIPS']
h17.columns = ['State','County','Metal','Issuer','Type','FIPS']
h18.columns = ['State','County','Metal','Issuer','Type','FIPS']


# In[75]:


#create groupbys to operate on
state15_groupby = h15.groupby('State')
fips15_groupby = h15.groupby('FIPS')
state15_metal_groupby = h15.groupby(['Metal','State'])
fips15_metal_groupby = h15.groupby(['Metal','FIPS'])
state15_issuer_groupby = h15.groupby(['Issuer','State'])
fips15_issuer_groupby = h15.groupby(['Issuer','FIPS'])
state15_type_groupby = h15.groupby(['Type','State'])
fips15_type_groupby = h15.groupby(['Type','FIPS'])

state16_groupby = h16.groupby('State')
fips16_groupby = h16.groupby('FIPS')
state16_metal_groupby = h16.groupby(['Metal','State'])
fips16_metal_groupby = h16.groupby(['Metal','FIPS'])
state16_issuer_groupby = h16.groupby(['Issuer','State'])
fips16_issuer_groupby = h16.groupby(['Issuer','FIPS'])
state16_type_groupby = h16.groupby(['Type','State'])
fips16_type_groupby = h16.groupby(['Type','FIPS'])

state17_groupby = h17.groupby('State')
fips17_groupby = h17.groupby('FIPS')
state17_metal_groupby = h17.groupby(['Metal','State'])
fips17_metal_groupby = h17.groupby(['Metal','FIPS'])
state17_issuer_groupby = h17.groupby(['Issuer','State'])
fips17_issuer_groupby = h17.groupby(['Issuer','FIPS'])
state17_type_groupby = h17.groupby(['Type','State'])
fips17_type_groupby = h17.groupby(['Type','FIPS'])

state18_groupby = h18.groupby('State')
fips18_groupby = h18.groupby('FIPS')
state18_metal_groupby = h18.groupby(['Metal','State'])
fips18_metal_groupby = h18.groupby(['Metal','FIPS'])
state18_issuer_groupby = h18.groupby(['Issuer','State'])
fips18_issuer_groupby = h18.groupby(['Issuer','FIPS'])
state18_type_groupby = h18.groupby(['Type','State'])
fips18_type_groupby = h18.groupby(['Type','FIPS'])


# In[76]:


#get counts for each groupby
state15_count = state15_groupby[['FIPS']].count()
#right now this is cast to a string because jsonify didn't like numpy results??
state15_count['FIPS'] = state15_count['FIPS'].astype(str)
state15_count = state15_count.reset_index(drop=False)
state15_count.columns = ['State','Count']

fips15_count = fips15_groupby[['Type']].count()
fips15_count['Type'] = fips15_count['Type'].astype(str)
fips15_count = fips15_count.reset_index(drop=False)
fips15_count.columns = ['FIPS','Count']
fips15_count['FIPS'] = fips15_count['FIPS'].astype(str)

state16_count = state16_groupby[['FIPS']].count()
state16_count['FIPS'] = state16_count['FIPS'].astype(str)
state16_count = state16_count.reset_index(drop=False)
state16_count.columns = ['State','Count']

fips16_count = fips16_groupby[['Type']].count()
fips16_count['Type'] = fips16_count['Type'].astype(str)
fips16_count = fips16_count.reset_index(drop=False)
fips16_count.columns = ['FIPS','Count']
fips16_count['FIPS'] = fips16_count['FIPS'].astype(str)

state17_count = state17_groupby[['FIPS']].count()
state17_count['FIPS'] = state17_count['FIPS'].astype(str)
state17_count = state17_count.reset_index(drop=False)
state17_count.columns = ['State','Count']

fips17_count = fips17_groupby[['Type']].count()
fips17_count['Type'] = fips17_count['Type'].astype(str)
fips17_count = fips17_count.reset_index(drop=False)
fips17_count.columns = ['FIPS','Count']
fips17_count['FIPS'] = fips17_count['FIPS'].astype(str)

state18_count = state18_groupby[['FIPS']].count()
state18_count['FIPS'] = state18_count['FIPS'].astype(str)
state18_count = state18_count.reset_index(drop=False)
state18_count.columns = ['State','Count']

fips18_count = fips18_groupby[['Type']].count()
fips18_count['Type'] = fips18_count['Type'].astype(str)
fips18_count = fips18_count.reset_index(drop=False)
fips18_count.columns = ['FIPS','Count']
fips18_count['FIPS'] = fips18_count['FIPS'].astype(str)


# In[77]:


#get count for each metal type by state and FIPS
state15_metal_count = state15_metal_groupby[['FIPS']].count()
state15_metal_count['FIPS'] = state15_metal_count['FIPS'].astype(str)
state15_metal_count = state15_metal_count.reset_index(drop=False)
state15_metal_count.columns = ['Metal','State','Count']

fips15_metal_count = fips15_metal_groupby[['State']].count()
fips15_metal_count['State'] = fips15_metal_count['State'].astype(str)
fips15_metal_count = fips15_metal_count.reset_index(drop=False)
fips15_metal_count.columns = 'Metal','FIPS','Count'
fips15_metal_count['FIPS'] = fips15_metal_count['FIPS'].astype(str)

state16_metal_count = state16_metal_groupby[['FIPS']].count()
state16_metal_count['FIPS'] = state16_metal_count['FIPS'].astype(str)
state16_metal_count = state16_metal_count.reset_index(drop=False)
state16_metal_count.columns = ['Metal','State','Count']

fips16_metal_count = fips16_metal_groupby[['State']].count()
fips16_metal_count['State'] = fips16_metal_count['State'].astype(str)
fips16_metal_count = fips16_metal_count.reset_index(drop=False)
fips16_metal_count.columns = 'Metal','FIPS','Count'
fips16_metal_count['FIPS'] = fips16_metal_count['FIPS'].astype(str)

state17_metal_count = state17_metal_groupby[['FIPS']].count()
state17_metal_count['FIPS'] = state17_metal_count['FIPS'].astype(str)
state17_metal_count = state17_metal_count.reset_index(drop=False)
state17_metal_count.columns = ['Metal','State','Count']

fips17_metal_count = fips17_metal_groupby[['State']].count()
fips17_metal_count['State'] = fips17_metal_count['State'].astype(str)
fips17_metal_count = fips17_metal_count.reset_index(drop=False)
fips17_metal_count.columns = 'Metal','FIPS','Count'
fips17_metal_count['FIPS'] = fips17_metal_count['FIPS'].astype(str)

state18_metal_count = state18_metal_groupby[['FIPS']].count()
state18_metal_count['FIPS'] = state18_metal_count['FIPS'].astype(str)
state18_metal_count = state18_metal_count.reset_index(drop=False)
state18_metal_count.columns = ['Metal','State','Count']

fips18_metal_count = fips18_metal_groupby[['State']].count()
fips18_metal_count['State'] = fips18_metal_count['State'].astype(str)
fips18_metal_count = fips18_metal_count.reset_index(drop=False)
fips18_metal_count.columns = 'Metal','FIPS','Count'
fips18_metal_count['FIPS'] = fips18_metal_count['FIPS'].astype(str)


# In[78]:


#get count for each issuer by state and FIPS
state15_issuer_count = state15_issuer_groupby[['FIPS']].count()
state15_issuer_count[['FIPS']] = state15_issuer_count[['FIPS']].astype(str)
state15_issuer_count = state15_issuer_count.reset_index(drop=False)
state15_issuer_count.columns = ['Issuer','State','Count']

fips15_issuer_count = fips15_issuer_groupby[['State']].count()
fips15_issuer_count[['State']] = fips15_issuer_count[['State']].astype(str)
fips15_issuer_count = fips15_issuer_count.reset_index(drop=False)
fips15_issuer_count.columns = ['Issuer','FIPS','Count']
fips15_issuer_count['FIPS'] = fips15_issuer_count['FIPS'].astype(str)

state16_issuer_count = state16_issuer_groupby[['FIPS']].count()
state16_issuer_count[['FIPS']] = state16_issuer_count[['FIPS']].astype(str)
state16_issuer_count = state16_issuer_count.reset_index(drop=False)
state16_issuer_count.columns = ['Issuer','State','Count']

fips16_issuer_count = fips16_issuer_groupby[['State']].count()
fips16_issuer_count[['State']] = fips16_issuer_count[['State']].astype(str)
fips16_issuer_count = fips16_issuer_count.reset_index(drop=False)
fips16_issuer_count.columns = ['Issuer','FIPS','Count']
fips16_issuer_count['FIPS'] = fips16_issuer_count['FIPS'].astype(str)

state17_issuer_count = state17_issuer_groupby[['FIPS']].count()
state17_issuer_count[['FIPS']] = state17_issuer_count[['FIPS']].astype(str)
state17_issuer_count = state17_issuer_count.reset_index(drop=False)
state17_issuer_count.columns = ['Issuer','State','Count']

fips17_issuer_count = fips17_issuer_groupby[['State']].count()
fips17_issuer_count[['State']] = fips17_issuer_count[['State']].astype(str)
fips17_issuer_count = fips17_issuer_count.reset_index(drop=False)
fips17_issuer_count.columns = ['Issuer','FIPS','Count']
fips17_issuer_count['FIPS'] = fips17_issuer_count['FIPS'].astype(str)

state18_issuer_count = state18_issuer_groupby[['FIPS']].count()
state18_issuer_count[['FIPS']] = state18_issuer_count[['FIPS']].astype(str)
state18_issuer_count = state18_issuer_count.reset_index(drop=False)
state18_issuer_count.columns = ['Issuer','State','Count']

fips18_issuer_count = fips18_issuer_groupby[['State']].count()
fips18_issuer_count[['State']] = fips18_issuer_count[['State']].astype(str)
fips18_issuer_count = fips18_issuer_count.reset_index(drop=False)
fips18_issuer_count.columns = ['Issuer','FIPS','Count']
fips18_issuer_count['FIPS'] = fips18_issuer_count['FIPS'].astype(str)


# In[79]:


#get count of plan type for each state and FIPS
state15_type_count = state15_type_groupby[['FIPS']].count()
state15_type_count['FIPS'] = state15_type_count['FIPS'].astype(str)
state15_type_count = state15_type_count.reset_index(drop=False)
state15_type_count.columns = ['Type','State','Count']

fips15_type_count = fips15_type_groupby[['State']].count()
fips15_type_count['State'] = fips15_type_count['State'].astype(str)
fips15_type_count.columns = (['Count'])
fips15_type_count = fips15_type_count.reset_index(drop=False)
fips15_type_count.columns = ['Type','FIPS','Count']
fips15_type_count['FIPS'] = fips15_type_count['FIPS'].astype(str)

state16_type_count = state16_type_groupby[['FIPS']].count()
state16_type_count['FIPS'] = state16_type_count['FIPS'].astype(str)
state16_type_count = state16_type_count.reset_index(drop=False)
state16_type_count.columns = ['Type','State','Count']

fips16_type_count = fips16_type_groupby[['State']].count()
fips16_type_count['State'] = fips16_type_count['State'].astype(str)
fips16_type_count.columns = (['Count'])
fips16_type_count = fips16_type_count.reset_index(drop=False)
fips16_type_count.columns = ['Type','FIPS','Count']
fips16_type_count['FIPS'] = fips16_type_count['FIPS'].astype(str)

state17_type_count = state17_type_groupby[['FIPS']].count()
state17_type_count['FIPS'] = state17_type_count['FIPS'].astype(str)
state17_type_count = state17_type_count.reset_index(drop=False)
state17_type_count.columns = ['Type','State','Count']

fips17_type_count = fips17_type_groupby[['State']].count()
fips17_type_count['State'] = fips17_type_count['State'].astype(str)
fips17_type_count.columns = (['Count'])
fips17_type_count = fips17_type_count.reset_index(drop=False)
fips17_type_count.columns = ['Type','FIPS','Count']
fips17_type_count['FIPS'] = fips17_type_count['FIPS'].astype(str)
fips17_type_count['FIPS'] = fips17_type_count['FIPS'].str[:5]

state18_type_count = state18_type_groupby[['FIPS']].count()
state18_type_count['FIPS'] = state18_type_count['FIPS'].astype(str)
state18_type_count = state18_type_count.reset_index(drop=False)
state18_type_count.columns = ['Type','State','Count']

fips18_type_count = fips18_type_groupby[['State']].count()
fips18_type_count['State'] = fips18_type_count['State'].astype(str)
fips18_type_count.columns = (['Count'])
fips18_type_count = fips18_type_count.reset_index(drop=False)
fips18_type_count.columns = ['Type','FIPS','Count']
fips18_type_count['FIPS'] = fips18_type_count['FIPS'].astype(str)
fips18_type_count['FIPS'] = fips18_type_count['FIPS'].str[:5]


# In[80]:


fips_type_count = fips18_type_count
fips_type_count['FIPS'] = fips_type_count['FIPS'].str[:5]
fips18_type_count.head()


# In[81]:


#turn dfs into dicts for jsonification
state15_count_obs = []
pointer = state15_count
counter = 0
for plan in pointer.iterrows():
    state15_count_obs.append({'State':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

fips15_count_obs = []
pointer = fips15_count
counter = 0
for plan in pointer.iterrows():
    fips15_count_obs.append({'FIPS':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state15_metal_obs = []
pointer = state15_metal_count
counter = 0
for plan in pointer.iterrows():
    state15_metal_obs.append({'State':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1
    
fips15_metal_obs = []
pointer = fips15_metal_count
counter = 0
for plan in pointer.iterrows():
    fips15_metal_obs.append({'FIPS':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state15_issuer_obs = []
pointer = state15_issuer_count
counter = 0
for plan in pointer.iterrows():
    state15_issuer_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
fips15_issuer_obs = []
pointer = fips15_issuer_count
counter = 0
for plan in pointer.iterrows():
    fips15_issuer_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
state15_type_obs = []
pointer = state15_type_count
counter = 0
for plan in pointer.iterrows():
    state15_type_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
fips15_type_obs = []
pointer = fips15_type_count
counter = 0
for plan in pointer.iterrows():
    fips15_type_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
###end of year

#turn dfs into dicts for jsonification
state16_count_obs = []
pointer = state16_count
counter = 0
for plan in pointer.iterrows():
    state16_count_obs.append({'State':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

fips16_count_obs = []
pointer = fips16_count
counter = 0
for plan in pointer.iterrows():
    fips16_count_obs.append({'FIPS':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state16_metal_obs = []
pointer = state16_metal_count
counter = 0
for plan in pointer.iterrows():
    state16_metal_obs.append({'State':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1
    
fips16_metal_obs = []
pointer = fips16_metal_count
counter = 0
for plan in pointer.iterrows():
    fips16_metal_obs.append({'FIPS':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state16_issuer_obs = []
pointer = state16_issuer_count
counter = 0
for plan in pointer.iterrows():
    state16_issuer_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
fips16_issuer_obs = []
pointer = fips16_issuer_count
counter = 0
for plan in pointer.iterrows():
    fips16_issuer_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
state16_type_obs = []
pointer = state16_type_count
counter = 0
for plan in pointer.iterrows():
    state16_type_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
fips16_type_obs = []
pointer = fips16_type_count
counter = 0
for plan in pointer.iterrows():
    fips16_type_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
###end of year

#turn dfs into dicts for jsonification
state17_count_obs = []
pointer = state17_count
counter = 0
for plan in pointer.iterrows():
    state17_count_obs.append({'State':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

fips17_count_obs = []
pointer = fips17_count
counter = 0
for plan in pointer.iterrows():
    fips17_count_obs.append({'FIPS':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state17_metal_obs = []
pointer = state17_metal_count
counter = 0
for plan in pointer.iterrows():
    state17_metal_obs.append({'State':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1
    
fips17_metal_obs = []
pointer = fips17_metal_count
counter = 0
for plan in pointer.iterrows():
    fips17_metal_obs.append({'FIPS':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state17_issuer_obs = []
pointer = state17_issuer_count
counter = 0
for plan in pointer.iterrows():
    state17_issuer_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
fips17_issuer_obs = []
pointer = fips17_issuer_count
counter = 0
for plan in pointer.iterrows():
    fips17_issuer_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
state17_type_obs = []
pointer = state17_type_count
counter = 0
for plan in pointer.iterrows():
    state17_type_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
fips17_type_obs = []
pointer = fips17_type_count
counter = 0
for plan in pointer.iterrows():
    fips17_type_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
###end of year

#turn dfs into dicts for jsonification
state18_count_obs = []
pointer = state18_count
counter = 0
for plan in pointer.iterrows():
    state18_count_obs.append({'State':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

fips18_count_obs = []
pointer = fips18_count
counter = 0
for plan in pointer.iterrows():
    fips18_count_obs.append({'FIPS':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state18_metal_obs = []
pointer = state18_metal_count
counter = 0
for plan in pointer.iterrows():
    state18_metal_obs.append({'State':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1
    
fips18_metal_obs = []
pointer = fips18_metal_count
counter = 0
for plan in pointer.iterrows():
    fips18_metal_obs.append({'FIPS':pointer.iloc[counter,1],'Metal':pointer.iloc[counter,0],'Count':pointer.iloc[counter,-1]})
    counter = counter +1

state18_issuer_obs = []
pointer = state18_issuer_count
counter = 0
for plan in pointer.iterrows():
    state18_issuer_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
fips18_issuer_obs = []
pointer = fips18_issuer_count
counter = 0
for plan in pointer.iterrows():
    fips18_issuer_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Issuer':pointer.iloc[counter,0]})
    counter = counter +1
    
state18_type_obs = []
pointer = state18_type_count
counter = 0
for plan in pointer.iterrows():
    state18_type_obs.append({'State':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
fips18_type_obs = []
pointer = fips18_type_count
counter = 0
for plan in pointer.iterrows():
    fips18_type_obs.append({'FIPS':pointer.iloc[counter,1],'Count':pointer.iloc[counter,-1], 'Type':pointer.iloc[counter,0]})
    counter = counter +1
    
###end of year


# In[82]:


fips18_type_obs


# In[84]:


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/data")
def data():
    return render_template("data.html")
    
@app.route("/conclusions")
def conclusions():
    return render_template("conclusions.html")
    
@app.route("/info")
def welcome():
    return 'Available routes:/state_count15, /fips_count15, /state_metal15, /fips_metal15, /state_issuer15, /fips_issuer15, /state_type15, /fips_type15, /state_count16, /fips_count16, /state_metal16, /fips_metal16, /state_issuer16, /fips_issuer16, /state_type16, /fips_type16, /state_count17, /fips_count17, /state_metal17, /fips_metal17, /state_issuer17, /fips_issuer17, /state_type17, /fips_type17, /state_count18, /fips_count18, /state_metal18, /fips_metal18, /state_issuer18, /fips_issuer18, /state_type18, /fips_type18'

@app.route("/state_count15")
def stateCount15():
    return jsonify(state15_count_obs)

@app.route("/fips_count15")
def fipsCount15():
    return jsonify(fips15_count_obs)

@app.route("/state_metal15")
def stateMetal15():
    return jsonify(state15_metal_obs)

@app.route("/fips_metal15")
def fipsMetal15():
    return jsonify(fips15_metal_obs)

@app.route("/state_issuer15")
def stateIssuer15():
    return jsonify(state15_issuer_obs)

@app.route("/fips_issuer15")
def fipsIssuer15():
    return jsonify(fips15_issuer_obs)

@app.route("/state_type15")
def stateType15():
    return jsonify(state15_type_obs)

@app.route("/fips_type15")
def fipsType15():
    return jsonify(fips15_type_obs)
##end of year


@app.route("/state_count16")
def stateCount16():
    return jsonify(state16_count_obs)

@app.route("/fips_count16")
def fipsCount16():
    return jsonify(fips16_count_obs)

@app.route("/state_metal16")
def stateMetal16():
    return jsonify(state16_metal_obs)

@app.route("/fips_metal16")
def fipsMetal16():
    return jsonify(fips16_metal_obs)

@app.route("/state_issuer16")
def stateIssuer16():
    return jsonify(state16_issuer_obs)

@app.route("/fips_issuer16")
def fipsIssuer16():
    return jsonify(fips16_issuer_obs)

@app.route("/state_type16")
def stateType16():
    return jsonify(state16_type_obs)

@app.route("/fips_type16")
def fipsType16():
    return jsonify(fips16_type_obs)
##end of year

@app.route("/state_count17")
def stateCount17():
    return jsonify(state17_count_obs)

@app.route("/fips_count17")
def fipsCount17():
    return jsonify(fips17_count_obs)

@app.route("/state_metal17")
def stateMetal17():
    return jsonify(state17_metal_obs)

@app.route("/fips_metal17")
def fipsMetal17():
    return jsonify(fips17_metal_obs)

@app.route("/state_issuer17")
def stateIssuer17():
    return jsonify(state17_issuer_obs)

@app.route("/fips_issuer17")
def fipsIssuer17():
    return jsonify(fips17_issuer_obs)

@app.route("/state_type17")
def stateType17():
    return jsonify(state17_type_obs)

@app.route("/fips_type17")
def fipsType17():
    return jsonify(fips17_type_obs)
##end of year

@app.route("/state_count18")
def stateCount18():
    return jsonify(state18_count_obs)

@app.route("/fips_count18")
def fipsCount18():
    return jsonify(fips18_count_obs)

@app.route("/state_metal18")
def stateMetal18():
    return jsonify(state18_metal_obs)

@app.route("/fips_metal18")
def fipsMetal18():
    return jsonify(fips18_metal_obs)

@app.route("/state_issuer18")
def stateIssuer18():
    return jsonify(state18_issuer_obs)

@app.route("/fips_issuer18")
def fipsIssuer18():
    return jsonify(fips18_issuer_obs)

@app.route("/state_type18")
def stateType18():
    return jsonify(state18_type_obs)

@app.route("/fips_type18")
def fipsType18():
    return jsonify(fips18_type_obs)

##end of year
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




