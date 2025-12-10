from pymavlink import mavutil
import time
import threading

# Connect to the autopilot
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=57600)

def print_wheel_distance():
    while True:
        msg = master.recv_match(type='WHEEL_DISTANCE', blocking=True, timeout=1)
        if msg is not None:
            print(f"Wheel distances: {msg.distance}")

# Start wheel distance printing thread
distance_thread = threading.Thread(target=print_wheel_distance, daemon=True)
distance_thread.start()

# Wait for the heartbeat
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

def arm():
    print("Arming...")
    if not send_command(mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 1):
        print("Failed to arm. Check safety switch, RC, and sensors.")
        return False
    return True

# Arm the rover
if not arm():
    exit(1)

# Wait a moment for mode change
time.sleep(1)

# Send movement command: 1m forward at 0.2 m/s
print("Sending movement command...")
master.mav.set_position_target_local_ned_send(
    0,  # time_boot_ms
    master.target_system,
    master.target_component,
    mavutil.mavlink.MAV_FRAME_LOCAL_NED,
    0b110111100111,  # type_mask: Use position (x) and velocity (vx)
    1.0, 0, 0,  # x, y, z positions (meters)
    0.2, 0, 0,  # x, y, z velocities (m/s)
    0, 0, 0,  # x, y, z accelerations (not used)
    0, 0  # yaw, yaw_rate (not used)
)

print("Movement command sent.")
time.sleep(10)  # Let the rover move for 10 seconds

