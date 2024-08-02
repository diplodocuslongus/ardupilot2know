"""
connect to fc and return info from heartbeat
https://mavlink.io/en/messages/minimal.html#HEARTBEAT
"""

import time
from pymavlink import mavutil

# Create the connection
#  If using a companion computer
#  the default connection is available
#  at ip 192.168.2.1 and the port 14550
# Note: The connection is done with 'udpin' and not 'udpout'.
#  You can check in http:192.168.2.2:2770/mavproxy that the communication made for 14550
#  uses a 'udpbcast' (client) and not 'udpin' (server).
#  If you want to use QGroundControl in parallel with your python script,
#  it's possible to add a new output port in http:192.168.2.2:2770/mavproxy as a new line.
#  E.g: --out udpbcast:192.168.2.255:yourport
master = mavutil.mavlink_connection('/dev/ttyACM0')
# master = mavutil.mavlink_connection('udpin:0.0.0.0:14550')

# Make sure the connection is valid
master.wait_heartbeat()
time.sleep(1)
print('go')
msg = master.recv_msg()
if msg is not None:
    msg_type = msg.get_type()
    if msg_type == "HEARTBEAT":
        vehictype = msg.type
        print(f'vehicle type  = {vehictype},')

# Get properly formatted information 
while False:
    msg = master.recv_msg()
    if msg is not None:
        msg_type = msg.get_type()
        if msg_type == "HEARTBEAT":
            vehictype = msg.type
            print(f'vehicle type  = {vehictype},')

