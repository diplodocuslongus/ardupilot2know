# ardupilot and ros2

Follow everything [here](https://ardupilot.org/dev/docs/ros2.html), given that mavproxy and ros2 humble were already installed on my system (FW notebook, pop-os 22).

    cd ~
    mkcd ROS2_workspaces
    mkcd ardupilot_ws
    mkdir src
    vcs import --recursive --input  https://raw.githubusercontent.com/ArduPilot/ardupilot/master/Tools/ros2/ros2.repos src
    sudo apt update
    rosdep update
    rosdep install --from-paths src --ignore-src
    sudo apt install default-jre
    git clone --recurse-submodules https://github.com/ardupilot/Micro-XRCE-DDS-Gen.git
    cd Micro-XRCE-DDS-Gen
    ./gradlew assemble
    echo "export PATH=\$PATH:$PWD/scripts" >> ~/.bashrc
    source ~/.bashrc
    microxrceddsgen -version
    # returned : null

## Testing the installation:

    colcon build --packages-up-to ardupilot_dds_tests
    source ./install/setup.bash
    colcon test --executor sequential --parallel-workers 0 --base-paths src/ardupilot --event-handlers=console_cohesion+
    colcon test-result --all --verbose

Returned that all tests passed.

## ROS2 and SITL

    colcon build --packages-up-to ardupilot_sitl
    source install/setup.bash
    ros2 launch ardupilot_sitl sitl_dds_udp.launch.py transport:=udp4 synthetic_clock:=True wipe:=False model:=quad speedup:=1 slave:=0 instance:=0 defaults:=$(ros2 pkg prefix ardupilot_sitl)/share/ardupilot_sitl/config/default_params/copter.parm,$(ros2 pkg prefix ardupilot_sitl)/share/ardupilot_sitl/config/default_params/dds_udp.parm sim_address:=127.0.0.1 master:=tcp:127.0.0.1:5760 sitl:=127.0.0.1:5501

Returned:

    [INFO] [launch]: All log files can be found below /home/ludofw/.ros/log/2024-09-11-15-25-28-009443-52-0960514-95-108925
    [INFO] [launch]: Default logging verbosity is set to INFO
    namespace:        
    transport:        udp4
    middleware:       dds
    verbose:          4
    discovery:        7400
    port:             2019
    command:          arducopter
    model:            quad
    speedup:          1
    slave:            0
    sim_address:      127.0.0.1
    instance:         0
    defaults:         /home/ludofw/ROS2_workspaces/ardupilot_ws/install/ardupilot_sitl/share/ardupilot_sitl/config/default_params/copter.parm,/home/ludofw/ROS2_workspaces/ardupilot_ws/install/ardupilot_sitl/share/ardupilot_sitl/config/default_params/dds_udp.parm
    synthetic_clock:  True
    command:          mavproxy.py
    master:           tcp:127.0.0.1:5760
    sitl:             127.0.0.1:5501
    out:              127.0.0.1:14550
    console:          False
    map:              False
    [INFO] [micro_ros_agent-1]: process started with pid [108926]
...

See ros2 related info for ros commands.
In another terminal / tab, run:

    $ ros2 node list
    /ardupilot_dds

    $ ros2 node info /ardupilot_dds 
    /ardupilot_dds
      Subscribers:
        /ap/cmd_gps_pose: ardupilot_msgs/msg/GlobalPosition
        /ap/cmd_vel: geometry_msgs/msg/TwistStamped
        /ap/joy: sensor_msgs/msg/Joy
        /ap/tf: tf2_msgs/msg/TFMessage
      Publishers:
        /ap/battery/battery0: sensor_msgs/msg/BatteryState
        /ap/clock: rosgraph_msgs/msg/Clock
        /ap/geopose/filtered: geographic_msgs/msg/GeoPoseStamped
        /ap/gps_global_origin/filtered: geographic_msgs/msg/GeoPointStamped
        /ap/imu/experimental/data: sensor_msgs/msg/Imu
        /ap/navsat/navsat0: sensor_msgs/msg/NavSatFix
        /ap/pose/filtered: geometry_msgs/msg/PoseStamped
        /ap/tf_static: tf2_msgs/msg/TFMessage
        /ap/time: builtin_interfaces/msg/Time
        /ap/twist/filtered: geometry_msgs/msg/TwistStamped
      Service Servers:
        /ap/arm_motors: ardupilot_msgs/srv/ArmMotors
        /ap/mode_switch: ardupilot_msgs/srv/ModeSwitch
      Service Clients:

      Action Servers:

      Action Clients:

### Echo a topic published from ArduPilot

    $ ros2 topic echo /ap/geopose/filtered
    ---
    header:
      stamp:
        sec: 1726040592
        nanosec: 963366000
      frame_id: base_link
    pose:
      position:
        latitude: -35.36326217651367
        longitude: 149.1652374267578
        altitude: 584.0800170898438
      orientation:
        x: 0.0008078372338786721
        y: 0.0001052378211170435
        z: 0.7409986257553101
        w: 0.6715060472488403
    ---
## Gazebo, ROS2 and ardupilot

https://ardupilot.org/dev/docs/ros2-gazebo.html


### gazebo installation

gazebo refers to either gazebo classic or the new gazebo.
On my system, gazebo -version returns:

    $ gazebo -version
    Gazebo multi-robot simulator, version 11.10.2

This is the so called gazebo11. The new gazebo has versions refered to by names: harmonic, garden. It's possible to have classic and new gazebo coexist, it is even recommended, and can be done with (when an exisiting classic is installed as on my system):

    sudo add-apt-repository ppa:openrobotics/gazebo11-gz-cli
    sudo apt update
    sudo apt install gazebo11

References:

- https://gazebosim.org/docs/harmonic/install_gz11_side_by_side/
- https://gazebosim.org/docs/harmonic/install_ubuntu/

(to install gazebo harmonic)

    sudo apt update
    sudo apt install lsb-release gnupg

    sudo curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] http://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null
    sudo apt update
    sudo apt install gz-harmonic

Test by launching `gz sim` (works).

Add `export GZ_VERSION=harmonic` to ~/.bashrc.

Source .bashrc.

Pursue installation

### Update ROS dependencies:

    cd ~/ardu_ws
    source /opt/ros/humble/setup.bash
    sudo apt update
    rosdep update
    rosdep install --from-paths src --ignore-src -r

### Build and Run Tests¶

Build:

    cd ~/ardu_ws
    colcon build --packages-up-to ardupilot_gz_bringup

If you’d like to test your installation, run:

    cd ~/ardu_ws
    source install/setup.bash
    colcon test --packages-select ardupilot_sitl ardupilot_dds_tests ardupilot_gazebo ardupilot_gz_applications ardupilot_gz_description ardupilot_gz_gazebo ardupilot_gz_bringup
    colcon test-result --all --verbose

    Summary: 319 tests, 0 errors, 7 failures, 69 skipped
See also video:

https://www.youtube.com/watch?time_continue=1&v=HZKXrSAE-ac&embeds_referring_euri=https%3A%2F%2Fardupilot.org%2F&source_ve_path=Mjg2NjY




