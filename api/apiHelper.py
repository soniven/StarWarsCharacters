import requests

from star_war_characters.starWarCharacter import StarWarCharacter


def logs_args(func):
  def func_wrapper(*args):
    print args
    return func(*args)
  return func_wrapper

class ApiHelper(object):

  def fetch_API_response(self,page_number):
    #retrieve response
    self.api_url = "https://swapi.co/api/people"
    return requests.get(self.api_url, params={'page':page_number}).json()

  @logs_args
  def star_wars_characters_list(self,page_nr):
    # Returns a list (or generator)
    # of the name, height, and gender of each
    # Star Wars character
    api_object = ApiHelper()
    response_data = api_object.fetch_API_response(page_nr)

    starWarsCharactersList = []
    if response_data.get('results') != None :
      #if data is not empty, append to the list
      for starwar_character in response_data['results']:
        starWarsCharactersList.append(StarWarCharacter(starwar_character['name'], starwar_character['height'], starwar_character['gender']))
    return starWarsCharactersList
