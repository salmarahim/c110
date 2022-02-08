import statistics
import random
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

dataset=[]
for i in range(0,100):
    random_index=random.randint(0,len(data))
    value=data[random_index]
    dataset.append(value)

mean=statistics.mean(dataset)
standard_dev=statistics.stdev(dataset)

print(mean)
print(standard_dev)

fig=ff.create_distplot([data],["Temperature"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0,17],mode="lines",name="Mean"))
fig.show()
