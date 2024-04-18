import requests

api_key = '505f575a3507e31e849fcdecb6936148'

city = 'Adelaide'

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = round(data['main']['temp']-273.15,2)
    desc = data['weather'][0]['description']
    print(f'{temp} \u00b0C with {desc}')
else:
    print('Error fetching weather data')
