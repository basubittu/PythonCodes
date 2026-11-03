import pandas as pd

data = {
    "ID": [1, 2, 3],
    "Name": ["Abhishek", "Rahul", "Amit"],
    "Status": ["PASS", "FAIL", "PASS"]
}

df = pd.DataFrame(data)

df.to_csv("C:/pythonData/PythonCodes/data.csv", index=False)

print("Data written successfully1")