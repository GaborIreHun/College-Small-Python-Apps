# Matplotlib Exercise: Bar chart of web server market share

# Import matplotlib here
import matplotlib.pyplot as plt
# Create an empty dictionary data
# (key is the developer, value is the percentage share)
data = {}

# Open data file
with open("webservers_202211.csv") as data_file:   
    # Read the first line
    _ = data_file.readline()
    
    # For each other line in data file
    for line in data_file:
        developer, share = line.split(",")

        # Convert the market share to float and insert in the dictionary
        data[developer] = float(share)

# Calculate remaining percentage
remaining = 100 - sum(data.values())
# Insert into the dictionary
data["Others"] = remaining

# Add code for the Pie Chart here
fig, ax = plt.subplots(figsize=(15, 10))

# Setting title
ax.set_title("Web Server Market Share - November 2022")

# Plotting
ax.pie(data.values(), labels=data.keys(), autopct="%.f%%")

fig.show()

# Saving chart
fig.savefig("Web_Server_Market_Share.png")