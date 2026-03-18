# Data Preprocessing – Chronic Kidney Disease Dataset

## Project Description

This project demonstrates **data preprocessing techniques** using the Chronic Kidney Disease dataset.
The main objective is to **identify and handle missing values** and prepare the dataset for further analysis or machine learning.

## Dataset

The dataset used in this project is the **Chronic Kidney Disease Dataset**.

## Preprocessing Steps Performed

1. **Load the dataset** using Pandas.
2. **Identify missing values** in the dataset.
3. **Separate quantitative and qualitative columns**.
4. For **numerical columns**, skewness was calculated to understand the distribution of data.
5. If the data was **normally distributed (skew between -0.5 and 0.5)**, missing values were replaced using the **mean**.
6. If the data was **skewed**, missing values were replaced using the **median**.
7. For **categorical columns**, missing values were replaced using the **most frequent value (mode)**.
8. After preprocessing, the dataset was checked again to confirm that **all missing values were removed**.

## Tools and Libraries Used

* Python
* Pandas
* NumPy
* Scikit-learn (SimpleImputer)

## Files in this Folder

* **Data Preprocessing.ipynb** – Jupyter notebook containing preprocessing code.
* **kidney_disease.csv** – Chronic Kidney Disease dataset used for the assignment.

## Conclusion

Data preprocessing is an important step in data analysis. By handling missing values and cleaning the dataset, the data becomes more reliable and ready for further statistical analysis or machine learning models.

