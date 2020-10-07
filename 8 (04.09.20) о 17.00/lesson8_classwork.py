# Example. With a free OWM API Key (work code): 

# from pyowm import OWM

# owm = OWM('1250f5d30b063ec8a638c3e8ac131b17')  # You MUST provide a valid API key

# # Search for current weather in London (Great Britain)
# mgr = owm.weather_manager()
# observation = mgr.weather_at_place('London,GB')
# w = observation.weather
# print(w)                  # <Weather - reference time=2013-12-18 09:20, status=Clouds>

# # Weather details
# w.wind()                  # {'speed': 4.6, 'deg': 330}
# w.humidity                # 87
# w.temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = mgr.weather_around_coords(-22.57, -43.12)

################################################# 

# # code from the presentation (species, work code):
# # cmd: pip install pyowm​

# import pyowm

# # city = input("What city you are interested: ")

# owm = pyowm.OWM('1250f5d30b063ec8a638c3e8ac131b17')
# mgr = owm.weather_manager()
# # You MUST provide a valid API key​
# # Have a pro subscription? Then use:​
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')​
# # Search for current weather in the city​
# observation = mgr.weather_at_place("London")
# w = observation.weather
# temperature = w.temperature('celsius') #['temp']
# # print("In London is the temperature of the air" + " " + str(temperature) + " for the Celsius")
# print(f"Min temperature {w.temperature('celsius')['temp_min']}")
# print(f"Max temperature {temperature['temp_max']}")
# print(f"Temperature {temperature['temp_max']}")
# print(temperature)
# # print("In this city "+ w.detailed_status())
# print(w.detailed_status)

##################################################

# import pyowm

# city = input("What city you are interested:")
# owm = pyowm.OWM('1250f5d30b063ec8a638c3e8ac131b17')    

# mgr = owm.weather_manager()
# observation = mgr.weather_at_place(city)
# w = observation.weather
# temperature = w.temperature('celsius')

# print(f"Min temperature {w.temperature('celsius')['temp_min']}")
# print(f"Max temperature {temperature['temp_max']}")
# print(f"Temperature {temperature['temp']}")
# print(temperature)

# # print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
# print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature['temp']) + " for the Celsius")
# print("In this city "+ w.detailed_status)
# # print(w.detailed_status)

################################################# 

# Python has a built-in package called re, which can be used to work with Regular Expressions.
# import re

# result_1 = re.match(r'IT', 'IT Academy SoftServe')
# result_2 = re.match(r'Academy', 'IT Academy SoftServe')
# print(result_1)
# print(result_1.group(0))
# print(result_2)

################################################# 
# Returns a Match object if there is a match anywhere in the string.​
# import re

# result = re.search(r"Academy", 'IT Academy SoftServe')
# print(result)
# print(result.group(0))

#################################################
# Returns a list containing all matches.​
# import re

# result = re.findall(r"IT", 'IT Academy SoftServe IT IT')
# print(result)

###############################################
# Returns a list where the string has been split at each match.​
# import re
# result_1 = re.split(r"em", "IT Academy SoftServeITemIT")
# result_2 = re.split(r"e", "IT Academy SoftServeIT IT")
# result_3 = re.split(r"e", "IT Academy SoftServeIT IT", maxsplit = 2)
# print(result_1)
# print(result_2)
# print(result_3)

#############################################
# Replaces one or many matches with a string.​
# import re

# result_1 = re.sub('e', '9', 'IT Academy SoftServeITemIT')
# result_2 = re.sub('e','@','IT Academy SoftServeIT IT', 2)
# print(result_1)
# print(result_2)

###############################################

# Write a Python program to check the validity of a password (input from users).​
# Validation :​
# At least 1 letter between [a-z] and 1 letter between [A-Z].​
# At least 1 number between [0-9].​
# At least 1 character from [$#@].​
# Minimum length 6 characters.​ 
# Maximum length 16 characters.

###########################################################

import re

user_password = input('Enter your password: ')

while True:

    condition_1 = re.findall('[a-z]', user_password)
    condition_2 = re.findall("[A-Z]", user_password)
    condition_3 = re.findall('\d', user_password)
    condition_4 = re.findall('$|#|@', user_password)
    condition_5 = 5 < len(user_password) < 17

    if condition_1 and condition_2 and condition_3 and condition_4 and condition_5:
        print("The password is appropriate")
        # return "The password is appropriate"
        break
    else:
        user_password = input('Enter your password again: ')
        condition_1 = re.findall('[a-z]', user_password)
        condition_2 = re.findall("[A-Z]", user_password)
        condition_3 = re.findall('\d', user_password)
        condition_4 = re.findall('$|#|@', user_password)
        condition_5 = 5 < len(user_password) < 17

#########################

# import re

# def passValidator (passCheck):
#     if  re.search(r"[a-z]", passCheck) \
#         and re.search(r"[A-Z]", passCheck) \
#         and re.search('$|#|@', passCheck) \
#         and 5 < len(passCheck) < 17:
#         return "The password is appropriate"
#     else:
#         new_try = input('Enter valid pass: ')
#         passValidator(new_try)


#import passValidator
#passValidator.passValidator("qweQWE123@")