import pandas as pd
import json

with open('boys.json', 'r', encoding='utf-8') as f:
    boys_data = json.load(f)

boys_series = pd.Series(boys_data)

boys_series = pd.to_datetime(boys_series)

with open('dtm.json', 'w', encoding='utf-8') as f:
    json.dump(boys_series.dt.strftime('%Y-%m-%d').to_dict(), f, ensure_ascii=False, indent=4)

print("Дані успішно збережено у dtm.json")