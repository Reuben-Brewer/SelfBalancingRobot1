# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision G, 05/10/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
from Joystick2DdotDisplay_ReubenPython2and3Class import *
from LowPassFilter_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import math
import collections
from copy import * #for deepcopy
import inspect #To enable 'TellWhichFileWereIn'
import threading
import traceback
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
#########################################################

#########################################################
if sys.version_info[0] < 3:
    import Queue  # Python 2
else:
    import queue as Queue  # Python 3
#########################################################

#########################################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
######################################################### "sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

#########################################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

#########################################################
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Net import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.DigitalInput import *
from Phidget22.Devices.DigitalOutput import *
from Phidget22.Devices.VoltageInput import *
from Phidget22.Devices.VoltageRatioInput import *
#########################################################

class PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    #######################################################################################################################
    #######################################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__ starting. ####################")

        #########################################################
        #########################################################
        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = -1
        self.EnableInternal_MyPrint_Flag = 0
        self.MainThread_still_running_flag = 0

        self.StartingTime_GlobalAcrossAllThreads = self.getPreciseSecondsTimeStampString()

        ###
        self.CurrentTime_CalculatedFromMainThread = -11111.0
        self.LastTime_CalculatedFromMainThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromMainThread = -11111.0
        self.DataStreamingDeltaT_CalculatedFromMainThread = -11111.0

        self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback = -11111.0
        self.LastTime_TimestampFromVoltageRatioInput0DataCallback = -11111.0
        self.DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = -11111.0
        self.DataStreamingDeltaT_TimestampFromVoltageRatioInput0DataCallback = -11111.0

        self.CurrentTime_TimestampFromVoltageRatioInput1DataCallback = -11111.0
        self.LastTime_TimestampFromVoltageRatioInput1DataCallback = -11111.0
        self.DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = -11111.0
        self.DataStreamingDeltaT_TimestampFromVoltageRatioInput1DataCallback = -11111.0

        self.CurrentTime_TimestampFromDigitalInput0DataCallback = -11111.0
        self.LastTime_TimestampFromDigitalInput0DataCallback = -11111.0
        self.DataStreamingFrequency_TimestampFromDigitalInput0DataCallback = -11111.0
        self.DataStreamingDeltaT_TimestampFromDigitalInput0DataCallback = -11111.0

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach = -11111.0
        self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Attach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach = -1

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach = -11111.0
        self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Detach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach = -1

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach = -11111.0
        self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Attach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach = -1

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach = -11111.0
        self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Detach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach = -1

        self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach = -11111.0
        self.LastTime_TimestampForEventFiring_DigitalInput0Object_Attach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Attach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach = -1

        self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach = -11111.0
        self.LastTime_TimestampForEventFiring_DigitalInput0Object_Detach = -11111.0
        self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Detach = -1
        self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach = -1
        ###

        self.VoltageRatioInput0Object_DeviceConnectedFlag = 0
        self.VoltageRatioInput1Object_DeviceConnectedFlag = 0
        self.DigitalInput0Object_DeviceConnectedFlag = 0

        self.VoltageRatioInput0Object_VoltageRatio = -11111.0
        self.VoltageRatioInput1Object_VoltageRatio = -11111.0
        self.DigitalInput0Object_State = 0

        self.MostRecentDataDict = dict()

        self.VoltageRatioInput0Object_DataEventHandler_Queue = Queue.Queue()
        self.VoltageRatioInput1Object_DataEventHandler_Queue = Queue.Queue()
        self.DigitalInput0Object_DataEventHandler_Queue = Queue.Queue()

        #########################################################
        #########################################################
        self.DetectedDeviceName = "default"
        self.DetectedDeviceID = "default"
        self.DetectedDeviceVersion = "default"
        self.DetectedDeviceSerialNumber = "default"
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if platform.system() == "Linux":

            if "raspberrypi" in platform.uname(): #os.uname() doesn't work in windows
                self.my_platform = "pi"
            else:
                self.my_platform = "linux"

        elif platform.system() == "Windows":
            self.my_platform = "windows"

        elif platform.system() == "Darwin":
            self.my_platform = "mac"

        else:
            self.my_platform = "other"

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "GUIparametersDict" in setup_dict:
            self.GUIparametersDict = setup_dict["GUIparametersDict"]

            #########################################################
            #########################################################
            if "USE_GUI_FLAG" in self.GUIparametersDict:
                self.USE_GUI_FLAG = self.PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", self.GUIparametersDict["USE_GUI_FLAG"])
            else:
                self.USE_GUI_FLAG = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, must pass in 'root'")
                return
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: NumberOfPrintLines: " + str(self.NumberOfPrintLines))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: GUIparametersDict: " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VINT_DesiredSerialNumber" in setup_dict:
            try:
                self.VINT_DesiredSerialNumber = int(setup_dict["VINT_DesiredSerialNumber"])
            except:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, VINT_DesiredSerialNumber invalid.")
        else:
            self.VINT_DesiredSerialNumber = -1

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VINT_DesiredSerialNumber: " + str(self.VINT_DesiredSerialNumber))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VINT_DesiredPortNumber" in setup_dict:
            try:
                self.VINT_DesiredPortNumber = int(setup_dict["VINT_DesiredPortNumber"])
            except:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, VINT_DesiredPortNumber invalid.")
        else:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, must initialize object with 'VINT_DesiredPortNumber' argument.")
            return

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VINT_DesiredPortNumber: " + str(self.VINT_DesiredPortNumber))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DesiredDeviceID" in setup_dict:
            try:
                self.DesiredDeviceID = int(setup_dict["DesiredDeviceID"])
            except:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, DesiredDeviceID invalid.")
        else:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: ERROR, must initialize object with 'DesiredDeviceID' argument.")
            return

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: DesiredDeviceID: " + str(self.DesiredDeviceID))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in setup_dict:
            self.NameToDisplay_UserSet = str(setup_dict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: NameToDisplay_UserSet + " + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WaitForAttached_TimeoutDuration_Milliseconds" in setup_dict:
            self.WaitForAttached_TimeoutDuration_Milliseconds = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("WaitForAttached_TimeoutDuration_Milliseconds", setup_dict["WaitForAttached_TimeoutDuration_Milliseconds"], 0.0, 60000.0))

        else:
            self.WaitForAttached_TimeoutDuration_Milliseconds = 5000

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WaitForAttached_TimeoutDuration_Milliseconds: " + str(self.WaitForAttached_TimeoutDuration_Milliseconds))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "UsePhidgetsLoggingInternalToThisClassObjectFlag" in setup_dict:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UsePhidgetsLoggingInternalToThisClassObjectFlag", setup_dict["UsePhidgetsLoggingInternalToThisClassObjectFlag"])
        else:
            self.UsePhidgetsLoggingInternalToThisClassObjectFlag = 1

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: UsePhidgetsLoggingInternalToThisClassObjectFlag: " + str(self.UsePhidgetsLoggingInternalToThisClassObjectFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "MainThread_TimeToSleepEachLoop" in setup_dict:
            self.MainThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("MainThread_TimeToSleepEachLoop", setup_dict["MainThread_TimeToSleepEachLoop"], 0.001, 100000)

        else:
            self.MainThread_TimeToSleepEachLoop = 0.005

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: MainThread_TimeToSleepEachLoop: " + str(self.MainThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "UpdateDeltaT_ms" in setup_dict:
            self.UpdateDeltaT_ms = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("UpdateDeltaT_ms", setup_dict["UpdateDeltaT_ms"], 20.0, 1000.0))
        else:
            self.UpdateDeltaT_ms = 20

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: UpdateDeltaT_ms: " + str(self.UpdateDeltaT_ms))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WirelessVINThub_ServerName_Str" in setup_dict:
            self.WirelessVINThub_ServerName_Str = str(setup_dict["WirelessVINThub_ServerName_Str"])
        else:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Error, 'WirelessVINThub_ServerName_Str' must be specified.")
            return

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WirelessVINThub_ServerName_Str: " + str(self.WirelessVINThub_ServerName_Str))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WirelessVINThub_Address_Str" in setup_dict:
            self.WirelessVINThub_Address_Str = str(setup_dict["WirelessVINThub_Address_Str"])
        else:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Error, 'WirelessVINThub_Address_Str' must be specified.")
            return

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WirelessVINThub_Address_Str: " + str(self.WirelessVINThub_Address_Str))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WirelessVINThub_Port_Int" in setup_dict:
            self.WirelessVINThub_Port_Int = int(setup_dict["WirelessVINThub_Port_Int"])
        else:
            self.WirelessVINThub_Port_Int = 5661

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WirelessVINThub_Port_Int: " + str(self.WirelessVINThub_Port_Int))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str" in setup_dict:
            self.WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str = str(setup_dict["WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str"])
        else:
            self.WirelessVINThub_Password_Str = ""

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str: " + str(self.WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "WirelessVINThub_Flags_Int" in setup_dict:
            self.WirelessVINThub_Flags_Int = int(setup_dict["WirelessVINThub_Flags_Int"])

            if self.WirelessVINThub_Flags_Int != 0:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: CAUTION, Phidgets API says that 'WirelessVINThub_Flags_Int' should be set to 0. Are you sure that you want to set it to " + str(self.WirelessVINThub_Flags_Int) + "?")
        else:
            self.WirelessVINThub_Flags_Int = 0

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: WirelessVINThub_Flags_Int: " + str(self.WirelessVINThub_Flags_Int))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VoltageRatioInput0Object_SteadyStateOffset" in setup_dict:
            self.VoltageRatioInput0Object_SteadyStateOffset = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("VoltageRatioInput0Object_SteadyStateOffset", setup_dict["VoltageRatioInput0Object_SteadyStateOffset"], -1.0, 1.0)
        else:
            self.VoltageRatioInput0Object_SteadyStateOffset = 0

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VoltageRatioInput0Object_SteadyStateOffset: " + str(self.VoltageRatioInput0Object_SteadyStateOffset))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VoltageRatioInput1Object_SteadyStateOffset" in setup_dict:
            self.VoltageRatioInput1Object_SteadyStateOffset = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("VoltageRatioInput1Object_SteadyStateOffset", setup_dict["VoltageRatioInput1Object_SteadyStateOffset"], -1.0, 1.0)
        else:
            self.VoltageRatioInput1Object_SteadyStateOffset = 0

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VoltageRatioInput1Object_SteadyStateOffset: " + str(self.VoltageRatioInput1Object_SteadyStateOffset))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VoltageRatioInput0Object_LowPassFilter_Lambda" in setup_dict:
            self.VoltageRatioInput0Object_LowPassFilter_Lambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("VoltageRatioInput0Object_LowPassFilter_Lambda", setup_dict["VoltageRatioInput0Object_LowPassFilter_Lambda"], 0.0, 1.0)
        else:
            self.VoltageRatioInput0Object_LowPassFilter_Lambda = 1.0 #Default to no filtering, new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VoltageRatioInput0Object_LowPassFilter_Lambda: " + str(self.VoltageRatioInput0Object_LowPassFilter_Lambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VoltageRatioInput1Object_LowPassFilter_Lambda" in setup_dict:
            self.VoltageRatioInput1Object_LowPassFilter_Lambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("VoltageRatioInput1Object_LowPassFilter_Lambda", setup_dict["VoltageRatioInput1Object_LowPassFilter_Lambda"], 0.0, 1.0)
        else:
            self.VoltageRatioInput1Object_LowPassFilter_Lambda = 1.0 #Default to no filtering, new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VoltageRatioInput1Object_LowPassFilter_Lambda: " + str(self.VoltageRatioInput1Object_LowPassFilter_Lambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.VoltageRatioInput0Object_LowPassFilter_Lambda_Object =  LowPassFilter_ReubenPython2and3Class(dict([("UseMedianFilterFlag", 1),
                                                    ("UseExponentialSmoothingFilterFlag", 1),
                                                    ("ExponentialSmoothingFilterLambda", self.VoltageRatioInput0Object_LowPassFilter_Lambda)]))

            self.VoltageRatioInput1Object_LowPassFilter_Lambda_Object =  LowPassFilter_ReubenPython2and3Class(dict([("UseMedianFilterFlag", 1),
                                                    ("UseExponentialSmoothingFilterFlag", 1),
                                                    ("ExponentialSmoothingFilterLambda", self.VoltageRatioInput1Object_LowPassFilter_Lambda)]))
        except:
            exceptions = sys.exc_info()[0]
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.PrintToGui_Label_TextInputHistory_List = [" "]*self.NumberOfPrintLines
        self.PrintToGui_Label_TextInput_Str = ""
        self.GUI_ready_to_be_updated_flag = 0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            Net.addServer(self.WirelessVINThub_ServerName_Str,
                          self.WirelessVINThub_Address_Str,
                          self.WirelessVINThub_Port_Int,
                          self.WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str, #Note that the server password is a different parameter than the VINT-generated wireless Access Point password!
                          self.WirelessVINThub_Flags_Int)

        except PhidgetException as e:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed 'Net.addServer', Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.VoltageRatioInput0Object = VoltageRatioInput()
            self.VoltageRatioInput1Object = VoltageRatioInput()
            self.DigitalInput0Object = DigitalInput()
        except PhidgetException as e:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to create VoltageRatioInput and DigitalInput objects, Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.VINT_DesiredSerialNumber != -1:
            try:
                self.VoltageRatioInput0Object.setDeviceSerialNumber(int(self.VINT_DesiredSerialNumber))
                self.VoltageRatioInput1Object.setDeviceSerialNumber(int(self.VINT_DesiredSerialNumber))
                self.DigitalInput0Object.setDeviceSerialNumber(int(self.VINT_DesiredSerialNumber))

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed 'setDeviceSerialNumber', Phidget Exception %i: %s" % (e.code, e.details))
                return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.VoltageRatioInput0Object.setHubPort(self.VINT_DesiredPortNumber)
            self.VoltageRatioInput0Object.setIsRemote(True)
            self.VoltageRatioInput0Object.setChannel(0) #Tell which axis.

            self.VoltageRatioInput1Object.setHubPort(self.VINT_DesiredPortNumber)
            self.VoltageRatioInput1Object.setIsRemote(True)
            self.VoltageRatioInput1Object.setChannel(1) #Tell which axis.

            self.DigitalInput0Object.setHubPort(self.VINT_DesiredPortNumber)
            self.DigitalInput0Object.setIsRemote(True)

        except PhidgetException as e:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed 'setHubPort' or 'setIsRemote', Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:

            self.VoltageRatioInput0Object.setOnVoltageRatioChangeHandler(self.Phidgets_VoltageRatioInput0Object_VoltageRatioChange_EventHandler)
            self.VoltageRatioInput0Object.setOnAttachHandler(self.Phidgets_VoltageRatioInput0Object_Attach_EventHandler)
            self.VoltageRatioInput0Object.setOnDetachHandler(self.Phidgets_VoltageRatioInput0Object_Detach_EventHandler)
            self.VoltageRatioInput0Object.setOnErrorHandler(self.Phidgets_VoltageRatioInput0Object_Error_EventHandler)

            self.VoltageRatioInput1Object.setOnVoltageRatioChangeHandler(self.Phidgets_VoltageRatioInput1Object_VoltageRatioChange_EventHandler)
            self.VoltageRatioInput1Object.setOnAttachHandler(self.Phidgets_VoltageRatioInput1Object_Attach_EventHandler)
            self.VoltageRatioInput1Object.setOnDetachHandler(self.Phidgets_VoltageRatioInput1Object_Detach_EventHandler)
            self.VoltageRatioInput1Object.setOnErrorHandler(self.Phidgets_VoltageRatioInput1Object_Error_EventHandler)

            self.DigitalInput0Object.setOnStateChangeHandler(self.Phidgets_DigitalInput0Object_StateChange_EventHandler)
            self.DigitalInput0Object.setOnAttachHandler(self.Phidgets_DigitalInput0Object_Attach_EventHandler)
            self.DigitalInput0Object.setOnDetachHandler(self.Phidgets_DigitalInput0Object_Detach_EventHandler)
            self.DigitalInput0Object.setOnErrorHandler(self.Phidgets_DigitalInput0Object_Error_EventHandler)

        except PhidgetException as e:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to set callback functions, Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.VoltageRatioInput0Object.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            self.VoltageRatioInput1Object.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)
            self.DigitalInput0Object.openWaitForAttachment(self.WaitForAttached_TimeoutDuration_Milliseconds)

        except PhidgetException as e:
            print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed on 'openWaitForAttachment', Phidget Exception %i: %s" % (e.code, e.details))
            return
        #########################################################
        #########################################################

        self.PhidgetsDeviceConnectedFlag = 1

        #########################################################
        #########################################################
        if self.PhidgetsDeviceConnectedFlag == 1:

            #########################################################
            if self.UsePhidgetsLoggingInternalToThisClassObjectFlag == 1:
                try:
                    Log.enable(LogLevel.PHIDGET_LOG_INFO, os.getcwd() + "\PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class_PhidgetLog_INFO.txt")
                    print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Enabled Phidget Logging.")
                except PhidgetException as e:
                    print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to enable Phidget Logging, Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceName = self.VoltageRatioInput0Object.getDeviceName()
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: DetectedDeviceName: " + self.DetectedDeviceName)

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to call 'getDeviceName', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.VINT_DetectedSerialNumber = self.VoltageRatioInput0Object.getDeviceSerialNumber()
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: VINT_DetectedSerialNumber: " + str(self.VINT_DetectedSerialNumber))

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to call 'getDeviceSerialNumber', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceID = self.VoltageRatioInput0Object.getDeviceID()
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: DetectedDeviceID: " + str(self.DetectedDeviceID))

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to call 'getDesiredDeviceID', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceVersion = self.VoltageRatioInput0Object.getDeviceVersion()
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: DetectedDeviceVersion: " + str(self.DetectedDeviceVersion))

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to call 'getDeviceVersion', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            try:
                self.DetectedDeviceLibraryVersion = self.VoltageRatioInput0Object.getLibraryVersion()
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: DetectedDeviceLibraryVersion: " + str(self.DetectedDeviceLibraryVersion))

            except PhidgetException as e:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Failed to call 'getLibraryVersion', Phidget Exception %i: %s" % (e.code, e.details))
            #########################################################

            #########################################################
            if self.VINT_DesiredSerialNumber != -1:
                if self.VINT_DetectedSerialNumber != self.VINT_DesiredSerialNumber:
                    print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: The desired Serial Number (" + str(self.VINT_DesiredSerialNumber) + ") does not match the detected serial number (" + str(self.VINT_DetectedSerialNumber) + ").")
                    input("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Press any key (and enter) to exit.")
                    sys.exit()
            #########################################################

            #########################################################
            if self.DetectedDeviceID != self.DesiredDeviceID:
                print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: The desired DesiredDeviceID (" + str(self.DesiredDeviceID) + ") does not match the detected Device ID (" + str(self.DetectedDeviceID) + ").")
                input("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class __init__: Press any key (and enter) to exit.")
                sys.exit()
            #########################################################

            #########################################################
            self.MainThread_ThreadingObject = threading.Thread(target=self.MainThread, args=())
            self.MainThread_ThreadingObject.start()
            #########################################################

            #########################################################
            if self.USE_GUI_FLAG == 1:
                self.StartGUI(self.root)
            #########################################################

            #########################################################
            self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
            #########################################################

        #########################################################
        #########################################################

    #######################################################################################################################
    #######################################################################################################################

    #######################################################################################################################
    #######################################################################################################################
    def __del__(self):
        pass
    #######################################################################################################################
    #######################################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber):

        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThrough0and1values_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be 0 or 1 (value was " +
                          str(InputNumber_ConvertedToFloat) +
                          "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue):
        try:
            InputNumber_ConvertedToFloat = float(InputNumber)
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber must be a float value, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()

        try:
            if InputNumber_ConvertedToFloat >= RangeMinValue and InputNumber_ConvertedToFloat <= RangeMaxValue:
                return InputNumber_ConvertedToFloat
            else:
                input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                          InputNameString +
                          "' must be in the range [" +
                          str(RangeMinValue) +
                          ", " +
                          str(RangeMaxValue) +
                          "] (value was " +
                          str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")

                sys.exit()
        except:
            exceptions = sys.exc_info()[0]
            print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            input("Press any key to continue")
            sys.exit()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def TellWhichFileWereIn(self):

        #We used to use this method, but it gave us the root calling file, not the class calling file
        #absolute_file_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        #filename = absolute_file_path[absolute_file_path.rfind("\\") + 1:]

        frame = inspect.stack()[1]
        filename = frame[1][frame[1].rfind("\\") + 1:]
        filename = filename.replace(".py","")

        return filename
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Attach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach - self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Attach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach
            ##########################

            self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach

            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Attach ++++++++++++")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach: " + str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach: " + str(self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Attach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Attach))
            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Attach ++++++++++++")

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Attach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Detach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach - self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Detach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach
            ##########################

            self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach

            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Detach -----------")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach: " + str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach: " + str(self.LastTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Detach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput0Object_Detach))
            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Detach -----------")

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Detach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Attach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach - self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Attach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach
            ##########################

            self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach

            '''
            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Attach ++++++++++++")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach: " + str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach: " + str(self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Attach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Attach))
            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Attach ++++++++++++")
            '''

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Attach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Detach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach - self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Detach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach
            ##########################

            self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach = self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach

            '''
            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Detach -----------")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach: " + str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach: " + str(self.LastTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Detach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_VoltageRatioInput1Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_VoltageRatioInput1Object_Detach))
            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Detach -----------")
            '''

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Detach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Attach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach = self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach - self.LastTime_TimestampForEventFiring_DigitalInput0Object_Attach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Attach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach
            ##########################

            self.LastTime_TimestampForEventFiring_DigitalInput0Object_Attach = self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach

            '''
            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Attach ++++++++++++")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach: " + str(self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_DigitalInput0Object_Attach: " + str(self.LastTime_TimestampForEventFiring_DigitalInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Attach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Attach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Attach))
            self.MyPrint_WithoutLogFile("++++++++++++ UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Attach ++++++++++++")
            '''

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Attach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Detach(self):

        try:
            self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach = self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach - self.LastTime_TimestampForEventFiring_DigitalInput0Object_Detach

            ##########################
            if self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach != 0.0:
                self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Detach = 1.0/self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach
            ##########################

            self.LastTime_TimestampForEventFiring_DigitalInput0Object_Detach = self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach

            '''
            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Detach -----------")
            self.MyPrint_WithoutLogFile("self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach: " + str(self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.LastTime_TimestampForEventFiring_DigitalInput0Object_Detach: " + str(self.LastTime_TimestampForEventFiring_DigitalInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Detach: " + str(self.DataStreamingFrequency_TimestampForEventFiring_DigitalInput0Object_Detach))
            self.MyPrint_WithoutLogFile("self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach: " + str(self.DataStreamingDeltaT_TimestampForEventFiring_DigitalInput0Object_Detach))
            self.MyPrint_WithoutLogFile("----------- UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Detach -----------")
            '''

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Detach ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampFromVoltageRatioInput0DataCallback(self):

        try:
            self.DataStreamingDeltaT_TimestampFromVoltageRatioInput0DataCallback = self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback - self.LastTime_TimestampFromVoltageRatioInput0DataCallback

            ##########################
            if self.DataStreamingDeltaT_TimestampFromVoltageRatioInput0DataCallback != 0.0:
                self.DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = 1.0/self.DataStreamingDeltaT_TimestampFromVoltageRatioInput0DataCallback
            ##########################

            self.LastTime_TimestampFromVoltageRatioInput0DataCallback = self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampFromVoltageRatioInput0DataCallback ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_TimestampFromVoltageRatioInput1DataCallback(self):

        try:
            self.DataStreamingDeltaT_TimestampFromVoltageRatioInput1DataCallback = self.CurrentTime_TimestampFromVoltageRatioInput1DataCallback - self.LastTime_TimestampFromVoltageRatioInput1DataCallback

            ##########################
            if self.DataStreamingDeltaT_TimestampFromVoltageRatioInput1DataCallback != 0.0:
                self.DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = 1.0/self.DataStreamingDeltaT_TimestampFromVoltageRatioInput1DataCallback
            ##########################

            self.LastTime_TimestampFromVoltageRatioInput1DataCallback = self.CurrentTime_TimestampFromVoltageRatioInput1DataCallback

        except:
            exceptions = sys.exc_info()[0]
            self.MyPrint_WithoutLogFile("UpdateFrequencyCalculation_TimestampFromVoltageRatioInput1DataCallback ERROR, exceptions: %s" % exceptions, 0)

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_MainThread(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread - self.LastTime_CalculatedFromMainThread

            if self.DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
                self.DataStreamingFrequency_CalculatedFromMainThread = 1.0/self.DataStreamingDeltaT_CalculatedFromMainThread

            self.LastTime_CalculatedFromMainThread = self.CurrentTime_CalculatedFromMainThread
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_MainThread ERROR with Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_ServerAdded_EventHandler(self, HandlerSelf, VoltageRatio):

        self.MyPrint_WithoutLogFile("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Phidgets_ServerAdded_EventHandler event fired at " + str(self.getPreciseSecondsTimeStampString()) + " secconds! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%" + str(VoltageRatio))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_ServerRemoved_EventHandler(self, HandlerSelf, VoltageRatio):

        self.MyPrint_WithoutLogFile("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Phidgets_ServerRemoved_EventHandler event fired at " + str(self.getPreciseSecondsTimeStampString()) + " secconds! %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%" + str(VoltageRatio))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput0Object_Attach_EventHandler(self, HandlerSelf):

        try:
            #####################
            self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
            self.UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Attach()

            self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput0Object_Attach_EventHandler, Serial Number " +
                          str(self.VINT_DesiredSerialNumber) +
                          ", Attach event fired at " +
                          str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Attach) +
                          " seconds!")
            #####################

            #####################
            self.VoltageRatioInput0Object.setDataInterval(self.UpdateDeltaT_ms)
            self.MyPrint_WithoutLogFile("Setting the update rate on VoltageRatioInput0Object to every " + str(self.UpdateDeltaT_ms) + " ms.")
            self.MyPrint_WithoutLogFile("Confirmed by reading the device that the VoltageRatioInput0Object Data Interval is " + str(self.VoltageRatioInput0Object.getDataInterval()) + " ms.")
            #####################

            #####################
            self.VoltageRatioInput0Object.setVoltageRatioChangeTrigger(0) #Setting to 0 will result in the channel firing events every DataInterval. This is useful for applications that implement their own data filtering
            self.MyPrint_WithoutLogFile("Setting the SensorValueChangeTrigger on VoltageRatioInput0Object to 0 for continuous event-firing.")
            self.MyPrint_WithoutLogFile("Confirmed by reading the device that the VoltageRatioInput0Object SensorValueChangeTrigger is " + str(self.VoltageRatioInput0Object.getVoltageRatioChangeTrigger()))
            #####################

            self.VoltageRatioInput0Object_DeviceConnectedFlag = 1

        except PhidgetException as e:
            self.VoltageRatioInput0Object_DeviceConnectedFlag = 0
            self.MyPrint_WithoutLogFile("-------------------- Phidgets_VoltageRatioInput0Object_Attach_EventHandler ERROR, Phidget Exception %i: %s" % (e.code, e.details))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput0Object_Detach_EventHandler(self, HandlerSelf):

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
        self.UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput0Object_Detach()

        self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput0Object_Detach_EventHandler, Serial Number " +
                      str(self.VINT_DesiredSerialNumber) +
                      ", Detach event fired at " +
                      str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput0Object_Detach) +
                      " secconds!")

        self.VoltageRatioInput0Object_DeviceConnectedFlag = 0

        #NOTE THAT WE DO NOT HAVE TO ISSUE A openWaitForAttachment CALL HERE, AS ATTACH TAKES CARE OF PLUGGIN BACK IN

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput0Object_VoltageRatioChange_EventHandler(self, HandlerSelf, VoltageRatio):

        # self.VoltageRatioInput0Object_VoltageRatio = VoltageRatio

        self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads

        VoltageRatio_Filtered = self.VoltageRatioInput0Object_LowPassFilter_Lambda_Object.AddDataPointFromExternalProgram(VoltageRatio)["SignalOutSmoothed"]

        self.VoltageRatioInput0Object_DataEventHandler_Queue.put([VoltageRatio_Filtered, self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback])

        self.UpdateFrequencyCalculation_TimestampFromVoltageRatioInput0DataCallback()

        # self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput0Object_VoltageRatioChange_EventHandler: " + str(VoltageRatio))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput0Object_Error_EventHandler(self, HandlerSelf, code, description):

        self.MyPrint_WithoutLogFile("----------")
        self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput0Object_Error_EventHandler Code: " + ErrorEventCode.getName(code) + ", Description: " + str(description))
        self.MyPrint_WithoutLogFile("----------")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput1Object_Attach_EventHandler(self, HandlerSelf):

        try:
            #####################
            self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
            self.UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Attach()

            self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput1Object_Attach_EventHandler, Serial Number " +
                          str(self.VINT_DesiredSerialNumber) +
                          ", Attach event fired at " +
                          str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Attach) +
                          " seconds!")
            #####################

            #####################
            self.VoltageRatioInput1Object.setDataInterval(self.UpdateDeltaT_ms)
            self.MyPrint_WithoutLogFile("Setting the update rate on VoltageRatioInput1Object to every " + str(self.UpdateDeltaT_ms) + " ms.")
            self.MyPrint_WithoutLogFile("Confirmed by reading the device that the VoltageRatioInput1Object Data Interval is " + str(self.VoltageRatioInput1Object.getDataInterval()) + " ms.")
            #####################

            #####################
            self.VoltageRatioInput1Object.setVoltageRatioChangeTrigger(0) #Setting to 0 will result in the channel firing events every DataInterval. This is useful for applications that implement their own data filtering
            self.MyPrint_WithoutLogFile("Setting the SensorValueChangeTrigger on VoltageRatioInput1Object to 0 for continuous event-firing.")
            self.MyPrint_WithoutLogFile("Confirmed by reading the device that the VoltageRatioInput1Object SensorValueChangeTrigger is " + str(self.VoltageRatioInput1Object.getVoltageRatioChangeTrigger()))
            #####################

            self.VoltageRatioInput1Object_DeviceConnectedFlag = 1

        except PhidgetException as e:
            self.VoltageRatioInput1Object_DeviceConnectedFlag = 0
            self.MyPrint_WithoutLogFile("-------------------- Phidgets_VoltageRatioInput1Object_Attach_EventHandler ERROR, Phidget Exception %i: %s" % (e.code, e.details))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput1Object_Detach_EventHandler(self, HandlerSelf):

        self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
        self.UpdateFrequencyCalculation_TimestampForEventFiring_VoltageRatioInput1Object_Detach()

        self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput1Object_Detach_EventHandler, Serial Number " +
                      str(self.VINT_DesiredSerialNumber) +
                      ", Detach event fired at " +
                      str(self.CurrentTime_TimestampForEventFiring_VoltageRatioInput1Object_Detach) +
                      " secconds!")

        self.VoltageRatioInput1Object_DeviceConnectedFlag = 0

        # NOTE THAT WE DO NOT HAVE TO ISSUE A openWaitForAttachment CALL HERE, AS ATTACH TAKES CARE OF PLUGGIN BACK IN

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput1Object_Error_EventHandler(self, HandlerSelf, code, description):

        self.MyPrint_WithoutLogFile("----------")
        self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput1Object_Error_EventHandler Code: " + ErrorEventCode.getName(code) + ", Description: " + str(description))
        self.MyPrint_WithoutLogFile("----------")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_VoltageRatioInput1Object_VoltageRatioChange_EventHandler(self, HandlerSelf, VoltageRatio):

        # self.VoltageRatioInput1Object_VoltageRatio = VoltageRatio

        self.CurrentTime_TimestampFromVoltageRatioInput1DataCallback = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads

        VoltageRatio_Filtered = self.VoltageRatioInput1Object_LowPassFilter_Lambda_Object.AddDataPointFromExternalProgram(VoltageRatio)["SignalOutSmoothed"]

        self.VoltageRatioInput1Object_DataEventHandler_Queue.put([VoltageRatio_Filtered, self.CurrentTime_TimestampFromVoltageRatioInput1DataCallback])

        self.UpdateFrequencyCalculation_TimestampFromVoltageRatioInput1DataCallback()

        # self.MyPrint_WithoutLogFile("Phidgets_VoltageRatioInput1Object_VoltageRatioChange_EventHandler: " + str(VoltageRatio))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_DigitalInput0Object_Attach_EventHandler(self, HandlerSelf):

        try:
            self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
            self.UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Attach()

            self.MyPrint_WithoutLogFile("Phidgets_DigitalInput0Object_Attach_EventHandler, Serial Number " +
                          str(self.VINT_DesiredSerialNumber) +
                          ", Attach event fired at " +
                          str(self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Attach) +
                          " secconds!")

            #self.DigitalInput0Object.setDataInterval(self.UpdateDeltaT_ms) #NOT AVAILABLE FOR DIGITALINPUT
            #self.MyPrint_WithoutLogFile("Setting the update rate on DigitalInput0Object to every " + str(self.UpdateDeltaT_ms) + " ms.")
            #self.MyPrint_WithoutLogFile("Confirmed by reading the device that the DigitalInput0Object Data Interval is " + str(self.DigitalInput0Object.getDataInterval()) + " ms.")

            self.DigitalInput0Object_DeviceConnectedFlag = 1

        except PhidgetException as e:
            self.DigitalInput1Object_DeviceConnectedFlag = 0
            self.MyPrint_WithoutLogFile("-------------------- Phidgets_DigitalInput0Object_Attach_EventHandler ERROR, Phidget Exception %i: %s" % (e.code, e.details))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_DigitalInput0Object_Detach_EventHandler(self, HandlerSelf):

        self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
        self.UpdateFrequencyCalculation_TimestampForEventFiring_DigitalInput0Object_Detach()

        self.MyPrint_WithoutLogFile("Phidgets_DigitalInput0Object_Detach_EventHandler, Serial Number " +
                      str(self.VINT_DesiredSerialNumber) +
                      ", Detach event fired at " +
                      str(self.CurrentTime_TimestampForEventFiring_DigitalInput0Object_Detach) +
                      " secconds!")

        self.DigitalInput0Object_DeviceConnectedFlag = 0

        # NOTE THAT WE DO NOT HAVE TO ISSUE A openWaitForAttachment CALL HERE, AS ATTACH TAKES CARE OF PLUGGIN BACK IN

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_DigitalInput0Object_StateChange_EventHandler(self, HandlerSelf, State):

        # self.DigitalInput0Object_State = State

        self.CurrentTime_TimestampFromDigitalInput0DataCallback = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads

        self.DigitalInput0Object_DataEventHandler_Queue.put([State, self.CurrentTime_TimestampFromDigitalInput0DataCallback])

        # self.UpdateFrequencyCalculation_TimestampFromDigitalInput0DataCallback()

        # self.MyPrint_WithoutLogFile("Phidgets_DigitalInput0Object_StateChange_EventHandler: " + str(State))

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Phidgets_DigitalInput0Object_Error_EventHandler(self, HandlerSelf, code, description):

        self.MyPrint_WithoutLogFile("----------")
        self.MyPrint_WithoutLogFile("Phidgets_DigitalInput0Object_Error_EventHandler Code: " + ErrorEventCode.getName(code) + ", Description: " + str(description))
        self.MyPrint_WithoutLogFile("----------")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:

            self.MostRecentDataDict = dict([("VoltageRatioInput0Object_VoltageRatio", self.VoltageRatioInput0Object_VoltageRatio),
                                ("VoltageRatioInput1Object_VoltageRatio", self.VoltageRatioInput1Object_VoltageRatio),
                                ("DigitalInput0Object_State", self.DigitalInput0Object_State),
                                ("DataStreamingFrequency_CalculatedFromMainThread", self.DataStreamingFrequency_CalculatedFromMainThread),
                                ("DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback", self.DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback),
                                ("DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback", self.DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback),
                                ("Time", self.CurrentTime_TimestampFromVoltageRatioInput0DataCallback)])

            return deepcopy(self.MostRecentDataDict) #deepcopy IS required as MostRecentDataDict contains lists.

        else:
            return dict() #So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ########################################################################################################## unicorn
    def MainThread(self):

        self.MyPrint_WithoutLogFile("Started MainThread for PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class object.")
        
        self.MainThread_still_running_flag = 1

        #########################################################
        #########################################################
        while self.EXIT_PROGRAM_FLAG == 0:

            #########################################################
            self.CurrentTime_CalculatedFromMainThread = self.getPreciseSecondsTimeStampString() - self.StartingTime_GlobalAcrossAllThreads
            #########################################################

            #########################################################
            if self.VoltageRatioInput0Object_DataEventHandler_Queue.qsize() > 0:
                [VoltageRatioInput0Object_VoltageRatio_temp, timestamp0_temp] = self.VoltageRatioInput0Object_DataEventHandler_Queue.get()

                self.VoltageRatioInput0Object_VoltageRatio = VoltageRatioInput0Object_VoltageRatio_temp - self.VoltageRatioInput0Object_SteadyStateOffset
            #########################################################

            #########################################################
            if self.VoltageRatioInput1Object_DataEventHandler_Queue.qsize() > 0:
                [VoltageRatioInput1Object_VoltageRatio_temp, timestamp1_temp] = self.VoltageRatioInput1Object_DataEventHandler_Queue.get()

                self.VoltageRatioInput1Object_VoltageRatio = VoltageRatioInput1Object_VoltageRatio_temp - self.VoltageRatioInput1Object_SteadyStateOffset
            #########################################################

            #########################################################
            if self.DigitalInput0Object_DataEventHandler_Queue.qsize() > 0:
                [self.DigitalInput0Object_State, timestamp2_temp] = self.DigitalInput0Object_DataEventHandler_Queue.get()
            #########################################################

            ######################################################### USE THE TIME.SLEEP() TO SET THE LOOP FREQUENCY
            self.UpdateFrequencyCalculation_MainThread() #ONLY UPDATE IF WE HAD NEW DATA

            if self.MainThread_TimeToSleepEachLoop > 0.0:
                time.sleep(self.MainThread_TimeToSleepEachLoop)
            #########################################################

        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.VoltageRatioInput0Object.close()
            self.VoltageRatioInput1Object.close()
            self.DigitalInput0Object.close()

        except PhidgetException as e:
            self.MyPrint_WithoutLogFile("end_program_callback error: Phidget Exception %i: %s" % (e.code, e.details))

        #########################################################
        #########################################################

        self.MyPrint_WithoutLogFile("Finished MainThread for PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class object.")
        
        self.MainThread_still_running_flag = 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StartGUI(self, GuiParent):

        #self.GUI_Thread_ThreadingObject = threading.Thread(target=self.GUI_Thread, args=(GuiParent,))
        #self.GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        #self.GUI_Thread_ThreadingObject.start()

        self.GUI_Thread(GuiParent)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_Thread(self, parent):

        print("Starting the GUI_Thread for PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class object.")

        ###################################################
        self.root = parent
        self.parent = parent
        ###################################################

        ###################################################
        self.myFrame = Frame(self.root)

        if self.UseBorderAroundThisGuiObjectFlag == 1:
            self.myFrame["borderwidth"] = 2
            self.myFrame["relief"] = "ridge"

        self.myFrame.grid(row = self.GUI_ROW,
                          column = self.GUI_COLUMN,
                          padx = self.GUI_PADX,
                          pady = self.GUI_PADY,
                          rowspan = self.GUI_ROWSPAN,
                          columnspan= self.GUI_COLUMNSPAN,
                          sticky = self.GUI_STICKY)
        ###################################################

        ###################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        ###################################################

        #################################################
        self.DeviceInfo_Label = Label(self.myFrame, text="Device Info", width=40)

        self.DeviceInfo_Label["text"] = self.NameToDisplay_UserSet + \
                                        "\nDevice Name: " + self.DetectedDeviceName + \
                                        "\nDevice Serial Number: " + str(self.VINT_DetectedSerialNumber) + \
                                        "\nDevice ID: " + str(self.DetectedDeviceID) + \
                                        "\nDevice Version: " + str(self.DetectedDeviceVersion)

        self.DeviceInfo_Label.grid(row=0, column=0, padx=5, pady=1, columnspan=1, rowspan=1)
        #################################################

        #################################################
        self.Joystick2DdotDisplay_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", self.myFrame), ("GUI_ROW", 0), ("GUI_COLUMN", 1), ("GUI_PADX", 1), ("GUI_PADY", 1), ("GUI_ROWSPAN", 1), ("GUI_COLUMNSPAN", 1)])
        self.Joystick2DdotDisplay_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", self.Joystick2DdotDisplay_ReubenPython2and3ClassObject_GUIparametersDict)])
        self.Joystick2DdotDisplay_ReubenPython2and3ClassObject = Joystick2DdotDisplay_ReubenPython2and3Class(self.Joystick2DdotDisplay_ReubenPython2and3ClassObject_setup_dict)
        #################################################

        #################################################
        self.DataDisplayLabel = Label(self.myFrame, text="DataDisplayLabel", width=70)
        self.DataDisplayLabel.grid(row=0, column=2, padx=1, pady=1, columnspan=1, rowspan=1)
        #################################################

        #################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=150)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=1, column=0, padx=10, pady=10, columnspan=10, rowspan=10)
        #################################################

        #################################################
        self.GUI_ready_to_be_updated_flag = 1
        #################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_update_clock(self):

        #######################################################
        #######################################################
        #######################################################
        #######################################################
        if self.USE_GUI_FLAG == 1 and self.EXIT_PROGRAM_FLAG == 0:

            #######################################################
            #######################################################
            #######################################################
            if self.GUI_ready_to_be_updated_flag == 1:

                #######################################################
                #######################################################
                try:

                    #########################################################
                    self.DataDisplayLabel["text"] = "Time, CalculatedFromMainThread: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.CurrentTime_CalculatedFromMainThread, 0, 3) + \
                                            "\nData Frequency, CalculatedFromMainThread: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_CalculatedFromMainThread, 0, 3) + \
                                            "\nDataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback, 0, 3) + \
                                            "\nDataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback, 0, 3) + \
                                            "\nVoltageRatioInput0Object_VoltageRatio: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.VoltageRatioInput0Object_VoltageRatio, 0, 3) + \
                                            "\nVoltageRatioInput1Object_VoltageRatio: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.VoltageRatioInput1Object_VoltageRatio, 0, 3) + \
                                            "\nDigitalInput0Object_State: " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self.DigitalInput0Object_State, 0, 3)
                    #########################################################

                    #########################################################
                    self.Joystick2DdotDisplay_ReubenPython2and3ClassObject.UpdateDotCoordinatesAndDotColor(self.VoltageRatioInput0Object_VoltageRatio, self.VoltageRatioInput1Object_VoltageRatio, self.DigitalInput0Object_State)
                    self.Joystick2DdotDisplay_ReubenPython2and3ClassObject.GUI_update_clock()
                    #########################################################

                    #######################################################
                    self.PrintToGui_Label.config(text=self.PrintToGui_Label_TextInput_Str)
                    #######################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
                    traceback.print_exc()
                #######################################################
                #######################################################

            #######################################################
            #######################################################
            #######################################################

        #######################################################
        #######################################################
        #######################################################
        #######################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def MyPrint_WithoutLogFile(self, input_string):

        input_string = str(input_string)

        if input_string != "":

            #input_string = input_string.replace("\n", "").replace("\r", "")

            ################################ Write to console
            # Some people said that print crashed for pyinstaller-built-applications and that sys.stdout.write fixed this.
            # http://stackoverflow.com/questions/13429924/pyinstaller-packaged-application-works-fine-in-console-mode-crashes-in-window-m
            if self.PrintToConsoleFlag == 1:
                sys.stdout.write(input_string + "\n")
            ################################

            ################################ Write to GUI
            self.PrintToGui_Label_TextInputHistory_List.append(self.PrintToGui_Label_TextInputHistory_List.pop(0)) #Shift the list
            self.PrintToGui_Label_TextInputHistory_List[-1] = str(input_string) #Add the latest value

            self.PrintToGui_Label_TextInput_Str = ""
            for Counter, Line in enumerate(self.PrintToGui_Label_TextInputHistory_List):
                self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + Line

                if Counter < len(self.PrintToGui_Label_TextInputHistory_List) - 1:
                    self.PrintToGui_Label_TextInput_Str = self.PrintToGui_Label_TextInput_Str + "\n"
            ################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def IsInputList(self, InputToCheck):

        result = isinstance(InputToCheck, list)
        return result
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(self, input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

        number_of_decimal_places = max(1, number_of_decimal_places) #Make sure we're above 1

        ListOfStringsToJoin = []

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if isinstance(input, str) == 1:
            ListOfStringsToJoin.append(input)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, int) == 1 or isinstance(input, float) == 1:
            element = float(input)
            prefix_string = "{:." + str(number_of_decimal_places) + "f}"
            element_as_string = prefix_string.format(element)

            ##########################################################################################################
            ##########################################################################################################
            if element >= 0:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1)  # +1 for sign, +1 for decimal place
                element_as_string = "+" + element_as_string  # So that our strings always have either + or - signs to maintain the same string length
            else:
                element_as_string = element_as_string.zfill(number_of_leading_numbers + number_of_decimal_places + 1 + 1 + 1)  # +1 for sign, +1 for decimal place
            ##########################################################################################################
            ##########################################################################################################

            ListOfStringsToJoin.append(element_as_string)
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, list) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append(self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, tuple) == 1:

            if len(input) > 0:
                for element in input: #RECURSION
                    ListOfStringsToJoin.append("TUPLE" + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a list() or []
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        elif isinstance(input, dict) == 1:

            if len(input) > 0:
                for Key in input: #RECURSION
                    ListOfStringsToJoin.append(str(Key) + ": " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

            else: #Situation when we get a dict()
                ListOfStringsToJoin.append(str(input))

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        else:
            ListOfStringsToJoin.append(str(input))
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if len(ListOfStringsToJoin) > 1:

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            StringToReturn = ""
            for Index, StringToProcess in enumerate(ListOfStringsToJoin):

                ################################################
                if Index == 0: #The first element
                    if StringToProcess.find(":") != -1 and StringToProcess[0] != "{": #meaning that we're processing a dict()
                        StringToReturn = "{"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[0] != "(":  # meaning that we're processing a tuple
                        StringToReturn = "("
                    else:
                        StringToReturn = "["

                    StringToReturn = StringToReturn + StringToProcess.replace("TUPLE","") + ", "
                ################################################

                ################################################
                elif Index < len(ListOfStringsToJoin) - 1: #The middle elements
                    StringToReturn = StringToReturn + StringToProcess + ", "
                ################################################

                ################################################
                else: #The last element
                    StringToReturn = StringToReturn + StringToProcess

                    if StringToProcess.find(":") != -1 and StringToProcess[-1] != "}":  # meaning that we're processing a dict()
                        StringToReturn = StringToReturn + "}"
                    elif StringToProcess.find("TUPLE") != -1 and StringToProcess[-1] != ")":  # meaning that we're processing a tuple
                        StringToReturn = StringToReturn + ")"
                    else:
                        StringToReturn = StringToReturn + "]"

                ################################################

            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

        elif len(ListOfStringsToJoin) == 1:
            StringToReturn = ListOfStringsToJoin[0]

        else:
            StringToReturn = ListOfStringsToJoin

        return StringToReturn
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
