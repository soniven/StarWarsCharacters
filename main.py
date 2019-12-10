from api.apiHelper import ApiHelper
from file.csv import ExportToCSV
import tempfile


class StarWars(object):
    if __name__ == "__main__":
        apiObject = ApiHelper()  # ApiClass Object
        page_no = 1  # Set page number to 1

        csv_file_object = ExportToCSV()  # CSV class object
        starwars_character_arrayLength = 1

        # Get temp directory details
        path_to_store_csv_file = tempfile.gettempdir()

        # Call function to create CSV file and write first line as column headings
        csv_file_object.append_to_file(path_to_store_csv_file, "Name", "Height", "Gender")

        while starwars_character_arrayLength > 0:
            starWarChrsList = apiObject.star_wars_characters_list(page_no)
            print("page_no : " + str(page_no))
            starwars_character_arrayLength = len(starWarChrsList)

            for starwar_chrs in starWarChrsList:
                csv_file_object.append_to_file(path_to_store_csv_file, starwar_chrs.name, starwar_chrs.height,starwar_chrs.gender)
                print "StarWar Character Details: ", starwar_chrs.name, starwar_chrs.height,starwar_chrs.gender
            page_no += 1
