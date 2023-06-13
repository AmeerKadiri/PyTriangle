highway_number = input("Enter the highway number: ")
direction = ""
if 1 <= int(highway_number) <= 99:
    direction = "east/west"
elif 100 <= int(highway_number) <= 999:
    direction = "north/south"
else:
    direction = "unknown"
    
print("I-" + highway_number + " is primary, going " + direction)
