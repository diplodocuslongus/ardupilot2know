# this is for ardupilot, not px4
# save as check_param.py and run: python3 check_param.py
from pymavlink import mavutil
m = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)   # adjust port if needed
m.wait_heartbeat(timeout=10)
# request param list
m.param_fetch_all()
# small helper: get param value
def get_param(name):
    try:
        p = m.param[name]
        return p
    except Exception:
        return None

import time
time.sleep(1)  # give fetch a moment
print("EK3_FLOW_USE =", get_param('EK3_FLOW_USE'))
print("EK2_FLOW_USE =", get_param('EK2_FLOW_USE'))

