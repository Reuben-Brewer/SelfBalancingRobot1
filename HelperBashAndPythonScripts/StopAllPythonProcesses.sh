#!/bin/sh
#IF THIS SCRIPT CAN'T BE FOUND OR RUN IN THE COMMAND TERMINAL, TYPE "dos2unix filename.sh" to remove ^M characters that are preenting it from running.

echo "StopAllPythonProcesses.sh running"
sudo python3 -u /home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3.py "python" "sigkill"
sudo python3 -u /home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3.py "python3" "sigkill"
exit
