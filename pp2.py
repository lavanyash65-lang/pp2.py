temperature_c = float(input("Enter the temperature (in °C): "))
temperature_f = (temperature_c * 9/5) + 32

print(f"Equivalent Fahrenheit value: {temperature_f:.2f}°F")

if temperature_c >= 30:
    print("Hot")
elif temperature_c >= 15:
    print("Normal")
else:
    print("Cold")