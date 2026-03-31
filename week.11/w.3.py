import pandas as pd

# Country Series
countries = pd.Series(["India", "USA", "Japan", "Germany", "Brazil"])

# Population Series
population = pd.Series([1400, 330, 125, 83, 210])

# Combine into one Series
combined = pd.Series(data=population.values, index=countries.values)

print("Combined Series:")
print(combined)

                                                                                            