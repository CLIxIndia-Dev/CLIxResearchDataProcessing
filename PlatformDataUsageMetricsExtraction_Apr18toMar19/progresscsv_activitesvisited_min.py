'''
Purpose : 
This script fetches the min activities visited for a given module.

How to run:
Needs python shell and the cumulative csvs generated from collation script.
1. execfile('<path>/progresscsv_activitiesvisited_min')

'''
# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
progress_data = pd.read_csv('ct-cummulative-Apr18-Mar19.csv',usecols=['module_name','activities_visited'])

aggregation = {
				"activities_visited":{
					"min_activities_visited":'min'
					}
}

dt = progress_data.groupby(['module_name']).agg(aggregation)

dt.reset_index().to_csv('Collated_ct_total_activities_min.csv')
# for name,group in dt:
#     print name
#     print group.agg(aggregation)
