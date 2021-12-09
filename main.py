import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
from scipy import stats as s
import sys


def plot_pdf_csv(csv_file, column=[]):
    data = pd.read_csv(csv_file)
    # Loop over all the headers in the csv file to make plots for everything
    for i in data.head():
        if column == [] or i in column:
            data_selected = i
            values = data[data_selected]
            plot = pd.DataFrame(values).plot(kind='kde')

            # Calculate the median, Mode and mean using statistics and stats from scipy
            mean = stat.mean(values)
            mode = s.mode(values)[0]
            median = stat.median(values)

            # Adding the lines for mean, mode and median
            plot.axvline(mean, color='k', linestyle='--', label='mean')
            plot.axvline(mode, color='g', linestyle='--', label='mode')
            plot.axvline(median, color='r', linestyle='--', label="median")

            plot.legend(loc='upper right')

            # make a plot and save it as png
            plt.plot(data=plot)
            plt.savefig("{}.png".format(data_selected))


file = sys.argv[1]
columns = sys.argv[2:]

plot_pdf_csv(file, columns)
