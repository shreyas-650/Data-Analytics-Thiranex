import pandas as pd

# Load data
df = pd.read_csv("./online food delivery dataset.csv")

# Remove unnecessary columns
df.drop(columns=["Unnamed: 13", "latitude", "longitude", "Pin code"], inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill missing values
for col in df.select_dtypes(include="number").columns:
    df[col] = df[col].fillna(df[col].mean())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# Show cleaned data
print("Cleaned Data:")
print(df.head())

# Basic report
print("\nDataset Information:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary:")
print(df.describe())

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)

print("\nCleaned data saved successfully!")