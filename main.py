import requests

url = "https://truecaller4.p.rapidapi.com/api/v1/getDetails"

querystring = {"phone":"<REQUIRED>","countryCode":"<REQUIRED>"}

headers = {
	"X-RapidAPI-Key": "YOurKey",
	"X-RapidAPI-Host": "truecaller4.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())