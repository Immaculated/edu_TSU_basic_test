import pandas as pd
data = {
    'col 1': ['Я', 'Python', 'Буду'], 
    'col 2': ['люблю', 'мой', 'стараться'],
    'col 3': ['анализ', 'лучший', 'хорошо'], 
    'col 4': ['данных', 'друг', 'учиться']
}
df = pd.DataFrame(data)
print(df)