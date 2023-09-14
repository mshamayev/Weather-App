#Michelle Shamayev
#Weather App
import requests
import config

def getCoords():
   city_name = input("Enter City: ")
   state_code = input("Enter State: ")
   country_code = input("Enter Country: ")
   base_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit=1&appid={config.appid}"
   response = requests.get(base_url)
   data = response.json() 
   latitude = data[0]["lat"]
   longitude = data[0]["lon"]
   return (latitude, longitude)

def getWeather(lat,lon):
    base_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=imperial&appid={config.appid}"
    response = requests.get(base_url)
    data = response.json()
    temp = data['main']['temp']
    return temp


def main():
  lat,lon = getCoords()
  temp = getWeather(lat,lon)
  print("Temperature: ", temp)


     


          
if __name__ == "__main__":
    main()
