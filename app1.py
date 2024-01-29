
import numpy as np
import os


import pandas as pd
import streamlit as st
from PIL import Image
from sklearn.cluster import DBSCAN


df = pd.read_json('livedata.json')
print (df)
# this function will return list of affected person name


def affected_names(input_name):
    epsilon = 0.0018288 # a radial distance of 6 feet in kilometers
    model = DBSCAN(eps=epsilon,min_samples=3 , metric='haversine').fit(df[['latitude','logitude']])
    df['cluster'] = model.labels_.tolist()
    #the purpose of the code, is to extract the clusters associated with a given input_name from
    input_names_cluster = []
    for i in range(len(df)):
        if df['id'][i] in input_name:
            if df['cluster'][i] in input_names_cluster:
                pass
            else:
                input_names_cluster.append(df['cluster'][i])
                affected_names == []
    for cluster in input_names_cluster:
        if cluster != -1:
            cluster_idx = df.loc[df['cluster']==cluster,'id']
            for i in range(len(cluster_idx)):
                member_id = cluster_idx.iloc[i]
                if(member_id not in affected_names_list) and (member_id != input_names_cluster):
                    affected_names_list.append(member_id)
                else:
                    pass
    return affected_names_list


# web app
img = Image.open('img.png')
st.image(img, width=300)
st.title("Covid-19 Contact Tracking App")
name =st.text_input("enter person name")
if name:
    #1st check if this name contains within data set
    if name not in df['id'].unique():
        st.error("oopps this is not existed in this dataset")
    else:
        affected_names_list = affected_names(name)
        
        if len(affected_names_list)== 0:
            st.success("you have not been in the contact with affected person")
        else:
            st.error("ohh! you have been in caught in contact with the affected person")
            
            for idx, name in enumerate(affected_names_list):
                st.write(f"{idx + 1}",{name})
                
            