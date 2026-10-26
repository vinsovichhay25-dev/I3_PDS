def celsius_to_fahrenheit(celsius, round_to=1):
    fahrenheit = (celsius * 9) / 5 + 32
    return round(fahrenheit, round_to)

def fahrenheit_to_celsius(fahrenheit, round_to=1):
    celsius = ((fahrenheit - 32) * 5) / 9
    return round(celsius, round_to)

# a. Conversion table
print(" °C  | °F")
print("-" * 5 + "+" + "-" * 5)

for temp in range(0, 101, 20):
    fahrenheit = celsius_to_fahrenheit(temp)
    print(f"{temp:4} | {fahrenheit}")

# b. Convert 98.6°F to Celsius
print(f"\n98.6°F converted to Celsius = {fahrenheit_to_celsius(98.6)}°C")

# c. Convert 37°C to Fahrenheit and back to Celsius
fahrenheit = celsius_to_fahrenheit(37)
celsius = fahrenheit_to_celsius(fahrenheit)

print(f"\n37°C converted to Fahrenheit = {fahrenheit}°F")
print(f"{fahrenheit}°F converted back to Celsius = {celsius}°C")

# d. Call one function with round_to=3
print(f"\n37°C converted to Fahrenheit (3 decimal places) = {celsius_to_fahrenheit(37, round_to=3)}°F")
