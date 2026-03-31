import pandas as pd

population_dict = {}

# Take input for 5 countries' population
for i in range(5):
    country = input(f"Enter country name {i+1}: ")
    pop = int(input(f"Enter population of {country}: "))
    
    population_dict[country] = pop   # key = country name, value = population

# Create pandas Series
population = pd.Series(population_dict)

print("\nPopulation Series:")
print(population)