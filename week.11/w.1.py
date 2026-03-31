import pandas as pd

countries_dict = {}

# Take input for 5 countries
for i in range(5):
    country = input(f"Enter country {i+1}: ")
    countries_dict[i] = country   # key = index, value = country

# Create Pandas Series from dictionary
countries = pd.Series(countries_dict)

print("\nPandas Series:")
print(countries)                                                                                                     

