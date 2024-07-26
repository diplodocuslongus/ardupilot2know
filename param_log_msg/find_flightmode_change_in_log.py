# detects log with a change in flight mode
# flight mode message:
# https://ardupilot.org/copter/docs/logmessages.html#mode
# flight mode parameter
# https://ardupilot.org/copter/docs/parameters.html#fltmode1-flight-mode-1
# 0 Stabilize
# 1 Acro
# 2 AltHold
# 3 Auto
# 4 Guided
# 5 Loiter

from ardupilot_log_reader.reader import Ardupilot
import numpy as np
import os
import datetime as dt
import glob
# All files and directories ending with .txt and that don't begin with a dot:

HOME = os.getenv("HOME")
PATH2FILES = f'.'
PATH2FILES = f'{HOME}/Data/Drones/Flight_Logs/TrainBridge/x4_log'
#PATH2FILES = f'{HOME}/Data/Drones/Flight_Logs/TrainBridge'
# PATH2FILES = f'{HOME}/pCloudDrive/ITRI/Drones_UAV/FlightLogs/'
# LOGNAME = '2024-07-18 15-26-17.bin' # dynamic flight
print(glob.glob(PATH2FILES+'/*.BIN'))
# All files and directories ending with .txt with depth of 2 folders, ignoring names beginning with a dot:
LOGNAME = 'x4_krtc_mag_interference.BIN'
FULLNAME = f'{PATH2FILES}/{LOGNAME}'

file_list = glob.glob(PATH2FILES+'/*.BIN')
for logfile in file_list:
    # only check the MODE messages
    parser = Ardupilot.parse(logfile,types=['MODE'])
    mydf = parser.dfs['PARM']

    mydf_mode = parser.dfs['MODE']
    fly_mode = mydf_mode['Mode'] #.to_numpy()
    fly_modenum = mydf_mode['ModeNum'].to_numpy()
    fly_ts = mydf_mode['TimeUS'].to_numpy()
    nb_change_fm = len(fly_mode)
    # detect if flight mode contains code 0= stabilize
    stab_mode_idx = np.where(fly_mode==0)[0]

    # if len(stab_mode_idx) > 0: don't use len, as len(array([])) can be 1
    if stab_mode_idx.size > 0:
        print(f'{len(stab_mode_idx)} where is {stab_mode_idx}')
        print(f'this flight used stabilize mode')
        log_with_stab_mode = os.path.basename(logfile)
        print(f'this log {log_with_stab_mode} had a change in flight mode: \n {fly_mode}')

    if 0: #nb_change_fm > 1:
        print(f'where is {stab_mode_idx}')
        if 0 in fly_mode:
            print(f'this flight used manual mode')
            print(f'this log had a change in flight mode: \n {fly_mode}')
'''
# only check the MODE messages
parser = Ardupilot.parse(FULLNAME,types=['MODE'])
mydf = parser.dfs['PARM']

mydf_mode = parser.dfs['MODE']
fly_mode = mydf_mode['Mode'] #.to_numpy()
fly_modenum = mydf_mode['ModeNum'].to_numpy()
fly_ts = mydf_mode['TimeUS'].to_numpy()
nb_change_fm = len(fly_mode)

if nb_change_fm > 1:
    print(f'this log had a change in flight mode: \n {fly_mode}')
'''
