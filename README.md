# SmartCart Customer Segmentation System

An intelligent customer segmentation system for SmartCart, a growing e-commerce platform. This project uses unsupervised machine learning to group customers based on demographics, purchase behavior, and engagement metrics to enable personalized marketing and improve customer retention.

---

## Problem Statement
SmartCart currently applies generic marketing strategies for all customers, resulting in missed opportunities to retain high-value customers and delayed identification of churn-prone users. This system analyzes historical customer transaction data and creates meaningful clusters to support data-driven decision-making.

---

## Dataset
- **Rows:** 2,240 customer records  
- **Columns:** 22 attributes  
- **Key Features:**
  - Demographics: Year_Birth, Education, Marital_Status, Income, Kidhome, Teenhome
  - Purchase Behaviour: MntWines, MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts, MntGoldProds
  - Purchase Frequency: NumDealsPurchases, NumWebPurchases, NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth
  - Feedback & Recency: Recency, Complain

---

## Approach
1. **Data Preprocessing**
   - Handle missing values
   - Scale numerical features
2. **Feature Engineering**
   - Selected relevant purchase & engagement features
3. **Clustering**
   - Applied KMeans clustering
   - Used Elbow Method and Silhouette Score to select optimal clusters
4. **Cluster Analysis**
   - Analyzed patterns in spending, engagement, and loyalty

---

## Results & Insights
- Identified 4 customer segments:
  1. High-value loyal customers
  2. Bargain-focused frequent shoppers
  3. Low engagement / churn-prone users
  4. Moderate spenders with seasonal activity
- Generated actionable insights for personalized marketing strategies

---

## Business Impact
- Enables targeted marketing campaigns  
- Improves customer retention  
- Reduces churn and maximizes revenue from high-value customers

---

## Tech Stack
- Python, Pandas, NumPy, scikit-learn, Matplotlib, Streamlit  

---

## Live Demo
[SmartCart Customer Segmentation Dashboard](YOUR_DEPLOYED_LINK_HERE)

---

## How to Run Locally
1. Clone the repo:  
```bash
git clone https://github.com/UtkarshRepos/smartcart-customer-segmentation.git
