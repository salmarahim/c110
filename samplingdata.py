import random
import statistics
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
data=df["temp"].tolist()

def random_set_of_means(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    print(mean)

    fig=ff.create_distplot([df],["Tempertaure"],show_hist=False)
    fig.show()


def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_means(100)
        mean_list.append(set_of_means)

    show_fig(mean_list)
    std_dev=statistics.stdev(mean_list)
    print(std_dev)


    
setup()
