import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seoul_bike.settings")
import django
django.setup()
from seoul_bike.models import *
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.offline import plot
from plotly.subplots import make_subplots


# 1. 데이터 탐색 - 1년간 이용건수
def year_usage():
    month_usage = pd.DataFrame(list(MonthUsage.objects.all().values()))
    result = month_usage['usage_amt'].sum()

    return result

# 2. 강우량과 공공자전거 이용량
def rain_usage():
    rain_usage06 = pd.DataFrame(list(RainUsage06.objects.all().values()))

    # rain_amt 내림차순으로 sort 한 후 처음 0인 지점까지 가져온다
    # x : 강우량 y : 이용량
    rain_usage06 = rain_usage06.sort_values('rain_amt', ascending=False)
    rain_usage06 = rain_usage06.reset_index(drop=True)
    index = 0
    while(True):
        if(rain_usage06['rain_amt'][index] == 0):
            break
        else : index += 1
    rain_usage = rain_usage06[0:index+1]

    # print(rain_usage)

    fig = go.Figure(
        data=go.Bar(x=rain_usage.rain_amt, y=rain_usage['usage_amt'], marker=dict(color=rain_usage['usage_amt'], colorscale='blues')))
    fig.update_layout(template='plotly_white', margin={"r": 20, "t": 20, "l": 20, "b": 20})
    fig.update_yaxes(visible=False, showticklabels=False)

    plot_div = plot(fig, output_type='div')

    return plot_div

# rain_usage()