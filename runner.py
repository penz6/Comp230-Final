# Penn Potter, Natalie Forno, Cassidy Methot

# Comp 230 Final

# A program to pull data from our .json file, and plot the data we want to see
# uses up to 4 cores to plot due to memory constraints

import pandas as pd
import matplotlib.pyplot as plt
import multiprocessing as mp
from matplotlib.ticker import MaxNLocator
import statistics
# data from json, treat line as object
data = pd.read_json("data1.json",lines=True)

#clean data
data = data.drop(data['popularity'<750].index)
#print(data)

#multi threaded plotting
def multi_plot(arg):
    #args
    x,y,name = arg
    #scatter
    plt.scatter(x,y)
    #name
    plt.title(name)
    #limit amount of lables
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=5))
    plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5))

    plt.savefig(f"{name}.png")
    #close
    plt.close()

#what to plot
plotting_data = [[data['first_air_date'],data['popularity'],'X: Air Date | Y:Populairty'],[statistics.mean(data['episode_run_time']),data['popularity'],"X:Runtime | Y:Popularity"],[data['vote_count'],data["popularity"],"X:Vote Count | Y:Popularity"],[data['popularity'],data["vote_average"],"'X: Popularity | Y:Vote Score'"],[data['languages'],data['popularity'],"X: Language | Y: Popularity"]]
#multi_plot(plotting_data[0])
if __name__ == '__main__':
    #cpus
    pool = mp.Pool(4)
    pool.map(multi_plot,plotting_data)
    pool.close()
    pool.join()