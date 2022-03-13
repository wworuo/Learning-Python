import json
import plotly.express as px
import plotly.io as pio
import pandas as pd

filename='data/eq_data_30_day_m1.json'

with open(filename) as f:
    eq_datas=json.load(f)

eq_infos=eq_datas['features']
mags=[info['properties']['mag'] for info in eq_infos]#震级
titles=[info['properties']['title'] for info in eq_infos]
lons=[info['geometry']['coordinates'][0] for info in eq_infos]#经度
lats=[info['geometry']['coordinates'][1] for info in eq_infos]#纬度

#数据封装
data = pd.DataFrame(
    data=zip(lons,lats, titles, mags),
    columns=['longitude','latitude','position', 'power']
)

#绘图
fig= px.scatter(
    data,
    x='longitude',
    y='latitude',
    #等价表达式
#    x=lons,
#    y=lats,
#    labels={'x':'longitude','y':'latitude'},
    size='power',size_max=10,#用大小来表示强度
    color='power',#用颜色变化来表示强度
    hover_name='position',
    range_x=[-200,200],
    range_y=[-90,90],
    width=800,
    height=800,
    title="Global Earthquake",
)

#输出
fig.write_html('global_earthquake.html')
fig.show()

#pio.write_image(fig,'earthquake.png')
#pio.show(fig)