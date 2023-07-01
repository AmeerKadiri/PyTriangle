def convert_to_centimeters(value, unit):
    if unit == "meters":
        return value * 100
    elif unit == "inches":
        return value * 2.54
    elif unit == "feet":
        return value * 30.48
    else:
        print("Invalid unit. Conversion not supported.")
        return 0.0

def convert_to_meters(value, unit):
    if unit == "centimeters":
        return value / 100
    elif unit == "inches":
        return value * 0.0254
    elif unit == "feet":
        return value * 0.3048
    else:
        print("Invalid unit. Conversion not supported.")
        return 0.0

def convert_to_inches(value, unit):
    if unit == "centimeters":
        return value / 2.54
    elif unit == "meters":
        return value / 0.0254
    elif unit == "feet":
        return value * 12
    else:
        print("Invalid unit. Conversion not supported.")
        return 0.0

def convert_to_feet(value, unit):
    if unit == "centimeters":
        return value / 30.48
    elif unit == "meters":
        return value / 0.3048
    elif unit == "inches":
        return value / 12
    else:
        print("Invalid unit. Conversion not supported.")
        return 0.0

value = float(input("Enter a value: "))
unit = input("Enter the unit (centimeters, meters, inches, feet): ")

centimeters = convert_to_centimeters(value, unit)
meters = convert_to_meters(value, unit)
inches = convert_to_inches(value, unit)
feet = convert_to_feet(value, unit)

print("Centimeters:", centimeters)
print("Meters:", meters)
print("Inches:", inches)
print("Feet:", feet)