#!/usr/bin/env python

'''
rotate APMs on bench to test magnetometers

'''
from __future__ import print_function

import time
import os
from math import radians,sqrt
# from pymavlink.dialects.v20 import common as mavlink2 # use if not using mavutil
#os.environ["MAVLINK20"] = '1'
#os.environ['MAVLINK_DIALECT'] = 'common' # 'ardupilotmega'
#os.environ["MAVLINK10"] = '0'
from pymavlink import mavutil

from argparse import ArgumentParser
parser = ArgumentParser(description=__doc__)

parser.add_argument("--device1", required=True, help="mavlink device1")
parser.add_argument("--baudrate", type=int,
                  help="master port baud rate", default=115200)
args = parser.parse_args()

def request_message_interval(message_id: int, frequency_hz: float):
    """
    Request MAVLink message in a desired frequency,
    documentation for SET_MESSAGE_INTERVAL:
        https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL

    Args:
        message_id (int): MAVLink message ID
        frequency_hz (float): Desired frequency in Hz
    """
    mav1.mav.command_long_send(
        mav1.target_system, 
        mav1.target_component,
        mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL, 0,
        message_id, # The MAVLink message ID
        1e6 / frequency_hz, # The interval between two messages in microseconds. Set to -1 to disable and 0 to request default rate.
        0, 0, 0, 0, # Unused parameters
        0, # Target address of message stream (if message has target address fields). 0: Flight-stack default (recommended), 1: address of requestor, 2: broadcast.
    )

# create a mavlink instance
#mavutil.set_dialect("ardupilotmega")
mav1 = mavutil.mavlink_connection(args.device1, baud=args.baudrate)

# add the dialect at connection
#mav1 = mavutil.mavlink_connection(args.device1, baud=args.baudrate,dialect='common')

print(f'dialect: mavlink10 = {mav1.mavlink10()} mavlink20 = {mav1.mavlink20()}')
print("Waiting for HEARTBEAT")
mav1.wait_heartbeat()
print("Heartbeat from APM (system %u component %u)" % (mav1.target_system, mav1.target_component))

print("Waiting for MANUAL mode")

# test...
#mav1.mav.command_long_send( mav1.target_system, mav1.target_component,
#                             mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
#                             0, 176, 0, 1, 0, 0, 0)
print('set man mode for mav1')
#mav1.recv_match(type='SYS_STATUS', condition='SYS_STATUS.mode==2 and SYS_STATUS.nav_mode==4', blocking=False)

print("Setting declination")
mav1.mav.param_set_send(mav1.target_system, mav1.target_component,b'COMPASS_DEC', radians(12.33),mavutil.mavlink.MAV_PARAM_TYPE_REAL32)



#event = mavutil.periodic_event(30)
#pevent = mavutil.periodic_event(0.3)
rc3_min = 1060
rc3_max = 1850
rc4_min = 1080
rc4_max = 1500
rc3 = rc3_min
rc4 = 1160
delta3 = 2
delta4 = 1
use_pitch = 1

# determine if the vehicle support onboard compass cal. There isn't an easy way to
# do this. A hack is to send the mag cancel command and see if it is accepted.
print('check if FC can do onboard mag calib') # if accepts a mag calib cancel command then it can
if False:
    mav1.mav.command_long_send( mav1.target_system,
                                mav1.target_component,
                                mavutil.mavlink.MAV_CMD_DO_CANCEL_MAG_CAL , 
                               0, 0, 0, 0, 1, 0, 0, 0)
    if mav1.recv_match(type='ACTION_ACK'):
        print('cancel mag cal ack ok')
#MAV_ACTION_CALIBRATE_GYRO = 17
#mav1.mav.action_send(mav1.target_system, mav1.target_component, MAV_ACTION_CALIBRATE_GYRO)

if False:
    mav1.mav.command_long_send( mav1.target_system, 
                                mav1.target_component,
                                mavutil.mavlink.MAV_CMD_DO_START_MAG_CAL,
                                0, # magnetometer to calibrate
                                0, # no retry on failure
                                1, # autosave
                                1, # delay in s
                                0, # user reboot (1 for autoreboot)
                                0, 0, 0) # empty / unused

    print("Waiting for gyro calibration")
    mav1.recv_match(type='ACTION_ACK')

print("Resetting mag offsets")
print('set magoffset: ')
print(mav1.mav.set_mag_offsets_send(mav1.target_system, mav1.target_component, 0, 0, 0))

def TrueHeading(SERVO_OUTPUT_RAW):
    p = float(SERVO_OUTPUT_RAW.servo3_raw - rc3_min) / (rc3_max - rc3_min)
    return 172 + p*(326 - 172)

print("read mag offsets")
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_RAW_IMU, 1)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_SENSOR_OFFSETS, 1)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_VFR_HUD, 1)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_COMPASSMOT_STATUS, 1)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_EKF_STATUS_REPORT, 1)
while True:
    msg = mav1.recv_msg()
    if msg is not None:
        msg_type = msg.get_type()
        #print(f'msg_type : {msg_type}')
        if msg_type == "RAW_IMU":
            magx,magy,magz = msg.xmag,msg.ymag,msg.zmag
            magf_magn = sqrt(magx*magx+magy*magy+magz*magz)
            print(f'mag field (mGauss) = {magx,magy,magz}, magnitude = {magf_magn}')
        if msg_type == "EKF_STATUS_REPORT":
            print(f'EKF report: {msg.compass_variance}')
        if msg_type == "COMPASSMOT_STATUS":
            print(f'compass motor stat: {msg.CompensationX}')
        if msg_type == "VFR_HUD":
            print(f'VFR_HUD = {msg.heading}')
        if msg_type == "SENSOR_OFFSETS":
            print(f'sensor offset = {msg.mag_ofs_x}')
#    try:
#        print(mav1.recv_match().to_dict())
#    except:
#        pass
    time.sleep(0.1)
#while True:
#    msg = mav1.recv_msg()
#    if msg is not None:
#        msg_type = msg.get_type()
#        if msg_type == "SENSOR_OFFSETS":
#            print(f'sensor offset = {msg.mag_ofs_x}')
##    if event.trigger():
##        if not use_pitch:
##            rc4 = 1160
##        set_attitude(rc3, rc4)
##        rc3 += delta3
##        if rc3 > rc3_max or rc3 < rc3_min:
##            delta3 = -delta3
##            use_pitch ^= 1
##        rc4 += delta4
##        if rc4 > rc4_max or rc4 < rc4_min:
##            delta4 = -delta4
##    if pevent.trigger():
##        msg_type = msg.get_type()
##        if msg_type == "SENSOR_OFFSETS":
##            print(f'sensor offset = {msg.mag_ofs_x}')
#    time.sleep(0.01)
#
## 314M 326G
## 160M 172G
#
