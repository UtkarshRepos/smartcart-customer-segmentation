import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

st.title("SmartCart Customer Clustering System")

file = st.file_uploader("Upload Customer Dataset", type=["csv"])

if file:
    df = pd.read_csv(file)

    st.write("Dataset Preview", df.head())

    features = df.select_dtypes(include=['int64','float64'])

    scaler = StandardScaler()
    X = scaler.fit_transform(features)

    model = KMeans(n_clusters=4, random_state=42)
    df["Cluster"] = model.fit_predict(X)

    st.write("Clustered Data", df.head())
    st.bar_chart(df["Cluster"].value_counts())
