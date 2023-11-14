import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('A.csv')

# Boşluklu başlıkları güncelle
df.columns = df.columns.str.strip()

# "Source IP" ve "Destination IP" sütunlarındaki kombinasyonları gruplama ve sayma
attack_counts = df.groupby(['Source IP', 'Destination IP']).size().reset_index(name='Attack Count')

plt.figure(figsize=(12, 6))
pivot_table = attack_counts.pivot(index='Source IP', columns='Destination IP', values='Attack Count').fillna(0)
sns.heatmap(pivot_table, annot=True, fmt='g', cmap='YlGnBu')
plt.xlabel('Destination IP')
plt.ylabel('Source IP')
plt.title('Source IP - Destination IP Kombinasyonlarındaki Saldırı Sayısı')
plt.show()
