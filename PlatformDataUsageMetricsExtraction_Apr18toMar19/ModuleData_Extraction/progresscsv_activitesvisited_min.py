'''
#File creation : Durga Swetha


#Prerequisite : The collated csv should be created from the raw dataset of each state.


#Description : This script fetches the min activities visited for a given module.


#Steps to run the script : 1. Needs python shell and the cumulative csvs generated from collation script.
			   2. execfile('<path>/progresscsv_activitiesvisited_min')
			   
'''
# Import pandas as pd
import pandas as pd

progress_data = pd.read_csv('ct-cummulative-Apr18-Mar19.csv',usecols=['module_name','activities_visited'])

aggregation = {
				"activities_visited":{
					"min_activities_visited":'min'
					}
}

dt = progress_data.groupby(['module_name']).agg(aggregation)

dt.reset_index().to_csv('Collated_ct_total_activities_min.csv')

