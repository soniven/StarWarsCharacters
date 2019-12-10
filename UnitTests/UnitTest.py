import unittest
from api.apiHelper import ApiHelper

class UnitTest(unittest.TestCase):

	def test_verify_api_response(self):
		response_object = ApiHelper()
		fetch_list_length = 1
		page_no = 1

		while fetch_list_length > 0:
			fetch_list = response_object.star_wars_characters_list(page_no)
			fetch_list_length = len(fetch_list)
			print("Checking page number : " + str(page_no) + " -> This is a non empty list")
			page_no+=1

if __name__=="__main__":
	unittest.main()
