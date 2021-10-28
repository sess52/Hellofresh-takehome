import unittest
import retreive_recipies 

class Test_retrieve_recipies(unittest.TestCase):
	def setUp(self):
		self.df,self.top_10_df = retreive_recipies.main(testing = True)
		print('setupClass')

	def tearDown(self):
		print('tearDownClass')

	def test_files_is_not_empty(self):
		self.assertTrue(len(self.df)!= 0)
		self.assertTrue(len(self.top_10_df) != 0)

	def test_file_length(self):
		self.assertTrue(len(self.top_10_df) == 10)

	def test_file_width(self):
		self.assertTrue(len(self.df.columns) != 0)
		self.assertTrue(len(self.top_10_df.columns) != 0)