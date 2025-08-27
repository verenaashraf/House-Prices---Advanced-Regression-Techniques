# 🏡 House Price Prediction

## 📌 Project Overview
This project predicts house sale prices using **Machine Learning** techniques on the [Kaggle House Prices Dataset](https://www.kaggle.com/c/house-prices-advanced-regression-techniques).  
We experimented with **Linear Regression** as a baseline model and compared it with more advanced models such as **Random Forest Regressor**.  

The main goal is to understand the factors affecting house prices and build a model that achieves low prediction error.

---

## 📊 Dataset
- **Source**: Kaggle – House Prices: Advanced Regression Techniques  
- **Size**: ~1,460 rows, 80 features  
- **Features**:
  - **Numerical**: `LotArea`, `GrLivArea`, `OverallQual`, `GarageCars`, `TotalBsmtSF`, etc.  
  - **Categorical**: `Neighborhood`, `HouseStyle`, `RoofStyle`, etc.  
- **Target**: `SalePrice` (continuous variable)

---

## ⚙️ Steps in the Project
1. **Exploratory Data Analysis (EDA)**  
   - Visualized distributions (histograms, boxplots, scatterplots).  
   - Checked correlations between features and target (`SalePrice`).  

2. **Data Preprocessing**  
   - Handled missing values (imputation / removal).  
   - Converted categorical features into numeric (One-Hot Encoding).  
   - Removed outliers (IQR method).  

3. **Feature Engineering**  
   - Created new features such as **house age** and **total square footage**.  
   - Selected most relevant numerical features.  

4. **Modeling**  
   - **Baseline model**: Linear Regression.  
   - **Advanced model**: Random Forest Regressor.  

5. **Evaluation**  
   - Metric: **Root Mean Squared Error (RMSE)**.  
   - Compared model performance.

---

## 📈 Results
| Model              | RMSE        |
|---------------------|-------------|
| Linear Regression   | 21475.91     |

---

## 🖥️ Web Application
A **Flask web app** was built where users can input house features (e.g., `OverallQual`, `GrLivArea`, `GarageCars`, `TotalBsmtSF`) and get a predicted price instantly.  

**Preview of Web App:**  
(https://github.com/verenaashraf/House-Prices---Advanced-Regression-Techniques/blob/main/Screenshot%202025-08-27%20084813.png)  

---

## 🛠️ Technologies Used
- **Python**
- **Pandas, NumPy**
- **Matplotlib, Seaborn**
- **Scikit-learn**
- **Flask** (for deployment)
- **HTML, CSS, Bootstrap** (for frontend)
