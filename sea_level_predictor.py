import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
  

    # Create scatter plot

    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])


    # Create first line of best fit

    slope, intercept, r_value, p_value, std_err = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    
    years = range(1880, 2051)
    plt.plot(years, intercept + slope * years, color='red')
    
    

    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    slope_2000, intercept_2000, r_value_2000, p_value_2000, std_err_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    years2000 = range(2000, 2051)
    plt.plot(years2000, intercept_2000 + slope_2000 * years2000, color='blue')



    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    print(f"The correlation between sea level and year is {r_value:.2f}.")
    print((intercept_2000 + slope_2000 * years2000)*2.54)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()