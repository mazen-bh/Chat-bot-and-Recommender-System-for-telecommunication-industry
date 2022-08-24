
import pickle
import streamlit as st
import requests
import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


offre = pickle.load(open('offre.pkl','rb'))
coords = offre[['Forfait_Voix','Forfait_Data']]
kmeans = KMeans(n_clusters=5, init='k-means++')
kmeans.fit(coords)
y=kmeans.labels_
print("k = 5", " silhouette score",silhouette_score(coords,y,metric="euclidean"))
offre['cluster']=kmeans.predict(offre[['Forfait_Voix','Forfait_Data']])


def recommend (df,nb_appel,volume_data):
    #predict the cluster for number of calls and volume data provided

    cluster=kmeans.predict(np.array([nb_appel,volume_data]).reshape(1,-1))[0]
    recommend_df= df[df['cluster']==cluster].iloc[0:5][['Offre','Forfait_Voix','Forfait_Data','Image_Forfait']]
   
    
    recommended_package_names=recommend_df['Offre']
    recommended_package_images=recommend_df['Image_Forfait']
    return  recommended_package_names,recommended_package_images

# nb_appel= offre['Forfait_Voix'].values
# volume_data= offre['Forfait_Data'].values

st.header('Package Recommender System')



calls_nb=st.number_input('Number of Calls')

vol_data=st.number_input('Volume Data')


if st.button('Show Recommendation'):
   recommended_package_names,recommended_package_images= recommend(offre,calls_nb,vol_data)
   col1, col2, col3, col4, col5 = st.columns(5)
try:
   with col1:
        st.text(recommended_package_names.iloc[0])
        st.image(recommended_package_images.iloc[0])
   with col2:
        st.text(recommended_package_names.iloc[1])
        st.image(recommended_package_images.iloc[1])

   with col3:
        st.text(recommended_package_names.iloc[2])
        st.image(recommended_package_images.iloc[2])
   with col4:
        st.text(recommended_package_names.iloc[3])
        st.image(recommended_package_images.iloc[3])
   with col5:
        st.text(recommended_package_names.iloc[4])
        st.image(recommended_package_images.iloc[4])
except:
    pass







