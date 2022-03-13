import matplotlib.pyplot as plt

values = [v for v in range(1, 1001)]
cubes = [v ** 3 for v in range(1,1001)]

# fig表示整张图，ax表示图片中各个图表
fig, ax = plt.subplots()

ax.scatter(values, cubes,c=cubes,cmap=plt.cm.Reds, s=4)  # 设置曲线横纵坐标、粗细,绘制点！

#给坐标轴加标题
ax.set_title("Cube", fontsize=24)
ax.set_xlabel('value', fontsize=14)
ax.set_ylabel('cube of value', fontsize=14)

ax.axis([0, 1100, 0, 1100000000])


plt.savefig('cube_plot.png',bbox_inches='tight')#保存图片