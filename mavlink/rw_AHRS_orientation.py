"""
Read and write AHRS orientation
!!! unfinished!
parameter
https://ardupilot.org/copter/docs/parameters-Copter-stable-V4.5.4.html#ahrs-orientation-board-orientation
message
https://mavlink.io/en/messages/common.html#MAV_SENSOR_ORIENTATION

"""

import time
from pymavlink import mavutil

mav1 = mavutil.mavlink_connection('/dev/ttyACM0')
#master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

# Wait a heartbeat
master.wait_heartbeat()

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
#convenience function to read and print a message at a given frequency
def req_param(param_type):
    # Request parameter
    #bpar = bytes(param_type)
    master.mav.param_request_read_send(
        master.target_system, master.target_component,
        #b'COMPASS_OFS_X',
        param_type,
        -1
    )
    # Print parameter value
    message = master.recv_match(type='PARAM_VALUE', blocking=False).to_dict()
    print('name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))

#request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_MAV_SENSOR_ORIENTATION, 1)
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_RAW_IMU, 1)
#req_param(b'MAV_SENSOR_ORIENTATION')
#req_param(b'MAV_SENSOR_ORIENTATION')
time.sleep(1)
#if False: # don't write anything for now
if True:
    # Set parameter value
    # Set a parameter value TEMPORARILY to RAM. It will be reset to default on system reboot.
    # Send the ACTION MAV_ACTION_STORAGE_WRITE to PERMANENTLY write the RAM contents to EEPROM.
    # The parameter variable type is described by MAV_PARAM_TYPE in http://mavlink.org/messages/common.
    master.mav.param_set_send(
        master.target_system, master.target_component,
        b'AHRS_ORIENTATION',
        0,
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )

#    # Read ACK
#    # IMPORTANT: The receiving component should acknowledge the new parameter value by sending a
#    # param_value message to all communication partners.
#    # This will also ensure that multiple GCS all have an up-to-date list of all parameters.
#    # If the sending GCS did not receive a PARAM_VALUE message within its timeout time,
#    # it should re-send the PARAM_SET message.
#    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
#    print('name: %s\tvalue: %d' %
#          (message['param_id'], message['param_value']))
#
#    time.sleep(1)
#
#    # Request parameter value to confirm
#    master.mav.param_request_read_send(
#        master.target_system, master.target_component,
#        b'COMPASS_OFS_Z',
#        -1
#    )
#    # Print new value in RAM
#    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
#    print('New in RAM: name: %s\tvalue: %d' %
#          (message['param_id'], message['param_value']))
