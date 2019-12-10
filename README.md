# Project: StarWar Characters

StarWar Characters is an application which reads star wars characters details from an API and prints them to a CSV file.

## Import Library
Import requests http library using below:

```bash
import requests
```
## Folder structure and Files
```bash
UnitTests
  |-- unitTest.py
api
  |-- apiHelper.py
file
  |-- csv.py
star_war_characters
  |--starWarCharacter.py
main.py

```
## File Details

```bash
unitTest.py
def test_verify_api_response(self)
```
#Perform unit test to check if page is returning empty response
#self is used for class initilization

```bash
append_to_file(filepath,name,height,gender)
```
#outputs starwar character's name, height and gender to CSV file
#filepath - destination file location on server
#name - Name of starwar character
#height - Height of starwar character
#gender - Gender of starwar character

## Usage (Example)
Call above functions from main function
```
star_wars_characters(self,1) #reads data from 1st page

append_to_file('c:\\','Luke Skywalker','172','male')
```
