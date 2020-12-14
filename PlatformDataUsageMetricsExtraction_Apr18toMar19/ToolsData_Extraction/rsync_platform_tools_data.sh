#!/bin/bash

#File creation : Shivani Dixit


#Prerequisite : 1. Backup of both the source as well as destination folders must be taken, in case there is any issue.


#Description : This script syncs the "gstudio_tools_logs" folder from the backup folder to the syncthing folder.


#Steps to run the script : 1. Run the bash script using "sudo bash rsync_platform_tools_data.sh".
#                          2. Enter the ENTIRE syncthing folder path when the script prompts. The path entered should be till folder "data" present in syncthing folder.
#                             Example: /home/clix/syncthng_folder/data
#                          3. The script will ask for the state code. Enter according to the instructions there and your requirements.
#                          4. Enter the ENTIRE data backup folder path when the script prompts. The path entered should be till the folder "backup_${state_code}_tools_logs" present in data backup folder.
#                             Example: /home/clix/data_bckup/backup_${state_code}_tools_logs

function sync_platform_tools_data() {
  read -p "Enter the syncthing folder path: " sync_folder  #Enter the full syncthing folder path till the "data" folder.
  read -p "Enter the state code: " state_code   
  read -p "Enter the data backup folder path: " backup_folder  #Enter the full backup folder path of the state till the "backup_${state_code}_tools_logs" folder.
  for ((i=1 ; i<=300 ; i++))
  do 
    if [ -d ${backup_folder}/*${state_code}${i}/gstudio/gstudio_tools_logs ]; then   #To check if the gstudio_tools_logs folder is present
      sudo rsync -avPhz ${backup_folder}/*${state_code}${i}/gstudio/gstudio_tools_logs ${sync_folder}/${state_code}/2018/${state_code}${i}/2019/${state_code}/*${state_code}${i}/gstudio/ ;    #To sync the gstudio_tools_logs from data backup to the syncthing folder
    fi
  done    
} 

sync_platform_tools_data | tee rsync_${state_code}_tools_data.log;


