

#Import the geocoder module
import subprocess

# Install the geocoder module
#subprocess.run(["pip", "install", "geocoder"])
#subprocess.run(["pip", "install", "sqlite3"])

import geocoder
import sqlite3

#Save the apikey for openweather encrypted in a file on the file system
#Import the cryptography module
from cryptography.fernet import Fernet

#Create a key for encryption
key = Fernet.generate_key()
print(key)

#Store the key in a file
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()

#Read the key from the file
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#Encrypt the apikey
#Create a variable with the apikey
apikey = 'e6cacbe1061120267aa6107d82f7b2bb'
#Convert the apikey to bytes
apikey_bytes = apikey.encode()
#Encrypt the apikey
f = Fernet(key)
encrypted = f.encrypt(apikey_bytes)
print(encrypted)




apikey4openweather = 'e6cacbe1061120267aa6107d82f7b2bb'

#Import the pyopenweather module

from pyopenweather.weather import Weather

weather = Weather(lat=37.34, long=-121.89, api_key='" + apikey4openweather + "')

#Get the longitude and latitude for my current location
g = geocoder.ip('me')
print(g.latlng)
#Display city name of my location
print(g.city)
#Display country name of my location
print(g.country)
#Display longitude of my location
print(g.lng)
#Store longitude in a variable with the name longitude
longitude = g.lng
#Store latitude in a variable with the name latitude
latitude = g.lat

weather2 = Weather(lat=latitude, long=longitude, api_key='e6cacbe1061120267aa6107d82f7b2bb')

print(weather2.temperature)

temperature = weather2.temperature
pressure = weather2.pressure
print(weather2.pressure)

#Create a sqlite database and store the weather data in the database

#Import the sqlite3 module


#define the path for the database file
path = 'weather.db'
#Use the path to create a connection to the database
conn = sqlite3.connect(path)


#Create a cursor object
c = conn.cursor()

#Check if the table weather exists and if not create the table
c.execute('''CREATE TABLE IF NOT EXISTS weather
             (date text, temp real, pressure real)''')

#Today's date as date text

#Get today's date
import datetime
today = datetime.date.today()
print(today)
#Convert today's date to text
today_text = today.isoformat()
print(today_text)

#Insert a row of data from the weather data into the table weather use the variable from above

c.execute("INSERT INTO weather VALUES ('" + today_text + ", " + temperature  + ", "  + pressure + '"')

#Save (commit) the changes
conn.commit()
#Check if the data was saved to the database
c.execute("SELECT * FROM weather")
print(c.fetchone())
#Close the connection
conn.close()


