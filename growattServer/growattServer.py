import getpass
import growattServer

#Prompt user for username
username=input("Enter username:")

#Prompt user to input password
user_pass=getpass.getpass("Enter password:")

api = growattServer.GrowattApi()
login_response = api.login(<username>, <user_pass>)
#Get a list of growatt plants.
print(api.plant_list(login_response['user']['id']))