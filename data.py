import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def line_chart_example(x_ser, y_ser):
   
    plt.plot(x_ser, y_ser,
             label="Population",
             c="green", 
             lw=5) 
             label="Population x2",
             c="purple",
             ls="--") 

    plt.legend()
   
    plt.ylabel("Population (in millions)")
    plt.xlabel("City Class")
    plt.title("Chinese Population Analysis")
    
    plt.savefig("line.png") 

def scatter_chart_example(x_ser, y_ser):
    
    plt.figure()
    plt.scatter(x_ser,
                y_ser,
                s=300, # s is for size
                marker="x") # X instead of O
    plt.savefig("scatter.png")

def bar_chart_example(x_ser, y_ser):
    plt.figure()
    plt.bar(x_ser, y_ser)
    plt.savefig("bar.png")

def pie_chart_example(values_ser, labels_ser):
    plt.figure()
    plt.pie(values_ser,
            labels=labels_ser,
            autopct="%1.1f%%") # auto percent labels
    plt.savefig("pie.png")

def histogram_chart_example(values_ser1,
                            values_ser2):
    plt.figure()
    # default number of bins is 10
    plt.hist(values_ser1,
             bins=30,
             alpha=0.5) # transparency of bars
    plt.hist(values_ser2,
             bins=30,
             alpha=0.5)
    plt.ylabel("Count (Frequency) of each X-axis Bin")
    plt.savefig("histogram.png")

df = pd.read_csv("merged.csv")
print(df)
# grab the total population for each Class
# (Large, Medium, Small)
grouped_by_class = df.groupby("Class")
class_pop_ser = grouped_by_class["Population"].sum()
print(class_pop_ser)


line_chart_example(class_pop_ser.index, 
                   class_pop_ser) 

scatter_chart_example(class_pop_ser.index,
                      class_pop_ser)


bar_chart_example(class_pop_ser.index,
                  class_pop_ser)


pie_chart_example(class_pop_ser, # parts
                  class_pop_ser.index) # labels

mean = 100 # center of distribution
stdev = 25 # how spread out the data is from
# the mean
num_datapoints = 1000
# normal (Gaussian) means "bell-shaped"
rand_data1 = np.random.normal(mean,
                              stdev,
                              num_datapoints)

rand_data2 = np.random.normal(mean,
                              stdev / 2,
                              num_datapoints)
histogram_chart_example(rand_data1,
                        rand_data2)
