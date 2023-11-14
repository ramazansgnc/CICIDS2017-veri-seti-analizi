import pandas as pd
import matplotlib.pyplot as plt

# CSV dosyasını oku
df = pd.read_csv('A.csv')

# 'Destination IP' sütunundaki en çok tekrarlanan ilk 3 IP'yi bul
top_source_ips = df.iloc[:, 3].value_counts().nlargest(3)

# Grafiği oluştur
plt.bar(top_source_ips.index, top_source_ips.values)
plt.xlabel('Destination IP')
plt.ylabel('Tekrarlanma Sayısı')
plt.title('En Çok Tekrarlanan İlk 3 Source IP')
plt.show()
