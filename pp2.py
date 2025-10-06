temperature = float(input("Enter the temperature (in °C): "))

if temperature >= 30:
    print("Hot")
elif temperature >= 15:
    print("Normal")
else:
    print("Cold")