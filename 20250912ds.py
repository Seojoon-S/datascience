import csv
import matplotlib.pyplot as plt
f = open("sns_use.csv", "r", encoding = "euc-kr")
data = csv.reader(f)
next(data)
next(data)
year = ["2016", "2017", "2018"]
facebook = []
for row in data :
    facebook.append(float(row[2]))
f.close()
plt.title("facebook Occupancy ratio")
plt.plot(year, facebook, label = "facebook", color = "blue")
plt.legend()
plt.show()
