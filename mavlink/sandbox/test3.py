from pymavlink import mavutil
import time

# Connect to the autopilot at 115200 baud
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Function to send MAV_CMD_NAV_WAYPOINT command
def send_nav_waypoint(x, y, z):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,  # Navigate to waypoint command
        0,  # Confirmation
        0,  # Hold time
        0,  # Acceptance radius
        0,  # Pass through waypoint (0 = stop)
        x,  # Latitude/X position (meters in local frame)
        y,  # Longitude/Y position
        z,  # Altitude/Z position
        0   # Param7 (unused)
    )

# Send nav waypoint command: 0.3m forward
print("Sending nav waypoint command: 0.3m forward")
send_nav_waypoint(x=0.3, y=0, z=0)
print("Nav waypoint command sent.")

