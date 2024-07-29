# Parameters, logs and messages

There's a lot of parameters to set in the flight controller, some of them are criticals to obtaining a good flight, some are less important, some must be set by the user, some are set as default and usually don't need to be changed.

## Messages

Messages are pieces of information which can be recorded by the flight controller for analysis, debugging, optimization...

Some messages examples are :

A list of messages can be found at:

https://ardupilot.org/copter/docs/logmessages.html#logmessages

## log viewer and analysis

https://ardupilot.org/copter/docs/common-logs.html

MissionPlanner can load .bin log files but it's windows only.

QGC doesn't have a log viewer, according to this [post](https://discuss.ardupilot.org/t/log-analysis-using-qgc/32809) (dating some time ago but as of 2024 I didn't find a way to load an Ardupilot .bin file into QGC) 

Log may maybe loaded when they are stored on the flight controller:

https://docs.qgroundcontrol.com/master/en/qgc-user-guide/analyze_view/log_download.html

### APM Planner 

Installed the AppImage:
https://github.com/ArduPilot/apm_planner/releases

Very very small font, barely usable and impracticle.

Code
https://github.com/ArduPilot/apm_planner


https://discuss.ardupilot.org/t/how-to-dump-logs-in-apm-planner-2-0/2005/7

https://ardupilot.org/planner2/


### Plot dronee

https://plot.dronee.aero/

https://discuss.ardupilot.org/t/droneeplotter-an-elite-drone-flight-log-analysis-tool/39576

### MAVProxy

Installed in virtualenv Ardupilot.

pip3 install PyYAML mavproxy 

https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html


https://github.com/ArduPilot/MAVProxy
https://ardupilot.org/mavproxy/index.html
https://ardupilot.org/mavproxy/docs/getting_started/cheatsheet.html#mavproxy-cheetsheet

#### quickstart

https://ardupilot.org/mavproxy/docs/getting_started/quickstart.html



#### View path and waypoint on a map

Use:
mavflightview, part of mavproxy.

mavflightview.py ~/Data/Drones/Flight_Logs/TrainBridge/x4_log/00000289.BIN 

https://erlerobotics.gitbooks.io/erle-robotics-mav-tools-free/content/en/tools/mavflightview.html



