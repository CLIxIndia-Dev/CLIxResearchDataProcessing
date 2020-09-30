'''
#File creation : Durga Swetha


#Prerequisite : The raw data set for all the states should be available with the structure as is.


#Description : This script collates all the progress csvs till Apr 2018 - March 2019 into one csv.


#Steps to run the script : 1. Needs python shell.
			   2. execfile('<path>/progresscsv_collation')
			   3. prompts for the path of the data folder which has the progress csvs.

'''


import commands
import pandas as pd
import os
import sys
import csv
import datetime
import time
import re
import subprocess

global STATE_CODES  
global UNITNAMES 
global MONTH_VALUES
global DATA_DUMP_PATH
global PROGRESS_CSV_PATH
global COLLATED_FOLDER_NAME

UNITNAMES= {
			'eb-unit0-english-beginner':'11',
			'eb-unit1-english-beginner':'12',
			'ee-unit1-english-elementary':'13',
			'ee-unit2-english-elementary':'14',
			'gr1-unit1-concept-of-shape':'211',
			'gr1-unit2-analysing-describing-shapes':'212',
			'gr1-unit3-classifying-defining-shapes':'213',
			'gr2-unit1-property-based-reasoning':'221',
			'gr2-unit2-understanding-need-for-proof':'222',
			'pr-unit1-additive-to-multiplicative-thinking':'231',
			'pr-uni2-multiplicative-thinking':'232',
			'pr-unit3-ratios-proportions':'233',
			'pr-unit4-applications':'234',
			'le-unit1-making-solving-puzzles':'241',
			'le-unit2-exploring-telephone-tariffs':'242',
			'le-unit3-measuring-mustard-seed':'243',
			'le-unit4-finding-postal-charges':'244',
			'atom-in-chemistry':'30',
			'ast-unit1-earth':'31',
			'ast-unit2-moon':'32',
			'ast-unit3-solar-system':'33',
			'ecosystem':'34',
			'health-and-disease':'35',
			'sound':'36',
			'um-physics-motion':'37',
			'reflecting-on-values':'40',
			'pre-clix-survey':'50',
			'post-clix-survey':'51',
			}

STATE_CODES = ['rj','tg','ct','mz']

strg = "{:%d%m%Y-%Hh%Mm%Ss}".format(datetime.datetime.now())

def validate_args(state,schoolid):

	proceed_flag = True
	
	if state not in STATE_CODES:
		print "Given state code is not a defined value.\nPlease try again"
		proceed_flag = False

	if (schoolid and state == 'cg') and not schoolid.startswith('ct'):
		print "Given schoolid doesnt belong to the state given.\nPlease try again"
		proceed_flag = False
	elif schoolid and not str(schoolid).startswith(state):
		print "Given schoolid doesnt belong to the state given.\nPlease try again"
		proceed_flag = False
	else:
		pass
	if not proceed_flag:
		sys.exit()

def fetch_school_analytics_path(state,year,school_id):
	regex_parent_dir = re.compile(r'gstudio')
	top_path = PROGRESS_CSV_PATH+"/"+state+"/2018"+"/"+school_id+"/"+year
	print "top path:",top_path
	if os.path.exists(top_path):
		os.chdir(top_path)	
		#depth = 2
		#sep = os.sep
		#intial_depth = top_path.count(sep)	
		for path,walk_subdirs,files in os.walk(top_path):
			for each in walk_subdirs:
				print each	
				if regex_parent_dir.match(each):
					current_path = os.path.join(path, each)
					print current_path
					return current_path
			#current_depth = path.count(sep) - intial_depth
			#if current_depth < depth:
			#	continue
			#else:
			#	break
		#print "path:",path	
		#return path

def fetch_year_csv(school_id,unit,year,month):
	#if month == "":
	#	print "in month empty"
	#	filename = "(find -iname '*-"+school_id+"-"+unit+"-"+year+"*.csv')"
	#else:
	filename = "(find -iname '*-"+school_id+"-"+unit+"-"+year+month+"*.csv') | sort | tail -1"
	#filename = fname+" 
	result = commands.getoutput(filename)
	print "result for:"+month+"is"+result
	if result:
		if os.path.getsize(result) > 0:
			return result
		else:
			filename = "(find -iname '*-"+school_id+"-"+unit+"-"+year+month+"*.csv') | sort | tail -2"			
			result = commands.getoutput(filename).split()
			print "result:",result
			if len(result) == 2:
				print "in 2 if:",result[0]
				dname = result[0]
				siz = os.path.getsize(dname)
				if siz > 0:
					return dname
				else:
					filename = "(find -iname '*-"+school_id+"-"+unit+"-"+year+month+"*.csv') | sort | tail -3"			
					result = commands.getoutput(filename).split()
					print "result:",result
					if len(result) ==3:
						return result[0]	

