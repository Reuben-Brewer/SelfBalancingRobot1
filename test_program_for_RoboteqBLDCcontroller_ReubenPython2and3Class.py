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
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
from RoboteqBLDCcontroller_ReubenPython2and3Class import *
##########################################

##########################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
import keyboard
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
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
##########################################

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject
    global RoboteqBLDCcontroller_OPEN_FLAG
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG
    global RoboteqBLDCcontroller_MostRecentDict

    global MyPrint_ReubenPython2and3ClassObject
    global MYPRINT_OPEN_FLAG
    global SHOW_IN_GUI_MYPRINT_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if RoboteqBLDCcontroller_OPEN_FLAG == 1 and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG == 1:
                RoboteqBLDCcontroller_MostRecentDict_Label["text"]  = ConvertDictToProperlyFormattedStringForPrinting(RoboteqBLDCcontroller_MostRecentDict, NumberOfDecimalsPlaceToUse=3, NumberOfEntriesPerLine=3, NumberOfTabsBetweenItems=1)
            #########################################################

            #########################################################
            if RoboteqBLDCcontroller_OPEN_FLAG == 1 and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MYPRINT_OPEN_FLAG == 1 and SHOW_IN_GUI_MYPRINT_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback(OptionalArugment = 0):
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
##########################################################################################################
##########################################################################################################
def ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input, number_of_leading_numbers = 4, number_of_decimal_places = 3):

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
                ListOfStringsToJoin.append(ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

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
                ListOfStringsToJoin.append("TUPLE" + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(element, number_of_leading_numbers, number_of_decimal_places))

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
                ListOfStringsToJoin.append(str(Key) + ": " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(input[Key], number_of_leading_numbers, number_of_decimal_places))

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
def ConvertDictToProperlyFormattedStringForPrinting(DictToPrint, NumberOfDecimalsPlaceToUse = 3, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 3):

    ProperlyFormattedStringForPrinting = ""
    ItemsPerLineCounter = 0

    for Key in DictToPrint:

        if isinstance(DictToPrint[Key], dict): #RECURSION
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 Key + ": " + \
                                                 ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DictToPrint[Key], 0, NumberOfDecimalsPlaceToUse)

        if ItemsPerLineCounter < NumberOfEntriesPerLine - 1:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\t"*NumberOfTabsBetweenItems
            ItemsPerLineCounter = ItemsPerLineCounter + 1
        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + "\n"
            ItemsPerLineCounter = 0

    return ProperlyFormattedStringForPrinting
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_Thread():
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_TABS_IN_GUI_FLAG

    ################################################# KEY GUI LINE
    #################################################
    root = Tk()
    #################################################
    #################################################

    #################################################
    #################################################
    global TabControlObject
    global Tab_MainControls
    global Tab_RoboteqBLDCcontroller
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_RoboteqBLDCcontroller = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_RoboteqBLDCcontroller, text='   ROBOTEQ   ')

        Tab_MainControls = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MainControls, text='   Main Controls   ')

        Tab_MyPrint = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_MyPrint, text='   MyPrint Terminal   ')

        TabControlObject.pack(expand=1, fill="both")  # CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

        ############# #Set the tab header font
        TabStyle = ttk.Style()
        TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
        #############
        #################################################
    else:
        #################################################
        Tab_MainControls = root
        Tab_RoboteqBLDCcontroller = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_MostRecentDict_Label
    RoboteqBLDCcontroller_MostRecentDict_Label = Label(Tab_MainControls, text="RoboteqBLDCcontroller_MostRecentDict_Label", width=120, font=("Helvetica", 10))
    RoboteqBLDCcontroller_MostRecentDict_Label.grid(row=0, column=0, padx=1, pady=1, columnspan=1, rowspan=1)
    #################################################
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    #################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_RoboteqBLDCcontroller_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    #################################################
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    #################################################
    #################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
