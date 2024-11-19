import numpy as np
import mysql.connector

connection = mysql.connector.connect( host = 'localhost'  ,  
database = "Assets"    , 
user = "root" ,        
password = "bhanu786pal"    
    )

if connection.is_connected():
    print('Connected')
cursor = connection.cursor()
cursor.execute("SHOW TABLES;")



tables = cursor.fetchall()

for (table_name,) in tables:
            print(f"\nTable: {table_name}")



  # Execute a query to select 10 rows from the 'workorder' table
cursor.execute("SELECT * FROM work_orders ;")

# Fetch the column names
headers = [i[0] for i in cursor.description]
print("Headers:", headers)

# Fetch the 10 rows and print them
rows = cursor.fetchall()

for row in rows:
    print(row)


import pandas as pd
query = "SELECT * FROM work_orders"
Workorders= pd.read_sql(query, connection)

print(Workorders.head())

query = "SELECT * FROM assets"
assets= pd.read_sql(query, connection)

print(assets.head())

query = "SELECT * FROM category"
category= pd.read_sql(query, connection)

query = "SELECT * FROM customers"
customers= pd.read_sql(query, connection)


query = "SELECT * FROM work_requests"
work_requests= pd.read_sql(query, connection)

query = "SELECT * FROM preventie_maintenance"
preventie_maintenance= pd.read_sql(query, connection)



assets.head()
assets.isnull().sum()
assets.info()
assets.describe()
assets.drop_duplicates()


assets['type'].unique()
assets['type']=assets['type'].fillna('Unknown')


assets['serial_number'].unique()
assets["serial_number"]=assets["serial_number"].fillna(assets["serial_number"].mode()[0])

assets['location']=assets['location'].fillna('Unknown')

assets=assets.drop(columns=['qr_code'])
assets=assets.drop(columns=['bar_code'])

assets['category'].unique()
assets['category']=assets['category'].fillna('unknown')


assets.isnull().sum()
assets['description']=assets['description'].fillna('Unknown')
assets=assets.drop(columns=['deleted_at'])

assets['unique_id']=assets['unique_id'].fillna(0)


assets['date_of_manuf']=assets['date_of_manuf'].fillna( assets['date_of_manuf'].mean())


assets['date_of_purchase']=assets['date_of_purchase'].fillna( assets['date_of_purchase'].mean())

assets['type_of_purchase'].unique()

assets['type_of_purchase']=assets['type_of_purchase'].fillna('None')

assets['purchase_value']=assets['purchase_value'].fillna(assets['purchase_value'].mean())

assets['present_value']=assets['present_value'].fillna(assets['present_value'].mean())
assets.isnull().sum()

assets['end_of_life'].unique()

assets=assets.drop(columns='end_of_life')

assets=assets.drop(columns='last_service_date')

assets=assets.drop(columns='next_service_date')


assets=assets.drop(columns='warranty_end_date')
assets=assets.drop(columns='amc_end_date')


assets.isnull().sum()

assets.info()






import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
























import plotly.express as px
import streamlit as st

st.set_page_config(page_title='Clover Leaf Report',page_icon=':bar_chart:',layout='wide')


st.sidebar.header('Please filter here!')

Location_filter=st.sidebar.multiselect('Select the Location',options=pd.unique(assets['location']),default=assets['location'].unique())

df_sel=assets.query( 'location==@Location_filter')
# city=st.sidebar.multiselect("select the city" , options=assets['location'].unique(),default=assets['location'].unique())
# assets=assets[assets['location']]==Location_filter

st.title('Assets Dashboard' )
st.markdown('##')
st.base=("light")
total_assets=assets['id'].count()
# typ=pd.unique(assets['type'])
Total_types=len(set(assets['type']))

left_column,middle_column=st.columns(2)

with left_column:
       st.subheader('Total_Assets')
       st.subheader(f' {total_assets:,}')

with middle_column:
       st.subheader('Types Assets')
       st.subheader(f"{Total_types}")       




# create two columns for charts
fig_col1, fig_col2 ,fig_col3= st.columns(3)

with fig_col1:
    st.markdown("Assets By Types")
    fig = px.bar(
        data_frame=assets, y="id", x="type"
    )
    st.write(fig)


with fig_col2:
    st.markdown("Assets By Location")
    fig = px.bar(
        data_frame=assets, y="id", x="location"
    )
    st.write(fig)
assets.info()


assets['id']=assets['id'].astype(object)
with fig_col3:
    st.markdown("Assets Trend")
    fig = px.line(
        data_frame=assets,  x="created_at",y="id"
    )
    st.write(fig)


st.markdown("### Detailed Data View")
st.dataframe(assets)

assets.isnull().sum()
assets['status'].count()

hide_st_style=""" <style> #Mainmenu {visibility:hidden;}
footer {visibility:hidden;}
header  {visibility:hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)




chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])

st.line_chart(data= assets,y='id',x='created_at')