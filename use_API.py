import requests
from plotly.graph_objs import Bar
from plotly import offline


#执行API调用并储存响应
url='https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)#输入网址，得到反馈信息
print("Status code:",r.status_code)

#将API响应赋给一个变量
response_dict = r.json()#以json文件形式打开，得到一个字典类

print(response_dict.keys())
print(f"Total repositories: {response_dict['total_count']}")

item_dicts=response_dict['items']
print(f"Repositories returned: {len(item_dicts)}")

#创建数据内容
item_names=[value['name'] for value in item_dicts]
item_stars=[value['stargazers_count'] for value in item_dicts]
#更多的注释
item_labels=[f"{value['owner']['login']}<br />{value['description']}" for value in item_dicts]
#添加可点击的链接
item_links=[f"<a href='{value['html_url']}'>{value['name']}</a>" for value in item_dicts]


#柱状图，分成两部分
data=[{
    'type':'bar',
    'x':item_links,
    'y':item_stars,
    'hovertext':item_labels,
    'marker':{
        'color':'rgb(60,100,150)',
        'line':{'width':1.5 ,'color':'rgb(25,25,25)'}
    }
}]
my_layout={
    'title':'The most popular projects of Python in Github',
    'xaxis':{
        'title':'Repository',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
    'yaxis':{
        'title':'Stars',
        'titlefont':{'size':24},
        'tickfont':{'size':14},
    },
}
fig={'data':data,'layout':my_layout}


offline.plot(fig,filename='python_repos.html')