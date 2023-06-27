#!/usr/bin/env python
# coding: utf-8

# In[320]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import warnings


# In[330]:


housing_prices_data = pd.read_csv('Housing Prices.csv')
housing_prices_data.head()


# In[331]:


housing_prices_data.shape


# In[332]:


# Re-determining how many rows in data set
housing_prices_data.shape


# In[386]:


import pandas as pd

# Read the CSV file
housing_prices = pd.read_csv('Housing Prices.csv')

# Convert numeric columns to numeric type with error handling
numeric_columns = ['Detached','Condos', 'Town House']

housing_prices = housing_prices.fillna(housing_prices.mean(numeric_only=True))

# Formatting data frame
housing_prices_formatted = housing_prices.style.format({'Detached': '${:,.2f}',
                                                        'Condos': '${:,.2f}',
                                                        'Town House': '${:,.2f}'})

# Display the formatted DataFrame
display(housing_prices_formatted)



# In[334]:


# Grouping the housing prices by Region and Year and calculating the mean house prices
group_region_year = round(housing_prices.groupby(['Region','Year']).mean(),2)
group_region_year


# In[338]:


# Selecting composite price group to plot
group_comp = group_region_year['Detached']

# Unstacking df and plotting on a line plot
group_comp.unstack(level='Region').plot.line(figsize=(15,10), subplots=False)

# Adding labels to chart
plt.title('Detached Price per Region')
plt.ylabel('Price ($)')

# Saving and displaying plot

plt.show()


# In[344]:


# Selecting composite price group to plot
group_comp = group_region_year['Condos']

# Unstacking df and plotting on a line plot
group_comp.unstack(level='Region').plot.line(figsize=(15,10), subplots=False)

# Adding labels to chart
plt.title('Condos Price per Region')
plt.ylabel('Price ($)')

# Saving and displaying plot

plt.show()


# In[343]:


# Selecting composite price group to plot
group_comp = group_region_year['Town House']

# Unstacking df and plotting on a line plot
group_comp.unstack(level='Region').plot.line(figsize=(15,10), subplots=False)

# Adding labels to chart
plt.title('Town House Price per Region')
plt.ylabel('Price ($)')

# Saving and displaying plot

plt.show()


# In[352]:


### import pandas as pd
import matplotlib.pyplot as plt

# Select the desired columns
housingPrice_2018_2021 = housing_prices.loc[((housing_prices["Year"] == 2018) | (housing_prices["Year"] == 2021))]
housingPrice_2018_2021 = housingPrice_2018_2021[["Region", "Year", "Detached"]]

# Group the data by region and year, and calculate the mean price
housingPrice_grouped = housingPrice_2018_2021.groupby(["Region", "Year"]).mean().reset_index()

# Pivot the data
housingPrice_pivot = housingPrice_grouped.pivot(index="Region", columns="Year", values="Detached")

# Plot the bar chart
housingPrice_pivot.plot(kind="bar", rot=0, figsize=(10, 8))

# Set the x-axis label
plt.xlabel("Region")

# Set the y-axis label
plt.ylabel("Price")

# Set the title
plt.title("Detached Housing Prices by Region (2018-2021)")

# Show the plot
plt.show()





# In[354]:


### import pandas as pd
import matplotlib.pyplot as plt

# Select the desired columns
housingPrice_2018_2021 = housing_prices.loc[((housing_prices["Year"] == 2018) | (housing_prices["Year"] == 2021))]
housingPrice_2018_2021 = housingPrice_2018_2021[["Region", "Year", "Condos"]]

# Group the data by region and year, and calculate the mean price
housingPrice_grouped = housingPrice_2018_2021.groupby(["Region", "Year"]).mean().reset_index()

# Pivot the data
housingPrice_pivot = housingPrice_grouped.pivot(index="Region", columns="Year", values="Condos")

# Plot the bar chart
housingPrice_pivot.plot(kind="bar", rot=0, figsize=(10, 8))

# Set the x-axis label
plt.xlabel("Region")

# Set the y-axis label
plt.ylabel("Price")

# Set the title
plt.title("Condo Housing Prices by Region (2018-2021)")

# Show the plot
plt.show()





# In[356]:


### import pandas as pd
import matplotlib.pyplot as plt

# Select the desired columns
housingPrice_2018_2021 = housing_prices.loc[((housing_prices["Year"] == 2018) | (housing_prices["Year"] == 2021))]
housingPrice_2018_2021 = housingPrice_2018_2021[["Region", "Year", "Town House"]]

# Group the data by region and year, and calculate the mean price
housingPrice_grouped = housingPrice_2018_2021.groupby(["Region", "Year"]).mean().reset_index()

# Pivot the data
housingPrice_pivot = housingPrice_grouped.pivot(index="Region", columns="Year", values="Town House")

# Plot the bar chart
housingPrice_pivot.plot(kind="bar", rot=0, figsize=(10, 8))

# Set the x-axis label
plt.xlabel("Region")

# Set the y-axis label
plt.ylabel("Price")

# Set the title
plt.title("Town Houses Prices by Region (2018-2021)")

# Show the plot
plt.show()








# In[362]:


# Importing income per region data
income_region_data = pd.read_csv('Incomes.csv')
# Dropping all rows with missing data
income_region_data = income_region_data.dropna()

# Removing commas from "Average Income" column
income_region_data['Average Income'] = income_region_data['Average Income'].str.replace(',', '')

# Converting "Average Income" column to float
income_region_data['Average Income'] = income_region_data['Average Income'].astype(float)

# Creating a new DataFrame for analysis
income_region = income_region_data[['Region', 'Year', 'Average Income']]

# Export file as a CSV, without the Pandas index, but with the header
income_region.to_csv("Incomes.csv", index=False, header=True)

# Formatting data frame
formatted_income_region = income_region.style.format({'Average Income':'${:,.2f}'})
formatted_income_region




# In[363]:


# Removing Year from group_region_year (housing analysis) index and adding to a column in df
group_region_year = group_region_year.reset_index(level=['Year'])

# Combine the housing_region data and income_region data into a single dataset
housing_income_region_data =pd.merge(group_region_year, income_region, on='Region')
housing_income_region_data


# In[364]:


# Creating a clean df by removing any years where we dont have income data for
housing_income_region_clean = housing_income_region_data.loc[housing_income_region_data['Year_x'] == housing_income_region_data['Year_y']]

# Creating a df for analysis
housing_income_region = housing_income_region_clean[['Region', 'Year_x', 'Average Income', 'Detached',
                                                      'Condos', 'Town House']]

# Rename the Year column and resetting index
housing_income_region = housing_income_region.rename(columns = {'Year_x':'Year'}).reset_index(drop=True)

# Export file as a CSV, without the Pandas index, but with the header
housing_income_region.to_csv("Incomes.csv", index=False, header=True)
housing_income_region


# In[365]:


# Calculating housing price vs income ratio
housing_income_region['House Price/Income Ratio'] = housing_income_region['Detached'] / housing_income_region['Average Income']

# Select the columns that we need to plot the chart
housing_income_region_ratio = housing_income_region[['Region', 'Year', 'House Price/Income Ratio']]
housing_income_region_ratio


# In[367]:


# Summarizing housing_income_region_ratio table with a pivot table
price_income_ratio = housing_income_region_ratio.pivot(index='Year', columns='Region', values='House Price/Income Ratio')
price_income_ratio.plot.line(figsize = (10, 8))

# Adding labels to chart
plt.title('Housing Price to Income Ratio by Region')
plt.ylabel('Price to Income Ratio')

# Saving and displaying plot
plt.show()


# In[385]:






# In[ ]:




