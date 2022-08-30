import urllib.request, urllib.parse, urllib.error
import json
import ssl
import datetime as dt                   #libraries
from pytz import timezone
import pandas as pd
import requests
import holidays
import os

ctx = ssl.create_default_context()
ctx.check_hostname = False               #Certificate
ctx.verify_mode = ssl.CERT_NONE

tz = timezone("US/Eastern")             
date_time = dt.datetime.now(tz)         #setting time zones
year = date_time.year

def getQuote():
  quotesApi = 'http://quotes.rest/qod.json'
  quotesData = json.loads(urllib.request.urlopen(quotesApi, context=ctx).read())
  quote = quotesData['contents']['quotes'][0]['quote']
  author = quotesData['contents']['quotes'][0]['author']             #Get the daily quote
  fQuote= '\"' +quote+'\"' + " - " + author
  return fQuote
  
def getWeather(location):
  weatherApi = 'http://api.weatherapi.com/v1/forecast.json?' 
  weatherApiKey = #your api key
  fUrl = weatherApi + urllib.parse.urlencode({'key': weatherApiKey, 'q': location, 'alerts': 'yes'})
  weatherData = json.loads(urllib.request.urlopen(fUrl, context=ctx).read())                           #get the current weather
  weatherCondition = weatherData['current']['condition']['text']                    
  high = float(weatherData['forecast']['forecastday'][0]['day']['maxtemp_f'])
  low = float(weatherData['forecast']['forecastday'][0]['day']['mintemp_f'])
  temp = str(weatherData['current']['temp_f'])
  alerts = []
  [alerts.append((weatherData['alerts']['alert'][i]['desc'].split('...')[1]).upper()) for i  in range(0, len(weatherData['alerts']['alert'])) if (weatherData['alerts']['alert'][i]['desc'].split('...')[1]).upper() not in alerts]
  pic= urllib.request.urlretrieve('http:'+weatherData['current']['condition']['icon'],'img.png')
  icon = 'img.png'
  return weatherCondition,temp,high,low, alerts,icon

def getRecommendation(temp):
  if temp <= 40:
    return recommendations['Coat'],
  elif temp > 40 and temp <= 55:
    return recommendations['Thick_Hoodie']
  elif temp > 55 and temp <= 60:
    return recommendations['Hoodie']
  elif temp > 60 and temp <= 70:
    return recommendations['Light_Hoodie']
  elif temp > 70 and temp <= 80:                              # Give suggestions
    return recommendations['No_Hoodie']
  elif temp > 80 and temp <= 90:
    return recommendations['Light_Clothing']
  elif temp > 90:
    return recommendations['Danger']
  
def sendText(msg,image,user):
  apiToken = #your api token
  apiKey = #your api key                                         #Sending text
  r = requests.post("https://api.pushover.net/1/messages.json", data = {     
  "token": apiToken,
  "user": apiKey,
  "message": msg,
  "device":user
  }, 
  files = {
  "attachment": (image, open(image, "rb"), "image/jpeg")
  })
  
  return r.text
  
manager = #creater                                

allUsers = {
  #username : {
    'Location' : {
      'Home': #Home Location,
      'School': #School Location
    },
    'Important Dates' : {
      dt.date(year, 5, 25) : 'Happy Birthday!',
      'School Breaks' : 
        pd.date_range(start=str(year)+'-11-24',end=str(year)+'-11-27').astype(str).tolist()+ #Thanksgiving Break
        pd.date_range(start=str(year)+'-12-21',end=str(year)+'-12-31').astype(str).tolist()+ #Christmas break
        pd.date_range(start=str(year)+'-1-1',end=str(year)+'-1-16').astype(str).tolist()+ #New Years Break
        pd.date_range(start=str(year)+'-3-11',end=str(year)+'-3-19').astype(str).tolist()+ #Spring Break
        pd.date_range(start=str(year)+'-5-11',end=str(year)+'-8-28').astype(str).tolist() #Summer Break
      ,
      dt.date(year, 9, 6): 'Today is the start of the Fall semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 12, 23):'Today is the end of the Fall semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 1, 17):'Today is the start of the Spring semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 5, 10): 'Today is the end of the Spring semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 12, 16): 'Good Luck on finals, You Got this',
      dt.date(year, 5, 4): 'Good Luck on finals, You Got this'
    }
  },

   #username : {
    'Location' : {
      'Home': #Home Location,
      'School': #School Location
    },
    'Important Dates' : {
      dt.date(year, 5, 25) : 'Happy Birthday!',
      'School Breaks' : 
        pd.date_range(start=str(year)+'-11-24',end=str(year)+'-11-27').astype(str).tolist()+ #Thanksgiving Break
        pd.date_range(start=str(year)+'-12-21',end=str(year)+'-12-31').astype(str).tolist()+ #Christmas break
        pd.date_range(start=str(year)+'-1-1',end=str(year)+'-1-16').astype(str).tolist()+ #New Years Break
        pd.date_range(start=str(year)+'-3-11',end=str(year)+'-3-19').astype(str).tolist()+ #Spring Break
        pd.date_range(start=str(year)+'-5-11',end=str(year)+'-8-28').astype(str).tolist() #Summer Break
      ,
      dt.date(year, 9, 6): 'Today is the start of the Fall semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 12, 23):'Today is the end of the Fall semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 1, 17):'Today is the start of the Spring semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 5, 10): 'Today is the end of the Spring semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 12, 16): 'Good Luck on finals, You Got this',
      dt.date(year, 5, 4): 'Good Luck on finals, You Got this'
    }
  },
  
  #username : {
    'Location' : {
      'Home': #Home Location,
      'School': #School Location
    },
    'Important Dates' : {
      dt.date(year, 5, 25) : 'Happy Birthday!',
      'School Breaks' : 
        pd.date_range(start=str(year)+'-11-24',end=str(year)+'-11-27').astype(str).tolist()+ #Thanksgiving Break
        pd.date_range(start=str(year)+'-12-21',end=str(year)+'-12-31').astype(str).tolist()+ #Christmas break
        pd.date_range(start=str(year)+'-1-1',end=str(year)+'-1-16').astype(str).tolist()+ #New Years Break
        pd.date_range(start=str(year)+'-3-11',end=str(year)+'-3-19').astype(str).tolist()+ #Spring Break
        pd.date_range(start=str(year)+'-5-11',end=str(year)+'-8-28').astype(str).tolist() #Summer Break
      ,
      dt.date(year, 9, 6): 'Today is the start of the Fall semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 12, 23):'Today is the end of the Fall semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 1, 17):'Today is the start of the Spring semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 5, 10): 'Today is the end of the Spring semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 12, 16): 'Good Luck on finals, You Got this',
      dt.date(year, 5, 4): 'Good Luck on finals, You Got this'
    }
  },
   #username : {
    'Location' : {
      'Home': #Home Location,
      'School': #School Location
    },
    'Important Dates' : {
      dt.date(year, 5, 25) : 'Happy Birthday!',
      'School Breaks' : 
        pd.date_range(start=str(year)+'-11-24',end=str(year)+'-11-27').astype(str).tolist()+ #Thanksgiving Break
        pd.date_range(start=str(year)+'-12-21',end=str(year)+'-12-31').astype(str).tolist()+ #Christmas break
        pd.date_range(start=str(year)+'-1-1',end=str(year)+'-1-16').astype(str).tolist()+ #New Years Break
        pd.date_range(start=str(year)+'-3-11',end=str(year)+'-3-19').astype(str).tolist()+ #Spring Break
        pd.date_range(start=str(year)+'-5-11',end=str(year)+'-8-28').astype(str).tolist() #Summer Break
      ,
      dt.date(year, 9, 6): 'Today is the start of the Fall semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 12, 23):'Today is the end of the Fall semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 1, 17):'Today is the start of the Spring semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 5, 10): 'Today is the end of the Spring semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 12, 16): 'Good Luck on finals, You Got this',
      dt.date(year, 5, 4): 'Good Luck on finals, You Got this'
    }
  },
  
   #username : {
    'Location' : {
      'Home': #Home Location,
      'School': #School Location
    },
    'Important Dates' : {
      dt.date(year, 5, 25) : 'Happy Birthday!',
      'School Breaks' : 
        pd.date_range(start=str(year)+'-11-24',end=str(year)+'-11-27').astype(str).tolist()+ #Thanksgiving Break
        pd.date_range(start=str(year)+'-12-21',end=str(year)+'-12-31').astype(str).tolist()+ #Christmas break
        pd.date_range(start=str(year)+'-1-1',end=str(year)+'-1-16').astype(str).tolist()+ #New Years Break
        pd.date_range(start=str(year)+'-3-11',end=str(year)+'-3-19').astype(str).tolist()+ #Spring Break
        pd.date_range(start=str(year)+'-5-11',end=str(year)+'-8-28').astype(str).tolist() #Summer Break
      ,
      dt.date(year, 9, 6): 'Today is the start of the Fall semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 12, 23):'Today is the end of the Fall semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 1, 17):'Today is the start of the Spring semester, Good Luck! Work Hard! and Have Fun!!!',
      dt.date(year, 5, 10): 'Today is the end of the Spring semester, I know you worked hard and I am VERY proud of you!!!',
      dt.date(year, 12, 16): 'Good Luck on finals, You Got this',
      dt.date(year, 5, 4): 'Good Luck on finals, You Got this'
    }
  }
}

