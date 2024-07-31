"""
Example code of how to read and write vehicle parameters using pymavlink
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
        #b'COMPASS_OFS_X',
        param_type,
        -1
    )
    # Print parameter value
    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    print('name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))

# Request parameter
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'COMPASS_OFS_X',
    -1
)
# Print parameter value
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'], message['param_value']))

# same for COMPASS_OFS_Y
master.mav.param_request_read_send(
    master.target_system, master.target_component,
    b'COMPASS_OFS_Y',
    -1
)
req_param(b'COMPASS_OFS_Z')
# Print parameter value
message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
print('name: %s\tvalue: %d' %
      (message['param_id'], message['param_value']))
time.sleep(1)
#if False: # don't write anything for now
if True:
    # Set parameter value
    # Set a parameter value TEMPORARILY to RAM. It will be reset to default on system reboot.
    # Send the ACTION MAV_ACTION_STORAGE_WRITE to PERMANENTLY write the RAM contents to EEPROM.
    # The parameter variable type is described by MAV_PARAM_TYPE in http://mavlink.org/messages/common.
    master.mav.param_set_send(
        master.target_system, master.target_component,
        b'COMPASS_OFS_X',
        -12,
        mavutil.mavlink.MAV_PARAM_TYPE_REAL32
    )

    # Read ACK
    # IMPORTANT: The receiving component should acknowledge the new parameter value by sending a
    # param_value message to all communication partners.
    # This will also ensure that multiple GCS all have an up-to-date list of all parameters.
    # If the sending GCS did not receive a PARAM_VALUE message within its timeout time,
    # it should re-send the PARAM_SET message.
    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    print('name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))

    time.sleep(1)

    # Request parameter value to confirm
    master.mav.param_request_read_send(
        master.target_system, master.target_component,
        b'COMPASS_OFS_Z',
        -1
    )
    # Print new value in RAM
    message = master.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    print('New in RAM: name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))
