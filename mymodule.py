from urllib.request import urlopen
import json

api_key = "xxxxxxx"

def get_weather(city):
    sock = urlopen("http://api.openweathermap.org/data/2.5/weather?q=" +
                           city + "&appid=" + api_key)
    result = sock.read()
    sock.close()
    weather = json.loads(result)
    return weather["main"["temp"] -273.15

def postal_lookup(postal_code):
    sock = urlopen("http://api.postcodes.io/postcodes/" +
                           postal_code)
    result = sock.read()
    sock.close()
    details = json.loads(result)
    return (details["result"]["latitude"], details["result"]["longtitude"]
                   
if__name__=="__main__":
    degrees = get_weather("OSLO")
    print("weather in Oslo is %.2f dedgrees Celsius" % degrees)
    location = postal_lookup("B323PP")
    print(location)
           
