import requests
import json
import pandas as pd
import mock_data

url = "https://hellofresh-au.free.beeceptor.com/menus/2021-W10/classic-box"

s3_bucket = './s3_bucket'

#Flattern the courses component of the json data for easy transformations
def flattern_course_data(course_list,week):
	df = pd.json_normalize(course_list,sep = '_')
	
	#To judge top 10 recipes take the average of the recipy ranking from both ['recipe_ratingsCount','recipe_favoritesCount'] columns
	df[['recipe_ratingsCount_perctile','recipe_favoritesCount_perctile']] = df[['recipe_ratingsCount','recipe_favoritesCount']].rank()/len(df)
	df['final_rank'] =  ((df['recipe_favoritesCount_perctile'] + df['recipe_ratingsCount_perctile'])/2).rank()
	df = df.sort_values(by = 'final_rank',ascending = False)
	top_10_index = df.iloc[0:10,:].index
	top_10_df = df.loc[top_10_index,:] #collect only top 10 highest rated courses
	return df,top_10_df

def main(testing = False):
	if testing == False:
		response = requests.get(url)
		if response.status_code == 200:
			data = json.loads(response.content)
		else:
			print(f"request response code : {response.status_code}")
			print('Gracefully error out')
			zz
	else: #Collect mock data to prevent over calling the API
		data = mock_data.data 
	
	week = data['items'][0]['week'].replace('W','').replace('-','_') #Creates the date information later used for file naming
	course_list = data['items'][0]['courses']	
	
	df,top_10_df = flattern_course_data(course_list,week)

	if testing == False: 
		df.to_csv(path_or_buf = f'./s3_bucket/{week}_menu.csv',header = True)
		top_10_df.to_csv(path_or_buf = f'./s3_bucket/{week}_top_10.csv',header = True)
	else: #return csv's for unit testing
		return df,top_10_df

if __name__ == '__main__':
	main(testing = True)