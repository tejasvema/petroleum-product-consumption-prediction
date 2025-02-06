# Petroleum Product Consumption Prediction

## Project Overview
This project focuses on predicting the consumption of petroleum products in India using a dataset from [data.gov.in](https://data.gov.in/). The primary goal was to analyze historical data and forecast future consumption patterns based on various features such as month, year, and product type.

## Dataset
The dataset used in this project was sourced from [data.gov.in](https://data.gov.in/) and includes:
- **Month**: The month of the recorded data.
- **Year**: The year corresponding to the data.
- **PRODUCTS**: Various petroleum products such as ATF, Bitumen, HSD, MS, LPG, etc.
- **Quantity (in Metric Tonnes)**: The amount of each petroleum product consumed.

## Machine Learning Model
- **Algorithm Used**: RandomForestRegressor
- **Reason for Selection**: The Random Forest algorithm was chosen for its robustness in handling complex, non-linear relationships in the data.
- **Performance**: The model achieved an accuracy of **9.7%**, indicating the need for further improvements.

## Implementation Steps
1. **Data Preprocessing**
   - Handling missing values.
   - Encoding categorical variables.
   - Scaling numerical features.
2. **Exploratory Data Analysis (EDA)**
   - Visualization of product consumption trends.
   - Identification of seasonal patterns.
3. **Model Training**
   - Splitting data into training and testing sets.
   - Training the RandomForestRegressor model.
4. **Evaluation**
   - Calculating accuracy and error metrics.
   - Comparing predictions with actual values.

## Results & Insights
- The model demonstrated a certain level of predictive capability but requires further tuning for improved accuracy.
- Feature engineering and hyperparameter tuning may enhance performance.

## Future Work
- Experimenting with other machine learning models like XGBoost and LSTM.
- Incorporating additional external factors such as economic indicators and crude oil prices.

## Tools & Technologies Used
- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn
- **Environment**: Jupyter Notebook / VS Code

## Conclusion
This project serves as a foundational step in leveraging machine learning for petroleum product consumption forecasting. Future improvements can enhance its predictive power and practical applications in fuel demand estimation and supply chain management.

## Author
**Tejas**

feel free to contribute to future improvements!

