# Exercise: Visualise Earthquake data from a csv file

# matplotlib import
import matplotlib.pyplot as plt

# an empty list for the earthquake magnitudes
magnitudes = []

# open the file (delivberately leaving out exception handling)
with open("earthquakes_2019.csv") as data_file:
    _ = data_file.readline() # discard the headers
    
    for line in data_file:
        #split the line into 5 variables
        # maxsplit leaves the last column in a single variable
        # this avoids the complication of the place containing commas
        time_string, latitude, longitude, magnitude, place = line.split(",",maxsplit=4)        
        
        # add to the list
        magnitudes.append(float(magnitude))

# Create the figure and axes

# Set the title for the figure

# 1 histogram    
# Set the title

# set the axis labels

# create a list for the histogram boundaries

# set the ticks on the x-axis
   
# Display a histogram of the patient numbers

# 2. Box plot
# Set the title

# set the axis labels

# Display a box plot of the patients numbers

# 3. Violin plot 
# Set the title

# set the axis labels

# Display a box plot of the patients numbers

# show the plot

# save the plot