def fetch_latest_csv_files(path,school_id,year):

	final_progresscvs = []
	print "current directory :",os.getcwd()
	
	for eachunit in UNITNAMES.keys():
		print eachunit
		if year == "2019":
			rel = fetch_year_csv(school_id,eachunit,year,"03")
			if rel:			
				final_progresscvs.append(rel)
			else:
				rel = fetch_year_csv(school_id,eachunit,year,"02")
				if rel:				
					final_progresscvs.append(rel)
				else:				
					rel = fetch_year_csv(school_id,eachunit,year,"01")
					if rel:		
						final_progresscvs.append(rel)
					else:
						rel = fetch_year_csv(school_id,eachunit,"2018","")
						if rel:		
							final_progresscvs.append(rel)
		else:
			rel = fetch_year_csv(school_id,eachunit,year,"")
			if rel:			
				final_progresscvs.append(rel)
	return final_progresscvs

def collated_csv_school_level(fpath,latestfiles,school_id):

	headernames=['Date','Day','Month','Year','unit_code','server_id','school_name','school_code','module_name','unit_name','username','user_id','first_name','last_name','roll_no','grade',
		'enrollment_status','buddy_userids','buddy_usernames','total_lessons','lessons_visited','percentage_lessons_visited','total_activities',
		'activities_visited','percentage_activities_visited','total_quizitems''visited_quizitems','attempted_quizitems','unattempted_quizitems',
		'correct_attempted_quizitems','notapplicable_quizitems','incorrect_attempted_quizitems','user_files','total_files_viewed_by_user',
		'other_viewing_my_files','unique_users_commented_on_user_files','total_rating_rcvd_on_files','commented_on_others_files','cmts_on_user_files',
		'total_cmnts_by_user','user_notes','others_reading_my_notes','cmts_on_user_notes','cmnts_rcvd_by_user','total_notes_read_by_user',
		'commented_on_others_notes','total_rating_rcvd_on_notes','correct_attempted_assessments','unattempted_assessments','visited_assessments',
		'notapplicable_assessments','incorrect_attempted_assessments','attempted_assessments','total_assessment_items']
	os.chdir(PROGRESS_CSV_PATH)
	if not os.path.exists(PROGRESS_CSV_PATH+"/"+COLLATED_FOLDER_NAME):
		os.mkdir(PROGRESS_CSV_PATH+"/"+COLLATED_FOLDER_NAME,0755)

	for eachfile in latestfiles:
		if eachfile.startswith('./'):
			file = eachfile[2:]
		else:
			file = eachfile

		filename = fpath+"/"+file
		print "file :",file
		date_string= file.split("-")[-2]
		
		date_object=datetime.datetime.strptime(date_string,'%Y%m%d')
		set_date= date_object.date().strftime("%d %B %Y")
		day = set_date.split(" ")[0]
		month = set_date.split(" ")[1]
		year = set_date.split(" ")[2]

		data = pd.read_csv(filename)
		data['Date']=set_date
		data['Day']=day
		data['Month']=month
		data['Year']=year
		data['unit_code']=UNITNAMES[data['unit_name'][0]]
		usernames = data['username']
		users = []
		for key,value in usernames.iteritems():
			users.append(value)
		pattern = re.escape(school_id)
		drop_users = [x for x in users if not re.search(pattern, x)]
		fdata = data[~data['username'].isin(drop_users)]
		outputfilepath =PROGRESS_CSV_PATH+"/"+COLLATED_FOLDER_NAME+"/"+file
		print "collated csvs folder :",outputfilepath
		if not fdata.empty:
			print "before to_csv"
			fdata.to_csv(outputfilepath,sep=',',index=False,columns=headernames)
			
