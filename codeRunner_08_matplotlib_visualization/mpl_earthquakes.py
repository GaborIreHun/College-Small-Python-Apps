#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Program to visualise Earthquake data from a csv file
Example of: Visualisation with Matplotlib

@author: cormac
"""
import datetime

import matplotlib.pyplot as plt

# the dictionary will contain
# as key: a datetime object representing the date and time of the earthquake
# as value: the magnitude of the corresponding earthquake
earthquakes = {}

# open the file (deliberately leaving out exception handling)
with open("earthquakes_2019.csv") as data_file:
    _ = data_file.readline() # discard the headers
    
    for line in data_file:
        #split the line into 5 variables
        # maxsplit leaves the last column in a single variable
        # this avoids the complication of the place containing commas
        time_string, latitude, longitude, magnitude, place = line.split(",",maxsplit=4)
        
        when = datetime.datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S.%fZ")
        
        # insert into the dictionary
        earthquakes[when] = float(magnitude)


# visualisations

fig, axs = plt.subplots(1,3, figsize=(15,10))

fig.suptitle("Visualization of Earthquake Magnitudes")

# Creating Histogram

axs[0].set_title("Histogram")

axs[0].set_ylabel("Frequency")

bins = range(int(max(earthquakes.values())+2))

axs[0].set_xticks(bins)

axs[0].hist(earthquakes.values(),bins,ec="black")


# Creating Box Plot

axs[1].set_title("Box Plot")

axs[1].set_ylabel("Magnitudes")

axs[1].boxplot(earthquakes.values(), showmeans=True, meanline=True)


# Creating Violin Plot

axs[2].set_title("Violin Plot")

axs[2].set_ylabel("Magnitudes")

axs[2].violinplot(earthquakes.values(), showmeans=True)

fig.savefig("earthquake_visualization.png")


fig.show()
