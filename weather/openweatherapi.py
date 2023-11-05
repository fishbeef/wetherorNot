import requests
import json

#Access the openwaetherapi and save the data to a json file
# You need to replace the API key below with your own key
# You can get an API key for free by creating an account at https://openweathermap.org/
api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={e6cacbe1061120267aa6107d82f7b2bb}'
#api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid={e6cacbe1061120267aa6107d82f7b2bb}'

#Set the filename and path for the JSON file
json_file_path = '/Users/Boike/Dev/Growatt Python/PyPi_GrowattServer/weather/openweatherapi.json' #Replace this with the desired filename and path


try:
    #Sent a GET request to the API
    response = requests.get(api_url)

    #Check if the request was successful (status code 200)
    if response.status_code == 200:
        #Convert API response to JSON format
        data = response.json()


        #Save JSON data to a file
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f'Data successfully saved to {json_file_path}.')
    else:
        print(f'Error during the API call. Status code: {response.status_code}')

except Exception as e:
    print(f'Error during the API call. {e}')

#Read the JSON file and print the data
with open(json_file_path, 'r') as json_file:
    data = json.load(json_file)
    print(data)

#Print the temperature
print(data['main']['temp'])

# Print the tempetature for tomorrow
print(data['daily'][1]['temp']['day'])

