# for now essentially pymavlink

## essential references

### messages

dialect ardupilotmega:
https://mavlink.io/en/messages/ardupilotmega.html

common:

https://mavlink.io/en/messages/common.html

Message ID list
https://groups.google.com/g/mavlink/c/1zgHUM67E-A

### parameters

https://www.ardusub.com/developers/full-parameter-list.html

ardupilot parameter, copter.

https://ardupilot.org/copter/docs/parameters.html#compass-ofs-x-compass-offsets-in-milligauss-on-the-x-axis

### mavlink commands

https://ardupilot.org/dev/docs/mavlink-commands.html


### microservices

### examples

https://www.ardusub.com/developers/pymavlink.html



https://mavlink.io/en/mavgen_python/

## setting connection

https://mavlink.io/en/mavgen_python/#setting_up_connection

### example connection

https://docs.px4.io/main/en/companion_computer/pixhawk_rpi.html

https://ardupilot.org/dev/docs/raspberry-pi-via-mavlink.html

## sensor calibrations

### magnetometer / compass

https://discuss.bluerobotics.com/t/pixhawk-accelerometer-and-compass-calibration-though-pymavlink/11453/2


## dialect

Dialects in MAVLink define communication protocols and other types of messages, most commonly for specific HW vendors. They are defined in .xml files.

https://mavlink.io/en/messages/#dialects

pymavlink comes with 2 dialects, and depending on which one is set, some command will not be understood.
For example running magtest.py from the examples will return MAVLink object has no attribute 'action_send'.

This is because the default is mavlinkv10 which doesn't know this command.

https://mavlink.io/en/mavgen_python/#dialect_file

https://discuss.ardupilot.org/t/enabling-mavlink-2-0-packet-and-signing-with-pymavlink-library/69351

## links and references (to order)

https://discuss.bluerobotics.com/t/accessing-real-time-mavlink-messages-via-pymavlink/11355/3



### pixhawk mini4

https://docs.px4.io/main/en/flight_controller/pixhawk4_mini.html

https://raw.githubusercontent.com/PX4/PX4-user_guide/main/assets/flight_controller/pixhawk4mini/pixhawk4mini_pinouts.pdf

# MAVSDK

https://mavsdk.mavlink.io/main/en/index.html
t
https://discuss.ardupilot.org/t/enabling-mavlink-2-0-packet-and-signing-with-pymavlink-library/69351

https://github.com/ArduPilot/pymavlink/blob/e192ad8114f203220f404f37f971d6359dd5e3d2/mavutil.py#L545

https://github.com/ArduPilot/pymavlink/blob/e192ad8114f203220f404f37f971d6359dd5e3d2/examples/magtest.py#L71

https://mavlink.io/en/messages/common.html

examples:

https://www.ardusub.com/developers/pymavlink.html#control-camera-gimbal

Parameters

https://mavlink.io/en/messages/common.html#PARAM_SET

https://mavlink.io/en/mavgen_python/

https://mavlink.io/en/messages/common.html#MAV_MODE
https://ardupilot.org/copter/docs/flight-modes.html#flight-modes

https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_MODE

https://mavlink.io/en/messages/common.html#HEARTBEAT

compassrelated

https://ardupilot.org/plane/docs/parameters.html

PX4:
https://discuss.px4.io/t/mav-cmd-do-set-mode-all-possible-modes/8495/2

