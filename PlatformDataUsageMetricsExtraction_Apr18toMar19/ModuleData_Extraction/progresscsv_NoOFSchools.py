'''
#File creation : Durga Swetha


#Prerequisite : The collated csv should be created from the raw dataset of each state.


#Description : This script fetches the no of schools in which this has been rolled out for a given module.


#Steps to run the script : 1. Needs python shell and the cumulative csvs generated from collation script.
			   2. execfile('<path>/progresscsv_NoOfSchools')

'''


# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
progress_data = pd.read_csv('ct-cummulative-Apr18-Mar19.csv',usecols=['module_name','server_id'])

aggregation = {

				"server_id":{
					"NO_Schools_Rolled_Out":'nunique'
					}
}

dt = progress_data.groupby(['module_name']).agg(aggregation)

dt.reset_index().to_csv('Collated_ct_Module_Schools_Rolled_out.csv')
# for name,group in dt:
#     print name
#     print group.agg(aggregation)
