"""
REad magnetometer data and plot it live
"""

import time
# Import mavutil
from pymavlink import mavutil
import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

fig, ax = plt.subplots()

# animated=True tells matplotlib to only draw the artist when we
# explicitly request it
x = np.linspace(0, 2 * np.pi, 100)
#(ln,) = ax.plot(x, np.sin(x), animated=True)
(ln,) = ax.plot(1, np.sin(1), animated=True)

# make sure the window is raised, but the script keeps going
plt.show(block=False)


# Create the connection
mav1 = mavutil.mavlink_connection('/dev/ttyACM0')
#mav1 = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
mav1.wait_heartbeat()

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
plt.pause(0.1)
# get copy of entire figure (everything inside fig.bbox) sans animated artist
bg = fig.canvas.copy_from_bbox(fig.bbox)
# draw the animated artist, this uses a cached renderer
ax.draw_artist(ln)
# show the result to the screen, this pushes the updated RGBA buffer from the
# renderer to the GUI framework so you can see it
fig.canvas.blit(fig.bbox)
magmagseq = []
while True:
    msg = mav1.recv_msg()
    if msg is not None:
        msg_type = msg.get_type()
        #print(f'msg_type : {msg_type}')
        if msg_type == "RAW_IMU":
            magx,magy,magz = msg.xmag,msg.ymag,msg.zmag
            magf_magn = sqrt(magx*magx+magy*magy+magz*magz)
            magmagseq.append(magf_magn)
            print(f'mag field (mGauss) = {magx,magy,magz}, magnitude = {magf_magn}')
            # reset the background back in the canvas state, screen unchanged
            fig.canvas.restore_region(bg)
            # update the artist, neither the canvas state nor the screen have changed
            ln.set_ydata(magmagseq)
            # re-render the artist, updating the canvas state, but not the screen
            ax.draw_artist(ln)
            # copy the image to the GUI state, but screen might not be changed yet
            fig.canvas.blit(fig.bbox)
            # flush any pending GUI events, re-painting the screen if needed
            fig.canvas.flush_events()
            # you can put a pause in if you want to slow things down
            # plt.pause(.1)

