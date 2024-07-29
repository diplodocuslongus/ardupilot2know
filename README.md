# ardupilot2know

## Intro

## Parameters, logs and messages

See the README in directory param_log_msg.

## ardupilot and ROS and Gazebo

## Install ardupilot

This will install ardupilot, the MAVProxy Ground Control Station (MAVProxy GCS) and the Software In the Loop (SITL) simulations of the vehicle code. One can build the ardupilot code and run or verify the build in the ArduPilot SITL simulator.

Installed in `$HOME/builds/ArduPilot` on the gonze and the 76.

    git clone --recurse-submodules git@github.com:ArduPilot/ardupilot.git
    cd ardupilot/

    Tools/environment_install/install-prereqs-ubuntu.sh -y
    . ~/.profile


https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux

    $ ./waf list_boards
    SACNS-CM4Pilot ACNS-F405AIO aero AeroFox-Airspeed AeroFox-Airspeed-DLVR AeroFox-GNSS_F9P AeroFox-PMU airbotf4 AIRLink Airvolute-DCS2 AnyleafH7 Aocoda-RC-H743Dual AR-F407SmartBat ARK_CANNODE ARK_GPS ARK_RTK_GPS ARKV6X AtomRCF405NAVI bbbmini BeastF7 BeastF7v2 BeastH7 BeastH7v2 bebop BETAFPV-F405 bhat BirdCANdy BlitzF745AIO  ... sw-spar-f407 Swan-K1 TBS-Colibri-F7 thepeach-k1 thepeach-r1 TMotorH743 vnav VRBrain-v51 VRBrain-v52 VRBrain-v54 VRCore-v10 VRUBrain-v51 YJUAV_A6 YJUAV_A6SE YJUAV_A6SE_H743 YJUAV_A6Ultra ZubaxGNSS zynq

Info:

https://ardupilot.org/dev/docs/building-the-code.html

https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux

github:
https://github.com/ArduPilot/ardupilot
Test:
https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md

## SITL

The installation of ardupilot above also setup the  SITL environmnent.
Basic launch of SITL for a copter:

    cd ArduCopter/
    sim_vehicle.py --console --map -w

https://ardupilot.org/dev/docs/sitl-simulator-software-in-the-loop.html#sitl-simulator-software-in-the-loop

https://ardupilot.org/dev/docs/setting-up-sitl-on-linux.html

https://ardupilot.org/dev/docs/using-sitl-for-ardupilot-testing.html#using-sitl-for-ardupilot-testing


## ardupilot-gazebo

Install gazebo harmonic

    sudo apt update
    sudo apt install libgz-sim8-dev rapidjson-dev

Ensure the GZ_VERSION environment variable is set to either garden or harmonic.

    export GZ_VERSION=harmonic

Clone the repo and build:

    git clone https://github.com/ArduPilot/ardupilot_gazebo
    cd ardupilot_gazebo
    mkdir build && cd build
    cmake .. -DCMAKE_BUILD_TYPE=RelWithDebInfo
    make -j4

Export to bashrc

Add this ad the end of bashrc:

    export GZ_SIM_SYSTEM_PLUGIN_PATH=$HOME/builds/ArduPilot/ardupilot_gazebo/build:${GZ_SIM_SYSTEM_PLUGIN_PATH}
    export GZ_SIM_RESOURCE_PATH=$HOME/builds/ArduPilot/ardupilot_gazebo/models:$HOME/builds/ArduPilot/ardupilot_gazebo/worlds:${GZ_SIM_RESOURCE_PATH}


Test:

    gz sim -v4 -r iris_runway.sdf

It will start the simu window (and slow down the computer!)
If the export wasn't correct (wrong path) we get:

    $ gz sim -v4 -r iris_runway.sdf
    [Wrn] [gz.cc:102] Fuel world download failed because Fetch failed. Other errors


Info:

https://github.com/ArduPilot/ardupilot_gazebo

## MAVProxy (TODO)

https://ardupilot.org/mavproxy/docs/getting_started/download_and_installation.html

## install MAVExplorer

Enables to explore .bin log files.
tested and installed on fw but didn't document the install because of a crash, the following may work:


In a virtual environment, 

pip install wxpython
pip install  pymavlink mavproxy

Then launch:

MAVExplorer.py path/to/ardupilot_log.bin
https://ardupilot.org/dev/docs/using-mavexplorer-for-log-analysis.html

# EKF

## source switching

https://ardupilot.org/copter/docs/common-ekf-sources.html

Example: swtich from using the compass to not using the compass and only relying on the IMU for heading.

