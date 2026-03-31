import pandas as pd

data = {}
n = int(input("Enter number of countries: "))

for i in range(n):
    country = input(f"Enter country name:{i+1} ").lower()
    population = int(input("Enter population: "))
    data[country] = population

series = pd.Series(data)
print(series)
# Search
name = input("Enter country to search: ").lower()

if name in series:
    print("Population:", series[name])
else:
    print("Country not found")
