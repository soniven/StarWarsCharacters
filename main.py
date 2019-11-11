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

#Append results into CSV file
def append_to_file(filepath,name,height,gender):
  f = open(filepath +"star_wars_characters.csv", "a")
  f.write(name+','+height+','+gender )
  f.write('\n')
  f.close() 

#main function
if __name__=="__main__": 
  a = ApiHelper() #ApiClass Object 
  arrayLen = 1 
  i = 1
  append_to_file("C:\\",'Name','Height','Gender')
  print("Start fetching data..")
  while arrayLen > 0:
    starWarChrsList = a.star_wars_characters(i)
    arrayLen = len(starWarChrsList)
    for starwar_chrs in starWarChrsList:    
        append_to_file("C:\\",starwar_chrs.name,
        starwar_chrs.height,
        starwar_chrs.gender )
    i += 1
  print("Completed..!!")