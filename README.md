# SmartCart Customer Clustering System

**Live Demo:** [SmartCart Customer Segmentation App](https://smartcart-customer-segmentation-qlmeicj3ecusb9ckqhtexy.streamlit.app/)

---

## Project Overview

SmartCart is a growing e-commerce platform serving customers across multiple countries.  
The company collected **2,240 customer records** with **22 features** including demographics, purchase behavior, website activity, and customer feedback.

Currently, SmartCart uses **generic marketing strategies** for all customers, resulting in missed opportunities to retain high-value customers and delayed identification of churn-prone users.  

This project implements a **customer segmentation system** using **KMeans clustering** to group customers into meaningful clusters for **personalized marketing and retention strategies**.

---

## Dataset Description

- Each row represents a customer and contains multiple attributes:
  - **Demographics:** Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome
  - **Purchase Behavior (Amount):** MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds
  - **Purchase Behavior (Frequency):** NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth
  - **Customer Feedback & Constants:** Recency, Complain

- Dataset used: `smartcart_customers.csv`

---

## Features

- Handles **missing values** using median imputation  
- Scales features using **StandardScaler**  
- Implements **KMeans clustering** with adjustable number of clusters (K)  
- Displays:
  - Clustered dataset preview  
  - Cluster distribution chart  
  - Average spending per cluster  
- Built with **Streamlit** for interactive analysis

---

## How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/UtkarshRepos/smartcart-customer-segmentation.git
cd smartcart-customer-segmentation

2.Install dependencies:

pip install -r requirements.txt


3. Run the Streamlit app:

streamlit run app.py


Upload smartcart_customers.csv in the app to start clustering.


Live App

You can explore the live app here:
https://smartcart-customer-segmentation-qlmeicj3ecusb9ckqhtexy.streamlit.app/
