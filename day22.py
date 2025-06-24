import argparse

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

parser = argparse.ArgumentParser(description="🌡️ Temperature Converter CLI Tool")

parser.add_argument("temperature", type=float, help="Temperature value to convert")
parser.add_argument("--to", choices=["celsius", "fahrenheit"], required=True, help="Convert to: celsius or fahrenheit")

args = parser.parse_args()

if args.to == "celsius":
    result = fahrenheit_to_celsius(args.temperature)
    print(f"{args.temperature}°F = {result:.2f}°C")
else:
    result = celsius_to_fahrenheit(args.temperature)
    print(f"{args.temperature}°C = {result:.2f}°F")
