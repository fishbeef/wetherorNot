#Create a random python function that will produce findings in sonarqube
#This is a test file to see if sonarqube will pick up the findings
#This file is not used in the application

import random

def random_function():
    """This function will produce a random number between 1 and 10"""
    return random.randint(1, 10)

def main():
    """Main function"""
    print(random_function())    #This is a print statement

if __name__ == "__main__":
    main()

#This is a comment
