# ardurover

## required items

- chassis (a wood plank can work!)
- motors
- motor controller
- encoder (optional, see below)
- wheels
- autopilot (flight controller)
- cabling
- RC

### autopilot

Autopilot supported by ardupilot rover:
https://ardupilot.org/rover/docs/common-autopilots.html


### motors and motor drivers

https://ardupilot.org/rover/docs/common-brushed-motors.html

Supported (verified) drivers from pololu:

https://ardupilot.org/rover/docs/common-brushed-motors.html
Pololu G2 High-Power Motor Driver supports “BrushedWithRelay”
Pololu DRV8838 Motor Driver supports “BrushedWithRelay”
The [DRV8835](https://www.pololu.com/product/2135) is the dual version of the DRV8838 and will work fine too.


### encoders

ArduRover doesn't require encoders from the motor signal, but they can be used as an optional input to the autopilot to improve performance. 
The system can operate using other sensors for navigation, such as GPS and Inertial Measurement Units (IMUs). 

*Scenarios when encoders are not required*


- GPS-based navigation in outdoor environments, 
- Simple manual or RC control

*Benefits of using encoders*

Integrating wheel encoders improves the vehicle's navigation.

- Improved position estimation: (By measuring wheel rotation, encoders can improve the accuracy of position and distance traveled)
- Better speed control: Encoders provide more accurate feedback on wheel speed, allowing for more precise throttle control.
- More accurate turning: For vehicles with skid-steer systems (like tanks, the pololu romi, etc...), encoders help the autopilot better determine how far each wheel has turned, which can help reduce error accumulation from wheel slip during turns.
- Support for the Extended Kalman Filter (EKF3): For advanced and more accurate navigation, ArduRover uses an EKF to fuse sensor data. Encoders can be integrated into the EKF3 algorithm to improve the vehicle's position estimation. 

*Using encoders with ArduRover*

https://ardupilot.org/rover/docs/wheel-encoder.html

Connect their A and B outputs to the autopilot's GPIO pins, such as the AUX OUT pins on a Pixhawk controller. 
Configure parameters in ArduRover: 

    WENC_TYPE and WENC2_TYPE
    WENC_CPR (Counts Per Revolution)
    WENC_RADIUS (Wheel Radius)
    EKF3 parameters to enable encoder data input

## posts from the forum

https://discuss.ardupilot.org/t/ardurover-with-the-pololu-romi/41991


## flash the bootloader on the autopilot

https://ardupilot.org/planner/docs/common-loading-firmware-onto-chibios-only-boards.html
and:
https://www.mateksys.com/?p=6905

https://ardupilot.org/rover/docs/common-matekh743-wing.html

Got the mateksys h743-SLIM v3 (EOL)

https://www.mateksys.com/?portfolio=h743-slim#tab-id-3


STM32CubeProgrammer: Download the latest version  for Linux from the STMicroelectronics website. 

https://www.st.com/en/development-tools/stm32cubeprog.html#get-software

ArduRover Firmware: Go to the ArduPilot firmware server to download the correct firmware for your board.

    Navigate to https://firmware.ardupilot.org. (https://firmware.ardupilot.org/Rover/latest/MatekH743/)
    Click on Rover.
    Select the stable or latest version.
    Look for the folder that matches your flight controller, which is MatekH743.
    Download the .hex file that includes the bootloader in its name, such as ardurover_with_bl.hex

Flashing the FW on the autopilot
1. Install STM32CubeProgrammer

    Make the installer executable and run it with root privileges.

    chmod +x SetupSTM32CubeProgrammer-*.linux
    sudo ./SetupSTM32CubeProgrammer-*.linux


Follow the on-screen instructions to complete the installation. 

I ended up with is installed in /usr/local, start it with:

    sudo /usr/local/STMicroelectronics/STM32Cube/STM32CubeProgrammer/bin/./STM32CubeProgrammerLauncher

2. Prepare the Matek H743-Slim

    Press and hold the BOOT button on the Matek H743-Slim
    While holding the button, connect the flight controller to computer using a USB-C cable.
    Release the BOOT button after connecting. The board is now in Device Firmware Update (DFU) mode. 

3. Flash the firmware with STM32CubeProgrammer

    Launch the STM32CubeProgrammer application.
    In the main window, look for the connection options on the right side. Select the USB connection type.
    Click the Refresh button. A USB port should appear in the dropdown menu.
    Click the Connect button.
    On the left-hand "3 lines icon" menu, select the Erasing & Programming tab.
    Click the Browse button and select the ardurover_with_bl.hex file you downloaded earlier.
    Check the box for Full chip erase. This is highly recommended for a clean install, especially if you are switching from a different firmware like Betaflight or INAV.
    Click Start Programming to begin the flash process.
    Wait for the process to complete. A message confirming a successful flash will be displayed. 

4. Post-flashing steps

    After the programming is finished, click Disconnect in STM32CubeProgrammer.
    Unplug the USB cable from the flight controller.
    Plug the USB cable back in (without holding the BOOT button) to allow the board to boot normally into ArduRover firmware.
    You can now connect to the board using an ArduPilot ground station software like QGroundControl to continue configuration.

Done 22oct2025, on the gonze, and QGC on the FW recognizes the autopilot as a rover.
