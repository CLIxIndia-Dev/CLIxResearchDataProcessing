**Following are the steps to extract the module data metrics for the period 2018-19**
---
* The raw datasets need to be downloaded into local destination. This path has to be provided for the below mentioned script.
* Firstly to fetch the metrics, the progress csv data for the period Mar2018-Apr2019 need to be fetched and collated in to a sheet. For this need to run the script `progress_collation.py`
* This collated sheet forms the basis to generate any metric.
* Run the following scripts to generate the given metric:
    - `progresscsv_activitesvisited_min.py` -- Gives the min activities visited per module.
    - `progresscsv_activitiesvisited_max.py` -- Max activities visited per module
    - `progresscsv_activitiesvisited_median.py` -- Median value of activities visited per module
    - `progresscsv_num_of_students.py` -- Number of unique student visits per module
    - `progresscsv_NoOFSchools.py` -- Number of schools a particular module has been rolled out.
    - `progresscsv_buddies.py` and `progresscsv_collation_buddies_userids.py` -- Gives the Buddies count per module.
