import requests

url = 'https://www.w3schools.com/python/'
response = requests.get(url)

print("Status Code:", response.status_code)
print("Content:")
print(response.text[:500]) 