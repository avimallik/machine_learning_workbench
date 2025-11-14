is_numeric = df.bore.str.match(r'^-?\d+(\.\d+)?$')                             
num_count = is_numeric.sum()
text_count = len(df.bore) - num_count

percent_num = ((num_count/len(df.bore)) * 100)
percent_text = ((text_count/len(df.bore)) * 100)

df.bore = pd.to_numeric(df.bore, errors='coerce')

mean_bore = df.bore.mean()
df.bore = df.bore.fillna(mean_bore)
df.bore.to_csv('bore_col.csv')