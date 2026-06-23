#Answer 1 
import numpy as np
arr = np.random.randint(1, 101, 20)
print("Array:", arr)
minimum = np.min(arr)
maximum = np.max(arr)
mean = np.mean(arr)
std_dev = np.std(arr)
print("Minimum:", minimum)
print("Maximum:", maximum)
print("Mean:", mean)
print("Standard Deviation:", std_dev)
#Answer 2 
import numpy as np
# Create a 4×4 matrix
matrix = np.array([
    [12, 5, 8, 3],
    [7, 14, 9, 2],
    [6, 11, 4, 15],
    [10, 13, 1, 16]
])
print("Original Matrix:")
print(matrix)
# Extract diagonal elements
diagonal = np.diag(matrix)
print("\nDiagonal Elements:")
print(diagonal)
# Replace all even numbers with 0
matrix[matrix % 2 == 0] = 0
print("\nMatrix after replacing even numbers with 0:")
print(matrix)
# Find index of maximum value
max_index = np.argmax(matrix)
print("\nIndex of Maximum Value:", max_index)
#Answer 3
import numpy as np
# Create two 3×3 NumPy arrays
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])
print("Matrix A:")
print(A)
print("\nMatrix B:")
print(B)
# Element-wise Addition
addition = A + B
print("\nElement-wise Addition (A + B):")
print(addition)
# Element-wise Subtraction
subtraction = A - B
print("\nElement-wise Subtraction (A - B):")
print(subtraction)
# Matrix Multiplication
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (A × B):")
print(multiplication)
#Answer 4
import numpy as np
# Create arrays
arr1 = np.linspace(1, 5, 5)   
arr2 = np.zeros(5)           
arr3 = np.ones(5)             
print("Array from linspace:")
print(arr1)
print("\nArray of zeros:")
print(arr2)
print("\nArray of ones:")
print(arr3)
# Stack arrays vertically
stacked_array = np.vstack((arr1, arr2, arr3))
print("\nFinal Stacked Array:")
print(stacked_array)
#Answer 5
import pandas as pd
# Create a DataFrame
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan",
             "Pooja", "Vikas", "Neha", "Arjun", "Riya"],
    "Age": [20, 21, 19, 22, 20, 21, 23, 20, 22, 19],
    "Marks": [85, 72, 90, 68, 77, 81, 65, 88, 74, 95],
    "City": ["Delhi", "Mumbai", "Jaipur", "Pune", "Chennai",
             "Kolkata", "Hyderabad", "Delhi", "Mumbai", "Jaipur"]
}
df = pd.DataFrame(data)
# Display first 5 rows
print("First 5 Rows:")
print(df.head())
# Show basic statistics
print("\nBasic Statistics:")
print(df.describe())
# Filter students with marks > 75
print("\nStudents Scoring More Than 75 Marks:")
high_scorers = df[df["Marks"] > 75]
print(high_scorers)
# Sort by Marks in descending order
print("\nStudents Sorted by Marks (Descending):")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)
#Answer 6
import pandas as pd
import numpy as np
# Create DataFrame with missing values
data = {
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, np.nan, 90, np.nan, 77],
    "City": ["Delhi", "Mumbai", np.nan, "Pune", np.nan]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Identify missing values
print("\nMissing Values:")
print(df.isnull())
# Fill missing marks with column mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)
print("\nDataFrame after filling missing Marks with mean:")
print(df)
# Drop rows where City is missing
df_city = df.dropna(subset=["City"])
print("\nDataFrame after dropping rows with missing City:")
print(df_city)
#Answer 7
import pandas as pd
# Create sample sales data and save as CSV
data = {
    "Product": ["Laptop", "Phone", "Tablet", "Monitor", "Printer",
                "Keyboard", "Mouse", "Speaker", "Camera", "Router"],
    "Category": ["Electronics", "Electronics", "Electronics", "Accessories", "Accessories",
                 "Accessories", "Accessories", "Electronics", "Electronics", "Networking"],
    "Sales": [50000, 35000, 20000, 15000, 12000,
              8000, 6000, 18000, 25000, 10000],
    "Region": ["North", "South", "East", "West", "North",
               "South", "East", "West", "North", "South"]
}
df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)
sales_df = pd.read_csv("sales_data.csv")
print("Sales Data:")
print(sales_df)
# Group by Category and calculate total Sales
category_sales = sales_df.groupby("Category").agg(
    Total_Sales=("Sales", "sum")
)
print("\nTotal Sales by Category:")
print(category_sales)
# Find top 3 products by sales
top_products = sales_df.sort_values(
    by="Sales", ascending=False
).head(3)
print("\nTop 3 Products by Sales:")
print(top_products)
#Answer 8
import pandas as pd
# DataFrame 1
df1 = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Karan"],
    "Department": ["CSE", "IT", "ECE", "CSE", "ME"]
})
# DataFrame 2
df2 = pd.DataFrame({
    "StudentID": [101, 102, 103, 104, 105],
    "Marks": [85, 72, 91, 68, 88],
    "Grade": ["A", "B", "A", "C", "A"]
})
# Merge DataFrames on StudentID
merged_df = pd.merge(df1, df2, on="StudentID")
print("Merged DataFrame:")
print(merged_df)
# Display students with Grade 'A'
grade_a = merged_df[merged_df["Grade"] == "A"]
print("\nStudents with Grade 'A':")
print(grade_a)
#Answer 9
import matplotlib.pyplot as plt
# 1.Line Plot: Marks Trend Across 5 Subjects
subjects = ["Math", "Science", "English", "Computer", "History"]
marks = [85, 78, 92, 88, 80]
plt.figure(figsize=(8, 5))
plt.plot(subjects, marks, marker='o', label="Student Marks")
plt.title("Marks Trend Across 5 Subjects")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
# 2. Bar Chart: Marks of 5 Students
students = ["Amit", "Priya", "Rahul", "Sneha", "Karan"]
student_marks = [85, 72, 90, 68, 88]
plt.figure(figsize=(8, 5))
plt.bar(students, student_marks, label="Marks")
plt.title("Marks Comparison of 5 Students")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()
#Answer 10
import pandas as pd
import matplotlib.pyplot as plt
# Create a dataset with 4 numeric columns
data = {
    "Math": [85, 78, 92, 88, 75, 81, 95, 69, 84, 90],
    "Science": [80, 74, 89, 91, 70, 85, 93, 72, 79, 88],
    "English": [78, 82, 85, 87, 73, 80, 90, 75, 81, 86],
    "Computer": [90, 85, 95, 92, 80, 88, 98, 77, 86, 94],
    "Category": ["A", "B", "A", "A", "C", "B", "A", "C", "B", "A"]
}
df = pd.DataFrame(data)
# 1. Histogram for Marks Distribution (Math)
df["Math"].plot(
    kind="hist",
    bins=5,
    title="Math Marks Distribution"
)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()
# 2. Box Plot for Numeric Columns
df[["Math", "Science", "English", "Computer"]].plot(
    kind="box",
    title="Marks Spread and Outliers"
)
plt.ylabel("Marks")
plt.grid(True)
plt.show()
# 3. Pie Chart for Category-wise Percentage
df["Category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    title="Category-wise Percentage"
)
plt.show()
