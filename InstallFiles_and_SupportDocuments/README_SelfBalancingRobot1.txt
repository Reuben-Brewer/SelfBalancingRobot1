######################################################
######################################################

SelfBalancingRobot1

Code for self-balancing robot!

Reuben Brewer, Ph.D.

reuben.brewer@gmail.com

www.reubotics.com

Apache 2 License

Software Revision H, 09/24/2023

SelfBalancingRobot1.py verified working on:
Python 3.9
Windows  10 64-bit
Raspberry Pi Bullseye

######################################################
######################################################

###################################################### Python module installation instructions, all OS's
######################################################

######################################################
SelfBalancingRobot1.py, ListOfModuleDependencies: ['keyboard', 'LowPassFilter_ReubenPython2and3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class', 'PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class', 'PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class', 'RoboteqBLDCcontroller_ReubenPython2and3Class', 'scipy.spatial.transform']
SelfBalancingRobot1.py, ListOfModuleDependencies_TestProgram: []
SelfBalancingRobot1.py, ListOfModuleDependencies_NestedLayers: ['EntryListWithBlinking_ReubenPython2and3Class', 'ftd2xx', 'future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'LowPassFilter_ReubenPython2and3Class', 'LowPassFilterForDictsOfLists_ReubenPython2and3Class', 'numpy', 'pexpect', 'Phidget22', 'psutil', 'scipy.spatial.transform', 'serial', 'serial.tools', 'ZeroAndSnapshotData_ReubenPython2and3Class']
SelfBalancingRobot1.py, ListOfModuleDependencies_All:['EntryListWithBlinking_ReubenPython2and3Class', 'ftd2xx', 'future.builtins', 'Joystick2DdotDisplay_ReubenPython2and3Class', 'keyboard', 'LowPassFilter_ReubenPython2and3Class', 'LowPassFilterForDictsOfLists_ReubenPython2and3Class', 'MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class', 'MyPrint_ReubenPython2and3Class', 'numpy', 'pexpect', 'Phidget22', 'PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class', 'PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class', 'PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class', 'psutil', 'RoboteqBLDCcontroller_ReubenPython2and3Class', 'scipy.spatial.transform', 'serial', 'serial.tools', 'ZeroAndSnapshotData_ReubenPython2and3Class']

sudo pip install pygame
sudo pip install keyboard
sudo pip install pyserial (do NOT install "sudo pip install serial" or else you'll get the error "ModuleNotFoundError: No module named 'serial.tools'")
sudo pip install scipy (*AFTER* 'sudo apt install -y python3-scipy' if on Raspberry Pi)
sudo pip install numpy
sudo pip install ftd2xx #PROBABLY SKIP THIS IN UBUNTU AS IT'S VERY PAINFUL AND BUGGY

sudo chmod 777 -R ~/Desktop/
######################################################

######################################################
SelfBalancingRobot1.py run via command:
sudo ./Launch_SelfBalancingRobot1_Normal.sh
(if this script fails, then try "sudo chmod 777 Launch_SelfBalancingRobot1_Normal.sh" and "sudo dos2unix Launch_SelfBalancingRobot1_Normal.sh")
or
sudo python SelfBalancingRobot1.py "software_launch_method":"USERCLICKED"
(In Linux, may need to run as sudo to get the keyboard module to work properly. Definitely need to run as sudo to get the ftd2xx module to work.)
######################################################

######################################################
Set USB-Serial latency_timer

In Windows:

Manual method:
Follow the instructions in the included image "LatencyTimer_SetManuallyInWindows.png".

Automated method:
python LatencyTimer_DynamixelU2D2_ReadAndWrite_Windows.py

In Linux (including Raspberry Pi):
Run the included script:
sudo dos2unix LatencyTimer_Set_LinuxScript.sh
sudo chmod 777 LatencyTimer_Set_LinuxScript.sh
sudo ./LatencyTimer_Set_LinuxScript.sh 1
######################################################

###################################################### ftd2xx

########################## ftd2xx installation on Windows:
If the required driver is already on your Windows machine, then it will be installed automatically when the U2D2 is first plugged-in (note that this installation will occur separately for EACH separate USB port, and that the latency_timer will need to be set for EACH separate USB port.
However, if you don't see a new USB-Serial device appearing with a new "COM" number in Device Manger after Windows says it's done installing your new device, then you'll need to install the driver separately using Windows_FTDI_USBserial_driver_061020-->CDM21228_Setup.exe

To install the Python module:
pip3 install ftd2xx==1.0 (this 1.0 is VERY IMPORTANT as the later versions appear to have issues, including when installed from the whl file 'pip install C:\ftd2xx-1.1.2-py2-none-any.whl').
##########################

########################## ftd2xx installation on Raspberry Pi:

To install the Python module:
sudo pip3 install ftd2xx==1.0

####### IMPORTANT
sudo gedit /usr/local/lib/python3.7/dist-packages/ftd2xx/ftd2xx.py

Add the lines:
"elif sys.platform == 'linux':

	from . import _ftd2xx_linux as _ft"
right before the linux2 line (otherwise it breaks when run in Python 3).
Alternatively, you can copy Reuben's version of this file (ftd2xx_ReubenModified.py) to /usr/local/lib/python3.7/dist-packages/ftd2xx/ftd2xx.py.
#######

To install the driver:
Download the 1.4.6 ARMv6 hard-float (suits Raspberry Pi) source code from ftdi (http://www.ftdichip.com/Drivers/D2XX.htm) or use the included file.
Install following these instructions (modified from the readme that comes with the driver):

tar --extract --file libftd2xx-arm-v6-hf-1.4.6.tgz
cd release
cd build
sudo -s (become root)
cp libftd2xx.* /usr/local/lib
chmod 0755 /usr/local/lib/libftd2xx.so.1.4.6
ln -sf /usr/local/lib/libftd2xx.so.1.4.6 /usr/local/lib/libftd2xx.so
exit
THIS LAST STEP ISN'T IN THE READ ME BUT IS CRITICAL: 'sudo ldconfig' so that your code can find the new library.
##########################

########################## ftd2xx installation on Ubuntu (a very painful and buggy process which you might want to skip)

https://ftdichip.com/wp-content/uploads/2020/08/AN_220_FTDI_Drivers_Installation_Guide_for_Linux-1.pdf

https://ftdichip.com/drivers/d2xx-drivers/

https://ftdichip.com/wp-content/uploads/2022/07/libftd2xx-x86_64-1.4.27.tgz

sudo rmmod ftdi_sio #MIGHT HAVE TO DO THIS AFTER REBOOT
sudo rmmod usbserial #MIGHT HAVE TO DO THIS AFTER REBOOT
extract libftd2xx-x86_64-1.4.27.tgz #will put "release" folder onto the Desktop
sudo chmod 777 -R ~/Desktop/
sudo cp release/build/lib* /usr/local/lib

cd /usr/local/lib
sudo ln -s libftd2xx.so.1.4.27 libftd2xx.so
sudo chmod 0755 libftd2xx.so.1.4.27
sudo ldconfig #otherwise can’t find libftd2xx.so

check for cable: lsusb -v | grep "FT"

NOTE: CURRENTLY YOU HAVE TO USE SUDO FOR FTD2XX
##########################

######################################################

######################################################
######################################################

###################################################### Phidgets installation instructions, all OS's
######################################################

######################################################
https://pypi.org/project/Phidget22/#files

To install the Python module using pip:
pip install Phidget22       (with "sudo" if on Linux/Raspberry Pi)

To install the Python module from the downloaded .tar.gz file, enter downloaded folder and type "python setup.py install"
######################################################

###################################################### Library/driver installation instructions, Windows

https://www.phidgets.com/docs/OS_-_Windows

######################################################

###################################################### Library/driver installation instructions, Linux (other than Raspberry Pi)

https://www.phidgets.com/docs/OS_-_Linux#Quick_Downloads

######################################################

###################################################### Library/driver installation instructions, Raspberry Pi (models 2 and above)

https://www.phidgets.com/education/learn/getting-started-kit-tutorial/install-libraries/

curl -fsSL https://www.phidgets.com/downloads/setup_linux | sudo -E bash -
sudo apt-get install -y libphidget22

######################################################

######################################################
######################################################