if __name__ == '__main__':
	try:

		PROGRESS_CSV_PATH = raw_input("\n\tEnter absolute path of folder containing thin data (e.g '/home/durga/Rj_SyncthingDump/data/ct'):")
		state = raw_input("\n\tEnter the State code(in following pattern eg ct/mz/rj/tg):")
		school_id = raw_input("\n\tEnter the school for which you data need to be collated (Optional, if not given collates at state level):")
		#month = raw_input("\n\tEnter the month for which you need the data to be collated for (in 'MM' format e.g. January then enter 01):")
		#year = raw_input("\n\tEnter the year for which you need the data to be collated for (in 'yyyy' format e.g. 2018):")
		cwd_path = os.getcwd()
		#print cwd_path
		if os.path.exists(PROGRESS_CSV_PATH):
			flg = validate_args(state,school_id)
			if school_id:
				COLLATED_FOLDER_NAME = school_id+'-progresscsvs-'+month+"-"+strg
				fpath = fetch_school_analytics_path(state,2019,school_id)
				#print "Path :",fpath
				os.chdir(fpath+"/gstudio-exported-users-analytics-csvs")
			
				final_progresscvs = fetch_latest_csv_files(fpath+"/gstudio-exported-users-analytics-csvs",school_id,2019)
				collated_csv_school_level(fpath+"/gstudio-exported-users-analytics-csvs",final_progresscvs,school_id)
				fpath = fetch_school_analytics_path(state,2018,school_id)
				#print "Path :",fpath
				os.chdir(fpath+"/gstudio-exported-users-analytics-csvs")
			
				final_progresscvs = fetch_latest_csv_files(fpath+"/gstudio-exported-users-analytics-csvs",school_id,2018)
				collated_csv_school_level(fpath+"/gstudio-exported-users-analytics-csvs",final_progresscvs,school_id)
			else:
				COLLATED_FOLDER_NAME = state+'-progresscsvs-'+"-"+strg
				os.chdir(PROGRESS_CSV_PATH+"/"+state+"/")
				print PROGRESS_CSV_PATH+"/"+state+"/"
				for root,dirs,files in os.walk(PROGRESS_CSV_PATH+"/"+state+"/2018/"):
					for dr in dirs:
						print "Processing:",dr
						if len(os.listdir(PROGRESS_CSV_PATH+"/"+state+"/2018/"+dr)) > 0:
							fpath = fetch_school_analytics_path(state,"2019",dr)
							if fpath:
								os.chdir(fpath+"/gstudio-exported-users-analytics-csvs")
								final_progresscvs = fetch_latest_csv_files(fpath+"/gstudio-exported-users-analytics-csvs",dr,"2019")
								collated_csv_school_level(fpath+"/gstudio-exported-users-analytics-csvs",final_progresscvs,dr)
							else:							
								fpath = fetch_school_analytics_path(state,"2018",dr)
								if fpath:
									os.chdir(fpath+"/gstudio-exported-users-analytics-csvs")
									final_progresscvs = fetch_latest_csv_files(fpath+"/gstudio-exported-users-analytics-csvs",dr,"2018")
									collated_csv_school_level(fpath+"/gstudio-exported-users-analytics-csvs",final_progresscvs,dr)
						os.chdir(PROGRESS_CSV_PATH+"/"+state+"/")
					break		
			#print "Final_csvs :",final_progresscvs
		else:
			print "No relevant data found in the mentioned path.\n Please try again"
			sys.exit()
		
		os.chdir(PROGRESS_CSV_PATH)
		for root,dirs,files in os.walk(PROGRESS_CSV_PATH+"/"+COLLATED_FOLDER_NAME):
			if len(files) > 0:
				collation_attempt=pd.concat([pd.read_csv(PROGRESS_CSV_PATH+"/"+COLLATED_FOLDER_NAME+"/"+l) for l in files])
				if school_id:
					collation_attempt.to_csv(school_id+"-progresscsvs-"+"-"+strg+".csv",index = False)
				else:
					collation_attempt.to_csv(state+"-progresscsv-"+"-"+strg+".csv",index = False)
				print "Collation completed"
			else:
				print "No data found for the given month"
		os.chdir(cwd_path)
	except:
		# http://stackoverflow.com/questions/1000900/how-to-keep-a-python-script-output-window-open#1000968
		import traceback
		print "in print of exc_info",sys.exc_info()[0]
		print "in print of traceback",traceback.format_exc()
