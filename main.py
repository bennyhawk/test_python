import requests

response = requests.get("https://dummy.restapiexample.com/api/v1/employees")

print(response.json())
