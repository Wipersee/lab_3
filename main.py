 
import cx_Oracle
import chart_studio.plotly as py
import plotly.graph_objs as go

my_conn = cx_Oracle.connect("hr/11@localhost:1521/orcl")
cursor = my_conn.cursor()


re2 ="""select 
sum(NA_sales) as SUMMARY_NA_sales
,sum(EU_sales) as SUMMARY_EU_sales
,sum(JP_sales) as SUMMARY_JP_sales,
sum(Other_sales) as SUMMARY_Other_sales 
FROM region_sales"""
cursor.execute(re2)
dictionary = {}

names = []
for name in cursor.description:
        names.append(name[0])

for row in cursor:
    x = row

data = [go.Bar(
            x=names,
            y=list(x)
    )]
 
layout = go.Layout(
    title='Regions and summary sales',
    xaxis=dict(
        title='Region',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Sales',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=data, layout=layout)
 
