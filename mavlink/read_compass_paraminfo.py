"""
REad compass (and magnetometer) related information
"""

import time
# Import mavutil
from pymavlink import mavutil

# Create the connection
master = mavutil.mavlink_connection('/dev/ttyACM0')
#master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
master.wait_heartbeat()

def req_param(param_type):
    # Request parameter
    #bpar = bytes(param_type)
    master.mav.param_request_read_send(
        master.target_system, master.target_component,
        param_type,
        -1
    )
    # Print parameter value
    # TODO add timeout timer to avoid long blocking
    #try:
    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    print('name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))

# Request parameter
try:
    print('per-motor compass correction enable:')
    req_param(b'COMPASS_PMOT_EN')
except:
    print('only one compass in FC')
try:
    req_param(b'COMPASS_PRIMARY')
except:
    print('only one compass in FC')
req_param(b'COMPASS_EXTERNAL') # Compass is attached via an external cable
try:
    req_param(b'COMPASS_ORIENT') # Compass orientation for the first external compass
    req_param(b'AHRS_ORIENT') # 
except:
    print('no external compass')
req_param(b'COMPASS_OFFS_MAX')
print('Compass calibration fitness: ')
req_param(b'COMPASS_CAL_FIT') #Compass calibration fitness (ex. if very strict, will be hard to obtain proper calibration)
print('Compass declination (rad): ')
req_param(b'COMPASS_DEC') # compass declination (compensate between the true north and magnetic north)
req_param(b'COMPASS_USE') # use compass for yaw (can be disabled)
print('Motor interference compensation for body frame X,Y,Z axis (mGauss/A)')
req_param(b'COMPASS_MOT_X') # Motor interference compensation for body frame X axis
req_param(b'COMPASS_MOT_Y') # Motor interference compensation for body frame Y axis
req_param(b'COMPASS_MOT_Z') # Motor interference compensation for body frame Z axis
req_param(b'COMPASS_OFS_X') # Compass offsets in milligauss on the X axis
req_param(b'COMPASS_OFS_Y')
req_param(b'COMPASS_OFS_Z')
print('Compass soft-iron matrix components')
req_param(b'COMPASS_DIA_X')
req_param(b'COMPASS_PMOT1_X')
print('EK3_MAG_CAL: Magnetometer default fusion mode')
req_param(b'EK3_MAG_CAL') # Magnetometer default fusion mode
print('Finished')
time.sleep(1)
