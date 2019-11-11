# Project: StarWar Characters

StarWar Characters is an application which reads star wars characters details from an API and prints them to a CSV file.

## Import Library
Import requests http library using below:

```bash
import requests
```
## Function Definitions

```bash
star_wars_characters(self,page_nr)
```
#retrieves data from specified page number
#self is used for class initilization
#page_nr is an argument to set Page Number 
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
