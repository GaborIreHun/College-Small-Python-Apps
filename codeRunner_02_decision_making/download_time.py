
file_size = float(input("Enter the file size in MB: "))

connection_speed = float(input("Enter the connection speed in Mbps: "))

time = (file_size * 8.388608) / connection_speed

print(f"Download time is {time:.2f} seconds")

if time < 60:
    print("Download will take less than a minute")
elif time < 300:
    print("Download will take less than 5 minutes")
else:
    print("Too long to download")
