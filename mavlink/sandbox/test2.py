
from pymavlink import mavutil
import time

# Connect to the autopilot at 115200 baud
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Function to send MAV_CMD_DO_SET_ROVER_CONTROL command
def send_rover_control(steering, throttle, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        master.mav.command_long_send(
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_CMD_DO_SET_ROVER_CONTROL,  # Rover control command
            0,  # Confirmation
            steering,  # Steering (-1 to 1)
            throttle,  # Throttle (-1 to 1)
            0, 0, 0, 0, 0  # Unused parameters
        )
        time.sleep(0.1)  # Send command at 10Hz

# Send rover control command: move forward at half throttle for 3 seconds
print("Sending rover control command: move forward for 3 seconds")
send_rover_control(steering=0, throttle=0.5, duration=3)
print("Rover control command sent.")

