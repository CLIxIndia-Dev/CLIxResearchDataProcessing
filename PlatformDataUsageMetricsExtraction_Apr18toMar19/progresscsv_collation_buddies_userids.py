'''
Purpose : 
This script fetches the buddy count and out of this the no of buddies who has entry in the progresscsv.
The diff of these provides the number of buddies who are extra and to be added to the number of unique logins for a given module

How to run:
Needs python shell
cumulative csvs generated from collation script.
Buddies csv generated for each module

1. execfile('<path>/progresscsv_collation_buddies_userids')

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
       #unt = str(dt1['unit_name'][ind])
       #print unt,type(unt)
       new_df = progress_data[(progress_data.module_name == mod)]
       new_df = list(new_df['user_id'].unique())
       print dt1['module_name'][ind]
       li = dt1['No_Buddies'][ind].strip('][').strip("'").split(',')
       #print li
       for each in li:
          d = each.strip("'").strip().strip("'").strip().strip()
          if d == '':
               continue
          else:
              final.append(int(d))
            #print "*"*30
       print final,len(final)
  
       #new_df['user_id'].apply(lambda x: any([k == x for k in final]))
       #print new_df
       ind1 =[]
       #print new_df
       for value in new_df:
          #x = 0
          #print value
          if value in final:
    	      ind1.append(True)
    	      #x = 1
    	      #break
	  else:    	    
	      ind1.append(False)
  
       print ind1.count(True)
       print "*"*30

