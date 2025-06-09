import pandas as pd

items = {
    "Назва": ["Молоко", "Хліб", "Сир", "Яблуко", "Хліб", "Молоко", "Яблуко"],
    "Ціна": [30, 20, 90, 15, 22, 32, 17],
    "Кількість": [1, 2, 1, 5, 1, 2, 3]
}

df = pd.DataFrame(items)

print("Початковий DataFrame:")
print(df)

df_agg = df.groupby("Назва").agg({
    "Ціна": "mean",              
    "Кількість": "sum"            
}).rename(columns={"Ціна": "Середня ціна", "Кількість": "Загальна кількість"})

print("\nАгрегований DataFrame:")
print(df_agg)