if __name__ == '__main__':

    #################################################
    #################################################
    global my_platform

    if platform.system() == "Linux":

        if "raspberrypi" in platform.uname():  # os.uname() doesn't work in windows
            my_platform = "pi"
        else:
            my_platform = "linux"

    elif platform.system() == "Windows":
        my_platform = "windows"

    elif platform.system() == "Darwin":
        my_platform = "mac"

    else:
        my_platform = "other"

    print("The OS platform is: " + my_platform)
    #################################################
    #################################################

    #################################################
    #################################################
    global USE_GUI_FLAG
    USE_GUI_FLAG = 1

    global USE_TABS_IN_GUI_FLAG
    USE_TABS_IN_GUI_FLAG = 1

    global USE_RoboteqBLDCcontroller_FLAG
    USE_RoboteqBLDCcontroller_FLAG = 1

    global USE_KEYBOARD_FLAG
    USE_KEYBOARD_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1

    global USE_PLOTTER_FLAG
    USE_PLOTTER_FLAG = 1

    global USE_SINUSOIDAL_INPUT_FLAG
    USE_SINUSOIDAL_INPUT_FLAG = 0 #unicorn
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG
    SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG = 1

    global SHOW_IN_GUI_MYPRINT_FLAG
    SHOW_IN_GUI_MYPRINT_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_RoboteqBLDCcontroller
    global GUI_COLUMN_RoboteqBLDCcontroller
    global GUI_PADX_RoboteqBLDCcontroller
    global GUI_PADY_RoboteqBLDCcontroller
    global GUI_ROWSPAN_RoboteqBLDCcontroller
    global GUI_COLUMNSPAN_RoboteqBLDCcontroller
    GUI_ROW_RoboteqBLDCcontroller = 1

    GUI_COLUMN_RoboteqBLDCcontroller = 0
    GUI_PADX_RoboteqBLDCcontroller = 1
    GUI_PADY_RoboteqBLDCcontroller = 1
    GUI_ROWSPAN_RoboteqBLDCcontroller = 1
    GUI_COLUMNSPAN_RoboteqBLDCcontroller = 1

    global GUI_ROW_MYPRINT
    global GUI_COLUMN_MYPRINT
    global GUI_PADX_MYPRINT
    global GUI_PADY_MYPRINT
    global GUI_ROWSPAN_MYPRINT
    global GUI_COLUMNSPAN_MYPRINT
    GUI_ROW_MYPRINT = 2

    GUI_COLUMN_MYPRINT = 0
    GUI_PADX_MYPRINT = 1
    GUI_PADY_MYPRINT = 1
    GUI_ROWSPAN_MYPRINT = 1
    GUI_COLUMNSPAN_MYPRINT = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0

    global CurrentTime_MainLoopThread
    CurrentTime_MainLoopThread = -11111.0

    global StartingTime_MainLoopThread
    StartingTime_MainLoopThread = -11111.0

    global root

    global root_Xpos
    root_Xpos = 900

    global root_Ypos
    root_Ypos = 0

    global root_width
    root_width = 1920 - root_Xpos

    global root_height
    root_height = 1020 - root_Ypos

    global TabControlObject
    global Tab_MainControls
    global Tab_RoboteqBLDCcontroller
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    global SINUSOIDAL_INPUT_TO_COMMAND
    SINUSOIDAL_INPUT_TO_COMMAND = 0.0

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle = 2.0

    global SINUSOIDAL_MOTION_INPUT_MinValue
    SINUSOIDAL_MOTION_INPUT_MinValue = -100.0

    global SINUSOIDAL_MOTION_INPUT_MaxValue
    SINUSOIDAL_MOTION_INPUT_MaxValue = 100.0

    global ControlMode_AcceptableValuesList
    ControlMode_AcceptableValuesList = []

    global SINUSOIDAL_CONTROL_MODE
    #SINUSOIDAL_CONTROL_MODE = "ClosedLoopSpeedPosition"
    #SINUSOIDAL_CONTROL_MODE = "ClosedLoopTorque"
    SINUSOIDAL_CONTROL_MODE = "OpenLoop"
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject

    global RoboteqBLDCcontroller_OPEN_FLAG
    RoboteqBLDCcontroller_OPEN_FLAG = -1

    global RoboteqBLDCcontroller_MostRecentDict
    RoboteqBLDCcontroller_MostRecentDict = dict()

    global RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter
    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_SpeedRPM
    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_MotorPowerOutputApplied
    RoboteqBLDCcontroller_MostRecentDict_MotorPowerOutputApplied = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_CorrectInt
    RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_CorrectInt = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_EnglishString
    RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_EnglishString = "unknown"

    global RoboteqBLDCcontroller_MostRecentDict_FaultFlags
    RoboteqBLDCcontroller_MostRecentDict_FaultFlags = -11111.0

    '''
    global RoboteqBLDCcontroller_MostRecentDict_TorqueTarget
    RoboteqBLDCcontroller_MostRecentDict_TorqueTarget = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_MotorCurrentRMSamps
    RoboteqBLDCcontroller_MostRecentDict_MotorCurrentRMSamps = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_MotorCurrentPeakAmps
    RoboteqBLDCcontroller_MostRecentDict_MotorCurrentPeakAmps = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps
    RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10
    RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10 = -11111.0
    '''

    global RoboteqBLDCcontroller_MostRecentDict_Position_Rev
    RoboteqBLDCcontroller_MostRecentDict_Position_Rev = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Position_Radians
    RoboteqBLDCcontroller_MostRecentDict_Position_Radians = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Position_Degrees
    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_Calculated
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_Calculated = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_Calculated
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_Calculated = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_Calculated
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_Calculated = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_Calculated
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_Calculated = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_Time
    RoboteqBLDCcontroller_MostRecentDict_Time = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread = -11111.0

    '''
    global RoboteqBLDCcontroller_MostRecentDict_PID_Kp
    RoboteqBLDCcontroller_MostRecentDict_PID_Kp = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_PID_Ki
    RoboteqBLDCcontroller_MostRecentDict_PID_Ki = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_PID_Kd
    RoboteqBLDCcontroller_MostRecentDict_PID_Kd = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent
    RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent = -11111.0
    '''
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MYPRINT_OPEN_FLAG
    MYPRINT_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global PLOTTER_OPEN_FLAG
    PLOTTER_OPEN_FLAG = -1

    global MyPlotterPureTkinter_MostRecentDict
    MyPlotterPureTkinter_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_MainLoopThread_PLOTTER
    LastTime_MainLoopThread_PLOTTER = -11111.0
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        print("Starting GUI thread...")
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True) #Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  #Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        root = None
        Tab_MainControls = None
        Tab_RoboteqBLDCcontroller = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG),
                                    ("root", Tab_RoboteqBLDCcontroller),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_RoboteqBLDCcontroller),
                                    ("GUI_COLUMN", GUI_COLUMN_RoboteqBLDCcontroller),
                                    ("GUI_PADX", GUI_PADX_RoboteqBLDCcontroller),
                                    ("GUI_PADY", GUI_PADY_RoboteqBLDCcontroller),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_RoboteqBLDCcontroller),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_RoboteqBLDCcontroller)])


    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_ClosedLoopTorque
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_ClosedLoopTorque= dict([("GUIparametersDict", RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                ("DesiredSerialNumber_USBtoSerialConverter", "FT5ALD6OA"), #M0=FT5ALD6OA,M1=FT5AKLUOA, CHANGE THIS TO MATCH YOUR UNIQUE USB-TO-RS232 CONVERTER SERIAL NUMBER
                                                                                ("NameToDisplay_UserSet", "Reuben's Test RoboteQ SBL1360A Program"),
                                                                                ("ControlMode_Starting", SINUSOIDAL_CONTROL_MODE),
                                                                                ("OpenLoopPower_Target_Min_UserSet", -100.0),
                                                                                ("OpenLoopPower_Target_Max_UserSet", 100.0),
                                                                                ("OpenLoopPower_Target_Starting", 0.0),
                                                                                ("Acceleration_Target_Min_UserSet", 0.0),
                                                                                ("Acceleration_Target_Max_UserSet", 500000.0),
                                                                                ("Acceleration_Target_Starting", 500000.0),
                                                                                ("Current_Amps_Min_UserSet", 1.0),
                                                                                ("Current_Amps_Max_UserSet", 10.0),
                                                                                ("Current_Amps_Starting", 10.0),
                                                                                ("DedicatedRxThread_TimeToSleepEachLoop", 0.002),
                                                                                ("DedicatedTxThread_TimeToSleepEachLoop", 0.002),
                                                                                ("SerialRxBufferSize", 6),
                                                                                ("SerialTxBufferSize", 15),
                                                                                ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", 1),
                                                                                ("HeartbeatTimeIntervalMilliseconds", 1000.00), #0 turns the Heartbeat off, reset to 1000.00
                                                                                ("NumberOfMagnetsInMotor", 30),
                                                                                ("VariableStreamingSendDataEveryDeltaT_MillisecondsInt", 5),
                                                                                ("Speed_RPS_Calculated_LowPassFilter_ExponentialSmoothingFilterLambda", 0.05),
                                                                                ("SetBrushlessCounterTo0atStartOfProgramFlag", 1)])

    '''
    ("Position_Target_Min_UserSet", -1000.0),
    ("Position_Target_Max_UserSet", 1000.0),
    ("Position_Target_Starting", 0.0),
    ("Speed_Target_Min_UserSet", -1000.0),
    ("Speed_Target_Max_UserSet", 1000.0),
    ("Speed_Target_Starting", 0.0),
    ("Torque_Amps_Min_UserSet", 1.0),
    ("Torque_Amps_Max_UserSet", 10.0),
    ("Torque_Amps_Starting", 10.0),
    ("PID_Kp", 0.5),
    ("PID_Ki", 3.0),
    ("PID_Kd", 0.0),
    ("PID_IntegratorCap1to100percent", 100.0),
    '''

    if USE_RoboteqBLDCcontroller_FLAG == 1:
        try:
            #RoboteqBLDCcontroller_ReubenPython2and3ClassObject = RoboteqBLDCcontroller_ReubenPython2and3Class(RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_ClosedLoopSpeedPosition)

            RoboteqBLDCcontroller_ReubenPython2and3ClassObject = RoboteqBLDCcontroller_ReubenPython2and3Class(RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_ClosedLoopTorque)

            RoboteqBLDCcontroller_OPEN_FLAG = RoboteqBLDCcontroller_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("RoboteqBLDCcontroller_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MYPRINT_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MYPRINT),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MYPRINT),
                                                                        ("GUI_PADX", GUI_PADX_MYPRINT),
                                                                        ("GUI_PADY", GUI_PADY_MYPRINT),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MYPRINT),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MYPRINT)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MYPRINT_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict = dict([("EnableInternal_MyPrint_Flag", 1),
                                                                                                ("NumberOfPrintLines", 10),
                                                                                                ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                                                ("GraphCanvasWidth", 890),
                                                                                                ("GraphCanvasHeight", 700),
                                                                                                ("GraphCanvasWindowStartingX", 0),
                                                                                                ("GraphCanvasWindowStartingY", 0),
                                                                                                ("GUI_RootAfterCallbackInterval_Milliseconds_IndependentOfParentRootGUIloopEvents", 20)])

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("ParentPID", os.getpid()),
                                                                                        ("WatchdogTimerExpirationDurationSeconds_StandAlonePlottingProcess", 0.0),
                                                                                        ("MarkerSize", 3),
                                                                                        ("CurvesToPlotNamesAndColorsDictOfLists", dict([("NameList", ["Channel0", "Channel1", "Channel2", "Channel3"]),("ColorList", ["Red", "Green", "Blue", "Black"])])),
                                                                                        ("NumberOfDataPointToPlot", 100),
                                                                                        ("XaxisNumberOfTickMarks", 10),
                                                                                        ("YaxisNumberOfTickMarks", 10),
                                                                                        ("XaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("YaxisNumberOfDecimalPlacesForLabels", 3),
                                                                                        ("XaxisAutoscaleFlag", 1),
                                                                                        ("YaxisAutoscaleFlag", 1),
                                                                                        ("X_min", 0.0),
                                                                                        ("X_max", 20.0),
                                                                                        ("Y_min", -0.0015),
                                                                                        ("Y_max", 0.0015),
                                                                                        ("XaxisDrawnAtBottomOfGraph", 0),
                                                                                        ("XaxisLabelString", "Time (sec)"),
                                                                                        ("YaxisLabelString", "Y-units (units)"),
                                                                                        ("ShowLegendFlag", 1)])

    if USE_PLOTTER_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            PLOTTER_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_KEYBOARD_FLAG == 1:
        keyboard.on_press_key("esc", ExitProgram_Callback)
        #keyboard.on_press_key("q", ExitProgram_Callback)
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_RoboteqBLDCcontroller_FLAG == 1 and RoboteqBLDCcontroller_OPEN_FLAG != 1:
        print("Failed to open RoboteqBLDCcontroller_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MYPRINT_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_PLOTTER_FLAG == 1 and PLOTTER_OPEN_FLAG != 1:
        print("Failed to open MyPlotterPureTkinterClass_Object.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    print("Starting main loop 'test_program_for_RoboteqBLDCcontroller_ReubenPython2and3Class.py'")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG == 1:

            RoboteqBLDCcontroller_MostRecentDict = RoboteqBLDCcontroller_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in RoboteqBLDCcontroller_MostRecentDict:
                RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter = RoboteqBLDCcontroller_MostRecentDict["AbsoluteBrushlessCounter"]
                #RoboteqBLDCcontroller_MostRecentDict_SpeedRPM = RoboteqBLDCcontroller_MostRecentDict["SpeedRPM"]
                #RoboteqBLDCcontroller_MostRecentDict_MotorPowerOutputApplied = RoboteqBLDCcontroller_MostRecentDict["MotorPowerOutputApplied"]

                RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_CorrectInt = RoboteqBLDCcontroller_MostRecentDict["ActualOperationMode_CorrectInt"]
                RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_EnglishString = RoboteqBLDCcontroller_MostRecentDict["ActualOperationMode_EnglishString"]
                RoboteqBLDCcontroller_MostRecentDict_FaultFlags = RoboteqBLDCcontroller_MostRecentDict["FaultFlags"]

                #RoboteqBLDCcontroller_MostRecentDict_TorqueTarget = RoboteqBLDCcontroller_MostRecentDict["TorqueTarget"]
                #RoboteqBLDCcontroller_MostRecentDict_MotorCurrentRMSamps = RoboteqBLDCcontroller_MostRecentDict["MotorCurrentRMSamps"]
                #RoboteqBLDCcontroller_MostRecentDict_MotorCurrentPeakAmps = RoboteqBLDCcontroller_MostRecentDict["MotorCurrentPeakAmps"]
                #RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps = RoboteqBLDCcontroller_MostRecentDict["BatteryCurrentInAmps"]
                #RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10 = RoboteqBLDCcontroller_MostRecentDict["BatteryVoltsX10"]

                RoboteqBLDCcontroller_MostRecentDict_Position_Rev = RoboteqBLDCcontroller_MostRecentDict["Position_Rev"]
                RoboteqBLDCcontroller_MostRecentDict_Position_Radians = RoboteqBLDCcontroller_MostRecentDict["Position_Radians"]
                RoboteqBLDCcontroller_MostRecentDict_Position_Degrees = RoboteqBLDCcontroller_MostRecentDict["Position_Degrees"]

                #RoboteqBLDCcontroller_MostRecentDict_Speed_RPM = RoboteqBLDCcontroller_MostRecentDict["Speed_RPM"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_RPS = RoboteqBLDCcontroller_MostRecentDict["Speed_RPS"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec = RoboteqBLDCcontroller_MostRecentDict["Speed_RadiansPerSec"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec = RoboteqBLDCcontroller_MostRecentDict["Speed_DegreesPerSec"]

                #RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_Calculated = RoboteqBLDCcontroller_MostRecentDict["Speed_RPM_Calculated"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_Calculated = RoboteqBLDCcontroller_MostRecentDict["Speed_RPS_Calculated"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_Calculated = RoboteqBLDCcontroller_MostRecentDict["Speed_RadiansPerSec_Calculated"]
                #RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_Calculated = RoboteqBLDCcontroller_MostRecentDict["Speed_DegreesPerSec_Calculated"]

                RoboteqBLDCcontroller_MostRecentDict_Time = RoboteqBLDCcontroller_MostRecentDict["Time"]
                RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread = RoboteqBLDCcontroller_MostRecentDict["DataStreamingFrequency_CalculatedFromDedicatedRxThread"]
                RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread = RoboteqBLDCcontroller_MostRecentDict["DataStreamingFrequency_CalculatedFromDedicatedTxThread"]
                RoboteqBLDCcontroller_MostRecentDict_PID_Kp = RoboteqBLDCcontroller_MostRecentDict["PID_Kp"]
                RoboteqBLDCcontroller_MostRecentDict_PID_Ki = RoboteqBLDCcontroller_MostRecentDict["PID_Ki"]
                RoboteqBLDCcontroller_MostRecentDict_PID_Kd = RoboteqBLDCcontroller_MostRecentDict["PID_Kd"]
                RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent = RoboteqBLDCcontroller_MostRecentDict["PID_IntegratorCap1to100percent"]
                RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_CorrectInt = RoboteqBLDCcontroller_MostRecentDict["ActualOperationMode_CorrectInt"]
                RoboteqBLDCcontroller_MostRecentDict_ActualOperationMode_EnglishString = RoboteqBLDCcontroller_MostRecentDict["ActualOperationMode_EnglishString"]

                #print("RoboteqBLDCcontroller_MostRecentDict_Time: " + str(RoboteqBLDCcontroller_MostRecentDict_Time))
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG == 1:

            if USE_SINUSOIDAL_INPUT_FLAG == 1:
                time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
                SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)*math.sin(1.0*time_gain*CurrentTime_MainLoopThread)

                RoboteqBLDCcontroller_ReubenPython2and3ClassObject.SendCommandToMotor_ExternalClassFunction(SINUSOIDAL_INPUT_TO_COMMAND, SINUSOIDAL_CONTROL_MODE)

        ###################################################
        ###################################################

        ####################################################
        ####################################################
        if PLOTTER_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_MainLoopThread - LastTime_MainLoopThread_PLOTTER >= 0.030:
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1", "Channel2"], [CurrentTime_MainLoopThread]*3, [RoboteqBLDCcontroller_MostRecentDict_Position_Rev, RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec, RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_Calculated])

                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_MainLoopThread]*2, [SINUSOIDAL_INPUT_TO_COMMAND, RoboteqBLDCcontroller_MostRecentDict_MotorPowerOutputApplied])


                        LastTime_MainLoopThread_PLOTTER = CurrentTime_MainLoopThread
            ####################################################

        ####################################################
        ####################################################

        time.sleep(0.002)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_RoboteqBLDCcontroller_ReubenPython2and3Class.")

    #################################################
    if RoboteqBLDCcontroller_OPEN_FLAG == 1:
        RoboteqBLDCcontroller_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MYPRINT_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if PLOTTER_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################