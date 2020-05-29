import requests
from geopy.geocoders import Nominatim

class getWeather:
        def __init__(self, city):
                self.appid = '5d9d9f7178756dbc78d68958da985841'
                self.city = city

        def weather_data(self, lantitude, lontitude):
                try:
                        res = requests.get('https://api.openweathermap.org/data/2.5/onecall?lat=' + str(lantitude) + '&lon=' + str(lontitude) + '&exclude=hourly,daily&lang=ru&units=metric&appid=' + self.appid)
                        data = res.json()
                        lstData = [data['lat'], data['lon'], data['timezone'], data['current']['temp'], data['current']['pressure'],
                              data['current']['humidity'], data['current']['clouds'], data['current']['wind_speed'],
                              data['current']['wind_deg'], data['current']['weather'][0]['description']]
                        return lstData
                except Exception as e:
                        return False
		
        def geo_location(self):
                try:
                        locator = Nominatim (user_agent = 'myGeocoder')
                        location = locator.geocode (self.city)
                        return self.weather_data(location.latitude, location.longitude)
                except Exception as e:
                        return False
