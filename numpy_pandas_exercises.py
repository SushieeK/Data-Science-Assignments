
import numpy as np
import pandas as pd

# Question 1: Define two custom numpy arrays A and B, and stack them vertically and horizontally
A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

# Vertical stack
vertical_stack = np.vstack((A, B))

# Horizontal stack
horizontal_stack = np.hstack((A, B))

# Question 2: Find common elements between A and B (intersection of two sets)
common_elements = np.intersect1d(A, B)

# Question 3: Extract all numbers from A which are between 5 and 10
numbers_in_range = A[(A >= 5) & (A <= 10)]

# Question 4: Filter rows of iris_2d where petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])

filtered_iris = iris_2d[(iris_2d[:, 2] > 1.5) & (iris_2d[:, 0] < 5.0)]

# Pandas Questions

# Question 5: Filter 'Manufacturer', 'Model', and 'Type' for every 20th row starting from 1st
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
filtered_rows = df.loc[::20, ['Manufacturer', 'Model', 'Type']]

# Question 6: Replace missing values in 'Min.Price' and 'Max.Price' with their respective mean
df['Min.Price'].fillna(df['Min.Price'].mean(), inplace=True)
df['Max.Price'].fillna(df['Max.Price'].mean(), inplace=True)

# Question 7: Get rows of a DataFrame with row sum > 100
df_random = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))
rows_with_sum_greater_than_100 = df_random[df_random.sum(axis=1) > 100]
