import datetime

earthquakes = {}

with open("earthquakes_2021.csv", "r", encoding="utf-8") as infile:

    infile.readline()

    for line in infile:

        date_string, latitude, longitude, depth, magnitude = line.strip().split(",")

        datetime_object = datetime.datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%fZ")

        earthquakes[datetime_object] = float(magnitude)

    print("Number of earthquakes:", len(earthquakes))

    print("Largest earthquake: {} with magnitude {}".format(max(earthquakes, key=earthquakes.get), max(earthquakes.values())))

    print("Most recent earthquake: {} with magnitude {}".format( max(earthquakes), earthquakes.get(max(earthquakes))))

    print("Least recent earthquake: {} with magnitude {}".format(min(earthquakes), earthquakes.get(min(earthquakes))))

    print("Time difference:", max(earthquakes) - min(earthquakes))