import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

st.set_page_config(page_title="SmartCart Customer Clustering", layout="wide")
st.title("SmartCart Customer Clustering System")
st.markdown("""
This app allows you to upload SmartCart customer data, performs KMeans clustering to segment customers based on demographics, spending, and engagement patterns, and visualizes the results.
""")

# Upload CSV
file = st.file_uploader("Upload Customer Dataset", type=["csv"])

if file:
    df = pd.read_csv(file)
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head())
    
    # Check missing values
    st.subheader("Missing Values Per Column")
    st.dataframe(df.isnull().sum())
    
    # Select numeric features for clustering
    numeric_features = df.select_dtypes(include=['int64','float64'])
    
    # Handle missing values with median
    imputer = SimpleImputer(strategy='median')
    X = imputer.fit_transform(numeric_features)
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Choose number of clusters
    n_clusters = st.slider("Select number of clusters (K)", min_value=2, max_value=10, value=4)
    
    # KMeans clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    cluster_labels = kmeans.fit_predict(X_scaled)
    
    # Add cluster labels to dataframe
    df["Cluster"] = cluster_labels
    
    st.subheader("Clustered Dataset")
    st.dataframe(df.head(20))
    
    # Show cluster distribution
    st.subheader("Cluster Distribution")
    st.bar_chart(df["Cluster"].value_counts())
    
    # Show average spending per cluster
    st.subheader("Average Spending per Cluster")
    spending_cols = [col for col in df.columns if "Mnt" in col]  # All purchase columns
    cluster_avg = df.groupby("Cluster")[spending_cols].mean()
    st.dataframe(cluster_avg)
    
    st.markdown("""
    **Instructions:**  
    - Use the slider to adjust the number of clusters (K) and see how the segmentation changes.  
    - Analyze `Cluster Distribution` to understand how many customers fall into each group.  
    - `Average Spending per Cluster` helps identify high-value and low-value customer segments.
    """)
else:
    st.info("Please upload a CSV file to begin clustering.")
