# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
dframe = pd.read_csv('tg_tmp1.csv',usecols=['tool_name','school_server_code','num_users_reg', 'num_users_nonreg'])
df = dframe.groupby(['tool_name','school_server_code']).apply(lambda x: x.drop_duplicates(subset=['tool_name','school_server_code','num_users_reg','num_users_nonreg'], keep='first'))
#dframe.drop_duplicates(subset=['tool_name','school_server_code','num_users_reg', 'num_users_nonreg'],keep=False)
df.to_csv('tg_tmp2.csv')


dframe = pd.read_csv('tg_tmp1.csv',usecols=['tool_name','school_server_code','session_id','time_spent','time_spent_seconds', 'date_created','user_id'])
#df = dframe.groupby(['tool_name','school_server_code','user_id','session_id','date_created']).apply(lambda x: #x.drop_duplicates(subset=['tool_name','school_server_code','user_id','session_id','date_created'], keep='first'))
#dframe.drop_duplicates(subset=['tool_name','school_server_code','num_users_reg', 'num_users_nonreg'],keep=False)

aggregation = {
				"time_spent":{
					"total_time_spent":'sum'
					}
}

dframe.groupby(['tool_name','school_server_code','session_id','time_spent','time_spent_seconds', 'date_created','user_id']).agg(aggregation).to_csv('tg_tmp3.csv')

