import requests

BASE = "http://127.0.0.1:5000/"

videos = [{"name": "parrot sings and flies across the room", "likes": 94, "views": 2042}]

print("get all:")
response = requests.get(BASE + "/videos")
print(response.json())

print("get:")
response = requests.get(BASE + "/videos/1")
print(response.json())

print("post:")
response = requests.post(BASE + "/videos/1", videos[0])
print(response.json())

print("post:")
response = requests.post(BASE + "/videos/1", videos[0])
print(response.json())

print("get:")
response = requests.get(BASE + "/videos/1")
print(response.json())

print("delete:")
requests.delete(BASE + "/videos/1")
print(response.json())

print("get:")
response = requests.get(BASE + "/videos/1")
print(response.json())

print("delete:")
requests.delete(BASE + "/videos/1")
print(response.json())
