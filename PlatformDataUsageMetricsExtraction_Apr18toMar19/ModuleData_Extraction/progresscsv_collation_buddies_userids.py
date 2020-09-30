'''
#File creation : Durga Swetha


#Prerequisite : The Buddies sheet churned out and the cummulative data set.

#Description : This script fetches the buddy count and out of this the no of buddies who has entry in the progresscsv.
  	       The diff of these provides the number of buddies who are extra and to be added to the number of unique logins for a given module

#Steps to run the script : 1. Needs python shell and the buddies csv and the cumulative csvs.
			   2. execfile('<path>/progresscsv_collation_buddies_userids')

'''

# Import pandas as pd
import pandas as pd

dt1 = pd.read_csv('Collated_ct_Module_Buddies.csv',usecols=['module_name','No_Buddies'])

print "dt1:",dt1

progress_data = pd.read_csv('ct-cummulative-Apr18-Mar19.csv',usecols=['module_name','user_id'])
#dt1 = progress_data.groupby(['module_name'])

for ind in dt1.index:
       li = []
       final = []
       mod = str(dt1['module_name'][ind])

       new_df = progress_data[(progress_data.module_name == mod)]
       new_df = list(new_df['user_id'].unique())
       print dt1['module_name'][ind]
       li = dt1['No_Buddies'][ind].strip('][').strip("'").split(',')
       for each in li:
          d = each.strip("'").strip().strip("'").strip().strip()
          if d == '':
               continue
          else:
              final.append(int(d))
       print final,len(final)
       ind1 =[]
       for value in new_df:
          if value in final:
    	      ind1.append(True)
	  else:    	    
	      ind1.append(False)
  
       print ind1.count(True)
       print "*"*30

