Steps to fetch the required collated data for tools
------
1. Open python shell and import all the methods from `tools_proc.py`
2. Define a list as `schools_list` containing the schools list whose data has to be collated
3. Run the below commands
    1. `tools_log_level_data = fetch_log_level_data_tools(<path to the dataset>, schools_list, <state_code>)`
    2. `date_range = ['2018-04-01', '2019-03-31']`
    3. `dt = get_tool_data_metrics(tools_log_level_data, date_range)`
4. Save the above data frame for further processing into a csv file.
5. Provide the csv file saved in the previous step in the file `unique_logins.py`.
6. Execute the python script on the shell as below
    1. `exec(open("unique_logins.py").read())`
7. The above script will provide the collated data along with some calculations which will be used later. The name of the collated csv can be changed if needed.
