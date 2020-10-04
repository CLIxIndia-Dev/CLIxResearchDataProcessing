# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
dframe = pd.read_csv('tg_tools_data.csv')
#print dframe

def get_reg_users(df):
    df['num_users_reg'] = len(df['user_id'].unique())
    return df

def get_anon_users(df):
    df['num_users_nonreg'] = len(df['session_id'].unique())
    return df


users_perday_dframe = dframe.groupby(['tool_name','school_server_code']).apply(lambda x: get_reg_users(x)).reset_index(level=None, drop=True)

users_perday_dframe = users_perday_dframe.groupby(['tool_name','school_server_code']).apply(lambda x: get_anon_users(x)).reset_index(level=None, drop=True)

#users_perday_dframe = users_perday_dframe.groupby(['tool_name','school_server_code','session_id']).apply(lambda x: get_time_spent(x)).reset_index(level=None, drop=True)

#anon_users_mask = users_perday_dframe["user_id"] == 0
users_perday_dframe.to_csv('tg_tmp1.csv')
#users_perday_dframe['num_students_day'] = anon_users_mask*users_perday_dframe['num_users_nonreg'] + ~anon_users_mask * users_perday_dframe["num_users_reg"]
#users_perday_dframe.drop_duplicates(subset =['school_server_code','tool_name','date_created','user_id','session_id'],keep = False, inplace = True)
#users_perday_dframe.to_csv('ct_unique_logins.csv')

#users_perday_dframe = dframe.groupby(['tool_name']).apply(lambda x: get_num_users(x)).reset_index(level=None, drop=True)

