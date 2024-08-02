"""
REad magnetometer data and plot it live
approach adapted from sparkfun
This code redraws the plot each time
Pros: 
    - adjust y scale as data comes in
    - easy way to add time stamps
Cons:
    - slower than when plot isn't redrawns
"""

import time
import datetime as dt
from pymavlink import mavutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import sqrt


# Create the connection
mav1 = mavutil.mavlink_connection('/dev/ttyACM0')
#mav1 = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
mav1.wait_heartbeat()
fig,ax = plt.subplots() 
#fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []
N =20
# called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read mag
    msg = mav1.recv_msg()
    if msg is not None:
        msg_type = msg.get_type()
        #print(f'msg_type : {msg_type}')
        if msg_type == "RAW_IMU":
            magx,magy,magz = msg.xmag,msg.ymag,msg.zmag
            magf_magn = sqrt(magx*magx+magy*magy+magz*magz)

            # Add x and y to lists
            xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
            ys.append(magf_magn)

    # Limit x and y lists to N items
    xs = xs[-N:]
    ys = ys[-N:]
    
    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Mag field')
    plt.ylabel('mag field (mGauss)')

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
def req_param(param_type):
    # Request parameter
    #bpar = bytes(param_type)
    mav1.mav.param_request_read_send(
        mav1.target_system, mav1.target_component,
        param_type,
        -1
    )
    # Print parameter value
    # TODO add timeout timer to avoid long blocking
    #try:
    message = mav1.recv_match(type='PARAM_VALUE', blocking=True).to_dict()
    print('name: %s\tvalue: %d' %
          (message['param_id'], message['param_value']))
#while True:
#    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
#    plt.show()
#ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
ani = animation.FuncAnimation(fig, animate,frames=N, fargs=(xs, ys), interval=10)
#ani = animation.FuncAnimation(fig, animate,frames=N, fargs=(xs, ys), interval=10, blit=True)
plt.show()
