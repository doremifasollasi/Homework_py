# import pyowm

# city=input("What city you are interested:")
# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    

# observation = owm.weather_at_place(city)
# w = observation.get_weather()
# temperature=w.get_temperature('celsius')

# print(f"Min temperature {w.get_temperature('celsius')['temp_min']}")
# print(f"Max temperature {temperature['temp_max']}")
# print(f"Temperature {temperature['temp']}")
# print(temperature)

# print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
# print("In this city "+ w.get_detailed_status())
# # print(w.get_detailed_status())

################################################# 

from pyowm import OWM

city=input("What city you are interested:")
owm = OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# Weather details
w.wind()                  # {'speed': 4.6, 'deg': 330}
w.humidity                # 87
w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# Search current weather observations in the surroundings of
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
observation_list = mgr.weather_around_coords(-22.57, -43.12)

###############################################

Write a Python program to check the validity of a password (input from users).​
Validation :​
At least 1 letter between [a-z] and 1 letter between [A-Z].​
At least 1 number between [0-9].​
At least 1 character from [$#@].​
Minimum length 6 characters.​
Maximum length 16 characters.