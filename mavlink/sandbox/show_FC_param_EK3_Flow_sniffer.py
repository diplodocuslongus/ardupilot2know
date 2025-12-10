# sniff_mavlink.py
from pymavlink import mavutil

m = mavutil.mavlink_connection('/dev/ttyACM0', baud=115200)
print("Waiting for heartbeat...")
m.wait_heartbeat(timeout=10)
print("Heartbeat from SYS", m.target_system, "COMP", m.target_component)

print("Listening... (Ctrl-C to stop)")
while True:
    msg = m.recv_match(blocking=True)
    if msg is None:
        continue

    # Extract msg id safely
    try:
        mid = msg.get_msgId()
    except:
        try:
            mid = msg.msgid
        except:
            mid = None

    # Sender info
    try:
        sysid = msg.get_srcSystem()
        compid = msg.get_srcComponent()
    except:
        sysid = getattr(msg, 'sysid', None)
        compid = getattr(msg, 'compid', None)

    print(f"MSGID={mid} TYPE={msg.get_type()} SYS={sysid} COMP={compid}")

