temperatures = [35, 25, 26, 25, 29, 27, 38]
total = sum(temperatures)
average = total / len(temperatures)
print(average)

for i, t in enumerate(temperatures):
    print(f"วันที่ {i+1} มีค่า {t} องศา")

def classify(t, avg):
    if t > avg:
        return "ร้อน"
    else:
        return "เย็น"

print(classify(20, average))

import pandas as pd

df = pd.read_csv("pokemon.csv")
print(df.head())


