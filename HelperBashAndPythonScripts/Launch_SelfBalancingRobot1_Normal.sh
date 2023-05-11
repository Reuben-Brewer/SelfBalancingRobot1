#!/bin/sh
#IF THIS SCRIPT CAN'T BE FOUND OR RUN IN THE COMMAND TERMINAL, TYPE "dos2unix filename.sh" to remove ^M characters that are preenting it from running.

CurrentTimeVariable=`date +%s`
echo "CurrentTimeVariable in seconds = $CurrentTimeVariable"

LogFileFullPath="/home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/LogFiles/SelfBalancingRobot1_ExecutionLog_$CurrentTimeVariable.txt"
echo "LogFileFullPath = $LogFileFullPath"

echo "Running Launch_SelfBalancingRobot1_Normal.sh" | tee -a $LogFileFullPath

echo "Launch_SelfBalancingRobot1_Normal.sh running GetPIDsByProcessEnglishNameAndOptionallyKill.py" | tee -a $LogFileFullPath
sudo python3 -u /home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3.py "python" "sigkill" | tee -a $LogFileFullPath
sudo python3 -u /home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3.py "python3" "sigkill" | tee -a $LogFileFullPath

echo "Launch_SelfBalancingRobot1_Normal.sh running SelfBalancingRobot1.py" | tee -a $LogFileFullPath
sudo python3 -u /home/pi/Desktop/SelfBalancingRobot1_PythonDeploymentFiles/SelfBalancingRobot1.py "SOFTWARE_LAUNCH_METHOD:USERCLICKED" | tee -a $LogFileFullPath

exit
