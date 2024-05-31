# ardupilot2know

## Intro

## Parameters, logs and messages

See the README in directory param_log_msg.

## ardupilot and ROS and Gazebo

## Install ardupilot

Installed in `$HOME/builds/ArduPilot` on the gonze.

    git clone --recurse-submodules git@github.com:ArduPilot/ardupilot.git
    cd ardupilot/

    Tools/environment_install/install-prereqs-ubuntu.sh -y
    . ~/.profile


https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux

    $ ./waf list_boards
    ACNS-CM4Pilot ACNS-F405AIO aero AeroFox-Airspeed AeroFox-Airspeed-DLVR AeroFox-GNSS_F9P AeroFox-PMU airbotf4 AIRLink Airvolute-DCS2 AnyleafH7 Aocoda-RC-H743Dual AR-F407SmartBat ARK_CANNODE ARK_GPS ARK_RTK_GPS ARKV6X AtomRCF405NAVI bbbmini BeastF7 BeastF7v2 BeastH7 BeastH7v2 bebop BETAFPV-F405 bhat BirdCANdy BlitzF745AIO blue BotBloxSwitch C-RTK2-HP canzero CarbonixF405 CarbonixL496 crazyflie2 CUAV-Nora CUAV-Nora-bdshot CUAV-X7 CUAV-X7-bdshot CUAV_GPS CUAVv5 CUAVv5-bdshot CUAVv5Nano CUAVv5Nano-bdshot CubeBlack CubeBlack+ CubeBlack-periph CubeGreen-solo CubeOrange CubeOrange-bdshot CubeOrange-joey CubeOrange-ODID CubeOrange-periph CubeOrange-periph-heavy CubeOrange-SimOnHardWare CubeOrangePlus CubeOrangePlus-bdshot CubeOrangePlus-SimOnHardWare CubePilot-CANMod CubePilot-PPPGW CubePurple CubeRedPrimary CubeRedPrimary-PPPGW CubeRedSecondary CubeSolo CubeYellow CubeYellow-bdshot dark DevEBoxH7v2 disco DrotekP3Pro Durandal Durandal-bdshot edge erleboard erlebrain2 esp32buzz esp32diy esp32empty esp32icarus esp32nick esp32s3devkit esp32s3empty esp32tomte76 f103-ADSB f103-Airspeed f103-GPS f103-HWESC f103-QiotekPeriph f103-RangeFinder f103-Trigger f303-GPS f303-HWESC f303-M10025 f303-M10070 f303-MatekGPS f303-PWM f303-TempSensor f303-Universal F35Lightning f405-MatekAirspeed f405-MatekGPS F4BY FlyingMoonF407 FlyingMoonF427 FlyingMoonH743 FlywooF405Pro FlywooF405S-AIO FlywooF745 FlywooF745Nano fmuv2 fmuv3 fmuv3-bdshot fmuv5 FoxeerH743v1 FreeflyRTK G4-ESC H757I_EVAL H757I_EVAL_intf HEEWING-F405 HEEWING-F405v2 Here4AP Here4FC Hitec-Airspeed HitecMosaic HolybroG4_Compass HolybroG4_GPS HolybroGPS iomcu iomcu-dshot iomcu-f103 iomcu-f103-dshot iomcu_f103_8MHz JFB100 JFB110 JHEM_JHEF405 JHEMCU-GSF405A JHEMCU-GSF405A-RX2 KakuteF4 KakuteF4Mini KakuteF7 KakuteF7-bdshot KakuteF7Mini KakuteH7 KakuteH7-bdshot KakuteH7-Wing KakuteH7Mini KakuteH7Mini-Nand KakuteH7v2 kha_eth linux luminousbee4 luminousbee5 MambaF405-2022 MambaF405US-I2C MambaF405v2 MambaH743v4 MatekF405 MatekF405-bdshot MatekF405-CAN MatekF405-STD MatekF405-TE MatekF405-TE-bdshot MatekF405-Wing MatekF405-Wing-bdshot MatekF765-SE MatekF765-Wing MatekF765-Wing-bdshot MatekH743 MatekH743-bdshot MatekH743-periph MatekH7A3 MatekL431-ADSB MatekL431-Airspeed MatekL431-BattMon MatekL431-bdshot MatekL431-DShot MatekL431-EFI MatekL431-GPS MatekL431-HWTelem MatekL431-MagHiRes MatekL431-Periph MatekL431-Proximity MatekL431-Rangefinder MatekL431-RC MatekL431-Serial MazzyStarDrone MicoAir405v2 mindpx-v2 mini-pix modalai_fc-v1 mRo-M10095 mRoCANPWM-M10126 mRoControlZeroClassic mRoControlZeroF7 mRoControlZeroH7 mRoControlZeroH7-bdshot mRoControlZeroOEMH7 mRoCZeroOEMH7-bdshot mRoKitCANrevC mRoNexus mRoPixracerPro mRoPixracerPro-bdshot mRoX21 mRoX21-777 navigator navio navio2 Nucleo-G491 Nucleo-L476 Nucleo-L496 NucleoH743 NucleoH755 obal ocpoc_zynq omnibusf4 omnibusf4pro omnibusf4pro-bdshot omnibusf4pro-one omnibusf4v6 OMNIBUSF7V2 OmnibusNanoV6 OmnibusNanoV6-bdshot OrqaF405Pro PH4-mini PH4-mini-bdshot Pix32v5 PixC4-Jetson PixFlamingo PixFlamingo-F767 Pixhawk1 Pixhawk1-1M Pixhawk1-1M-bdshot Pixhawk1-bdshot Pixhawk4 Pixhawk4-bdshot Pixhawk5X Pixhawk6C Pixhawk6C-bdshot Pixhawk6X Pixhawk6X-bdshot Pixhawk6X-ODID Pixhawk6X-PPPGW PixPilot-C3 PixPilot-V3 PixPilot-V6 Pixracer Pixracer-bdshot Pixracer-periph PixSurveyA1 PixSurveyA1-IND PixSurveyA2 pocket pxf pxfmini QioTekAdeptF407 QioTekZealotF427 QioTekZealotH743 QioTekZealotH743-bdshot R9Pilot RadiolinkPIX6 RADIX2HD ReaperF745 revo-mini revo-mini-bdshot revo-mini-i2c revo-mini-i2c-bdshot revo-mini-sd rFCU rGNSS rst_zynq SDMODELH7V1 Sierra-F405 Sierra-F412 Sierra-F9P Sierra-L431 Sierra-PrecisionPoint Sierra-TrueNavIC Sierra-TrueNavPro Sierra-TrueNavPro-G4 Sierra-TrueNorth Sierra-TrueSpeed sitl SITL_arm_linux_gnueabihf sitl_periph sitl_periph_gps sitl_periph_universal SITL_static SITL_x86_64_linux_gnu SIYI_N7 SkystarsH7HD SkystarsH7HD-bdshot skyviper-f412-rev1 skyviper-journey skyviper-v2450 sparky2 speedybeef4 SpeedyBeeF405Mini SpeedyBeeF405WING speedybeef4v3 speedybeef4v4 SPRacingH7 SPRacingH7RF SuccexF4 sw-nav-f405 sw-spar-f407 Swan-K1 TBS-Colibri-F7 thepeach-k1 thepeach-r1 TMotorH743 vnav VRBrain-v51 VRBrain-v52 VRBrain-v54 VRCore-v10 VRUBrain-v51 YJUAV_A6 YJUAV_A6SE YJUAV_A6SE_H743 YJUAV_A6Ultra ZubaxGNSS zynq

Info:

https://ardupilot.org/dev/docs/building-the-code.html

https://ardupilot.org/dev/docs/building-setup-linux.html#building-setup-linux

github:
https://github.com/ArduPilot/ardupilot
Test:
https://github.com/ArduPilot/ardupilot/blob/master/BUILD.md


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

