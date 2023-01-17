import math
power = float(input("Enter the power: "))
resistance = float(input("Enter the resistance: "))
voltage = math.sqrt(power*resistance)
print(f"Voltage is {voltage:.1f}")