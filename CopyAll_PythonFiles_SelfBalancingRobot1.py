# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision N, 02/02/2025

Verified working on: Python 3.12 for Windows 11 64-bit and Raspberry Pi Bullseye.
'''

__author__ = 'reuben.brewer'

#########################################################
import os
import sys
import time
import datetime
import shutil #For copying file
import traceback
#########################################################

#########################################################
import distutils #For CopyEntireDirectoryWithContents(). Both imports are needed to avoid errors in 'distutils.dir_util.copy_tree("./foo", "./bar")'
from distutils import dir_util #For CopyEntireDirectoryWithContents(). Both imports are needed to avoid errors in 'distutils.dir_util.copy_tree("./foo", "./bar")'
#########################################################

#######################################################################################################################
def CreateNewDirectoryIfItDoesntExist(directory):
    try:
        #print("CreateNewDirectoryIfItDoesntExist, directory: " + directory)
        if os.path.isdir(directory) == 0: #No directory with this name exists
            os.makedirs(directory)
    except:
        exceptions = sys.exc_info()[0]
        print("CreateNewDirectoryIfItDoesntExist, Exceptions: %s" % exceptions)
        traceback.print_exc()
#######################################################################################################################

#######################################################################################################################
def CopyEntireDirectoryWithContents(SourceDir, DestDir): #Destination directory doesn't need to exist first
    distutils.dir_util.copy_tree(SourceDir, DestDir)  # Copies the entire directoy
#######################################################################################################################

#######################################################################################################################
def getTimeStampString():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m_%d_%Y---%H_%M_%S')

    return st
#######################################################################################################################

#######################################################################################################################
def IsTheTimeCurrentlyAM():
    ts = time.time()
    hour = int(datetime.datetime.fromtimestamp(ts).strftime('%H'))
    if hour < 12:
        return 1
    else:
        return 0
#######################################################################################################################

FileWorkingDirectory = "E:\\" #Use "E:\\" if the filepath length is too long
#FileWorkingDirectory = os.getcwd() #Use "E:\\" if the filepath length is too long

AMflag = IsTheTimeCurrentlyAM()
if AMflag == 1:
    AMorPMstring = "AM"
else:
    AMorPMstring = "PM"

FileDirectoryToCreate = FileWorkingDirectory + "\\SelfBalancingRobot1_PythonDeploymentFiles_" + getTimeStampString() + AMorPMstring
CreateNewDirectoryIfItDoesntExist(FileDirectoryToCreate)

#######################
ParametersToBeLoaded_DirectoryToCopy = FileWorkingDirectory + "\\ParametersToBeLoaded"
#######################

try:
    shutil.copy("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\SelfBalancingRobot1.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\SelfBalancingRobot1_NonAdmin.bat", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\CopyAll_PythonFiles_SelfBalancingRobot1.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\ExcelPlot_CSVdataLogger_ReubenPython3Code__SelfBalancingRobot1.py", FileDirectoryToCreate)

    CopyEntireDirectoryWithContents("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\ParametersToBeLoaded", FileDirectoryToCreate + "\\ParametersToBeLoaded") #Copies the entire directory
    CopyEntireDirectoryWithContents("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\InstallFiles_and_SupportDocuments", FileDirectoryToCreate + "\\InstallFiles_and_SupportDocuments") #Copies the entire directory
    CopyEntireDirectoryWithContents("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\HelperBashAndPythonScripts", FileDirectoryToCreate + "\\HelperBashAndPythonScripts") #Copies the entire directory
    CopyEntireDirectoryWithContents("G:\\My Drive\\CodeReuben\\SelfBalancingRobot1\\IconDesktopAndRClocalFiles", FileDirectoryToCreate + "\\IconDesktopAndRClocalFiles") #Copies the entire directory
    CreateNewDirectoryIfItDoesntExist(FileDirectoryToCreate + "\\LogFiles")

    #shutil.copy("G:\\My Drive\\CodeReuben\\ArucoTagDetectionFromCameraFeed_ReubenPython3Class\\ArucoTagDetectionFromCameraFeed_ReubenPython3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\ArucoTagDetectionFromCameraFeed_ReubenPython3Class\\test_program_for_ArucoTagDetectionFromCameraFeed_ReubenPython3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\BarGraphDisplay_ReubenPython3Class\\BarGraphDisplay_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\BarGraphDisplay_ReubenPython3Class\\test_program_for_BarGraphDisplay_ReubenPython3Class.py", FileDirectoryToCreate)

    #shutil.copy("G:\\My Drive\\CodeReuben\\CameraStreamerClass_ReubenPython2and3Class\\CameraStreamerClass_ReubenPython2and3Class.py", FileDirectoryToCreate)
    #shutil.copy("G:\\My Drive\\CodeReuben\\CameraStreamerClass_ReubenPython2and3Class\\test_program_for_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\CSVdataLogger_ReubenPython3Class\\CSVdataLogger_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\CSVdataLogger_ReubenPython3Class\\test_program_for_CSVdataLogger_ReubenPython3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\EntryListWithBlinking_ReubenPython2and3Class\\EntryListWithBlinking_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\EntryListWithBlinking_ReubenPython2and3Class\\test_program_for_EntryListWithBlinking_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3\\GetPIDsByProcessEnglishNameAndOptionallyKill_ReubenPython2and3.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\Joystick2DdotDisplay_ReubenPython2and3Class\\Joystick2DdotDisplay_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\Joystick2DdotDisplay_ReubenPython2and3Class\\test_program_for_Joystick2DdotDisplay_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilter_ReubenPython2and3Class\\LowPassFilter_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilter_ReubenPython2and3Class\\test_program_for_LowPassFilter_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilterForDictsOfLists_ReubenPython2and3Class\\LowPassFilterForDictsOfLists_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\LowPassFilterForDictsOfLists_ReubenPython2and3Class\\test_program_for_LowPassFilterForDictsOfLists_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class\\test_program_for_MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\MyPrint_ReubenPython2and3Class\\MyPrint_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\MyPrint_ReubenPython2and3Class\\test_program_for_MyPrint_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\Phidgets4EncoderAndDInput1047_ReubenPython2and3Class\\Phidgets4EncoderAndDInput1047_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\Phidgets4EncoderAndDInput1047_ReubenPython2and3Class\\test_program_for_Phidgets4EncoderAndDInput1047_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class\\PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class\\test_program_for_PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class\\PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class\\test_program_for_PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class\\PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class\\test_program_for_PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\RoboteqBLDCcontroller_ReubenPython2and3Class\\RoboteqBLDCcontroller_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\RoboteqBLDCcontroller_ReubenPython2and3Class\\test_program_for_RoboteqBLDCcontroller_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\RoboteqBLDCcontroller_ReubenPython2and3Class\\RoboteqBLDCcontroller_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\RoboteqBLDCcontroller_ReubenPython2and3Class\\test_program_for_RoboteqBLDCcontroller_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\UDPdataExchanger_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\test_program_for_UDPdataExchanger_ReubenPython3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Rx_BareBonesUDPtest_ReubenPython3.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Tx_BareBonesUDPtest_ReubenPython3.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Tx___INTERNAL_test_program_for_UDPdataExchanger_ReubenPython3Class_NonAdmin.bat", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Rx___INTERNAL_test_program_for_UDPdataExchanger_ReubenPython3Class_NonAdmin.bat", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Tx___EXTERNAL_test_program_for_UDPdataExchanger_ReubenPython3Class_NonAdmin.bat", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\UDPdataExchanger_ReubenPython3Class\\Rx___EXTERNAL_test_program_for_UDPdataExchanger_ReubenPython3Class_NonAdmin.bat", FileDirectoryToCreate)

    shutil.copy("G:\\My Drive\\CodeReuben\\ZeroAndSnapshotData_ReubenPython2and3Class\\ZeroAndSnapshotData_ReubenPython2and3Class.py", FileDirectoryToCreate)
    shutil.copy("G:\\My Drive\\CodeReuben\\ZeroAndSnapshotData_ReubenPython2and3Class\\test_program_for_ZeroAndSnapshotData_ReubenPython2and3Class.py", FileDirectoryToCreate)

    shutil.make_archive(FileDirectoryToCreate, 'zip', FileDirectoryToCreate)

except:
    exceptions = sys.exc_info()[0]
    print("CopyAll_PythonFiles_SelfBalancingRobot1 ERROR, Exceptions: %s" % exceptions)
    traceback.print_exc()

print("CopyAll_PythonFiles_SelfBalancingRobot1 copied all files successfully.")
