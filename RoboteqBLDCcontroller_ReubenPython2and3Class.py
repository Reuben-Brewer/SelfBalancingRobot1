# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision J, 11/10/2024

Verified working on: Python 2.7, 3.12 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (may work on Mac in non-GUI mode, but haven't tested yet).
'''

__author__ = 'reuben.brewer'

##########################################
from LowPassFilter_ReubenPython2and3Class import *
from EntryListWithBlinking_ReubenPython2and3Class import *
##########################################

##########################################
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
##########################################

##########################################
if sys.version_info[0] < 3:
    from Tkinter import * #Python 2
    import tkFont
    import ttk
else:
    from tkinter import * #Python 3
    import tkinter.font as tkFont #Python 3
    from tkinter import ttk
##########################################

##########################################
if sys.version_info[0] < 3:
    import Queue  # Python 2
else:
    import queue as Queue  # Python 3
##########################################

##########################################
if sys.version_info[0] < 3:
    from builtins import raw_input as input
else:
    from future.builtins import input as input
########################################## "sudo pip3 install future" (Python 3) AND "sudo pip install future" (Python 2)

##########################################
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
##########################################

#########################################################

##########################
import serial #___IMPORTANT: pip install pyserial (NOT pip install serial).
from serial.tools import list_ports
##########################

##########################
global ftd2xx_IMPORTED_FLAG
ftd2xx_IMPORTED_FLAG = 0
try:
    import ftd2xx #https://pypi.org/project/ftd2xx/ 'pip install ftd2xx', current version is 1.3.1 as of 05/06/22. For SetAllFTDIdevicesLatencyTimer function
    ftd2xx_IMPORTED_FLAG = 1

except:
    exceptions = sys.exc_info()[0]
    print("**********")
    print("********** RoboteqBLDCcontroller_ReubenPython2and3Class __init__: ERROR, failed to import ftdtxx, Exceptions: %s" % exceptions + " ********** ")
    print("**********")
##########################

##########################
if sys.version_info[0] < 3:
    from builtins import bytes #Necessary to make bytes() function call work in Python 2.7
##########################

#########################################################

class RoboteqBLDCcontroller_ReubenPython2and3Class(Frame): #Subclass the Tkinter Frame

    ##########################################################################################################
    ##########################################################################################################
    def __init__(self, setup_dict): #Subclass the Tkinter Frame

        print("#################### RoboteqBLDCcontroller_ReubenPython2and3Class __init__ starting. ####################")

        self.PrintAllReceivedSerialMessageForDebuggingFlag = 0

        self.PrintAllSentSerialMessageForDebuggingFlag = 0

        self.EXIT_PROGRAM_FLAG = 0
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 0
        self.EnableInternal_MyPrint_Flag = 0
        self.MainThread_still_running_flag = 0

        self.SerialObject = serial.Serial()
        self.SerialConnectedFlag = 0
        self.SerialBaudRate = 115200
        self.SerialTimeoutSeconds = 0.5
        self.SerialParity = serial.PARITY_NONE
        self.SerialStopBits = serial.STOPBITS_ONE
        self.SerialByteSize = serial.EIGHTBITS

        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ
        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ
        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ
        self.SerialXonXoffSoftwareFlowControl = 1 #important for the Roboteq even though I've never had to use this with other USB-serial devices.
        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ
        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ
        ##### DO NOT SET THIS TO 1 FOR ANY SERIAL DEVICE OTHER THAN ROBOTEQ

        self.SerialPortNameCorrespondingToCorrectSerialNumber = "default"
        self.SerialRxThread_still_running_flag = 0
        self.SerialTxThread_still_running_flag = 0
        self.DedicatedTxThread_TxMessageToSend_Queue = Queue.Queue()
        self.SerialStrToTx_LAST_SENT = ""

        #########################################################
        #########################################################
        self.CurrentTime_CalculatedFromDedicatedTxThread = -11111.0
        self.LastTime_CalculatedFromDedicatedTxThread = -11111.0
        self.StartingTime_CalculatedFromDedicatedTxThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromDedicatedTxThread = -11111.0
        self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread = -11111.0

        self.LastTimeHeartbeatWasSent_CalculatedFromDedicatedTxThread = -11111.0

        self.CurrentTime_CalculatedFromDedicatedRxThread = -11111.0
        self.LastTime_CalculatedFromDedicatedRxThread = -11111.0
        self.StartingTime_CalculatedFromDedicatedRxThread = -11111.0
        self.DataStreamingFrequency_CalculatedFromDedicatedRxThread = -11111.0
        self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread = -11111.0
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        '''
        self.DetectedDeviceName = "default"
        self.DetectedDeviceID = "default"
        self.DetectedDeviceVersion = "default"
        self.DetectedDeviceSerialNumber = "default"
        '''
        #########################################################
        #########################################################

        self.HomeOrBrushlessCounterOnDevice_NeedsToBeChangedFlag = 0
        self.HomeOrBrushlessCounterOnDevice_ToBeSet = 0
        
        self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_ToBeSet = 0.0
        self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_NeedsToBeChangedFlag = 0

        self.EnabledState_ToBeSet = 1
        self.EnabledState_NeedsToBeChangedFlag = 0

        self.EmergencyStopState_ToBeSet = 0
        self.EmergencyStopState_NeedsToBeChangedFlag = 0

        self.StopInAllModes_NeedsToBeChangedFlag = 0

        self.ControlMode_IntegerValue = -1 #Not set
        self.ControlMode_EnlishString = "unknown"

        self.ToggleMinMax_StateToBeSet = 0
        self.ToggleMinMax_EventNeedsToBeFiredFlag = 0

        '''
        0: Open-loop
        1: Closed-loop speed #Not very accurate speed setting, tends to go unstable.
        2: Closed-loop position relative. Phidgets motor works for Kp = 200000.0, Ki = 10000.0
        3: Closed-loop count position #Can't get this to work 01/20/23.
        4: Closed-loop position tracking
        5: Closed-loop torque #Can't get this to work via UART 01/20/23. Also doesn't work for AnalogInput to Pin 4 (AI1).
        6: Closed-loop speed position #Accurate speed control. Phidgets motor works via UART for Kp = 100.0, Ki = 1000000.0. Also working with AnalogInput to Pin 4 (AI1).
        '''

        self.ControlMode_AcceptableValues_ListOfEnglishStrings = ["OpenLoop",   #0
                                                 "ClosedLoopSpeed",             #1
                                                 "ClosedLoopPositionRelative",  #2
                                                 "ClosedLoopCountPosition",     #3
                                                 "ClosedLoopPositionTracking",  #4
                                                 "ClosedLoopTorque",            #5
                                                 "ClosedLoopSpeedPosition"]     #6

        self.ControlMode_AcceptableValues_DictWithIntegersAsKeys = dict([(0, "OpenLoop"),
                                                                            (1, "ClosedLoopSpeed"),
                                                                            (2, "ClosedLoopPositionRelative"),
                                                                            (3, "ClosedLoopCountPosition"),
                                                                            (4, "ClosedLoopPositionTracking"),
                                                                            (5, "ClosedLoopTorque"),
                                                                            (6, "ClosedLoopSpeedPosition")])

        self.ControlMode_AcceptableValues_DictWithEnglishStringsAsKeys = dict([("OpenLoop", 0),
                                                                            ("ClosedLoopSpeed", 1),
                                                                            ("ClosedLoopPositionRelative", 2),
                                                                            ("ClosedLoopCountPosition", 3),
                                                                            ("ClosedLoopPositionTracking", 4),
                                                                            ("ClosedLoopTorque", 5),
                                                                            ("ClosedLoopSpeedPosition", 6)])

        ### Our commanded control modes are working, but we're receiving incorrect values. Below, we map the received values of Actual Operation Mode ("AOM") to what they are in reality (confirmed through RoboRun+).
        self.ActualOperationModeReceived_ConvertIntToEnglishName_EMPIRICALLY_DETERMINTED_DictWithIntegersAsKeys = dict([(0, "OpenLoop"), #Commanded 0 -->, received 0
                                                                            (3, "ClosedLoopSpeed"),             #Commanded 1 --> received 3
                                                                            (-1, "ClosedLoopPositionRelative"),  #Commanded 2 --> received -1
                                                                            (1, "ClosedLoopCountPosition"),     #Commanded 3 --> received 1
                                                                            (-2, "ClosedLoopPositionTracking"),  #Commanded 4 --> received -2
                                                                            (4, "ClosedLoopTorque"),            #Commanded 5 --> received 4
                                                                            (-3, "ClosedLoopSpeedPosition")])    #Commanded 6 --> received -3

        self.ActualOperationModeReceived_ConvertReceivedIntToRealInt_EMPIRICALLY_DETERMINTED_DictWithIntegersAsKeys = dict([(0, 0), #Commanded 0 -->, received 0
                                                                            (3, 1),             #Commanded 1 --> received 3
                                                                            (-1, 2),  #Commanded 2 --> received -1
                                                                            (1, 3),     #Commanded 3 --> received 1
                                                                            (-2, 4),  #Commanded 4 --> received -2
                                                                            (4, 5),            #Commanded 5 --> received 4
                                                                            (-3, 6)])    #Commanded 6 --> received -3
        ###

        self.OpenLoopPower_Target_Min_MotorHardLimit = -1000.0 #Minimum for !G command
        self.OpenLoopPower_Target_Max_MotorHardLimit = 1000.0 #Maximum for !G command

        self.Position_Target_Min_MotorHardLimit = -1000.0 #Minimum for !G command
        self.Position_Target_Max_MotorHardLimit = 1000.0 #Maximum for !G command

        self.Speed_Target_Min_MotorHardLimit = -65535
        self.Speed_Target_Max_MotorHardLimit = 65535

        self.Acceleration_Target_Min_MotorHardLimit = 0
        self.Acceleration_Target_Max_MotorHardLimit = 500000

        self.Torque_Amps_Max_MotorHardLimit = 60.0
        self.Torque_Amps_Min_MotorHardLimit = -1.0*self.Torque_Amps_Max_MotorHardLimit

        self.Current_Amps_Min_MotorHardLimit = 1.0
        self.Current_Amps_Max_MotorHardLimit = 60.0

        '''
        Do not use default values. As a starting point, use P=2, I=0, D=0 in position modes
        (including Speed Position mode). Use P=0, I=1, D=0 in closed loop speed mode and in
        torque mode. Perform full tuning after that.
        
        In speed control mode, the PI controller. The "I" term will be dominant, not "P". I must always be larger than P. TORQUE WILL BE TERRIBLE.
        Use P=0, I=1, D=0 in closed loop speed mode and in torque mode. Perform full tuning after that.
        '''

        self.PID_Kp_Min = 0
        self.PID_Kp_Max = 2000000000

        self.PID_Ki_Min = 0
        self.PID_Ki_Max = 2000000000

        self.PID_Kd_Min = 0
        self.PID_Kd_Max = 2000000000

        self.PID_IntegratorCap1to100percent_Min = 0
        self.PID_IntegratorCap1to100percent_Max = 100

        self.PID_Kp_last = -1
        self.PID_Ki_last = -1
        self.PID_Kd_last = -1
        self.PID_IntegratorCap1to100percent_last = -1

        self.Position_Rev_Last = 0.0

        self.MostRecentDataDict = dict()

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

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: The OS platform is: " + self.my_platform)
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

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "root" in self.GUIparametersDict:
                self.root = self.GUIparametersDict["root"]
            else:
                print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: ERROR, must pass in 'root'")
                return
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "EnableInternal_MyPrint_Flag" in self.GUIparametersDict:
                self.EnableInternal_MyPrint_Flag = self.PassThrough0and1values_ExitProgramOtherwise("EnableInternal_MyPrint_Flag", self.GUIparametersDict["EnableInternal_MyPrint_Flag"])
            else:
                self.EnableInternal_MyPrint_Flag = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: EnableInternal_MyPrint_Flag: " + str(self.EnableInternal_MyPrint_Flag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "PrintToConsoleFlag" in self.GUIparametersDict:
                self.PrintToConsoleFlag = self.PassThrough0and1values_ExitProgramOtherwise("PrintToConsoleFlag", self.GUIparametersDict["PrintToConsoleFlag"])
            else:
                self.PrintToConsoleFlag = 1

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: PrintToConsoleFlag: " + str(self.PrintToConsoleFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "NumberOfPrintLines" in self.GUIparametersDict:
                self.NumberOfPrintLines = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfPrintLines", self.GUIparametersDict["NumberOfPrintLines"], 0.0, 50.0))
            else:
                self.NumberOfPrintLines = 10

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: NumberOfPrintLines: " + str(self.NumberOfPrintLines))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "UseBorderAroundThisGuiObjectFlag" in self.GUIparametersDict:
                self.UseBorderAroundThisGuiObjectFlag = self.PassThrough0and1values_ExitProgramOtherwise("UseBorderAroundThisGuiObjectFlag", self.GUIparametersDict["UseBorderAroundThisGuiObjectFlag"])
            else:
                self.UseBorderAroundThisGuiObjectFlag = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: UseBorderAroundThisGuiObjectFlag: " + str(self.UseBorderAroundThisGuiObjectFlag))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_ROW" in self.GUIparametersDict:
                self.GUI_ROW = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROW", self.GUIparametersDict["GUI_ROW"], 0.0, 1000.0))
            else:
                self.GUI_ROW = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_ROW: " + str(self.GUI_ROW))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMN" in self.GUIparametersDict:
                self.GUI_COLUMN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMN", self.GUIparametersDict["GUI_COLUMN"], 0.0, 1000.0))
            else:
                self.GUI_COLUMN = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_COLUMN: " + str(self.GUI_COLUMN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADX" in self.GUIparametersDict:
                self.GUI_PADX = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADX", self.GUIparametersDict["GUI_PADX"], 0.0, 1000.0))
            else:
                self.GUI_PADX = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_PADX: " + str(self.GUI_PADX))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_PADY" in self.GUIparametersDict:
                self.GUI_PADY = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_PADY", self.GUIparametersDict["GUI_PADY"], 0.0, 1000.0))
            else:
                self.GUI_PADY = 0

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_PADY: " + str(self.GUI_PADY))
            #########################################################
            #########################################################

            ##########################################
            if "GUI_ROWSPAN" in self.GUIparametersDict:
                self.GUI_ROWSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_ROWSPAN", self.GUIparametersDict["GUI_ROWSPAN"], 1.0, 1000.0))
            else:
                self.GUI_ROWSPAN = 1

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_ROWSPAN: " + str(self.GUI_ROWSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_COLUMNSPAN" in self.GUIparametersDict:
                self.GUI_COLUMNSPAN = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("GUI_COLUMNSPAN", self.GUIparametersDict["GUI_COLUMNSPAN"], 1.0, 1000.0))
            else:
                self.GUI_COLUMNSPAN = 1

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_COLUMNSPAN: " + str(self.GUI_COLUMNSPAN))
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if "GUI_STICKY" in self.GUIparametersDict:
                self.GUI_STICKY = str(self.GUIparametersDict["GUI_STICKY"])
            else:
                self.GUI_STICKY = "w"

            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUI_STICKY: " + str(self.GUI_STICKY))
            #########################################################
            #########################################################

        else:
            self.GUIparametersDict = dict()
            self.USE_GUI_FLAG = 0
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: No GUIparametersDict present, setting USE_GUI_FLAG: " + str(self.USE_GUI_FLAG))

        #print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: GUIparametersDict: " + str(self.GUIparametersDict))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DesiredSerialNumber_USBtoSerialConverter" in setup_dict:
            self.DesiredSerialNumber_USBtoSerialConverter = setup_dict["DesiredSerialNumber_USBtoSerialConverter"]

        else:
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: ERROR, must initialize object with 'DesiredSerialNumber_USBtoSerialConverter' argument.")
            return

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: DesiredSerialNumber_USBtoSerialConverter: " + str(self.DesiredSerialNumber_USBtoSerialConverter))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NameToDisplay_UserSet" in setup_dict:
            self.NameToDisplay_UserSet = str(setup_dict["NameToDisplay_UserSet"])
        else:
            self.NameToDisplay_UserSet = ""

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: NameToDisplay_UserSet" + str(self.NameToDisplay_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "ControlMode_Starting" in setup_dict:
            ControlMode_Starting_temp = setup_dict["ControlMode_Starting"]

            if ControlMode_Starting_temp not in self.ControlMode_AcceptableValues_ListOfEnglishStrings:
                print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: ERROR: ControlMode_Starting of " + str(ControlMode_Starting_temp) + " is invalid. You must choose from " + str(self.ControlMode_AcceptableValues_ListOfEnglishStrings))
                return

            self.ControlMode_Starting = ControlMode_Starting_temp

        else:
            self.ControlMode_Starting = "ClosedLoopSpeedPosition"

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: ControlMode_Starting: " + str(self.ControlMode_Starting))
        #########################################################
        #########################################################

        ##########################################################
        #########################################################
        if "OpenLoopPower_Target_Min_UserSet" in setup_dict:
            self.OpenLoopPower_Target_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("OpenLoopPower_Target_Min_UserSet", setup_dict["OpenLoopPower_Target_Min_UserSet"], self.OpenLoopPower_Target_Min_MotorHardLimit, self.OpenLoopPower_Target_Max_MotorHardLimit)

        else:
            self.OpenLoopPower_Target_Min_UserSet = self.OpenLoopPower_Target_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: OpenLoopPower_Target_Min_UserSet: " + str(self.OpenLoopPower_Target_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "OpenLoopPower_Target_Max_UserSet" in setup_dict:
            self.OpenLoopPower_Target_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("OpenLoopPower_Target_Max_UserSet", setup_dict["OpenLoopPower_Target_Max_UserSet"], self.OpenLoopPower_Target_Min_MotorHardLimit, self.OpenLoopPower_Target_Max_MotorHardLimit)

        else:
            self.OpenLoopPower_Target_Max_UserSet = self.OpenLoopPower_Target_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: OpenLoopPower_Target_Max_UserSet: " + str(self.OpenLoopPower_Target_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "OpenLoopPower_Target_Starting" in setup_dict:
            self.OpenLoopPower_Target_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("OpenLoopPower_Target_Starting", setup_dict["OpenLoopPower_Target_Starting"], self.OpenLoopPower_Target_Min_UserSet, self.OpenLoopPower_Target_Max_UserSet)

        else:
            self.OpenLoopPower_Target_Starting = self.OpenLoopPower_Target_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: OpenLoopPower_Target_Starting: " + str(self.OpenLoopPower_Target_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Position_Target_Min_UserSet" in setup_dict:
            self.Position_Target_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Position_Target_Min_UserSet", setup_dict["Position_Target_Min_UserSet"], self.Position_Target_Min_MotorHardLimit, self.Position_Target_Max_MotorHardLimit)

        else:
            self.Position_Target_Min_UserSet = self.Position_Target_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Position_Target_Min_UserSet: " + str(self.Position_Target_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Position_Target_Max_UserSet" in setup_dict:
            self.Position_Target_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Position_Target_Max_UserSet", setup_dict["Position_Target_Max_UserSet"], self.Position_Target_Min_MotorHardLimit, self.Position_Target_Max_MotorHardLimit)

        else:
            self.Position_Target_Max_UserSet = self.Position_Target_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Position_Target_Max_UserSet: " + str(self.Position_Target_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Position_Target_Starting" in setup_dict:
            self.Position_Target_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Position_Target_Starting", setup_dict["Position_Target_Starting"], self.Position_Target_Min_UserSet, self.Position_Target_Max_UserSet)

        else:
            self.Position_Target_Starting = self.Position_Target_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Position_Target_Starting: " + str(self.Position_Target_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Speed_Target_Min_UserSet" in setup_dict:
            self.Speed_Target_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Speed_Target_Min_UserSet", setup_dict["Speed_Target_Min_UserSet"], self.Speed_Target_Min_MotorHardLimit, self.Speed_Target_Max_MotorHardLimit)

        else:
            self.Speed_Target_Min_UserSet = self.Speed_Target_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Speed_Target_Min_UserSet: " + str(self.Speed_Target_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Speed_Target_Max_UserSet" in setup_dict:
            self.Speed_Target_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Speed_Target_Max_UserSet", setup_dict["Speed_Target_Max_UserSet"], self.Speed_Target_Min_MotorHardLimit, self.Speed_Target_Max_MotorHardLimit)

        else:
            self.Speed_Target_Max_UserSet = self.Speed_Target_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Speed_Target_Max_UserSet: " + str(self.Speed_Target_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Speed_Target_Starting" in setup_dict:
            self.Speed_Target_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Speed_Target_Starting", setup_dict["Speed_Target_Starting"], self.Speed_Target_Min_UserSet, self.Speed_Target_Max_UserSet)

        else:
            self.Speed_Target_Starting = self.Speed_Target_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Speed_Target_Starting: " + str(self.Speed_Target_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Acceleration_Target_Min_UserSet" in setup_dict:
            self.Acceleration_Target_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Acceleration_Target_Min_UserSet", setup_dict["Acceleration_Target_Min_UserSet"], self.Acceleration_Target_Min_MotorHardLimit, self.Acceleration_Target_Max_MotorHardLimit)

        else:
            self.Acceleration_Target_Min_UserSet = self.Acceleration_Target_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Acceleration_Target_Min_UserSet: " + str(self.Acceleration_Target_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Acceleration_Target_Max_UserSet" in setup_dict:
            self.Acceleration_Target_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Acceleration_Target_Max_UserSet", setup_dict["Acceleration_Target_Max_UserSet"], self.Acceleration_Target_Min_MotorHardLimit, self.Acceleration_Target_Max_MotorHardLimit)

        else:
            self.Acceleration_Target_Max_UserSet = self.Acceleration_Target_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Acceleration_Target_Max_UserSet: " + str(self.Acceleration_Target_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Acceleration_Target_Starting" in setup_dict:
            self.Acceleration_Target_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Acceleration_Target_Starting", setup_dict["Acceleration_Target_Starting"], self.Acceleration_Target_Min_UserSet, self.Acceleration_Target_Max_UserSet)

        else:
            self.Acceleration_Target_Starting = self.Acceleration_Target_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Acceleration_Target_Starting: " + str(self.Acceleration_Target_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Current_Amps_Min_UserSet" in setup_dict:
            self.Current_Amps_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Current_Amps_Min_UserSet", setup_dict["Current_Amps_Min_UserSet"], self.Current_Amps_Min_MotorHardLimit, self.Current_Amps_Max_MotorHardLimit)

        else:
            self.Current_Amps_Min_UserSet = self.Current_Amps_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Current_Amps_Min_UserSet: " + str(self.Current_Amps_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Current_Amps_Max_UserSet" in setup_dict:
            self.Current_Amps_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Current_Amps_Max_UserSet", setup_dict["Current_Amps_Max_UserSet"], self.Current_Amps_Min_MotorHardLimit, self.Current_Amps_Max_MotorHardLimit)

        else:
            self.Current_Amps_Max_UserSet = self.Current_Amps_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Current_Amps_Max_UserSet: " + str(self.Current_Amps_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Current_Amps_Starting" in setup_dict:
            self.Current_Amps_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Current_Amps_Starting", setup_dict["Current_Amps_Starting"], self.Current_Amps_Min_UserSet, self.Current_Amps_Max_UserSet)

        else:
            self.Current_Amps_Starting = self.Current_Amps_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Current_Amps_Starting: " + str(self.Current_Amps_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Torque_Amps_Min_UserSet" in setup_dict:
            self.Torque_Amps_Min_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Torque_Amps_Min_UserSet", setup_dict["Torque_Amps_Min_UserSet"], self.Torque_Amps_Min_MotorHardLimit, self.Torque_Amps_Max_MotorHardLimit)

        else:
            self.Torque_Amps_Min_UserSet = self.Torque_Amps_Min_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Torque_Amps_Min_UserSet: " + str(self.Torque_Amps_Min_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Torque_Amps_Max_UserSet" in setup_dict:
            self.Torque_Amps_Max_UserSet = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Torque_Amps_Max_UserSet", setup_dict["Torque_Amps_Max_UserSet"], self.Torque_Amps_Min_MotorHardLimit, self.Torque_Amps_Max_MotorHardLimit)

        else:
            self.Torque_Amps_Max_UserSet = self.Torque_Amps_Max_MotorHardLimit

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Torque_Amps_Max_UserSet: " + str(self.Torque_Amps_Max_UserSet))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Torque_Amps_Starting" in setup_dict:
            self.Torque_Amps_Starting = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Torque_Amps_Starting", setup_dict["Torque_Amps_Starting"], self.Torque_Amps_Min_UserSet, self.Torque_Amps_Max_UserSet)

        else:
            self.Torque_Amps_Starting = self.Torque_Amps_Max_UserSet

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Torque_Amps_Starting: " + str(self.Torque_Amps_Starting))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DedicatedRxThread_TimeToSleepEachLoop" in setup_dict:
            self.DedicatedRxThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("DedicatedRxThread_TimeToSleepEachLoop", setup_dict["DedicatedRxThread_TimeToSleepEachLoop"], 0.001, 100000)

        else:
            self.DedicatedRxThread_TimeToSleepEachLoop = 0.005

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: DedicatedRxThread_TimeToSleepEachLoop: " + str(self.DedicatedRxThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "DedicatedTxThread_TimeToSleepEachLoop" in setup_dict:
            self.DedicatedTxThread_TimeToSleepEachLoop = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("DedicatedTxThread_TimeToSleepEachLoop", setup_dict["DedicatedTxThread_TimeToSleepEachLoop"], 0.001, 100000)

        else:
            self.DedicatedTxThread_TimeToSleepEachLoop = 0.005

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: DedicatedTxThread_TimeToSleepEachLoop: " + str(self.DedicatedTxThread_TimeToSleepEachLoop))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "SerialRxBufferSize" in setup_dict:
            self.SerialRxBufferSize = round(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("SerialRxBufferSize", setup_dict["SerialRxBufferSize"], 0.0, 4096.0)) #Maybe 64 to 4096

        else:
            self.SerialRxBufferSize = 64

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: SerialRxBufferSize: " + str(self.SerialRxBufferSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "SerialTxBufferSize" in setup_dict:
            self.SerialTxBufferSize = round(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("SerialTxBufferSize", setup_dict["SerialTxBufferSize"], 0.0, 4096.0)) #Maybe 64 to 4096

        else:
            self.SerialTxBufferSize = 64

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: SerialTxBufferSize: " + str(self.SerialTxBufferSize))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "HeartbeatTimeIntervalMilliseconds" in setup_dict:
            HeartbeatTimeIntervalMilliseconds_TEMP = setup_dict["HeartbeatTimeIntervalMilliseconds"]
            if int(HeartbeatTimeIntervalMilliseconds_TEMP) in [-1, 0]:
                self.HeartbeatTimeIntervalMilliseconds = HeartbeatTimeIntervalMilliseconds_TEMP
            else:
                self.HeartbeatTimeIntervalMilliseconds = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("HeartbeatTimeIntervalMilliseconds", HeartbeatTimeIntervalMilliseconds_TEMP, 1.0*1000.0, 10.0*1000.0) #1 to 10seconds in milliseconds

        else:
            self.HeartbeatTimeIntervalMilliseconds = -1 #Off

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: HeartbeatTimeIntervalMilliseconds: " + str(self.HeartbeatTimeIntervalMilliseconds))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "NumberOfMagnetsInMotor" in setup_dict:
            self.NumberOfMagnetsInMotor = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("NumberOfMagnetsInMotor", setup_dict["NumberOfMagnetsInMotor"], 0.0, 1000000.0)

        else:
            self.NumberOfMagnetsInMotor = 2

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: NumberOfMagnetsInMotor: " + str(self.NumberOfMagnetsInMotor))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PID_Kp" in setup_dict:
            self.PID_Kp = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("PID_Kp", setup_dict["PID_Kp"], self.PID_Kp_Min, self.PID_Kp_Max)

        else:
            self.PID_Kp = 100.0

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: PID_Kp: " + str(self.PID_Kp))
        #########################################################
        #########################################################
        
        #########################################################
        #########################################################
        if "PID_Ki" in setup_dict:
            self.PID_Ki = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("PID_Ki", setup_dict["PID_Ki"], self.PID_Ki_Min, self.PID_Ki_Max)

        else:
            self.PID_Ki = 1000000.0

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: PID_Ki: " + str(self.PID_Ki))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PID_Kd" in setup_dict:
            self.PID_Kd = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("PID_Kd", setup_dict["PID_Kd"], self.PID_Kd_Min, self.PID_Kd_Max)

        else:
            self.PID_Kd = 0.0

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: PID_Kd: " + str(self.PID_Kd))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "PID_IntegratorCap1to100percent" in setup_dict:
            self.PID_IntegratorCap1to100percent = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("PID_IntegratorCap1to100percent", setup_dict["PID_IntegratorCap1to100percent"], self.PID_IntegratorCap1to100percent_Min, self.PID_IntegratorCap1to100percent_Max)

        else:
            self.PID_IntegratorCap1to100percent = 100.0

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: PID_IntegratorCap1to100percent: " + str(self.PID_IntegratorCap1to100percent))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag" in setup_dict:
            self.SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag = self.PassThrough0and1values_ExitProgramOtherwise("SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag", setup_dict["SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag"])
        else:
            self.SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag = 0

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag: " + str(self.SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag" in setup_dict:
            self.SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag = self.PassThrough0and1values_ExitProgramOtherwise("SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag", setup_dict["SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag"])
        else:
            self.SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag = 1

        print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag: " + str(self.SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "VariableStreamingSendDataEveryDeltaT_MillisecondsInt" in setup_dict:
            self.VariableStreamingSendDataEveryDeltaT_MillisecondsInt = int(self.PassThroughFloatValuesInRange_ExitProgramOtherwise("VariableStreamingSendDataEveryDeltaT_MillisecondsInt", setup_dict["VariableStreamingSendDataEveryDeltaT_MillisecondsInt"], 1, 1000000000))

        else:
            self.VariableStreamingSendDataEveryDeltaT_MillisecondsInt = 5 ##10 worked for longer set of ["CB 0", "BS", "TC", "BA", "V 2", "FF"], 5 works for shorter-set of ["CB 0", "BS", "FF"].

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: VariableStreamingSendDataEveryDeltaT_MillisecondsInt: " + str(self.VariableStreamingSendDataEveryDeltaT_MillisecondsInt))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if "Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda" in setup_dict:
            self.Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda = self.PassThroughFloatValuesInRange_ExitProgramOtherwise("Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda", setup_dict["Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda"], 0.0, 1.0)

        else:
            self.Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda = 0.05 #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        print("RoboteqBLDCcontroller_ReubenPython2and3Class: Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda: " + str(self.Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda))
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.DataStreamingFrequency_CalculatedFromDedicatedTxThread_LowPassFilter_ReubenPython2and3ClassObject = LowPassFilter_ReubenPython2and3Class(dict([("UseMedianFilterFlag", 1),
                                                                                                            ("UseExponentialSmoothingFilterFlag", 1),
                                                                                                            ("ExponentialSmoothingFilterLambda", 0.05)])) #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        except:
            exceptions = sys.exc_info()[0]
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: DataStreamingFrequency_CalculatedFromDedicatedTxThread_LowPassFilter_ReubenPython2and3ClassObject, Exceptions: %s" % exceptions)
            traceback.print_exc()
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.DataStreamingFrequency_CalculatedFromDedicatedRxThread_LowPassFilter_ReubenPython2and3ClassObject = LowPassFilter_ReubenPython2and3Class(dict([("UseMedianFilterFlag", 1),
                                                                                                            ("UseExponentialSmoothingFilterFlag", 1),
                                                                                                            ("ExponentialSmoothingFilterLambda", 0.05)])) #new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        except:
            exceptions = sys.exc_info()[0]
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: DataStreamingFrequency_CalculatedFromDedicatedRxThread_LowPassFilter_ReubenPython2and3ClassObject, Exceptions: %s" % exceptions)
            traceback.print_exc()
            return
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        try:
            self.Speed_RPS_Calculated_LowPassFilter_ReubenPython2and3ClassObject = LowPassFilter_ReubenPython2and3Class(dict([("UseMedianFilterFlag", 1),
                                                                                                            ("UseExponentialSmoothingFilterFlag", 1),
                                                                                                            ("ExponentialSmoothingFilterLambda", self.Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda)])) ##new_filtered_value = k * raw_sensor_value + (1 - k) * old_filtered_value

        except:
            exceptions = sys.exc_info()[0]
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: Speed_RPS_Calculated_LowPassFilter_ReubenPython2and3ClassObject, Exceptions: %s" % exceptions)
            traceback.print_exc()
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

            #########################################################
            if ftd2xx_IMPORTED_FLAG == 1:
                self.SetAllFTDIdevicesLatencyTimer()
            #########################################################

            #########################################################
            self.FindAssignAndOpenSerialPort()
            #########################################################

            #########################################################
            if self.SerialConnectedFlag != 1:
                return
            #########################################################

        except:
            exceptions = sys.exc_info()[0]
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
            return
        #########################################################
        #########################################################

        '''
        ######################################################### ONLY INCLUDE THIS CODE SNIPPET IF WE CAN ACTUALLY QUERY THE SERIAL NUMBER FROM THE ROBOTEQ CONTROLLER.
        #########################################################
        if self.DetectedDeviceSerialNumber != self.DesiredSerialNumber_USBtoSerialConverter:
            print("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: The desired Serial Number (" + str(self.DesiredSerialNumber_USBtoSerialConverter) + ") does not match the detected serial number (" + str(self.DetectedDeviceSerialNumber) + ").")
            input("RoboteqBLDCcontroller_ReubenPython2and3Class __init__: Press any key (and enter) to exit.")
            sys.exit()
        #########################################################
        #########################################################
        '''

        #########################################################
        #########################################################
        self.TimeToSleepBetweenConfigurationCommands = 0.050

        self.ClearBufferHistory()
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)

        self.SetSerialCommandEcho(0)
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)

        self.StartVariableStreaming()
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)

        '''
        0: Open-loop
        1: Closed-loop speed #Not very accurate speed setting, tends to go unstable.
        2: Closed-loop position relative. Phidgets motor works for Kp = 200000.0, Ki = 10000.0
        3: Closed-loop count position #Can't get this to work 01/20/23.
        4: Closed-loop position tracking
        5: Closed-loop torque #Can't get this to work via UART 01/20/23. Also doesn't work for AnalogInput to Pin 4 (AI1).
        6: Closed-loop speed position #Accurate speed control. Phidgets motor works via UART for Kp = 100.0, Ki = 1000000.0. Also working with AnalogInput to Pin 4 (AI1).
        
        Closed Loop Speed Position Control
        In this mode, the controller computes the position at which the motor must be at every
        1ms. Then a PID compares that expected position with the current position and applies
        the necessary power level in order for the motor to reach that position. This mode is especially
        effective for accurate control at very slow speeds.
        '''

        if self.ControlMode_Starting in ["OpenLoop"]:
            self.Motor_Target_Min_UserSet = self.OpenLoopPower_Target_Min_UserSet
            self.Motor_Target_Max_UserSet = self.OpenLoopPower_Target_Max_UserSet
            self.Motor_Target_ToBeSet = self.OpenLoopPower_Target_Starting

        elif self.ControlMode_Starting in ["ClosedLoopPositionRelative", "ClosedLoopCountPosition", "ClosedLoopPositionTracking"]:
            self.Motor_Target_Min_UserSet = self.Position_Target_Min_UserSet
            self.Motor_Target_Max_UserSet = self.Position_Target_Max_UserSet
            self.Motor_Target_ToBeSet = self.Position_Target_Starting
            self.SetSpeed(self.Speed_Target_Starting) #So that PositionControl knows how fast to move

        elif self.ControlMode_Starting in ["ClosedLoopTorque"]:
            self.Motor_Target_Min_UserSet = self.Torque_Amps_Min_UserSet
            self.Motor_Target_Max_UserSet = self.Torque_Amps_Max_UserSet
            self.Motor_Target_ToBeSet = self.Torque_Amps_Starting

        elif self.ControlMode_Starting in ["ClosedLoopSpeed", "ClosedLoopSpeedPosition"]:
            self.Motor_Target_Min_UserSet = self.Speed_Target_Min_UserSet
            self.Motor_Target_Max_UserSet = self.Speed_Target_Max_UserSet
            self.Motor_Target_ToBeSet = self.Speed_Target_Starting

        self.Motor_Target_NeedsToBeChangedFlag = 1
        self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 1

        #########################################################
        if self.SetBrushlessCounterOnDeviceTo0atStartOfProgramFlag == 1:
            self.SetCurrentPositionAsHomeOnDevice()
        #########################################################

        #########################################################
        if self.SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag == 1:
            self.SetCurrentPositionAsHomeSoftwareOffsetOnly()
        #########################################################

        #########################################################
        self.SetControlMode(self.ControlMode_Starting, SkipQueueAndSendImmediately = 1)
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        self.SetSerialWatchdogTimerInMilliseconds(self.HeartbeatTimeIntervalMilliseconds, SkipQueueAndSendImmediately = 1)
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        self.SetCurrentLimit(self.Current_Amps_Starting, SkipQueueAndSendImmediately = 1)
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        self.SetAcceleration(self.Acceleration_Target_Starting, SkipQueueAndSendImmediately = 1)
        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        if self.ControlMode_EnlishString != "ClosedLoopTorque" and self.ControlMode_EnlishString != "OpenLoop":
            self.SetPID_Kp(self.PID_Kp, SkipQueueAndSendImmediately = 1)

        elif self.ControlMode_EnlishString == "ClosedLoopTorque":
            self.SetPID_Kp_TorqueModeFOC(self.PID_Kp, SkipQueueAndSendImmediately=1)

        else:
            print("Did not st Kp gain.")

        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        if self.ControlMode_EnlishString != "ClosedLoopTorque" and self.ControlMode_EnlishString != "OpenLoop":
            self.SetPID_Ki(self.PID_Ki, SkipQueueAndSendImmediately = 1)

        elif self.ControlMode_EnlishString == "ClosedLoopTorque":
            self.SetPID_Ki_TorqueModeFOC(self.PID_Ki, SkipQueueAndSendImmediately=1)

        else:
            print("Did not st Ki gain.")

        time.sleep(self.TimeToSleepBetweenConfigurationCommands)
        #########################################################

        #########################################################
        if self.ControlMode_EnlishString != "ClosedLoopTorque" and self.ControlMode_EnlishString != "OpenLoop":
            self.SetPID_Kd(self.PID_Kd, SkipQueueAndSendImmediately = 1)
            time.sleep(self.TimeToSleepBetweenConfigurationCommands)

        else:
            print("Did not st Kd gain.")
        #########################################################

        #########################################################
        if self.ControlMode_EnlishString != "ClosedLoopTorque" and self.ControlMode_EnlishString != "OpenLoop":
            self.SetPID_IntegratorCap1to100percent(self.PID_IntegratorCap1to100percent, SkipQueueAndSendImmediately = 1)
            time.sleep(self.TimeToSleepBetweenConfigurationCommands)

        else:
            print("Did not set IntegratorCap1to100percent.")
        #########################################################

        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.DedicatedRxThread_ThreadingObject = threading.Thread(target=self.DedicatedRxThread, args=())
        self.DedicatedRxThread_ThreadingObject.start()
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.DedicatedTxThread_ThreadingObject = threading.Thread(target=self.DedicatedTxThread, args=())
        self.DedicatedTxThread_ThreadingObject.start()
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        if self.USE_GUI_FLAG == 1:
            self.StartGUI(self.root)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        time.sleep(0.25)
        #########################################################
        #########################################################

        #########################################################
        #########################################################
        self.OBJECT_CREATED_SUCCESSFULLY_FLAG = 1
        #########################################################
        #########################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def __del__(self):
        pass
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_IntOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = int(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def LimitNumber_FloatOutputOnly(self, min_val, max_val, test_val):
        if test_val > max_val:
            test_val = max_val

        elif test_val < min_val:
            test_val = min_val

        else:
            test_val = test_val

        test_val = float(test_val)

        return test_val
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetAllFTDIdevicesLatencyTimer(self, FTDI_LatencyTimer_ToBeSet = 1):

        FTDI_LatencyTimer_ToBeSet = self.LimitNumber_IntOutputOnly(1, 16, FTDI_LatencyTimer_ToBeSet)

        FTDI_DeviceList = ftd2xx.listDevices()
        print("FTDI_DeviceList: " + str(FTDI_DeviceList))

        if FTDI_DeviceList != None:

            for Index, FTDI_SerialNumber in enumerate(FTDI_DeviceList):

                #################################
                try:
                    if sys.version_info[0] < 3: #Python 2
                        FTDI_SerialNumber = str(FTDI_SerialNumber)
                    else:
                        FTDI_SerialNumber = FTDI_SerialNumber.decode('utf-8')

                    FTDI_Object = ftd2xx.open(Index)
                    FTDI_DeviceInfo = FTDI_Object.getDeviceInfo()

                    '''
                    print("FTDI device with serial number " +
                          str(FTDI_SerialNumber) +
                          ", DeviceInfo: " +
                          str(FTDI_DeviceInfo))
                    '''

                except:
                    exceptions = sys.exc_info()[0]
                    print("FTDI device with serial number " + str(FTDI_SerialNumber) + ", could not open FTDI device, Exceptions: %s" % exceptions)
                #################################

                #################################
                try:
                    FTDI_Object.setLatencyTimer(FTDI_LatencyTimer_ToBeSet)
                    time.sleep(0.005)

                    FTDI_LatencyTimer_ReceivedFromDevice = FTDI_Object.getLatencyTimer()
                    FTDI_Object.close()

                    if FTDI_LatencyTimer_ReceivedFromDevice == FTDI_LatencyTimer_ToBeSet:
                        SuccessString = "succeeded!"
                    else:
                        SuccessString = "failed!"

                    print("FTDI device with serial number " +
                          str(FTDI_SerialNumber) +
                          " commanded setLatencyTimer(" +
                          str(FTDI_LatencyTimer_ToBeSet) +
                          "), and getLatencyTimer() returned: " +
                          str(FTDI_LatencyTimer_ReceivedFromDevice) +
                          ", so command " +
                          SuccessString)

                except:
                    exceptions = sys.exc_info()[0]
                    print("FTDI device with serial number " + str(FTDI_SerialNumber) + ", could not set/get Latency Timer, Exceptions: %s" % exceptions)
                #################################

        else:
            print("SetAllFTDIdevicesLatencyTimer ERROR: FTDI_DeviceList is empty, cannot proceed.")
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def FindAssignAndOpenSerialPort(self):
        self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Finding all serial ports...")

        ##############
        SerialNumberToCheckAgainst = str(self.DesiredSerialNumber_USBtoSerialConverter)
        if self.my_platform == "linux" or self.my_platform == "pi":
            SerialNumberToCheckAgainst = SerialNumberToCheckAgainst[:-1] #The serial number gets truncated by one digit in linux
        else:
            SerialNumberToCheckAgainst = SerialNumberToCheckAgainst
        ##############

        ##############
        SerialPortsAvailable_ListPortInfoObjetsList = serial.tools.list_ports.comports()
        ##############

        ###########################################################################
        SerialNumberFoundFlag = 0
        for SerialPort_ListPortInfoObjet in SerialPortsAvailable_ListPortInfoObjetsList:

            SerialPortName = SerialPort_ListPortInfoObjet[0]
            Description = SerialPort_ListPortInfoObjet[1]
            VID_PID_SerialNumber_Info = SerialPort_ListPortInfoObjet[2]
            self.MyPrint_WithoutLogFile(SerialPortName + ", " + Description + ", " + VID_PID_SerialNumber_Info)

            if VID_PID_SerialNumber_Info.find(SerialNumberToCheckAgainst) != -1 and SerialNumberFoundFlag == 0: #Haven't found a match in a prior loop
                self.SerialPortNameCorrespondingToCorrectSerialNumber = SerialPortName
                SerialNumberFoundFlag = 1 #To ensure that we only get one device
                self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Found serial number " + SerialNumberToCheckAgainst + " on port " + self.SerialPortNameCorrespondingToCorrectSerialNumber)
                #WE DON'T BREAK AT THIS POINT BECAUSE WE WANT TO PRINT ALL SERIAL DEVICE NUMBERS WHEN PLUGGING IN A DEVICE WITH UNKNOWN SERIAL NUMBE RFOR THE FIRST TIME.
        ###########################################################################

        ###########################################################################
        if(self.SerialPortNameCorrespondingToCorrectSerialNumber != "default"): #We found a match

            try: #Will succeed as long as another program hasn't already opened the serial line.

                self.SerialObject = serial.Serial(self.SerialPortNameCorrespondingToCorrectSerialNumber, self.SerialBaudRate, timeout=self.SerialTimeoutSeconds, parity=self.SerialParity, stopbits=self.SerialStopBits, bytesize=self.SerialByteSize, xonxoff=self.SerialXonXoffSoftwareFlowControl)

                try:
                    if self.my_platform == "windows":
                        self.SerialObject.set_buffer_size(rx_size=self.SerialRxBufferSize, tx_size=self.SerialTxBufferSize)
                except:
                    self.SerialConnectedFlag = 0
                    exceptions = sys.exc_info()[0]
                    self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort, 'set_buffer_size' call failed, exception: %s" % exceptions)

                self.SerialConnectedFlag = 1
                self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: Serial is connected and open on port: " + self.SerialPortNameCorrespondingToCorrectSerialNumber)

            except:
                self.SerialConnectedFlag = 0
                self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: ERROR: Serial is physically plugged in but IS IN USE BY ANOTHER PROGRAM.")
                exceptions = sys.exc_info()[0]
                self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort, exception: %s" % exceptions)
        else:
            self.SerialConnectedFlag = -1
            self.MyPrint_WithoutLogFile("FindAssignAndOpenSerialPort: ERROR: Could not find the serial device. IS IT PHYSICALLY PLUGGED IN?")
        ###########################################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def PassThrough0and1values_ExitProgramOtherwise(self, InputNameString, InputNumber, ExitProgramIfFailureFlag = 0):

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error. InputNumber '" + InputNameString + "' must be a numerical value, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1.0:
                return InputNumber_ConvertedToFloat

            else:

                print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error. '" +
                              str(InputNameString) +
                              "' must be 0 or 1 (value was " +
                              str(InputNumber_ConvertedToFloat) +
                              "). Press any key (and enter) to exit.")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()

                else:
                    return -1
                ##########################

            ##########################################################################################################

        except:

            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -1
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def PassThroughFloatValuesInRange_ExitProgramOtherwise(self, InputNameString, InputNumber, RangeMinValue, RangeMaxValue, ExitProgramIfFailureFlag = 0):

        ##########################################################################################################
        ##########################################################################################################
        try:
            ##########################################################################################################
            InputNumber_ConvertedToFloat = float(InputNumber)
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error. InputNumber '" + InputNameString + "' must be a float value, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        try:

            ##########################################################################################################
            InputNumber_ConvertedToFloat_Limited = self.LimitNumber_FloatOutputOnly(RangeMinValue, RangeMaxValue, InputNumber_ConvertedToFloat)

            if InputNumber_ConvertedToFloat_Limited != InputNumber_ConvertedToFloat:
                print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" +
                      str(InputNameString) +
                      "' must be in the range [" +
                      str(RangeMinValue) +
                      ", " +
                      str(RangeMaxValue) +
                      "] (value was " +
                      str(InputNumber_ConvertedToFloat) + ")")

                ##########################
                if ExitProgramIfFailureFlag == 1:
                    sys.exit()
                else:
                    return -11111.0
                ##########################

            else:
                return InputNumber_ConvertedToFloat_Limited
            ##########################################################################################################

        except:
            ##########################################################################################################
            exceptions = sys.exc_info()[0]
            print(self.TellWhichFileWereIn() + ", PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
            traceback.print_exc()

            ##########################
            if ExitProgramIfFailureFlag == 1:
                sys.exit()
            else:
                return -11111.0
            ##########################

            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################

    ##########################################################################################################
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
    def getPreciseSecondsTimeStampString(self):
        ts = time.time()

        return ts
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GetMostRecentDataDict(self):

        if self.EXIT_PROGRAM_FLAG == 0:

            return deepcopy(self.MostRecentDataDict) #deepcopy IS required as MostRecentDataDict contains lists.

        else:
            return dict()  # So that we're not returning variables during the close-down process.
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_DedicatedTxThread_Filtered(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread - self.LastTime_CalculatedFromDedicatedTxThread

            if self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread != 0.0:
                DataStreamingFrequency_CalculatedFromDedicatedTxThread_TEMP = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedTxThread
                self.DataStreamingFrequency_CalculatedFromDedicatedTxThread = self.DataStreamingFrequency_CalculatedFromDedicatedTxThread_LowPassFilter_ReubenPython2and3ClassObject.AddDataPointFromExternalProgram(DataStreamingFrequency_CalculatedFromDedicatedTxThread_TEMP)["SignalOutSmoothed"]

            self.LastTime_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_DedicatedTxThread_Filtered ERROR with Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def UpdateFrequencyCalculation_DedicatedRxThread_Filtered(self):

        try:
            self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread - self.LastTime_CalculatedFromDedicatedRxThread

            if self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread != 0.0:
                DataStreamingFrequency_CalculatedFromDedicatedRxThread_TEMP = 1.0/self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread
                self.DataStreamingFrequency_CalculatedFromDedicatedRxThread = self.DataStreamingFrequency_CalculatedFromDedicatedRxThread_LowPassFilter_ReubenPython2and3ClassObject.AddDataPointFromExternalProgram(DataStreamingFrequency_CalculatedFromDedicatedRxThread_TEMP)["SignalOutSmoothed"]

            self.LastTime_CalculatedFromDedicatedRxThread = self.CurrentTime_CalculatedFromDedicatedRxThread
        except:
            exceptions = sys.exc_info()[0]
            print("UpdateFrequencyCalculation_DedicatedRxThread_Filtered ERROR with Exceptions: %s" % exceptions)
            traceback.print_exc()
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ConvertBytesObjectToString(self, InputBytesObject):

        if sys.version_info[0] < 3:  # Python 2
            OutputString = str(InputBytesObject)

        else:
            OutputString = InputBytesObject.decode('utf-8')

        return OutputString
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SendSerialStrToTx(self, SerialStrToTx):

        if self.SerialConnectedFlag == 1:

            try:

                if SerialStrToTx[-1] != "\r":
                    SerialStrToTx = SerialStrToTx + "\r"

                SerialStrToTx = SerialStrToTx

                self.SerialObject.write(SerialStrToTx.encode('utf-8'))

                self.SerialStrToTx_LAST_SENT = SerialStrToTx

                self.MostRecentDataDict["SerialStrToTx_LAST_SENT"] = self.SerialStrToTx_LAST_SENT

            except:
                exceptions = sys.exc_info()[0]
                print("SendSerialStrToTx, exceptions: %s" % exceptions)

        else:
            print("SendSerialStrToTx: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ClearBufferHistory(self, SkipQueueAndSendImmediately = 0):

        if self.SerialConnectedFlag == 1:
            try:

                self.SerialObject.flushInput()
                #self.SerialObject.write("# C \r".encode('utf-8'))  # Clear Buffer History

                StringToTx = "# C \r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("ClearBufferHistory, exceptions: %s" % exceptions)

        else:
            print("ClearBufferHistory: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetSerialWatchdogTimerInMilliseconds(self, WatchdogTimerDurationMilliseconds_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 274:
        This is the Serial Commands watchdog timeout parameter. It is used to detect when the
        controller is no longer receiving commands and switch to the next priority level. Any Realtime
        Command arriving from RS232, RS485, TCP, USB, CAN or Microbasic Scripting, The
        watchdog value is a number in ms (1000 = 1s). The watchdog function can be disabled by
        setting this value to 0. The watchdog will only detect the loss of real time commands, as
        shown in section 6. All other traffic on the serial port will not refresh the watchdog timer.
        As soon as a valid command is received, motor operation will resume.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                WatchdogTimerDurationMilliseconds_Input = self.LimitNumber_IntOutputOnly(0.0, 65000.0, WatchdogTimerDurationMilliseconds_Input)

                #Setting to 0 disables the watchdog!
                StringToTx = "^RWD " + str(WatchdogTimerDurationMilliseconds_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetSerialWatchdogTimerInMilliseconds, exceptions: %s" % exceptions)

        else:
            print("SetSerialWatchdogTimerInMilliseconds: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetSerialCommandEcho(self, EnabledState, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 270:
        ECHOF - Enable/Disable Serial Echo
        HexCode: 09
        Description:
        This command is used to disable/enable the echo on the RS232, RS485, TCP or USB port.
        By default, the controller will echo everything that enters the serial communication port.
        By setting ECHOF to 1, commands are no longer being echoed. The controller will only
        reply to queries and the acknowledgements to commands can be seen.
        Syntax Serial: ^ECHOF nn
        ~ECHOF
        Syntax Scripting: setconfig(_ECHOF, nn)
        Number of Arguments: 1
        '''

        if self.SerialConnectedFlag == 1:
            try:

                EnabledState = int(EnabledState)

                if EnabledState not in [0, 1]:
                    print("SetSerialCommandEcho: Error, EnabledState must be 0 or 1.")
                    return 0

                if EnabledState == 1:
                    IntToSend = 0 #The logical states are switched
                else:
                    IntToSend = 1

                StringToTx = "^ECHOF " + str(IntToSend) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetSerialCommandEcho, exceptions: %s" % exceptions)

        else:
            print("SetSerialCommandEcho: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    def StartVariableStreaming(self, SkipQueueAndSendImmediately = 0):

        '''
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ "Roboteq Controllers User Manual v2.0.pdf" pageS *202* HAS VARIABLES $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

        #TM Read time (only to the nearest second)
        #AI N Read Nth analog in
        #F read pos/vel sensor feedback
        #ANG read rotor angle DOESN'T SEEM TO WORK
        #A Motor current in amps

        FF Fault flags
        FF = f1 + f2*2 + f3*4 + ... + fn*2^n-1 Type: Unsigned 16-bit Min: 0 Max: 65535
        Where:
        f1 = Overheat
        f2 = Overvoltage
        f3 = Undervoltage
        f4 = Short circuit
        f5 = Emergency stop
        f6 = Motor/Sensor Setup fault
        f7 = MOSFET failure
        f8 = Default configuration loaded at startup

        #FF Read Runtime Status Flag ####THIS IS THE MONEY SHOT, READ ON "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 223
        #FS status flags "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 224
        #BCR Brushless count relative, seems to work OK
        #C encoder count absolute doesn't work currently trying to get hall count
        #CB Read Absolute Brushless Counter WORKS
        #BS Read BL Motor Speed in RPM WORKS
        #V volts, 1 : Internal volts, 2 : Battery volts, 3 : 5V output, nn = Volts * 10 for internal and battery volts. Milivolts for 5V output
        '''

        if self.SerialConnectedFlag == 1:
            try:

                self.PrefixOfReturnedMessages = "" #could be "d="
                self.DelimiterOfReturnedMessages = ":"

                self.QuoteString = "\""

                # ["CB", "BS", "TM", "AI 1", "F 0", "RMP", "POS"]

                #self.VariableNamesToStartStreamingList = ["F 0", "BCR", "S", "BS", "AI 1", "BA", "V 2", "FF"]
                #self.VariableNamesEnglishList = ["EncoderPosition", "BrushlessCountRelative", "EncoderSpeedRPM", "SpeedRPM", "AnalogInput1", "BatteryCurrentInAmps", "BatteryVoltsX10", "FaultFlags"]

                #### Longer set
                #self.VariableNamesToStartStreamingList = ["CB 0", "BS", "P", "TC", "A", "DPA", "BA", "V 2", "AOM", "FF"]
                #self.VariableNamesEnglishList = ["AbsoluteBrushlessCounter", "SpeedRPM", "MotorPowerOutputApplied", "TorqueTarget", "MotorCurrentRMSamps", "MotorCurrentPeakAmps", "BatteryCurrentInAmps", "BatteryVoltsX10", "ActualOperationMode", "FaultFlags"]
                #### Longer set

                #### Medium set
                #Was using this prior to 11/09/24 when we were relying on the position/velocity reports from the Roboteq (before switching to Phidgets External Encoder)
                #self.VariableNamesToStartStreamingList = ["CB 0", "BS", "P", "AOM", "FF"]
                #self.VariableNamesEnglishList = ["AbsoluteBrushlessCounter", "SpeedRPM", "MotorPowerOutputApplied", "ActualOperationMode", "FaultFlags"]
                #### Medium set

                #### Shorter set WITH POSITION DEBUGGING
                #self.VariableNamesToStartStreamingList = ["CB 0", "AOM", "FF"]
                #self.VariableNamesEnglishList = ["AbsoluteBrushlessCounter", "ActualOperationMode", "FaultFlags"]
                #### Shorter set WITH POSITION DEBUGGING

                #### Shortest set
                self.VariableNamesToStartStreamingList = ["AOM", "FF"]
                self.VariableNamesEnglishList = ["ActualOperationMode", "FaultFlags"]
                #### Shortest set

                StringToTx = "/" + self.QuoteString + self.PrefixOfReturnedMessages + self.QuoteString + "," + self.QuoteString + self.DelimiterOfReturnedMessages + self.QuoteString

                for VariableNamesToStartStreaming in self.VariableNamesToStartStreamingList:
                    StringToTx = StringToTx + "?" + VariableNamesToStartStreaming + "_"

                StringToTx = StringToTx + "_# " + str(self.VariableStreamingSendDataEveryDeltaT_MillisecondsInt) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("StartVariableStreaming, exceptions: %s" % exceptions)

        else:
            print("StartVariableStreaming: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GoToSpeedOrRelativePositionGeneric(self, SpeedOrRelativePosition_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 184:
          G is the main command for activating the motors. The command is a number ranging
        1000 to +1000 so that the controller respond the same way as when commanded using
        Analog or Pulse, which are also -1000 to +1000 commands. The effect of the command
        differs from one operating mode to another.
        In Open Loop Speed mode the command value is the desired power output level to be
        applied to the motor.
        In Closed Loop Speed mode, the command value is relative to the maximum speed that is
        stored in the MXRPM configuration parameter.
        In Closed Loop Position Relative and in the Closed Loop Tracking mode, the command is
        the desired relative destination position mode.
        The G command has no effect in the Position Count mode.
        In Torque mode, the command value is the desired Motor Amps relative to the Amps Limit
        configuration parameters
        Syntax Serial: !G [nn] mm
        Syntax Scripting: setcommand(_G, nn, mm)
        setcommand(_GO, nn, mm)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Value Type: Signed 32-bit
        Min: -1000 Max: 1000

        Where:
        cc = Motor channel
        nn = Command value
        Example:
        !G 1 500 : In Open Loop Speed mode, applies 50% power to motor channel 1
        !G 1 500 : In Closed Loop Speed mode, assuming that 3000 is contained in Max RPM parameter
        (MXRPM), motor will go to 1500 RPM
        !G 1 500 : In Closed Loop Relative or Closed Loop Tracking modes, the motor will move to
        75% position of the total -1000 to +1000 motion range
        !G 1 500 : In Torque mode, assuming that Amps Limit is 60A, motor power will rise until
        30A are measured.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                SpeedOrRelativePosition_Input = self.LimitNumber_IntOutputOnly(-1000.0, 1000.0, SpeedOrRelativePosition_Input)

                StringToTx = "!G 1 " + str(SpeedOrRelativePosition_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("GoToSpeedOrRelativePositionGeneric, exceptions: %s" % exceptions)

        else:
            print("GoToSpeedOrRelativePositionGeneric: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GoToRelativePosition(self, RelativePosition_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 188:
        Alias: MPOSREL HexCode: 11 CANOpen id: 0x200F
        Description:
        This command is used in the Position Count mode to make the motor move to a feedback
        sensor count position that is relative to its current desired position.
        Syntax Serial: PR [cc] nn
        Syntax Scripting: setcommand(_PR, cc, nn)
        setcommand(_MPOSREL, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Delta Type: Signed 32-bit
        Min: -2147M Max: +2147M
        Where:
        cc = Motor channel
        nn = Relative count position
        Example:
        !PR 1 10000 : while motor is stopped after power up and counter = 0, motor 1 will go to
        +10000
        !PR 2 10000 : while previous command was absolute goto position !P 2 5000, motor will
        go to +15000
        Note:
        Beware that counter will rollover at counter values +/-2’147’483’648.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                RelativePosition_Input = self.LimitNumber_IntOutputOnly(self.Position_Target_Min_UserSet, self.Position_Target_Max_UserSet, RelativePosition_Input)

                StringToTx = "!PR 1 " + str(RelativePosition_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("GoToRelativePosition, exceptions: %s" % exceptions)

        else:
            print("GoToRelativePosition: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GoToTorqueNM_TC(self, TorqueNM_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 162:
        '''

        if self.SerialConnectedFlag == 1:
            try:
                TorqueAmps_Input = 100.0*TorqueNM_Input #Command is 100x actual NM torque
                #TorqueAmps_Input = self.LimitNumber_IntOutputOnly(-1.0*self.max, self.min, TorqueNM_Input)

                StringToTx = "!TC 1 " + self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(TorqueAmps_Input, 0, 1) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("GoToTorqueNM_TC, exceptions: %s" % exceptions)

        else:
            print("GoToTorqueNM_TC: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GoToTorqueAmps_SinusoidalModeOnly(self, TorqueAmps_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 184:

        The torque mode uses the Motor Amps and not the Battery Amps. See “Battery Current
        vs. Motor Current”on "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 28. In some Roboteq controllers, Battery Amps is measured
        and Motor Amps is estimated. The estimation is fairly accurate at power level of 20% and
        higher. Its accuracy drops below 20% of PWM output and no motor current is measured
        at all when the power output level is 0%, even though current may be flowing in the
        motor, as it would be the case if the motor is pushed. The torque mode will therefore not
        operate with good precision at low power output levels.
        Furthermore the resolution of the amps capture is limited to around 0.5% of the full range.
        On high current controller models, for example, amps are measured with 500mA increments.
        If the amps limit is set to 100A, this means the torque will be adjustable with a 0.5%
        resolution. If on the same large controller the amps limit is changed to 10A, the torque will
        be adjustable with the same 500mA granularity which will result in 5% resolution. For best
        results use an amps limit that is at least 50% than the controller’s max rating. On newer
        Brushless motor controllers, amps sensors are placed at the motor output and motor amps
        are measured directly. Torque mode will work effectively on these models.
        '''

        if self.SerialConnectedFlag == 1:
            try:
                TorqueAmps_Input = 10.0*TorqueAmps_Input #Command is 10x actual AMPS
                TorqueAmps_Input = self.LimitNumber_IntOutputOnly(self.Torque_Amps_Min_MotorHardLimit, self.Torque_Amps_Max_UserSet, TorqueAmps_Input)

                StringToTx = "!GIQ 1 " + str(TorqueAmps_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("GoToTorqueAmps_SinusoidalModeOnly, exceptions: %s" % exceptions)

        else:
            print("GoToTorqueAmps_SinusoidalModeOnly: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetCurrentLimit(self, CurrentLimitAmps_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" "Roboteq Controllers User Manual v2.0.pdf" page 298:
        HexCode: 2A
        Description:
        This is the maximum Amps that the controller will be allowed to deliver to a motor regardless
        the load of that motor. The value is entered in Amps multiplied by 10. The value is the
        Amps that are measured at the motor and not the Amps measured from a battery. When
        the motor draws current that is above that limit, the controller will automatically reduce
        the output power until the current drops below that limit. For brushless controllers this
        value is considered to be in RMS.
        Syntax Serial: ^ALIM cc nn
        ~ALIM [cc]
        Syntax Scripting: setconfig(_ALIM, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Limit
        Type: Unsigned 16-bit
        Min: 10 Max: Max Amps in datasheet
        Default: See note
        Where:
        cc = Motor channel
        nn = Amps *10
        Example:
        ^ALIM1 455: Set Amp limit for Motor 1 to 45.5A
        Note:
        Default value is typically set to 75% of the controller’s max amps as defined in the datasheet
        '''

        if self.SerialConnectedFlag == 1:
            try:

                CurrentLimitAmps_Input = self.LimitNumber_FloatOutputOnly(self.Current_Amps_Min_UserSet, self.Current_Amps_Max_UserSet, CurrentLimitAmps_Input)
                CurrentLimitAmps_Input = CurrentLimitAmps_Input*10 #argument is 10xAmps

                StringToTx = "^ALIM 1 " + str(CurrentLimitAmps_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetCurrentLimit, exceptions: %s" % exceptions)

        else:
            print("SetCurrentLimit: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetHomeOrBrushlessCounterOnDevice(self, BrushlessCounterToBeSetAsHomeOnDevice_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 178:
        #Alias: SBLCNTR HexCode: 05 CANOpen id: 0x2004
        Description:
        This command loads the brushless counter with the value contained in the command
        argument. Beware that changing the controller value while operating in closed-loop mode
        can have adverse effects.
        Syntax Serial: !CB [cc] nn
        Syntax Scripting: setcommand(_CB, cc, nn)
        setcommand(_SBLCNTR, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Value Type: Signed 32-bit
        Min: -2147M Max: +2147M
        Where:
        cc = Motor channel
        nn = Counter value
        Example:
        !CB 1 -1000 : Loads -1000 in brushless counter 1
        !CB 2 0 : Clears brushless counter 2
        '''

        if self.SerialConnectedFlag == 1:
            try:

                BrushlessCounterToBeSetAsHomeOnDevice_Input = self.LimitNumber_FloatOutputOnly(self.Position_Target_Min_UserSet, self.Position_Target_Max_UserSet, BrushlessCounterToBeSetAsHomeOnDevice_Input)

                StringToTx = "!CB 1 " + str(BrushlessCounterToBeSetAsHomeOnDevice_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetHomeOrBrushlessCounterOnDevice, exceptions: %s" % exceptions)

        else:
            print("SetHomeOrBrushlessCounterOnDevice: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_Kp(self, Kp_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 311:
        HexCode: 2E
        Description:
        Sets the PID’s Proportional Gain for that channel. The value is set as the gain multiplied
        by 10^6. This gain is used in all closed loop modes. In Torque mode, on brushless contontrollers,
        the FOC’s PID is used instead and this parameter is used for the speed limiting
        tuning.
        Syntax Serial: ^KP cc nn
        ~KP
        Syntax Scripting: setconfig(_KP, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Gain Type: Unsigned 32-bit
        Min: 0 Max: 2,000,000,000 Default: 0
        Where:
        cc = Motor channel
        nn = Proportional Gain *1,000,000
        Example:
        ^KP 1 1500000: Set motor channel 1 Proportional Gain to 1.5.
        Note:
        Do not use default values. As a starting point, use P=2, I=0, D=0 in position modes (including
        Speed Position mode). Use P=0, I=1, D=0 in closed loop speed mode and in torque
        mode. Perform full tuning after that.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                Kp_Input = 1000000 * Kp_Input
                Kp_Input = self.LimitNumber_IntOutputOnly(self.PID_Kp_Min, self.PID_Kp_Max, Kp_Input)

                StringToTx = "^KP 1 " + str(Kp_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)


                print("SetPID_Kp: " + StringToTx)

                #self.Kp = Kp_Input/1000000

                #print("SetPID_Kp: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_Kp, exceptions: %s" % exceptions)

        else:
            print("SetPID_Kp: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_Kp_TorqueModeFOC(self, Kp_Input, FluxGain1trqGain2_Flag = 2, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 328:

        HexCode: 8E
        Description:
        On brushless motor controller operating in sinusoidal mode, this parameter sets the Integral
        gain in the PI that is used for Field Oriented Control. Two gains can be set for each
        motor channel, in order to control the Flux and Torque current. When operating in trapezoidal
        mode the gains for the Torque current are used for closed loop torque mode.
        Syntax Serial: ^KPF cc nn
        ~KPF [cc]

        Syntax Scripting: setconfig(_KPF, cc)
        Number of Arguments:
        Argument 1: AmpsChannel
        Min: 1 Max: 2 * Total Number of Motors
        Argument 2: Gain Type: Unsigned 32-bit
        Min: 0 Max: 2,000,000,000 Default: 0
        Where:
        cc (single channel) =
        1: Flux Gain
        2: Torque Gain
        cc (dual channel) =
        1: Flux Gain for motor 1
        2: Flux Gain for motor 2
        3: Torque Gain for motor 1
        4: Torque Gain for motor 2
        nn = Gain * 1,000,000
        Example:
        ^KPF 1 230000: Set motor channel 1 Flux Integral Gain to 0.23.
        '''

        FluxGain1trqGain2_Flag = int(FluxGain1trqGain2_Flag)
        if FluxGain1trqGain2_Flag not in [1, 2]:
            print("SetPID_Kp_TorqueModeFOC, ERROR: FluxGain1trqGain2_Flag must be 1 or 2.")
            return

        if self.SerialConnectedFlag == 1:
            try:

                Kp_Input = 1000000 * Kp_Input
                Kp_Input = self.LimitNumber_IntOutputOnly(self.PID_Kp_Min, self.PID_Kp_Max, Kp_Input)

                StringToTx = "^KPF " + str(FluxGain1trqGain2_Flag) + " " + str(Kp_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.Kp = Kp_Input/1000000

                print("SetPID_Kp_TorqueModeFOC: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_Kp_TorqueModeFOC, exceptions: %s" % exceptions)

        else:
            print("SetPID_Kp_TorqueModeFOC: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_Ki(self, Ki_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 310:
        HexCode: 2F
        Description:
        Sets the PID’s Integral Gain for that channel. The value is set as the gain multiplied by 10^6.
        This gain is used in all closed loop modes. In Torque mode, on brushless contontrollers, the
        FOC’s PID is used instead and this parameter is used for the speed limiting tuning.
        Syntax Serial: ^KI cc nn
        ~KI
        Syntax Scripting: setconfig(_KI, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Gain Type: Unsigned 32-bit
        Min: 0 Max: 2,000,000,000 Default: 0
        Where:
        cc = Motor channel
        nn = Integral Gain *1,000,000
        Example:
        ^KI 1 1500000: Set motor channel 1 Integral Gain to 1.5.
        Note:
        Do not use default values. As a starting point, use P=2, I=0, D=0 in position modes
        (including Speed Position mode). Use P=0, I=1, D=0 in closed loop speed mode and in
        torque mode. Perform full tuning after that.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                Ki_Input = 1000000 * Ki_Input
                Ki_Input = self.LimitNumber_IntOutputOnly(self.PID_Ki_Min, self.PID_Ki_Max, Ki_Input)

                StringToTx = "^KI 1 " + str(Ki_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.Ki = Ki_Input/1000000

                #print("SetPID_Ki: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_Ki, exceptions: %s" % exceptions)

        else:
            print("SetPID_Ki: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_Ki_TorqueModeFOC(self, Ki_Input, FluxGain1trqGain2_Flag = 2, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 328:

        HexCode: 8E
        Description:
        On brushless motor controller operating in sinusoidal mode, this parameter sets the Integral
        gain in the PI that is used for Field Oriented Control. Two gains can be set for each
        motor channel, in order to control the Flux and Torque current. When operating in trapezoidal
        mode the gains for the Torque current are used for closed loop torque mode.
        Syntax Serial: ^KIF cc nn
        ~KIF [cc]

        Syntax Scripting: setconfig(_KIF, cc)
        Number of Arguments:
        Argument 1: AmpsChannel
        Min: 1 Max: 2 * Total Number of Motors
        Argument 2: Gain Type: Unsigned 32-bit
        Min: 0 Max: 2,000,000,000 Default: 0
        Where:
        cc (single channel) =
        1: Flux Gain
        2: Torque Gain
        cc (dual channel) =
        1: Flux Gain for motor 1
        2: Flux Gain for motor 2
        3: Torque Gain for motor 1
        4: Torque Gain for motor 2
        nn = Gain * 1,000,000
        Example:
        ^KIF 1 230000: Set motor channel 1 Flux Integral Gain to 0.23.
        '''

        FluxGain1trqGain2_Flag = int(FluxGain1trqGain2_Flag)
        if FluxGain1trqGain2_Flag not in [1, 2]:
            print("SetPID_Ki_TorqueModeFOC, ERROR: FluxGain1trqGain2_Flag must be 1 or 2.")
            return

        if self.SerialConnectedFlag == 1:
            try:

                Ki_Input = 1000000 * Ki_Input
                Ki_Input = self.LimitNumber_IntOutputOnly(self.PID_Ki_Min, self.PID_Ki_Max, Ki_Input)

                StringToTx = "^KIF " + str(FluxGain1trqGain2_Flag) + " " + str(Ki_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.Ki = Ki_Input/1000000

                #print("SetPID_Ki_TorqueModeFOC: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_Ki_TorqueModeFOC, exceptions: %s" % exceptions)

        else:
            print("SetPID_Ki_TorqueModeFOC: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_Kd(self, Kd_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 309:
        HexCode: 30
        Description:
        Sets the PID’s Differential Gain for that channel. The value is set as the gain multiplied by
        10^6. This gain is used in all closed loop modes. In Torque mode, on brushless controllers,
        the FOC’s PID is used instead and this parameter is used for the speed limiting tuning.
        Syntax Serial: ^KD cc nn
        ~KD [cc]
        Syntax Scripting: setconfig(_KD, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Gain Type: Unsigned 32-bit
        Min: 0 Max: 2,000,000,000 Default: 0
        Where:
        cc = Motor channel
        nn = Differential Gain *1,000,000
        Example:
        ^KD 1 1500000: Set motor channel 1 Differential Gain to 1.5.
        Note:
        Do not use default values. As a starting point, use P=2, I=0, D=0 in position modes
        (including Speed Position mode). Use P=0, I=1, D=0 in closed loop speed mode and in
        torque mode. Perform full tuning after that.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                Kd_Input = 1000000 * Kd_Input
                Kd_Input = self.LimitNumber_IntOutputOnly(self.PID_Kd_Min, self.PID_Kd_Max, Kd_Input)

                StringToTx = "^KD 1 " + str(Kd_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.Kd = Kd_Input/1000000

                #print("SetPID_Kd: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_Kd, exceptions: %s" % exceptions)

        else:
            print("SetPID_Kd: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetPID_IntegratorCap1to100percent(self, IntegratorCap1to100percent_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 309:
        HexCode: 32
        Description:
        This parameter is the integral cap as a percentage. This parameter will limit maximum
        level of the Integral factor in the PID. It is particularly useful in position systems with long
        travel movement, and where the integral factor would otherwise become very large because
        of the extended time the integral would allow to accumulate. This parameter can
        be used to dampen the effect of the integral parameter without reducing the gain. This
        parameter may adversely affect system performance in closed loop speed mode as the
        Integrator must be allowed to reach high values in order for good speed control.
        Syntax Serial: ^ICAP cc nn
        ~ICAP [cc]
        Syntax Scripting: setconfig(_ICAP, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Cap
        Type: Unsigned 8-bit
        Min: 1 Max: 100
        Default: 100%
        Where:
        cc = Motor channel
        nn = Integral cap in %
        '''

        if self.SerialConnectedFlag == 1:
            try:

                IntegratorCap1to100percent_Input = self.LimitNumber_IntOutputOnly(1, 100, IntegratorCap1to100percent_Input)

                StringToTx = "^ICAP 1 " + str(IntegratorCap1to100percent_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.PID_IntegratorCap1to100percent = IntegratorCap1to100percent_Input

                #print("SetPID_IntegratorCap1to100percent: " + StringToTx)
                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetPID_IntegratorCap1to100percent, exceptions: %s" % exceptions)

        else:
            print("SetPID_IntegratorCap1to100percent: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetSpeed(self, Speed_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 191:
        Alias: MOTVEL HexCode: 03 CANOpen id: 0x2002
        Description:
        In the Closed-Loop Speed mode, this command will cause the motor to spin at the desired
        RPM speed. In Closed-Loop Position modes, this commands determines the speed
        at which the motor will move from one position to the next. It will not actually start the
        motion.
        Syntax Serial: !S [cc] nn
        Syntax Scripting: setcommand(_S, cc, nn)
        setcommand(_MOTVEL, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Value Type: Signed 32-bit
        Min:-65535 Max: 65535
        Where:
        cc = Motor channel
        nn = Speed value in RPM
        Example:
        !S 2500 : set motor 1 position velocity to 2500 RPM
        '''

        if self.SerialConnectedFlag == 1:
            try:

                Speed_Input = self.LimitNumber_IntOutputOnly(self.Speed_Target_Min_UserSet, self.Speed_Target_Max_UserSet, Speed_Input)

                StringToTx = "!S 1 " + str(Speed_Input) + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("Speed_Input, exceptions: %s" % exceptions)

        else:
            print("Speed_Input: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetAcceleration(self, Acceleration_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 175:
        Set the rate of speed change during acceleration for a motor channel. This command is
        identical to the MACC configuration command but is provided so that it can be changed
        rapidly during motor operation. Acceleration value is in 0.1 * RPM per second. When using
        controllers fitted with encoder, the speed and acceleration value are actual RPMs. Brushless
        motor controllers use the hall sensor for measuring actual speed and acceleration will
        also be in actual RPM/s. When using the controller without speed sensor, the acceleration
        value is relative to the Max RPM configuration parameter, which itself is a user-provided
        number for the speed normally expected at full power. Assuming that the Max RPM parameter
        is set to 1000, and acceleration value of 10000 means that the motor will go from
        0 to full speed in exactly 1 second, regardless of the actual motor speed. In Closed Loop
        Torque mode acceleration value is in 0.1 * miliAmps per second. This command is not
        applicable if either of the acceleration (MAC) or deceleration (MDEC) configuration value is
        set to 0.

        From "Roboteq Controllers User Manual v2.0.pdf" page 181:
        Set the rate of speed change during decceleration for a motor channel. This command is
        identical to the MDEC configuration command but is provided so that it can be changed
        rapidly during motor operation. Decceleration value is in 0.1 * RPM per second. When
        using controllers fitted with encoder, the speed and decceleration value are actual RPMs.
        Brushless motor controllers use the hall sensor for measuring actual speed and decceleration
        will also be in actual RPM/s. When using the controller without speed sensor,
        the decceleration value is relative to the Max RPM configuration parameter, which itself
        is a user-provided number for the speed normally expected at full power. Assuming that
        the Max RPM parameter is set to 1000, and decceleration value of 10000 means that
        the motor will go from full speed to 0 in exactly 1 second, regardless of the actual motor
        speed. In Closed Loop Torque mode deceleration value is in 0.1 * miliAmps per second.
        This command is not applicable if either of the acceleration (MAC) or deceleration (MDEC)
        configuration value is set to 0.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                Acceleration_Input = self.LimitNumber_IntOutputOnly(self.Acceleration_Target_Min_UserSet, self.Acceleration_Target_Max_UserSet, Acceleration_Input)

                StringToTx = "!AC 1 " + str(Acceleration_Input) + "\r" #Acceleration, "Roboteq Controllers User Manual v2.0.pdf" page 175

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)
                    time.sleep(self.TimeToSleepBetweenConfigurationCommands)

                StringToTx = "!DC 1 " + str(Acceleration_Input) + "\r" #Decelleration, "Roboteq Controllers User Manual v2.0.pdf" page 181

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("Acceleration_Input, exceptions: %s" % exceptions)

        else:
            print("Acceleration_Input: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ResetController(self, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 262:
        '''

        if self.SerialConnectedFlag == 1:
            try:

                StringToTx = "%RESET 321654987" + "\r"


                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                print("@@@@@ ResetController event fired! @@@@@")

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetSerialCommandEcho, exceptions: %s" % exceptions)

        else:
            print("SetSerialCommandEcho: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StopInAllModes(self, SkipQueueAndSendImmediately = 0):

        '''
        "Roboteq Controllers User Manual v2.0.pdf" page 187.
        '''

        if self.SerialConnectedFlag == 1:
            try:

                StringToTx = "!MS 1" + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                print("StopInAllModes event fired!")

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("StopInAllModes, exceptions: %s" % exceptions)

        else:
            print("StopInAllModes: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetEmergencyStopState(self, EmergencyStopState_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 184 and 187:
        '''

        if self.SerialConnectedFlag == 1:
            try:

                EmergencyStopState_Input = int(EmergencyStopState_Input)

                if EmergencyStopState_Input not in [0, 1]:
                    print("SetSerialCommandEcho: Error, EmergencyStopState must be 0 or 1.")
                    return 0

                if EmergencyStopState_Input == 1:
                    StringToTx = "!EX" + "\r"
                else:
                    StringToTx = "!MG" + "\r"

                if SkipQueueAndSendImmediately == 0:
                    self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                else:
                    self.SendSerialStrToTx(StringToTx)

                #self.EmergencyStopState = EmergencyStopState_Input

                print("@@@@@ SetEmergencyStopState event fired! @@@@@")

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetSerialCommandEcho, exceptions: %s" % exceptions)

        else:
            print("SetSerialCommandEcho: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetControlMode(self, ControlMode_IntegerValueOrEnglishString_Input, SkipQueueAndSendImmediately = 0):

        '''
        From "Roboteq Controllers User Manual v2.0.pdf" page 314:
        HexCode: 27
        Description:
        This parameter lets you select the operating mode for that channel. See manual for description
        of each mode.
        Syntax Serial: ^MMOD cc nn
        ~MMOD [cc]
        Syntax Scripting: setconfig(_MMOD, cc, nn)
        Number of Arguments: 2
        Argument 1: Channel
        Min: 1 Max: Total Number of Motors
        Argument 2: Mode
        Type: Unsigned 8-bit
        Min: 0 Max: 6
        Default: 0 = Open loop
        Where:
        cc = Motor channel
        nn =
        0: Open-loop
        1: Closed-loop speed
        2: Closed-loop position relative
        3: Closed-loop count position
        4: Closed-loop position tracking
        5: Closed-loop torque
        6: Closed-loop speed position
        Example:
        ^MMOD 2 : Select Closed loop position relative
        '''

        ##########################################################################################################
        if isinstance(ControlMode_IntegerValueOrEnglishString_Input, int) == 1 or isinstance(ControlMode_IntegerValueOrEnglishString_Input, float) == 1:
            ControlMode_IntegerValueOrEnglishString_Input = int(ControlMode_IntegerValueOrEnglishString_Input)

            if ControlMode_IntegerValueOrEnglishString_Input not in self.ControlMode_AcceptableValues_DictWithIntegersAsKeys:
                print("SetControlMode, error: input must be an integer within [0, 6] or a string in " + str(self.ControlMode_AcceptableValues_ListOfEnglishStrings))
                return 0
            else:
                ControlMode_IntegerValue_temp = ControlMode_IntegerValueOrEnglishString_Input
                ControlMode_EnglishString_temp = self.ControlMode_AcceptableValues_DictWithIntegersAsKeys[ControlMode_IntegerValue_temp]

        ##########################################################################################################

        ##########################################################################################################
        elif isinstance(ControlMode_IntegerValueOrEnglishString_Input, str) == 1:
            ControlMode_IntegerValueOrEnglishString_Input = str(ControlMode_IntegerValueOrEnglishString_Input)

            if ControlMode_IntegerValueOrEnglishString_Input not in self.ControlMode_AcceptableValues_DictWithEnglishStringsAsKeys:
                print("SetControlMode, error: input must be an integer within [0, 6] or a string in " + str(self.ControlMode_AcceptableValues_ListOfEnglishStrings))
                return 0
            else:
                ControlMode_EnglishString_temp = ControlMode_IntegerValueOrEnglishString_Input
                ControlMode_IntegerValue_temp =self.ControlMode_AcceptableValues_DictWithEnglishStringsAsKeys[ControlMode_EnglishString_temp]

        ##########################################################################################################
        else:
            print("SetControlMode, error: input must be an integer within [0, 6] or a string in " + str(self.ControlMode_AcceptableValues_ListOfEnglishStrings))
            return 0
        ##########################################################################################################

        ##########################################################################################################
        if self.SerialConnectedFlag == 1:
            try:

                #print("SetControlMode: setting ControlMode to " + ControlMode_EnglishString_temp)

                StringToTx = "^MMOD " + str(ControlMode_IntegerValue_temp) + "\r" #Do NOT includr the " 1" cc first argument (ambiguous in user manual, works without)..
                print("SetControlMode, StringToTx:" + StringToTx)

                for Counter in range(0, 10):
                    if SkipQueueAndSendImmediately == 0:
                        self.DedicatedTxThread_TxMessageToSend_Queue.put(StringToTx)
                    else:
                        self.SendSerialStrToTx(StringToTx)
                        time.sleep(self.TimeToSleepBetweenConfigurationCommands)

                self.ControlMode_IntegerValue = ControlMode_IntegerValue_temp
                self.ControlMode_EnlishString = ControlMode_EnglishString_temp

                print("SetControlMode event fired for self.ControlMode_EnlishString = " + self.ControlMode_EnlishString)

                return 1

            except:
                exceptions = sys.exc_info()[0]
                print("SetControlMode, exceptions: %s" % exceptions)

        else:
            print("SetControlMode: Error, SerialConnectedFlag = 0, cannot issue command.")
            return 0
        ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetCurrentPositionAsHomeOnDevice(self):

        self.HomeOrBrushlessCounterOnDevice_ToBeSet = 0
        self.HomeOrBrushlessCounterOnDevice_NeedsToBeChangedFlag = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetCurrentPositionAsHomeSoftwareOffsetOnly(self):

        self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_NeedsToBeChangedFlag = 1

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SendCommandToMotor_ExternalClassFunction(self, CommandValue, CommandTypeString, IgnoreNewDataIfQueueIsFullFlag = 1):

        try:
            if CommandTypeString not in self.ControlMode_AcceptableValues_ListOfEnglishStrings:
                print("SendCommandToMotor_ExternalClassFunction, ERROR: CommandTypeString of " + str(CommandTypeString) + " is invalid.")

            '''
            CommandToSendDict = dict([(CommandTypeString, CommandValue)])

            if self.SendCommandToMotor_Queue.qsize() < self.SendCommandToMotor_Queue_MaxSize:
                self.SendCommandToMotor_Queue.put(CommandToSendDict)

                self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 1

            else:
                if IgnoreNewDataIfQueueIsFullFlag != 1:
                    dummy = self.SendCommandToMotor_Queue.get()  # makes room for one more message
                    self.SendCommandToMotor_Queue.put(CommandToSendDict)  # backfills that message with new data

                    self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 1
            '''

            self.Motor_Target_ToBeSet = CommandValue
            self.Motor_Target_NeedsToBeChangedFlag = 1
            self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 1

        except:
            exceptions = sys.exc_info()[0]
            print("SendCommandToMotor_ExternalClassFunction: Exceptions: %s" % exceptions)
            traceback.print_exc()

    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    def DedicatedTxThread(self):

        self.MyPrint_WithoutLogFile("Started DedicatedTxThread for RoboteqBLDCcontroller_ReubenPython2and3Class object.")
        self.DedicatedTxThread_StillRunningFlag = 1

        self.StartingTime_CalculatedFromDedicatedTxThread = self.getPreciseSecondsTimeStampString()
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        while self.EXIT_PROGRAM_FLAG == 0:

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            self.CurrentTime_CalculatedFromDedicatedTxThread = self.getPreciseSecondsTimeStampString() - self.StartingTime_CalculatedFromDedicatedTxThread
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

            ########################################################################################################## These should be outside of the queue and heartbeat
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.EnabledState_NeedsToBeChangedFlag == 1:
                self.EmergencyStopState_ToBeSet = int(not self.EnabledState_ToBeSet) #WHY DOES THE EnabledState_NeedsToBeChangedFlag fire EmergencyStop?
                self.EmergencyStopState_NeedsToBeChangedFlag = 1
                self.EnabledState_NeedsToBeChangedFlag = 0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.EmergencyStopState_NeedsToBeChangedFlag == 1:
                self.SetEmergencyStopState(self.EmergencyStopState_ToBeSet)
                self.EmergencyStopState_NeedsToBeChangedFlag = 0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.StopInAllModes_NeedsToBeChangedFlag == 1:
                self.StopInAllModes()
                self.StopInAllModes_NeedsToBeChangedFlag = 0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.HomeOrBrushlessCounterOnDevice_NeedsToBeChangedFlag == 1:
                self.SetHomeOrBrushlessCounterOnDevice(self.HomeOrBrushlessCounterOnDevice_ToBeSet)
                self.HomeOrBrushlessCounterOnDevice_NeedsToBeChangedFlag = 0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.PID_Kp != self.PID_Kp_last:
                #self.SetPID_Kp(self.PID_Kp)

                #I DON'T UNDERSTAND WHEN I WOULD WANT TO ISSE SetPID_Kp_TorqueModeFOC VS SetPID_Kp
                #'''
                if self.ControlMode_EnlishString != "ClosedLoopTorque":
                    self.SetPID_Kp(self.PID_Kp)
                else:
                    self.SetPID_Kp_TorqueModeFOC(self.PID_Kp, FluxGain1trqGain2_Flag=2) #TORQUE GAIN
                #'''

                self.PID_Kp_last = self.PID_Kp
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.PID_Ki != self.PID_Ki_last:
                #self.SetPID_Ki(self.PID_Ki)

                #'''
                if self.ControlMode_EnlishString != "ClosedLoopTorque":
                    self.SetPID_Ki(self.PID_Ki)
                else:
                    self.SetPID_Ki_TorqueModeFOC(self.PID_Ki, FluxGain1trqGain2_Flag=2) #TORQUE GAIN
                #'''

                self.PID_Ki_last = self.PID_Ki
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.PID_Kd != self.PID_Kd_last:
                #self.SetPID_Kd(self.PID_Kd)

                #'''
                if self.ControlMode_EnlishString != "ClosedLoopTorque":
                    self.SetPID_Kd(self.PID_Kd)
                #'''

                self.PID_Kd_last = self.PID_Kd
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.PID_IntegratorCap1to100percent != self.PID_IntegratorCap1to100percent_last:
                #self.SetPID_IntegratorCap1to100percent(self.PID_IntegratorCap1to100percent)

                #'''
                if self.ControlMode_EnlishString != "ClosedLoopTorque":
                    self.SetPID_IntegratorCap1to100percent(self.PID_IntegratorCap1to100percent)
                #'''

                self.PID_IntegratorCap1to100percent_last = self.PID_IntegratorCap1to100percent
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.ToggleMinMax_EventNeedsToBeFiredFlag == 1:

                ##########################################################################################################
                if self.ToggleMinMax_StateToBeSet == 0:
                    self.ToggleMinMax_StateToBeSet = 1
                else:
                    self.ToggleMinMax_StateToBeSet = 0
                ##########################################################################################################

                ##########################################################################################################
                if self.ControlMode_EnlishString in ["OpenLoop"]:
                    MinToSet = self.OpenLoopPower_Target_Min_UserSet
                    MaxToSet = self.OpenLoopPower_Target_Max_UserSet

                elif self.ControlMode_EnlishString in ["ClosedLoopPositionRelative", "ClosedLoopCountPosition", "ClosedLoopPositionTracking"]:
                    MinToSet = self.Position_Target_Min_UserSet
                    MaxToSet = self.Position_Target_Max_UserSet

                elif self.ControlMode_EnlishString in ["ClosedLoopSpeed", "ClosedLoopSpeedPosition"]:
                    MinToSet = self.Speed_Target_Min_UserSet
                    MaxToSet = self.Speed_Target_Max_UserSet

                elif self.ControlMode_EnlishString in ["ClosedLoopTorque"]:
                    MinToSet = self.Torque_Amps_Min_UserSet
                    MaxToSet = self.Torque_Amps_Max_UserSet

                else:
                   MinToSet = 0.0
                   MaxToSet = 0.0

                ##########################################################################################################

                ##########################################################################################################
                if self.ToggleMinMax_StateToBeSet == 0:
                    self.Motor_Target_ToBeSet = MinToSet
                else:
                    self.Motor_Target_ToBeSet = MaxToSet
                ##########################################################################################################

                ##########################################################################################################
                self.Motor_Target_NeedsToBeChangedFlag = 1
                self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 1

                self.ToggleMinMax_EventNeedsToBeFiredFlag = 0
                ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            if self.Motor_Target_NeedsToBeChangedFlag == 1:

                if self.ControlMode_EnlishString in ["OpenLoop"]:
                    self.GoToSpeedOrRelativePositionGeneric(self.Motor_Target_ToBeSet)

                elif self.ControlMode_EnlishString in ["ClosedLoopPositionRelative", "ClosedLoopCountPosition", "ClosedLoopPositionTracking"]:
                    self.GoToSpeedOrRelativePositionGeneric(self.Motor_Target_ToBeSet) #DON'T USE self.GoToRelativePosition(self.Motor_Target_ToBeSet)

                elif self.ControlMode_EnlishString in ["ClosedLoopTorque"]:
                    self.GoToTorqueNM_TC(self.Motor_Target_ToBeSet) #DON'T USE self.GoToTorqueAmps_SinusoidalModeOnly(self.Motor_Target_ToBeSet)

                elif self.ControlMode_EnlishString in ["ClosedLoopSpeed", "ClosedLoopSpeedPosition"]:
                    self.SetSpeed(self.Motor_Target_ToBeSet) #USE FOR SPEED MODES

                self.Motor_Target_NeedsToBeChangedFlag = 0
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            if self.DedicatedTxThread_TxMessageToSend_Queue.qsize() > 0:
                try:

                    ##########################################################################################################
                    ##########################################################################################################
                    TxDataToWrite = self.DedicatedTxThread_TxMessageToSend_Queue.get()

                    if TxDataToWrite[-1] != "\r":
                        TxDataToWrite = TxDataToWrite + "\r"

                    self.SendSerialStrToTx(TxDataToWrite)
                    if self.PrintAllSentSerialMessageForDebuggingFlag == 1:
                        print("ByteLen = " + str(len(TxDataToWrite)) + ", TxDataToWrite = " + TxDataToWrite)
                    ##########################################################################################################
                    ##########################################################################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("RoboteqBLDCcontroller_ReubenPython2and3Class, DedicatedTxThread, Inner Exceptions: %s" % exceptions)
                    traceback.print_exc()

            else:

                if self.HeartbeatTimeIntervalMilliseconds > 0.0:
                    if self.CurrentTime_CalculatedFromDedicatedTxThread - self.LastTimeHeartbeatWasSent_CalculatedFromDedicatedTxThread >= self.HeartbeatTimeIntervalMilliseconds/1000.0:
                        if self.SerialStrToTx_LAST_SENT != "":# and self.SerialStrToTx_LAST_SENT.find("!") == -1: #There aren't any "!" commands
                            self.SendSerialStrToTx(self.SerialStrToTx_LAST_SENT)
                            #print("Heartbeat at time = " + str(self.CurrentTime_CalculatedFromDedicatedTxThread))
                            self.LastTimeHeartbeatWasSent_CalculatedFromDedicatedTxThread = self.CurrentTime_CalculatedFromDedicatedTxThread

            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            
            ########################################################################################################## USE THE TIME.SLEEP() TO SET THE LOOP FREQUENCY
            ##########################################################################################################
            ##########################################################################################################
            self.UpdateFrequencyCalculation_DedicatedTxThread_Filtered()

            if self.DedicatedTxThread_TimeToSleepEachLoop > 0.0:
                if self.DedicatedTxThread_TimeToSleepEachLoop > 0.001:
                    time.sleep(self.DedicatedTxThread_TimeToSleepEachLoop - 0.001) #The "- 0.001" corrects for slight deviation from intended frequency due to other functions being called.
                else:
                    time.sleep(self.DedicatedTxThread_TimeToSleepEachLoop)
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################

        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        ##########################################################################################################
        if self.ControlMode_EnlishString == "ClosedLoopTorque":
            Motor_Target_ToBeSet_AtStartOfWindDown  = self.Motor_Target_ToBeSet
            print("Motor_Target_ToBeSet_AtStartOfWindDown: " + str(Motor_Target_ToBeSet_AtStartOfWindDown))

            Counter = 0
            CounterLimit = 50
            for Counter in range(1, CounterLimit):

                ##########################################################################################################
                ##########################################################################################################
                ##########################################################################################################
                if Counter <= round(0.5*CounterLimit):
                    if Motor_Target_ToBeSet_AtStartOfWindDown >= 0:
                        self.Motor_Target_ToBeSet = -1.0*self.Torque_Amps_Max_UserSet
                    else:
                        self.Motor_Target_ToBeSet = 1.0*self.Torque_Amps_Max_UserSet
                else:
                    self.Motor_Target_ToBeSet = 0.0

                #print("WIND-DOWN: Motor_Target_ToBeSet = " + str(self.Motor_Target_ToBeSet))
                self.GoToTorqueNM_TC(self.Motor_Target_ToBeSet, SkipQueueAndSendImmediately=1)

                time.sleep(0.050)
                ##########################################################################################################
                ##########################################################################################################
                ##########################################################################################################


            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################
            ##########################################################################################################

        else:
            # self.SetEmergencyStopState(0, SkipQueueAndSendImmediately = 1)
            self.StopInAllModes(SkipQueueAndSendImmediately=1)

        self.MyPrint_WithoutLogFile("Finished DedicatedTxThread for RoboteqBLDCcontroller_ReubenPython2and3Class object.")
        self.DedicatedTxThread_StillRunningFlag = 0
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ########################################################################################################## unicorn
    ##########################################################################################################
    ##########################################################################################################
    def DedicatedRxThread(self):

        self.MyPrint_WithoutLogFile("Started DedicatedRxThread for RoboteqBLDCcontroller_ReubenPython2and3Class object.")
        self.DedicatedRxThread_StillRunningFlag = 1

        self.StartingTime_CalculatedFromDedicatedRxThread = self.getPreciseSecondsTimeStampString()
        ##########################################################################################################
        ##########################################################################################################
        while self.EXIT_PROGRAM_FLAG == 0:

            try:

                ##########################################################################################################
                RxMessage = self.SerialObject.read_until(b'\r')
                ##########################################################################################################

                ##########################################################################################################
                if len(RxMessage) > 0:

                    try:
                        '''
                        "Roboteq Controllers User Manual v2.0.pdf" page 172
                        Command Acknowledgment
                        The controller will acknowledge commands in one of the two ways:
                        For commands that cause a reply, such as a configuration read or a speed or amps queries,
                        the reply to the query must be considered as the command acknowledgment.
                        For commands where no reply is expected, such as speed setting, the controller will issue
                        a “plus” character (+) followed by a Carriage Return after every command as an acknowledgment.
                        '''

                        #print("RxMessage (original): " + str(RxMessage))

                        if chr(RxMessage[0]) != '+':

                            ##########################################################################################################
                            self.CurrentTime_CalculatedFromDedicatedRxThread = self.getPreciseSecondsTimeStampString() - self.StartingTime_CalculatedFromDedicatedRxThread
                            ##########################################################################################################

                            ##########################################
                            RxMessageString = self.ConvertBytesObjectToString(RxMessage)
                            RxMessageString = RxMessageString.replace("\r", "")
                            #print("RxMessageString: " + str(RxMessageString))
                            RxMessageStringList = RxMessageString.split(self.DelimiterOfReturnedMessages)
                            ##########################################

                            ##########################################
                            for Index, VarNameEnglish in enumerate(self.VariableNamesEnglishList):

                                if VarNameEnglish == "MotorCurrentRMSamps" or VarNameEnglish == "MotorCurrentPeakAmps":
                                    self.MostRecentDataDict[VarNameEnglish] = float(RxMessageStringList[Index])/10.0
                                elif VarNameEnglish == "TorqueTarget":
                                    self.MostRecentDataDict[VarNameEnglish] = float(RxMessageStringList[Index])/100.0
                                elif VarNameEnglish == "ActualOperationMode":
                                    #self.MostRecentDataDict[VarNameEnglish] = int(RxMessageStringList[Index]) #THIS HAS TO BE CORRECT

                                    ActualOperationMode_Int_TEMP_UNCORRECTED = int(RxMessageStringList[Index])

                                    self.MostRecentDataDict["ActualOperationMode_CorrectInt"] = self.ActualOperationModeReceived_ConvertReceivedIntToRealInt_EMPIRICALLY_DETERMINTED_DictWithIntegersAsKeys[ActualOperationMode_Int_TEMP_UNCORRECTED]
                                    self.MostRecentDataDict["ActualOperationMode_EnglishString"] = self.ActualOperationModeReceived_ConvertIntToEnglishName_EMPIRICALLY_DETERMINTED_DictWithIntegersAsKeys[ActualOperationMode_Int_TEMP_UNCORRECTED]

                                else:
                                    self.MostRecentDataDict[VarNameEnglish] = float(RxMessageStringList[Index])
                            ##########################################

                            ##########################################
                            if self.PrintAllReceivedSerialMessageForDebuggingFlag == 1:
                                print("ByteLen = " + str(len(RxMessageString)) + ", RxMessageString = " + RxMessageString + ", RxMessageStringList = " + str(RxMessageStringList))
                            ##########################################

                            ##########################################
                            #print("RxMessage: " + str(RxMessage) + ", self.CurrentTime_CalculatedFromDedicatedRxThread: " + str(self.CurrentTime_CalculatedFromDedicatedRxThread))
                            self.UpdateFrequencyCalculation_DedicatedRxThread_Filtered()
                            ##########################################

                            ##########################################################################################################
                            if self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_NeedsToBeChangedFlag == 1:
                                if "AbsoluteBrushlessCounter" in self.MostRecentDataDict:
                                    self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_ToBeSet = self.MostRecentDataDict["AbsoluteBrushlessCounter"]
                                    print("self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_ToBeSet: " + str(self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_ToBeSet))
                                    self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_NeedsToBeChangedFlag = 0
                            ##########################################################################################################

                            ##########################################
                            self.MostRecentDataDict["Time"] = self.CurrentTime_CalculatedFromDedicatedRxThread
                            self.MostRecentDataDict["DataStreamingFrequency_CalculatedFromDedicatedRxThread"] = self.DataStreamingFrequency_CalculatedFromDedicatedRxThread
                            self.MostRecentDataDict["DataStreamingFrequency_CalculatedFromDedicatedTxThread"] = self.DataStreamingFrequency_CalculatedFromDedicatedTxThread
                            self.MostRecentDataDict["PID_Kp"] = self.PID_Kp
                            self.MostRecentDataDict["PID_Ki"] = self.PID_Ki
                            self.MostRecentDataDict["PID_Kd"] = self.PID_Kd
                            self.MostRecentDataDict["PID_IntegratorCap1to100percent"] = self.PID_IntegratorCap1to100percent
                            self.MostRecentDataDict["ControlMode_IntegerValue"] = self.ControlMode_IntegerValue
                            self.MostRecentDataDict["ControlMode_EnglishString"] = self.ControlMode_EnlishString

                            #print("self.MostRecentDataDict: " + str(self.MostRecentDataDict))

                            if "AbsoluteBrushlessCounter" in self.MostRecentDataDict:
                                self.MostRecentDataDict["Position_Rev"] = (self.MostRecentDataDict["AbsoluteBrushlessCounter"] - self.HomeOrBrushlessCounterSoftwareOffsetOnly_AbsoluteBrushlessCounter_ToBeSet)/(self.NumberOfMagnetsInMotor*3.0)
                                self.MostRecentDataDict["Position_Radians"] = self.MostRecentDataDict["Position_Rev"]*2.0*math.pi
                                self.MostRecentDataDict["Position_Degrees"] = self.MostRecentDataDict["Position_Rev"]*360.0

                            if "SpeedRPM" in self.MostRecentDataDict:
                                self.MostRecentDataDict["Speed_RPM"] = self.MostRecentDataDict["SpeedRPM"]
                                self.MostRecentDataDict["Speed_RPS"] = self.MostRecentDataDict["Speed_RPM"]/60.0
                                self.MostRecentDataDict["Speed_RadiansPerSec"] = self.MostRecentDataDict["Speed_RPS"]/(self.NumberOfMagnetsInMotor*3.0)
                                self.MostRecentDataDict["Speed_DegreesPerSec"] = self.MostRecentDataDict["Speed_RadiansPerSec"]*360.0

                            self.MostRecentDataDict["RxMessage"]  = RxMessage
                            self.MostRecentDataDict["RxMessage_length"] = len(RxMessage)

                            self.MostRecentDataDict["Motor_Target_ToBeSet"] = self.Motor_Target_ToBeSet

                            if self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread > 0.0:
                                if "Position_Rev" in self.MostRecentDataDict:
                                    Speed_RPM_Calculated_Raw = (self.MostRecentDataDict["Position_Rev"] - self.Position_Rev_Last)/self.DataStreamingDeltaT_CalculatedFromDedicatedRxThread
                                    Speed_RPM_Calculated_Raw = 0.5*Speed_RPM_Calculated_Raw #WHY DO WE HAVE TO DIVIDE BY 2 HERE????
                                    self.MostRecentDataDict["Speed_RPS_Calculated"] = self.Speed_RPS_Calculated_LowPassFilter_ReubenPython2and3ClassObject.AddDataPointFromExternalProgram(Speed_RPM_Calculated_Raw)["SignalOutSmoothed"]

                                    self.MostRecentDataDict["Speed_RPM_Calculated"] = self.MostRecentDataDict["Speed_RPS_Calculated"]*60.0
                                    self.MostRecentDataDict["Speed_RadiansPerSec_Calculated"] = self.MostRecentDataDict["Speed_RPS_Calculated"]/(self.NumberOfMagnetsInMotor*3.0)
                                    self.MostRecentDataDict["Speed_DegreesPerSec_Calculated"] = self.MostRecentDataDict["Speed_RadiansPerSec_Calculated"]*360.0

                            '''
                            #IMPLMENT THIS CONVERSION OF THE RECEIVED FAULT FLAG
                            Reply:
                            FS = f1 + f2*2 + f3*4 + ... + fn*2^n-1 Type: Unsigned 16-bit Min: 0 Max: 65535
                            Where:
                            f1 = Overheat
                            f2 = Overvoltage
                            f3 = Undervoltage
                            f4 = Short circuit
                            f5 = Emergency stop
                            f6 = Motor/Sensor Setup fault
                            f7 = MOSFET failure
                            f8 = Default configuration loaded at startup
                            Example:
                            Q: ?FF
                            R: FF=2 : Overvoltage fault
                            '''
                            ##########################################

                            ##########################################
                            if "Position_Rev" in self.MostRecentDataDict:
                                self.Position_Rev_Last = self.MostRecentDataDict["Position_Rev"]
                            ##########################################

                            ##########################################
                            if self.DedicatedRxThread_TimeToSleepEachLoop > 0.0:
                                if self.DedicatedRxThread_TimeToSleepEachLoop > 0.001:
                                    time.sleep(self.DedicatedRxThread_TimeToSleepEachLoop - 0.001) #The "- 0.001" corrects for slight deviation from intended frequency due to other functions being called.
                                else:
                                    time.sleep(self.DedicatedRxThread_TimeToSleepEachLoop)
                            ##########################################

                            ##########################################

                    except:
                        exceptions = sys.exc_info()[0]
                        print("SerialRxThread ERROR: Original RxMessage: " + str(RxMessage) + ", RxMessageString: " + str(RxMessageString) + "LengthInBytes = " + str(len(RxMessage)) + ", Exceptions: %s" % exceptions)
                        #traceback.print_exc()
                ##########################################################################################################

            except:
                exceptions = sys.exc_info()[0]
                print("SerialRxThread ERROR: Exceptions: %s" % exceptions)
                #traceback.print_exc()
            ##########################################################################################################
            ##########################################################################################################

        self.MyPrint_WithoutLogFile("Finished DedicatedRxThread for RoboteqBLDCcontroller_ReubenPython2and3Class object.")
        self.DedicatedRxThread_StillRunningFlag = 0
    ##########################################################################################################
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ExitProgram_Callback(self):

        print("Exiting all threads for RoboteqBLDCcontroller_ReubenPython2and3Class object")

        self.EXIT_PROGRAM_FLAG = 1
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StartGUI(self, GuiParent):

        self.GUI_Thread(GuiParent)
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def GUI_Thread(self, parent):

        print("Starting the GUI_Thread for RoboteqBLDCcontroller_ReubenPython2and3Class object.")

        #################################################
        #################################################
        self.root = parent
        self.parent = parent
        #################################################
        #################################################

        #################################################
        #################################################
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
        #################################################
        #################################################

        #################################################
        #################################################
        self.TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
        self.TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
        self.TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
        self.TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
        self.TkinterScaleLabelWidth = 30
        self.TkinterScaleWidth = 10
        self.TkinterScaleLength = 250
        #################################################
        #################################################
        #################################################

        #################################################
        #################################################
        self.DeviceInfo_Label = Label(self.myFrame, text="Device Info", width=50)

        self.DeviceInfo_Label["text"] = self.NameToDisplay_UserSet + \
                                        "\nUSBtoSerialConverter Serial Number: " + str(self.DesiredSerialNumber_USBtoSerialConverter)

        self.DeviceInfo_Label.grid(row=0, column=0, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.Motor_Label = Label(self.myFrame, text="Motor_Label", width=120)
        self.Motor_Label.grid(row=1, column=0, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.ButtonsFrame = Frame(self.myFrame)
        self.ButtonsFrame.grid(row = 2, column = 0, padx = 10, pady = 10, rowspan = 1, columnspan = 2)
        self.ButtonWidth = 16
        #################################################
        #################################################

        #################################################
        #################################################
        self.SetCurrentPositionAsHomeOnDevice_Button = Button(self.ButtonsFrame, text="OnDevice Home", state="normal", width=self.ButtonWidth, command=lambda: self.SetCurrentPositionAsHomeOnDevice_Button_Response())
        self.SetCurrentPositionAsHomeOnDevice_Button.grid(row=0, column=0, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.SetCurrentPositionAsHomeSoftwareOffsetOnly_Button = Button(self.ButtonsFrame, text="Soft Home", state="normal", width=self.ButtonWidth, command=lambda: self.SetCurrentPositionAsHomeSoftwareOffsetOnly_Button_Response())
        self.SetCurrentPositionAsHomeSoftwareOffsetOnly_Button.grid(row=0, column=1, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.EnabledState_Button = Button(self.ButtonsFrame, text="Enabled", state="normal", width=self.ButtonWidth, command=lambda: self.EnabledState_Button_Response())
        self.EnabledState_Button.grid(row=0, column=2, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.StopInAllModes_Button = Button(self.ButtonsFrame, text="Stop", state="normal", width=self.ButtonWidth, command=lambda: self.StopInAllModes_Button_Response())
        self.StopInAllModes_Button.grid(row=0, column=3, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.EmergencyStopState_Button = Button(self.ButtonsFrame, text="EmergencyStop", state="normal", width=self.ButtonWidth, command=lambda: self.EmergencyStopState_Button_Response())
        self.EmergencyStopState_Button.grid(row=0, column=4, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################
        
        #################################################
        #################################################
        self.ToggleMinMax_Button = Button(self.ButtonsFrame, text="ToggleMinMax", state="normal", width=self.ButtonWidth, command=lambda: self.ToggleMinMax_Button_Response())
        self.ToggleMinMax_Button.grid(row=0, column=5, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=1, rowspan=1)
        #################################################
        #################################################

        #################################################
        #################################################
        self.GUIscaleFrame = Frame(self.myFrame)
        self.GUIscaleFrame.grid(row = 3, column = 0, padx = 10, pady = 10, rowspan = 1, columnspan = 2)
        #################################################
        #################################################

        ###################################################
        ###################################################
        self.Motor_Target_GUIscale_LabelObject = Label(self.GUIscaleFrame, text="ControlMode: " + self.ControlMode_EnlishString, width=self.TkinterScaleLabelWidth)
        self.Motor_Target_GUIscale_LabelObject.grid(row=0, column=0, padx=1, pady=1, columnspan=1, rowspan=1)

        self.Motor_Target_GUIscale_Value = DoubleVar()
        self.Motor_Target_GUIscale_ScaleObject = Scale(self.GUIscaleFrame,
                                        from_=self.Motor_Target_Min_UserSet,
                                        to=self.Motor_Target_Max_UserSet,
                                        #tickinterval=
                                        orient=HORIZONTAL,
                                        borderwidth=2,
                                        showvalue=True,
                                        width=self.TkinterScaleWidth,
                                        length=self.TkinterScaleLength,
                                        resolution=1,
                                        variable=self.Motor_Target_GUIscale_Value)

        self.Motor_Target_GUIscale_ScaleObject.bind('<Button-1>', lambda event: self.Motor_Target_GUIscale_EventResponse(event))
        self.Motor_Target_GUIscale_ScaleObject.bind('<B1-Motion>', lambda event: self.Motor_Target_GUIscale_EventResponse(event))
        self.Motor_Target_GUIscale_ScaleObject.bind('<ButtonRelease-1>', lambda event: self.Motor_Target_GUIscale_EventResponse(event))
        self.Motor_Target_GUIscale_ScaleObject.set(self.Motor_Target_ToBeSet)
        self.Motor_Target_GUIscale_ScaleObject.grid(row=0, column=1, padx=1, pady=1, columnspan=1, rowspan=1)
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        self.PIDgains_EntryWidth = 10
        self.PIDgains_LabelWidth = 35
        self.PIDgains_FontSize = 12
        
        self.EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", self.myFrame),("UseBorderAroundThisGuiObjectFlag", 0),("GUI_ROW", 4),("GUI_COLUMN", 0)])

        #Roboteq Controllers User Manual v2.0, "Roboteq Controllers User Manual v2.0.pdf" page 310 for values.
        #nn = Integral Gain *1,000,000, Example: ^KI 1 1500000: Set motor channel 1 Integral Gain to 1.5.
        self.EntryListWithBlinking_Variables_ListOfDicts = [dict([("Name", "Kp"),("Type", "float"), ("StartingVal", self.PID_Kp), ("MinVal", self.PID_Kp_Min), ("MaxVal", self.PID_Kp_Max), ("EntryWidth", self.PIDgains_EntryWidth),("LabelWidth", self.PIDgains_LabelWidth),("FontSize", self.PIDgains_FontSize)]),
                                                       dict([("Name", "Ki"),("Type", "float"), ("StartingVal", self.PID_Ki), ("MinVal", self.PID_Ki_Min), ("MaxVal", self.PID_Ki_Max),("EntryWidth", self.PIDgains_EntryWidth),("LabelWidth", self.PIDgains_LabelWidth),("FontSize", self.PIDgains_FontSize)]),
                                                       dict([("Name", "Kd"),("Type", "float"), ("StartingVal", self.PID_Kd), ("MinVal", self.PID_Kd_Min), ("MaxVal", self.PID_Kd_Max),("EntryWidth", self.PIDgains_EntryWidth),("LabelWidth", self.PIDgains_LabelWidth),("FontSize", self.PIDgains_FontSize)]),
                                                       dict([("Name", "IntegratorCap1to100percent"),("Type", "float"), ("StartingVal", self.PID_IntegratorCap1to100percent), ("MinVal", self.PID_IntegratorCap1to100percent_Min), ("MaxVal", self.PID_IntegratorCap1to100percent_Max),("EntryWidth", self.PIDgains_EntryWidth),("LabelWidth", self.PIDgains_LabelWidth),("FontSize", self.PIDgains_FontSize)])]

        self.EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", self.EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                              ("EntryListWithBlinking_Variables_ListOfDicts", self.EntryListWithBlinking_Variables_ListOfDicts),
                                                                              ("DebugByPrintingVariablesFlag", 0)])

        try:
            self.EntryListWithBlinking_ReubenPython2and3ClassObject = EntryListWithBlinking_ReubenPython2and3Class(self.EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.010)
            self.EntryListWithBlinking_OPEN_FLAG = self.EntryListWithBlinking_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("EntryListWithBlinking_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
        ###################################################
        ###################################################

        #################################################
        #################################################
        self.PrintToGui_Label = Label(self.myFrame, text="PrintToGui_Label", width=75)
        if self.EnableInternal_MyPrint_Flag == 1:
            self.PrintToGui_Label.grid(row=5, column=0, padx=self.GUI_PADX, pady=self.GUI_PADY, columnspan=10, rowspan=10)
        #################################################
        #################################################

        #################################################
        #################################################
        self.GUI_ready_to_be_updated_flag = 1
        #################################################
        #################################################

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def EnabledState_Button_Response(self):

        if self.EnabledState_ToBeSet == 1:
            self.EnableMotorsFromExternalProgram(0)
        else:
            self.EnableMotorsFromExternalProgram(1)

        #self.MyPrint_WithoutLogFile("EnabledState_Button_Response: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def EnableMotorsFromExternalProgram(self, EnabledStateInput):

        EnabledStateInput = int(EnabledStateInput)

        if EnabledStateInput in [0, 1]:
            self.EnabledState_ToBeSet = EnabledStateInput
            self.EnabledState_NeedsToBeChangedFlag = 1
    
            #self.MyPrint_WithoutLogFile("EnableMotorsFromExternalProgram: Event fired!")
        else:
            self.MyPrint_WithoutLogFile("EnableMotorsFromExternalProgram: Error, input value must be 0 or 1.")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def EmergencyStopState_Button_Response(self):

        if self.EmergencyStopState_ToBeSet == 1:
            self.EmergencyStopFromExternalProgram(0)
        else:
            self.EmergencyStopFromExternalProgram(1)

        #self.MyPrint_WithoutLogFile("EmergencyStopState_Button_Response: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def EmergencyStopFromExternalProgram(self, EmergencyStopStateInput):

        EmergencyStopStateInput = int(EmergencyStopStateInput)

        if EmergencyStopStateInput in [0, 1]:
            self.EmergencyStopState_ToBeSet = EmergencyStopStateInput
            self.EmergencyStopState_NeedsToBeChangedFlag = 1
    
            #self.MyPrint_WithoutLogFile("EmergencyStopFromExternalProgram: Event fired!")
        else:
            self.MyPrint_WithoutLogFile("EmergencyStopFromExternalProgram: Error, input value must be 0 or 1.")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def StopInAllModes_Button_Response(self):

        self.StopInAllModes_NeedsToBeChangedFlag = 1

        self.MyPrint_WithoutLogFile("StopInAllModes_Button_Response: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetCurrentPositionAsHomeOnDevice_Button_Response(self):

        self.SetCurrentPositionAsHomeOnDevice()

        #self.MyPrint_WithoutLogFile("SetCurrentPositionAsHomeOnDevice_Button_Response: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def SetCurrentPositionAsHomeSoftwareOffsetOnly_Button_Response(self):

        self.SetCurrentPositionAsHomeSoftwareOffsetOnly()

        #self.MyPrint_WithoutLogFile("SetCurrentPositionAsHomeSoftwareOffsetOnly_Button_Response: Event fired!")

    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def Motor_Target_GUIscale_EventResponse(self, event):

        self.Motor_Target_ToBeSet = self.Motor_Target_GUIscale_Value.get()
        self.Motor_Target_NeedsToBeChangedFlag = 1

        #self.MyPrint_WithoutLogFile("Motor_Target_GUIscale_EventResponse: Position set to " + str(self.Motor_Target_ToBeSet))
    ##########################################################################################################
    ##########################################################################################################

    ##########################################################################################################
    ##########################################################################################################
    def ToggleMinMax_Button_Response(self):

        self.ToggleMinMax_EventNeedsToBeFiredFlag = 1

        #self.MyPrint_WithoutLogFile("ToggleMinMax_Button_Response: Event fired!")

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

                    #######################################################
                    self.Motor_Label["text"] = self.ConvertDictToProperlyFormattedStringForPrinting(self.MostRecentDataDict,
                                                                                                    NumberOfDecimalsPlaceToUse = 2,
                                                                                                    NumberOfEntriesPerLine = 1,
                                                                                                    NumberOfTabsBetweenItems = 3)
                    #######################################################

                    #######################################################
                    if self.Motor_Target_GUIscale_NeedsToBeChangedFlag == 1:
                        self.Motor_Target_GUIscale_ScaleObject.set(self.Motor_Target_ToBeSet)
                        self.Motor_Target_GUIscale_NeedsToBeChangedFlag = 0
                    #######################################################

                    #######################################################
                    if self.EntryListWithBlinking_OPEN_FLAG == 1:
                        self.EntryListWithBlinking_ReubenPython2and3ClassObject.GUI_update_clock()

                        MostRecentDataDict_PID_EntryListWithBlinking = self.EntryListWithBlinking_ReubenPython2and3ClassObject.GetMostRecentDataDict()  # Get latest gain values

                        self.PID_Kp = MostRecentDataDict_PID_EntryListWithBlinking["Kp"]
                        self.PID_Ki = MostRecentDataDict_PID_EntryListWithBlinking["Ki"]
                        self.PID_Kd = MostRecentDataDict_PID_EntryListWithBlinking["Kd"]
                        self.PID_IntegratorCap1to100percent = MostRecentDataDict_PID_EntryListWithBlinking["IntegratorCap1to100percent"]
                    #######################################################

                    #######################################################
                    self.PrintToGui_Label.config(text=self.PrintToGui_Label_TextInput_Str)
                    #######################################################

                except:
                    exceptions = sys.exc_info()[0]
                    print("RoboteqBLDCcontroller_ReubenPython2and3Class GUI_update_clock ERROR: Exceptions: %s" % exceptions)
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
    def LimitTextEntryInput(self, min_val, max_val, test_val, TextEntryObject):

        try:
            test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

            if test_val > max_val:
                test_val = max_val
            elif test_val < min_val:
                test_val = min_val
            else:
                test_val = test_val

        except:
            pass

        try:
            if TextEntryObject != "":
                if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
                    TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
                else:
                    TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        except:
            pass

        return test_val
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

    ##########################################################################################################
    ##########################################################################################################
    def ConvertDictToProperlyFormattedStringForPrinting(self, DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

        ProperlyFormattedStringForPrinting = ""
        ItemsPerLineCounter = 0

        for Key in DictToPrint:

            ##########################################################################################################
            if isinstance(DictToPrint[Key], dict): #RECURSION
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     str(Key) + ":\n" + \
                                                     self.ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                     str(Key) + ": " + \
                                                     self.ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)
            ##########################################################################################################

            ##########################################################################################################
            if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
                ItemsPerLineCounter = ItemsPerLineCounter + 1
            else:
                ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
                ItemsPerLineCounter = 0
            ##########################################################################################################

        return ProperlyFormattedStringForPrinting
    ##########################################################################################################
    ##########################################################################################################