holidays = holidays.UnitedStates(years=year)

recommendations = {
  'Coat' : ['Its a very cold out! So I recommend wearing a coat! Consider adding multiple layers under'], # below 40
  'Thick_Hoodie' : ['Its very chilly out! So I recommend a thick Hoodie, You may need to add a Jacket later on'], #40 - 55 
  'Hoodie' : ['It not too chilly out, So I recommend a moderate to light hoodie'], #55 - 60
  'Light_Hoodie' : ['Its a moderate temperature outside, So I recommend a super light hoodie'], #60 - 70
  'No_Hoodie' : ['Its a little Hot, So I recommend not wearing a hoodie or any additional clothing.\n\nStay Hydrated!'], #70 - 80
  'Light_Clothing' : ['Its Hot, So I recommend keeping ALL clothing light!\n\nStay Hydrated!!'], #80 - 90
  'Danger' : ['Its very Hot! So I recommend Avoiding the outdoors if possible!\n\nSTAY HYDRATED!!!!']#above 90 
}

validHours = range(8,22)

if date_time.hour == 7 and date_time.minute <= 2: 
    
  try:
    for user in allUsers:
      
      if str(date_time.date()) in allUsers[user]['Important Dates']['School Breaks']:
        location = allUsers[user]['Location']['Home']
        
      else:
        location = allUsers[user]['Location']['School']
         
      quote = getQuote()
      print('Got the quote')

      weather = getWeather(location)
      weatherCondition = weather[0]
      temp = weather[1]
      high = weather[2]
      low = weather[3]
      alerts = "\n\n".join(weather[4])
      if len(alerts) == 0:
        alerts = 'None'
      image = weather[5]
      print('got the weather')
      
      morningMsg = f'Good Morning\n\nHope you slept well!\n\nIt is currently {weatherCondition} and {temp} degrees in {location}!\n\nToday is gonna have a high of {high} degrees and a low of {low} degrees\n\n\nWeather Alerts:\n{alerts}\n\nRemember,\n{quote}\n\nHave A Great Day!\n\n'

      sentText = sendText(morningMsg,image,user)
      print('Sent Morning Text to:',user)
      os.remove("img.png")

      if date_time.date() in allUsers[user]['Important Dates']:
        remeinderTxt = sendText(allUsers[user]['Important Dates'][date_time.date()],'heart.jpg',user)
        print('Sent remeinder text to:', user)

      if date_time.date() in holidays: 
        holidayMessage = f'Its {holidays[date_time.date()]}'
        holidayTxt = sendText(holidayMessage,'celebration.jpg',user)
        print('Sent Holiday Text to ',user)

      if date_time.date() == dt.date(2023, 8, 1):
        systemUpdateMessage = 'Its time to perform a System Update!'
        systemTxt = sendText(systemUpdateMessage,'smilling.jpg', manager)
  
  except:
    errorMsg = 'Something Went Wrong!'
    failDataCollection = sendText(errorMsg,'sadFace.png',manager)
    print('Sent Error Message')
    
elif date_time.hour == 22 and date_time.minute <= 2:
  for user in allUsers:
    nightMsg = f'Hey {user}\n\nHope you had a great day\n\n I know you worked hard today, now its time for bed\n\nHave a Great Night\n\nSweet Dreams\n\n'
    sentText = sendText(nightMsg,'night.jpg',user)
    print('Sent Night Message to: ', user)
  
elif date_time.hour in validHours and date_time.minute <= 2:
  for user in allUsers:
    
    if str(date_time.date()) in allUsers[user]['Important Dates']['School Breaks']:
      location = allUsers[user]['Location']['Home']
    
    else:
      location = allUsers[user]['Location']['School']
    
    weather = getWeather(location)
    weatherCondition = weather[0]
    temp = float(weather[1])
    alerts = "\n\n".join(weather[4])
    if len(alerts) == 0:
      alerts = 'None'
    image = weather[5]
    recommendation = getRecommendation(temp)
    hourlyWeatherMessage = f'Hope your day is going well!,\n\nIt is currently {weatherCondition} and {temp} degrees in {location}!\n\n{recommendation[0]}\n\n\nWeather Alerts:\n{alerts}\n\n'
    sentText = sendText(hourlyWeatherMessage,image,user)
    print('Sent Weather to ',user)
    os.remove("img.png")


    




