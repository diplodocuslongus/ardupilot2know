from pymavlink import mavutil

# Connect to the autopilot via SERIAL0 (USB)
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Send SET_POSITION_TARGET_LOCAL_NED command
print("Sending movement command: 0.3m forward")
master.mav.command_long_send(
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,  # Navigate to waypoint
    0,  # Confirmation
    0,  # Hold time (not used)
    0,  # Acceptance radius (not used)
    0,  # Pass through waypoint (0 = stop)
    0.3,  # Latitude/ X position (meters in local frame)
    0,    # Longitude/ Y position
    0,    # Altitude/ Z position
    0     # Yaw (not used)
)

# master.mav.set_position_target_local_ned_send(
#     0,  # time_boot_ms (not used)
#     master.target_system,
#     master.target_component,
#     mavutil.mavlink.MAV_FRAME_BODY_NED,  # Use body frame for rovers
#     0b0000111111111000,  # type_mask: Position and velocity ignored except for x (forward)
#     0.3,  # x position (forward, meters)
#     0,    # y position
#     0,    # z position
#     0,    # x velocity (not used)
#     0,    # y velocity
#     0,    # z velocity
#     0,    # x acceleration (not used)
#     0,    # y acceleration
#     0,    # z acceleration
#     0,    # yaw (not used)
#     0     # yaw_rate (not used)
# )

print("Movement command sent.")

