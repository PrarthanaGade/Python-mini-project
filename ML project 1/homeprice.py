import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

try:
    df = pd.read_csv(r"C:\Users\prart\Desktop\Python Mini projects\ML project 1\house price\house_cleaned.csv")
    
    # Check if required columns exist
    if 'area' not in df.columns or 'price' not in df.columns:
        print("Error: Required columns 'area' and 'price' not found in the dataset")
        print("Available columns:", df.columns.tolist())
    else:
        # Basic data information
        print("\nDataset Info:")
        print(df.info())
        print("\nFirst few rows:")
        print(df.head())
        
        # Plot the data
        plt.scatter(df.area, df.price, color='red', marker='+')
        plt.xlabel('area')
        plt.ylabel('price')
        plt.title('Area vs Price')
        plt.show()
        
        # Train the model
        reg = linear_model.LinearRegression()
        reg.fit(df[['area']], df.price)
        
        # Print model coefficients
        print("\nModel Coefficients:")
        print("Slope:", reg.coef_[0])
        print("Intercept:", reg.intercept_)
        
except FileNotFoundError:
    print("Error: The CSV file was not found at the specified path")
except Exception as e:
    print(f"An error occurred: {str(e)}")
