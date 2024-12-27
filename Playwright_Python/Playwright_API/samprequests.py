import requests
url = "https://reqres.in//api/users?page"
response = requests.get(url=url)
#print(response)
#print(response.status_code)
#Sprint(response.headers)
#print(response.request.headers)
#print(response.content)
print(response.text)