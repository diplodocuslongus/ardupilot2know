from pymavlink import mavutil
import time

# Connect to the autopilot
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Function to send SET_POSITION_TARGET_LOCAL_NED message for velocity control
def send_velocity_command(vx, vy, vz, duration):
    # Send the command for 'duration' seconds
    end_time = time.time() + duration
    while time.time() < end_time:
        master.mav.set_position_target_local_ned_send(
            0,  # time_boot_ms (not used)
            master.target_system,
            master.target_component,
            mavutil.mavlink.MAV_FRAME_BODY_NED,  # Use body frame for rovers
            0b0000111111000111,  # type_mask: Velocity and yaw rate
            0,  # x position (not used)
            0,  # y position (not used)
            0,  # z position (not used)
            vx,  # x velocity (m/s, forward)
            vy,  # y velocity (m/s, right)
            vz,  # z velocity (m/s, down)
            0,  # x acceleration (not used)
            0,  # y acceleration (not used)
            0,  # z acceleration (not used)
            0,  # yaw (not used)
            0   # yaw_rate (not used)
        )
        time.sleep(0.1)  # Send command at 10Hz

# Send velocity command: 0.1 m/s forward for 3 seconds (0.3 meters)
print("Sending velocity command: 0.1 m/s forward for 3 seconds")
send_velocity_command(vx=0.1, vy=0, vz=0, duration=3)
print("Velocity command sent.")

