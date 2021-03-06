import pandas as pd
import matplotlib.pyplot as plt;plt.rcdefaults()
import matplotlib as mpl
import numpy as np
import matplotlib.lines as mlines

#Test Data Lists Element
#entities = ['Entity1', 'Entity2', 'Entity3', 'Entity4', 'Entity5', 'Entity6','Entity7', 'Entity8', 'Entity9', 'Entity10']
#values = [1,20,13,21,5,22,7,23,9,20]

## New version arguments should be:
## 1) main_entity_name
## 2) article_name(probably plot title as well)
## 3) list of dictionaries of entities found keys(entity_label,count) e.g. [{'entity_label':"obama", 'count': 5},{'entity_label':"trump", 'count': 2}]
## 4) output_file_name (not including the .png that has to be appended here)
## 5) optionally, the number of the highest ranked entities (higher count). Leave this for last if there is time.
def visualize(main_entity_name, article_name, article_entities, output_name, bar_amount):
	#In Range of total pictures(png) to be made 
	for i in range(1,print_range+1):
		#Assign Superset figure(num) to pyplot
		plt.figure(i)
		#Implicitly make a dict , or else lists are fine too
		#dictionary = dict(zip(entities,values))
		dictionary = {}
		for entity in article_entities:
			dictionary[entity['entity_label']] = entity['count']
		#Initialize the pd. set with Values - Keys
		s = pd.Series(
			dictionary.values(),
			dictionary.keys()
		)
		mpl.rcParams['legend.numpoints'] = 1
		#remove the second legend marker
		
		#Set descriptions:
		plt.title("Entity Relation")
		plt.ylabel('Extracted Entities')
		plt.xlabel('Popularity', color='blue')

		#Set tick colors:
		ax = plt.gca()
		ax.tick_params(axis='x', colors='blue')
		ax.tick_params(axis='y', colors='purple')

		
		#Plot the data:
		my_colors = 'rgbkymc'  #red, green, blue, black, etc. palete
		
		#plot Horizontal Bar & Colors & Legend
		s.plot( 
			kind='barh', 
			color=my_colors,
			legend=True,
		)
		#MAX RANKED ENTITY
		max_val = dictionary.values().index(max(dictionary.values()))
		
		#Find the corresponded key/entity_name in the dictionary for the max valued entity 
		counter=0
		for j in dictionary:
			if counter == max_val:
				Entity = j
				break
			else:
				counter+=1

		#Adjust the entity in color palette (rgbkymc = 7)
		while( max_val - 7 >= 0): max_val-=7
		
		#Add Line2D object STAR 
		blue_line = mlines.Line2D([], [], color="rgbkymc"[max_val], marker='*',
							  markersize=20, label=Entity)
		#Initialize Legend and add it to Plot
		plt.legend(handles=[blue_line])
		#Create Image[ i ] file
		file = 'Entity-'+str(i)+'-.png'
		#Export 
		plt.savefig(file)