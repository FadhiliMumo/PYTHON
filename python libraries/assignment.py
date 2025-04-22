import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt

# 1. Create a NumPy array of numbers from 1 to 10 and calculate the mean
array = np.arange(1, 11)
mean_value = np.mean(array)
print("Mean of the array:", mean_value)

# 2. Load a small dataset into a pandas DataFrame and display summary statistics
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "Score": [85, 90, 95, 100]
}
df = pd.DataFrame(data)
print("\nSummary Statistics:")
print(df.describe())

# 3. Fetch data from a public API using requests and print a key piece of information
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
if response.status_code == 200:
    post_data = response.json()
    print("\nTitle of the post fetched from API:", post_data.get("title"))
else:
    print("\nFailed to fetch data from API. Status code:", response.status_code)

# 4. Plot a simple line graph using matplotlib
numbers = [1, 2, 3, 4, 5]
plt.plot(numbers, [n**2 for n in numbers], marker='o', label="y = x^2")
plt.title("Simple Line Graph")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()