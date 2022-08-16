import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "seoul_bike.settings")
import django
django.setup()

import plotly.express as px
import plotly.graph_objects as go
from seoul_bike.models import *
import numpy as np
import pandas as pd

import plotly.figure_factory as ff
from plotly.offline import plot
from plotly.subplots import make_subplots


#######  [ 데이터 탐색 ]  #######
# 따릉이 대여소 갯수 (station_near 기준)
def countStationId():
    df = pd.DataFrame(list(StationNear.objects.all().values('station_id')))
    result = df['station_id'].count()
    return result


# 1년간 이용건수
def year_usage():
    month_usage = pd.DataFrame(list(MonthUsage.objects.all().values()))
    result = month_usage['usage_amt'].sum()

    return result


# 따릉이 대여소 top3
def topStation_id():
    df = pd.DataFrame(list(StationUsage.objects.all().values('station_id', 'rent_amt', 'return_amt')))
    df2 = df.groupby(by=['station_id']).sum().reset_index()
    df2 = df2.sort_values(['rent_amt', 'return_amt'], ascending=False)
    result = dict()
    top1 = df2.iloc[0:1]
    top2 = df2.iloc[1:2]
    top3 = df2.iloc[2:3]
    result['top1_station_id'] = top1['station_id'].values[0]
    result['top1_rent_amt'] = top1['rent_amt'].values[0]
    result['top1_return_amt'] = top1['return_amt'].values[0]
    result['top2_station_id'] = top2['station_id'].values[0]
    result['top2_rent_amt'] = top2['rent_amt'].values[0]
    result['top2_return_amt'] = top2['return_amt'].values[0]
    result['top3_station_id'] = top3['station_id'].values[0]
    result['top3_rent_amt'] = top3['rent_amt'].values[0]
    result['top3_return_amt'] = top3['return_amt'].values[0]
    return result


# 강우량과 공공자전거 이용량
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

    fig = go.Figure(
        data=go.Bar(x=rain_usage.rain_amt, y=rain_usage['usage_amt'], marker=dict(color=rain_usage['usage_amt'], colorscale='blues')))
    fig.update_layout(template='plotly_white', margin={"r": 20, "t": 20, "l": 20, "b": 20})
    fig.update_yaxes(visible=False, showticklabels=False)

    plot_div = plot(fig, output_type='div')

    return plot_div


#######  [ 시간적 요소 ]  #######
# 윌/시간대 - 시간대별 따릉이 이용량
def timeusage():
    timeusage = pd.DataFrame(list(TimeUsage.objects.all().values()))
    fig = go.Figure()
    # fig = px.line(timeusage, x='base_tm', y='usage_amt', template='plotly_white')
    fig.add_trace(go.Scatter(x=timeusage.base_tm, y=timeusage.usage_amt, mode='lines',
                             line={'width': 5}, fill='tozeroy'))
    fig.update_coloraxes(showscale=False)
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    fig.update_xaxes(title_text="시간대")
    fig.update_yaxes(title_text="따릉이 이용량")
    plot_div = plot(fig, output_type='div')
    return plot_div


# 생활인구/유동인구 - 시간대별 생활인구와 따릉이 이용량
def lifeusage():
    populusage = pd.DataFrame(list(PopulUsage.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=populusage.base_tm, y=populusage['life_popul'], mode='lines+markers',
                             line={'width': 7}, marker=dict(color='gold', size=15)), secondary_y=True)
    fig.add_trace(go.Bar(x=populusage.base_tm, y=populusage['usage_amt'], name="사용량",
                        marker=dict(color=populusage['usage_amt'], colorscale='teal')), secondary_y=False)
    fig.update_layout(template='plotly_white', showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
    fig.update_xaxes(title_text="시간대별 생활인구와 따릉이 이용량", tickangle=45)
    fig.update_yaxes(title_text="생활인구", secondary_y=True)
    fig.update_yaxes(title_text="대여소 이용량", secondary_y=False)
    plot_div = plot(fig, output_type='div')
    return plot_div


# 생활인구/유동인구 - 시간대별 지하철 유동인구와 따릉이 이용량
def subusage():
    populusage = pd.DataFrame(list(PopulUsage.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=populusage.base_tm, y=populusage['sub_popul'], mode='lines+markers',
                            line={'width': 7}, marker=dict(color='gold', size=15)), secondary_y=True)
    fig.add_trace(go.Bar(x=populusage.base_tm, y=populusage['usage_amt'], name="사용량",
                        marker=dict(color=populusage['usage_amt'], colorscale='teal')), secondary_y=False)
    fig.update_layout(template='plotly_white', showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
    fig.update_xaxes(title_text="시간대별 지하철 유동인구와 따릉이 이용량", tickangle=45)
    fig.update_yaxes(title_text="지하철 유동인구", secondary_y=True)
    fig.update_yaxes(title_text="대여소 이용량", secondary_y=False)
    plot_div = plot(fig, output_type='div')
    return plot_div


# 생활인구/유동인구 - 시간대별 버스 유동인구와 따릉이 이용량
def bususage():
    populusage = pd.DataFrame(list(PopulUsage.objects.all().values()))
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=populusage.base_tm, y=populusage['bus_popul'], mode='lines+markers',
                            line={'width': 7}, marker=dict(color='gold', size=15)), secondary_y=True)
    fig.add_trace(go.Bar(x=populusage.base_tm, y=populusage['usage_amt'], name="사용량",
                        marker=dict(color=populusage['usage_amt'], colorscale='teal')), secondary_y=False)
    fig.update_layout(template='plotly_white', showlegend=False, margin=dict(l=10, r=10, t=10, b=10))
    fig.update_xaxes(title_text="시간대별 버스 유동인구와 따릉이 이용량", tickangle=45)
    fig.update_yaxes(title_text="버스 유동인구", secondary_y=True)
    fig.update_yaxes(title_text="대여소 이용량", secondary_y=False)
    plot_div = plot(fig, output_type='div')
    return plot_div