#import requests library
import requests
#Define StarWarChars Class
class StarWarChrs(object):     
    def __init__(self, name=None, height=None, gender=None):
        self.name = name
        self.height = height
        self.gender = gender     

class ApiHelper:
  def star_wars_characters(self,page_nr):
  # Returns a list (or generator)
  # of the name, height, and gender of each
  # Star Wars character
    api = "https://swapi.co/api/people/?page="
    
    #form api url with page numbers
    url = api + str(page_nr)
    #retrieve data
    data = requests.get(url).json()
    starWarChrsList = []
    if data.get('results') != None :
      #if data is not empty, append to the list
      for starwar_chrs in data['results']:       
        starWarChrsList.append(StarWarChrs(starwar_chrs['name'],
        starwar_chrs['height'],starwar_chrs['gender']))
    return starWarChrsList

#main function
if __name__=="__main__": 
  a = ApiHelper() #ApiHelper Class Object
  arrayLen = 1 
  i = 1
  
  while arrayLen > 0:
    starWarChrsList = a.star_wars_characters(i)
    arrayLen = len(starWarChrsList)
    if(arrayLen > 0):
      print('Checking Page No:'+ str(i) +' This is Non Empty Array');
    i += 1
     
