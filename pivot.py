import pandas as pd
df = pd.read_csv("raw-data/csv/get_fit_now_member.csv")

df = df.pivot(columns="person_id")

df.to_csv("raw-data/test_pivot.csv", index=False)
print(df)