import pandas as pd
df = pd.read_csv("people.csv")
print("--------------------------------")

print(df[df['yas']>30])
df.fillna(0,inplace=True)
sorted_dif=df.sort_values(by="maas",ascending=False)
print("---------------------------------")
ort_maas=df.groupby("departman")["maas"].mean()
print(f"ortalama maas{ort_maas} ")
print("--------------------------------")
print(sorted_dif)
print("--------------------------------")
print(sorted_dif[sorted_dif['yas']>30])