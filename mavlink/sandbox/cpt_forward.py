from pymavlink import mavutil
import time

# Connect via USB or UDP (replace with your correct master)
# e.g., 'udp:192.168.4.2:14550' if your laptop IP is 192.168.4.2
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for heartbeat
master.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (master.target_system, master.target_component))

# Send forward velocity in rover frame
vx = 0.5  # forward speed in m/s
vy = 0.0  # lateral speed (usually 0 for rover)
vz = 0.0  # vertical speed (0 for ground vehicles)
yaw_rate = 0.0  # keep current heading

# Use type_mask to enable velocity control only
# Bitmask explanation: https://mavlink.io/en/messages/common.html#SET_POSITION_TARGET_LOCAL_NED
# 0b0000111111000111 = 0x3C7 disables everything except vx, vy, vz
type_mask = 0b0000111111000111

# Send command repeatedly
for _ in range(50):
    master.mav.set_position_target_local_ned_send(
        int(time.time() * 1e6),       # time_boot_ms
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_FRAME_LOCAL_NED,  # frame
        type_mask,
        0, 0, 0,  # x, y, z positions (ignored)
        vx, vy, vz,  # velocities in m/s
        0, 0, 0,  # accelerations (ignored)
        0, yaw_rate
    )
    time.sleep(0.1)

