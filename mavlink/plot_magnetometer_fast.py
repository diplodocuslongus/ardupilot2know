"""
Read magnetometer data and plot it live
This code only update the data and doesn't
redraws the plot each time
Pros: 
    - can be fast
Cons:
    - can't easily change scale (Well, may be possible actually)
    - no easy way i could find to add time stamps(date, time)
"""

import time
import datetime as dt
# Import mavutil
from pymavlink import mavutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from math import sqrt

# plot settings
save_vid = True
#save_vid = False

# Create the connection
mav1 = mavutil.mavlink_connection('/dev/ttyACM1')
#mav1 = mavutil.mavlink_connection('udpin:0.0.0.0:14550')
# Wait a heartbeat before sending commands
mav1.wait_heartbeat()
#fig,ax = plt.subplots() # works but doesn't terminate qith `q` and ctl-c
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#xs = []
#ys = []
N =20
xs = list(range(0, N))
ys = [0] * N
ys1 = [0] * N
ys2 = [0] * N
ys3 = [0] * N
y_range = [-900, 900]  # Range of possible Y values to display
ax.set_ylim(y_range)
# Create a blank line. We will update the line in animate
line, = ax.plot(xs, ys, "ko-")
line1, = ax.plot(xs, ys1, "ro-")
line2, = ax.plot(xs, ys2, "go-")
line3, = ax.plot(xs, ys3, "bo-")
ax.set_title('Mag Field magnitude')
ax.set_ylabel('mag field (mGauss)')
if save_vid:
    # setup the formatting for moving files
    Writer = animation.writers['ffmpeg']
    Writer = Writer(fps=10, metadata=dict(artist="Me"), bitrate=-1)

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
request_message_interval(mavutil.mavlink.MAVLINK_MSG_ID_RAW_IMU, 5)
# This function is called periodically from FuncAnimation
def animate(i, xs, ys,ys1,ys2,ys3):
#def animate(i, xs, ys):

    # Read mag
    msg = mav1.recv_msg()
    if msg is not None:
        msg_type = msg.get_type()
        #print(f'msg_type : {msg_type}')
        if msg_type == "RAW_IMU":
            magx,magy,magz = msg.xmag,msg.ymag,msg.zmag
            magf_magn = sqrt(magx*magx+magy*magy+magz*magz)

            # Add x and y to lists
            #xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
            ys.append(magf_magn)
            ys1.append(magx)
            ys2.append(magy)
            ys3.append(magz)

    # Limit x and y lists to N items
    xs = xs[-N:]
    ys = ys[-N:]
    ys1 = ys1[-N:]
    ys2 = ys2[-N:]
    ys3 = ys3[-N:]
    
    # Update line with new Y values
    #line.set_data(xs,ys)
    #line.set_xdata(xs)
    line.set_ydata(ys)
    line1.set_ydata(ys1)
    line2.set_ydata(ys2)
    line3.set_ydata(ys3)

ani = animation.FuncAnimation(fig,
    animate,
    frames = 20*N,
    fargs=(xs,ys,ys1,ys2,ys3),
    #fargs=(ys,),
    interval=50,
    blit=False)
if save_vid:
    ani.save('magpix4hm.mp4', writer=Writer)
else:
    plt.show()
