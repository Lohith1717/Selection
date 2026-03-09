import pandas as pd

df = pd.read_excel("pandas_students_120.xlsx")

print("Dataset Loaded\n")

print("First 5 rows")
print(df.head())

print("\nLast 5 rows")
print(df.tail())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())


print("\nSelect single column (Marks)")
print(df["Marks"])

print("\nSelect multiple columns (Name, Marks)")
print(df[["Name","Marks"]])

print("\nFirst 5 rows using iloc")
print(df.iloc[0:5])

# Row and column selection
print("\nSelect rows 0-5 and columns 0-2")
print(df.iloc[0:5,0:3])

print("\nSelect rows and specific columns")
print(df.loc[0:10,["Name","Marks","Department"]])

print("\nStudents with Marks > 85")
print(df[df["Marks"] > 85])

print("\nStudents from CSE Department")
print(df[df["Department"] == "CSE"])

# Multiple conditions
print("\nCSE students with Marks > 85")
print(df[(df["Department"] == "CSE") & (df["Marks"] > 85)])

print("\nSorted by Marks (Descending)")
print(df.sort_values("Marks", ascending=False))

print("\nMissing Values Count")
print(df.isnull().sum())

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nDataset after filling missing values")
print(df.head())

print("\nAverage Marks by Department")
print(df.groupby("Department")["Marks"].mean())

print("\nDepartment Statistics")

print(df.groupby("Department").agg({
    "Marks": ["mean","max","min"],
    "Age": "mean"
}))