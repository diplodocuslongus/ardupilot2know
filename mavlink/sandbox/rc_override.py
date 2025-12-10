from pymavlink import mavutil
import time

# Connect to the autopilot
master = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)

# Wait for the heartbeat
print("Waiting for heartbeat...")
master.wait_heartbeat()
print(f"Heartbeat from system (system {master.target_system} component {master.target_component})")

# Function to send RC override command
def send_rc_override(throttle, duration):
    # Get current RC channels
    rc_chan = master.recv_match(type='RC_CHANNELS', blocking=True, timeout=1)
    if rc_chan is None:
        print("No RC_CHANNELS message received")
        return

    # Save current RC values
    current_channels = [rc_chan.chan1_raw, rc_chan.chan2_raw, rc_chan.chan3_raw, rc_chan.chan4_raw,
                         rc_chan.chan5_raw, rc_chan.chan6_raw, rc_chan.chan7_raw, rc_chan.chan8_raw]

    # Modify throttle channel (usually channel 3)
    current_channels[2] = throttle  # Set throttle value (e.g., 1500 for mid, 1600 for forward)

    # Send RC override command for 'duration' seconds
    end_time = time.time() + duration
    while time.time() < end_time:
        master.mav.rc_channels_override_send(
            master.target_system,  # target_system
            master.target_component,  # target_component
            *current_channels  # RC channel values
        )
        time.sleep(0.1)  # Send command at 10Hz

# Send RC override command: throttle forward for 3 seconds
print("Sending RC override command: throttle forward for 3 seconds")
send_rc_override(throttle=1600, duration=3)
print("RC override command sent.")

