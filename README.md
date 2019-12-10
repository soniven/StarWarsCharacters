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
## File/Function Details
### UnitTest.py
```
test_verify_api_response(self)
```
1. Function to verify empty page response
2. self is used for class initilization

### apiHelper.py
```
logs_args(func)
```
1. Decorator for logging
2. Arguments Passed: Function
```
fetch_API_response(self,page_number)
```
1. Function to fetch API response
2. Arguments Passed: Page Number
```
@logs_args
  star_wars_characters_list(self,page_nr)
```
1. Returns a list (or generator) of the name, height, and gender of each Star Wars character
2. Argument Passed : Page Number

### csv.py
```
append_to_file(self,filepath,name,height,gender)
```
1. Append the 'name', 'height' and 'gender' of each Star Wars character to a csv file provided by 'filepath'
2. Argument Passed :
    -> filepath : path where csv file need to be stored
    -> name : name of starwar character
    -> height: height of starwar character
    -> gender: gender of starwar character

### starWarCharacter.py
```
def __init__(self, name=None, height=None, gender=None)
```
1. Object initilization
2. Arguments Passed : name, height and gender of starWar Character

### main.py
main python file 


