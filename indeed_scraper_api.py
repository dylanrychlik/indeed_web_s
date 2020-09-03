import selenium
import json
import requests
from dictionaries import Dict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def AWS():
    return "AWS"
def GCP():
    return "GCP"
def Azure():
    return "Azure"
def Snowflake():
    return "Snowflake"
def Oracle():
    return "Oracle"
def SQLServer():
    return "SQLServer"
def mySQL():
    return "mySQL"
def Java():
    return "Java"
def Python():
    return "Python"
def CPlusPlus():
    return "C++"
def Spark():
    return "Spark"
def Hadoop():
    return "Hadoop"
def Tensorflow():
    return "Tensorflow"
def R():
    return "R"
def Sagemaker():
    return "Sagemaker"
def default():
    return "Invalid Entry"

switcher = {
    '1': AWS,
    '2': GCP,
    '3': Azure,
    '4': Snowflake,
    '5': Oracle,
    '6': SQLServer,
    '7': mySQL,
    '8': Java,
    '9': Python,
    '10': CPlusPlus,
    '11': Spark,
    '12': Hadoop,
    '13': Tensorflow,
    '14': R,
    '15': Sagemaker
    }

def Alabama():
    return "Alabama"
def Alaska():
    return "Alaska"
def Arizona():
    return "Arizona"
def Arkansas():
    return "Arkansas"
def California():
    return "California"
def Connecticut():
    return "Connecticut"
def Delaware():
    return "Delaware"
def Florida():
    return "Florida"
def Goergia():
    return "Goergia"
def Hawaii():
    return "Hawaii"
def Idaho():
    return "Idaho"
def Iliinois():
    return "Iliinois"
def Indiana():
    return "Indiana"
def Iwoa():
    return "Iwoa"

def Kansas():
    return "Kansas"
def Kentucky():
    return "Kentucky"
def Maine():
    return "Maine"
def Maryland():
    return "Maryland"
def Massachusetts():
    return "Massachusetts"
def Michigan():
    return "Michigan"
def Minnensota():
    return "Minnensota"
def Mississippi():
    return "Mississippi"
def Missouri():
    return "Missouri"
def Montana():
    return "Montana"
def Nevada():
    return "Nevada"
def NewHampsire():
    return "NewHampsire"

def NewMexico():
    return "NewMexico"
def NewYork():
    return "NewYork"
def NorthCarolina():
    return "NorthCarolina"
def NorthDakota():
    return "NorthDakota"
def Ohio():
    return "Ohio"
def Oklahoma():
    return "Oklahoma"
def Oregon():
    return "Oregon"
def Pennslyvania():
    return "Pennslyvania"
def RhodeIsland():
    return "RhodeIsland"
def SouthCarolina():
    return "SouthCarolina"
def SouthDakota():
    return "SouthDakota"
def Tennessee():
    return "Tennessee"
def Texas():
    return "Texas"
def Utah():
    return "Utah"
def Vermont():
    return "Vermont"
def Virginia():
    return "Virginia"
def Washington():
    return "Washington"
def WestVirginia():
    return "WestVirginia"
def Wisconsin():
    return "Wisconsin"
def Wyoming():
    return "Wyoming"


switcher2 = {
    '1': Alabama,
    '2': Alaska,
    '3': Arizona,
    '4': Arkansas,
    '5': California,
    '6': Connecticut,
    '7': Delaware,
    '8': Florida,
    '9': Goergia,
    '10': Hawaii,
    '11': Idaho,
    '12': Iliinois,
    '13': Indiana,
    '14': Iwoa,
    '15': Kansas,
    '16': Kansas,
    '17': Maryland,
    '18': Maine,
    '19': Maryland,
    '20': Massachusetts,
    '21': Michigan,
    '22': Minnensota,
    '23': Mississippi,
    '24': Missouri,
    '25': Montana,
    '26': Nevada,
    '27': NewHampsire,
    '28': NewMexico,
    '29': NewYork,
    '30': NorthCarolina,

    '31': NorthDakota,
    '32': Ohio,
    '33': Oklahoma,
    '34': Oregon,
    '35': Pennslyvania,
    '36': RhodeIsland,
    '37': SouthCarolina
,
    '38': SouthDakota,
    '39': Tennessee,
    '40': Texas,
    '41': Utah,
    '42': Vermont,
    '43': Virginia,
    '44': Washington,
    '45': WestVirginia,

    '46': Wisconsin,
    '47': Wyoming,
    '48': Arizona,
    '49': Arkansas,
    '50': California,
    }

def switch(Language):
    return switcher.get(Language, default)()

def switch2(State):
    return switcher2.get(State, default)()


def state_menu():
   state = ''
   print("Welcome to the indeed loader/web scrapper. \n Please choose from the following states:" )
   value = input("\n 1). Alabama \n 2). Alaska \n 3). Arizona \n 4). Arkansas \n 5). California \n 6). Connecticut \n 7). Delaware \n 8). Florida \n 9). Goergia \n 10). Hawaii \n 11). Idaho \n 12). Iliinois \n 13). Indiana \n 14). Iwoa \n 15). Kansas \n 16). New Hampsire \n 17). Massasschutes")
   
   state = switch2(value)
   
   return state

def language_menu():
   language = ''
   print("Welcome to the indeed loader/web scrapper. \n Please choose from the following languages:" )
   value = input("\n 1). AWS \n 2). GCP \n 3). Azure \n 4). Snowflake \n 5). Oracle \n 6). SQL Server \n 7). mySQL \n 8). Java \n 9). Python \n 10). C++ \n 11). Spark \n 12). Hadoop \n 13). Tensorflow \n 14). R \n 15). Sagemaker")
   print(value)
   language = switch(value)
   print(language)
   return language


language = language_menu()

state = state_menu()
#opens google chrome using the chrome driver
browser = webdriver.Chrome(executable_path="C:\\Users\\dylan\\Documents\\chromedriver.exe")
#load indeed.com
browser.get('http://www.indeed.com')
assert 'Indeed' in browser.title
#does a search for 'Python developer'
elem = browser.find_element_by_name('q')  # Find the search box
elem.send_keys(language, Keys.TAB,state,Keys.RETURN )

print('Sucess!')

#Commentted out webscrapping
#print the data
# #url = 'https://www.indeed.com/rpc/jsunload?tk=1eh5fa930p74n800'
#search_params = ""

#test = requests.post("https://www.indeed.com/rpc/jsunload?tk=1eh5fa930p74n800", json=search_params).json()['d']
#print('Hello world')
#print('Test json post: ' + test.text)

#data = json.loads(requests.post(url, json=search_params).json()['d'])

#for result in data['Results']:
#  print(result['JobTitle'])
#  print(result['Company'])
#  print(result['Address'])
#  print('-' * 80)

#with open('restraunts.json', 'w', encoding='utf-8') as f:
    #json.dump(data, f, ensure_ascii=False, indent=4)










