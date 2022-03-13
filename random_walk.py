from random import choice
import matplotlib.pyplot as plt


class RandomWalk:

    def __init__(self, num_points=5000):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):

        while len(self.x_values) < self.num_points:

            x_direction = choice([-1, 1])
            x_distance = choice(range(5))
            x_step = x_distance * x_direction

            y_direction = choice([-1, 1])
            y_distance = choice(range(5))
            y_step = y_distance * y_direction

            if x_step == 0 and y_step == 0:
                continue

            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)



rw = RandomWalk(5_000)
rw.fill_walk()

#绘图
plt.style.use('classic')
fig, ax = plt.subplots()

# 增加细节
#颜色的渐变
num_points_range=range(rw.num_points)
#绘制点———云彩
#ax.scatter(rw.x_values, rw.y_values,
#           c=num_points_range,
#           cmap=plt.cm.Blues,
#           edgecolors='none',s=15)
#绘制线———布朗运动
ax.plot(rw.x_values,rw.y_values,linewidth=0.3)
#起点与终点
ax.scatter(0,0,c='red',edgecolors='none',s=50)
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=50)
#隐藏坐标轴
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.savefig("Brownian_motion.png",bbox_inches='tight')


