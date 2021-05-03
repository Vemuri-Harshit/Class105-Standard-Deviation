import pandas as pd;
import plotly.express as px;
import csv;

with open("class2.csv", newline="") as f:
    data = csv.reader(f);
    data = list(data);

data.pop(0);

marks = 0;
n = len(data);

for mark in data:
    marks += float(mark[1]);

mean = marks / n;

df = pd.read_csv("class2.csv");
scatter_graph = px.scatter(df, x='Student Number', y='Marks');
scatter_graph.update_layout(shapes = [
    dict(
        type="line",
        y0= mean,
        y1= mean,
        x0= 0,
        x1= n 
    )
])

scatter_graph.update_yaxes(rangemode = 'tozero')

scatter_graph.show();
