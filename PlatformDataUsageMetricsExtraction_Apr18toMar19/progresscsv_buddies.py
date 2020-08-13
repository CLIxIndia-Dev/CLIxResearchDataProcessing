'''
Purpose : 
This script fetches the no of buddies for a given module.

How to run:
Needs python shell and the cumulative csvs generated from collation script.
1. execfile('<path>/progresscsv_buddies')

'''

# Import pandas as pd
import pandas as pd
import re
# Import the cars.csv data: cars
progress_data = pd.read_csv('ct-cummulative-Apr18-Mar19.csv',usecols=['module_name','buddy_userids'])

aggregation = {

				"buddy_userids":{
					"No_Buddies":'unique'
					}
}

dt1 = progress_data.groupby(['module_name']).agg(aggregation)

def compresslists(x):
	l1 = []
	val = x['buddy_userids']
	print "val",val['No_Buddies']
	for each in val['No_Buddies']:
		#print each
		
		y = each.strip("'[")
		y = y.strip("]'")
		#print y
		if y.find(', '): 
			l1.extend(y.split(', '))
		else:		
			l1.append(y)
		#print l1
		#print "="*30
	#print x[1]
	l1.remove('')
	print "before:",l1	
	l1 = [int(each) for each in l1]
	print "after:",l1
	l2 = list(set(l1))
	
	l2 = [str(each) for each in l2]	
	print "unique:", l2,len(l2)	
	return l2

dt1 = dt1.apply(compresslists,axis=1)

dt1.reset_index().to_csv('Collated_ct_Module_Buddies.csv')

