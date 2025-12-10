from pymavlink import mavutil
import time

# Connect to the autopilot
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=57600)

# Wait for the first heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

def send_command(command, param1=0, param2=0, param3=0, param4=0, param5=0, param6=0, param7=0):
    master.mav.command_long_send(
        master.target_system,
        master.target_component,
        command,
        0,  # confirmation
        param1, param2, param3, param4, param5, param6, param7
    )
    ack = master.recv_match(type='COMMAND_ACK', blocking=True, timeout=3)
    if ack is not None:
        print(f"Command {command} acknowledged: {mavutil.mavlink.enums['MAV_RESULT'][ack.result].name}")
        return ack.result == mavutil.mavlink.MAV_RESULT_ACCEPTED
    else:
        print(f"Command {command} not acknowledged")
        return False

def set_guided_mode():
    # Try setting GUIDED mode
    print("Setting GUIDED mode...")
    if not send_command(mavutil.mavlink.MAV_CMD_DO_SET_MODE, mavutil.mavlink.MAV_MODE_GUIDED_ARMED):
        print("Failed to set GUIDED mode. Check if GUIDED mode is enabled and all sensors are ready.")
        return False
    return True

def arm():
    print("Arming...")
    if not send_command(mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 1):
        print("Failed to arm. Check safety switch, RC, and sensors.")
        return False
    return True

# Arm the rover
if not arm():
    exit(1)

# Set to GUIDED mode
# if not set_guided_mode():
#     exit(1)

# Wait a moment for mode change
time.sleep(1)

# Send movement command: 0.3m forward
print("Sending movement command...")
master.mav.set_position_target_local_ned_send(
    0,  # time_boot_ms
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b110111111000,  # type_mask (ignore velocity/yaw)
    0.55, 0, 0,  # x, y, z positions
    0, 0, 0,  # x, y, z velocities
    0, 0, 0,  # x, y, z accelerations
    0, 0  # yaw, yaw_rate
)

print("Movement command sent.")


