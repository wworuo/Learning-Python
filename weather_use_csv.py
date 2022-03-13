import csv
import matplotlib.pyplot as plt
from datetime import datetime  # 读取时间

filename = 'data/death_valley_2018_full.csv'
with open(filename) as f:
    reader = csv.reader(f)#读取csv格式的文件,reader是文件指针
    header_row = list(next(reader))  # 读取文件下一行，第一次读是第一行

    index_low=header_row.index('TMIN')
    index_high=header_row.index('TMAX')
    index_date=header_row.index('DATE')
    temperature_high, temperature_low,dates = [], [], []
    #更安全地处理数据
    for row in reader:
        date=datetime.strptime(row[index_date], '%Y-%m-%d')
        try:
            low=int(row[index_low])
            high=int(row[index_high])
        except ValueError:
            print(f"Missing data for {date}")
        else:
            temperature_low.append(low)
            temperature_high.append(high)
            dates.append(date)


plt.style.use("seaborn")
fig, ax = plt.subplots()
#绘制线
ax.plot(dates, temperature_high, c='red')
ax.plot(dates,temperature_low,c='blue')#绘制两份图
ax.fill_between(dates, temperature_high, temperature_low, facecolor='blue', alpha=0.1)#填充图像间空隙
#增加细节
ax.set_title(f"The Highest Temperature Everyday in 2018")
fig.autofmt_xdate()  # 绘制倾斜日期

ax.set_xlabel('', fontsize=16)
ax.set_ylabel('temperature (F)', fontsize=16)
ax.tick_params(axis='both', width='major', labelsize=16)

plt.show()