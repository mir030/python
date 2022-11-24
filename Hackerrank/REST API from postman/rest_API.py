import requests
import json

"""Post Place"""

url = "https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123  "

payload = json.dumps({
  "location": {
    "lat": -38.383494,
    "lng": 33.427362
  },
  "accuracy": 50,
  "name": "Mir Karim",
  "phone_number": "(+91) 983 893 3937",
  "address": "29, side layout, cohen 09",
  "types": [
    "shoe park",
    "shop"
  ],
  "website": "http://google.com",
  "language": "French-IN"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
assert response.status_code == 200

response_dict = response.json()

print(response_dict)

place_id = response_dict["place_id"]


"""Get Place with the retrieved place ID"""

url = "http://rahulshettyacademy.com/maps/api/place/get/json?place_id=" + place_id + "&key=qaclick123"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200

print(response.text)

"""Put/update place"""

url = "http://rahulshettyacademy.com/maps/api/place/update/json?key=qaclick123"

address = "70 Summer walk, USA"

payload = json.dumps({
  "place_id": place_id,
  "address": address,
  "key": "qaclick123"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=payload)
assert response.status_code == 200

print(response.text)

response_dict = response.json()

assert response_dict["msg"] == "Address successfully updated"


"""Get updated place"""

url = "http://rahulshettyacademy.com/maps/api/place/get/json?place_id=" + place_id + "&key=qaclick123"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
assert response.status_code == 200

response_dict = response.json()

assert response_dict["address"] == address

print(response.text)

"Delete place"

url = "https://rahulshettyacademy.com/maps/api/place/delete/json?key=qaclick123"

payload = json.dumps({
  "place_id": place_id
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("DELETE", url, headers=headers, data=payload)
assert response.status_code == 200

print(response.text)
