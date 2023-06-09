# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision F, 05/10/2023

Verified working on: Python 3.9 for Windows 10 64-bit and Raspberry Pi Bullseye.
'''

__author__ = 'reuben.brewer'

#########################################################
#https://github.com/Reuben-Brewer/LowPassFilter_ReubenPython2and3Class
from LowPassFilter_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class
from MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/MyPrint_ReubenPython2and3Class
from MyPrint_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class
from PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class
from PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class
from PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/RoboteqBLDCcontroller_ReubenPython2and3Class
from RoboteqBLDCcontroller_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
from copy import * #for deep_copy of dicts
from collections import OrderedDict
import json
import keyboard #"sudo pip install keyboard" https://pypi.org/project/keyboard/, https://github.com/boppreh/keyboard
import subprocess #for beep command line call
import numpy
import re
from scipy.spatial.transform import Rotation

if platform.system() == "Windows":
    import winsound
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
import platform
if platform.system() == "Windows":
    import ctypes
    winmm = ctypes.WinDLL('winmm')
    winmm.timeBeginPeriod(1) #Set minimum timer resolution to 1ms so that time.sleep(0.001) behaves properly.
#########################################################

#######################################################################################################################
#######################################################################################################################
global ParametersToBeLoaded_Directory_Windows
ParametersToBeLoaded_Directory_Windows = os.getcwd().replace("\\", "//") + "//ParametersToBeLoaded"

global LogFile_Directory_Windows
LogFile_Directory_Windows = os.getcwd().replace("\\", "//") + "//Logs"

global ParametersToBeLoaded_Directory_RaspberryPi
ParametersToBeLoaded_Directory_RaspberryPi = "//home//pi//Desktop//SelfBalancingRobot1_PythonDeploymentFiles//ParametersToBeLoaded"

global LogFile_Directory_RaspberryPi
LogFile_Directory_RaspberryPi = "//home//pi//Desktop//SelfBalancingRobot1_PythonDeploymentFiles//Logs"

global ParametersToBeLoaded_Directory_LinuxNonRaspberryPi
ParametersToBeLoaded_Directory_LinuxNonRaspberryPi = os.getcwd().replace("\\", "//") + "//ParametersToBeLoaded"

global LogFile_Directory_LinuxNonRaspberryPi
LogFile_Directory_LinuxNonRaspberryPi = os.getcwd().replace("\\", "//") + "//Logs"

global ParametersToBeLoaded_Directory_Mac
ParametersToBeLoaded_Directory_Mac = os.getcwd().replace("\\", "//") + "//ParametersToBeLoaded"

global LogFile_Directory_Mac
LogFile_Directory_Mac = os.getcwd().replace("\\", "//") + "//Logs"
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_UseClassesFlags():
    global ParametersToBeLoaded_UseClassesFlags_Dict

    print("Calling LoadAndParseJSONfile_UseClassesFlags().")

    #################################
    JSONfilepathFull_UseClassesFlags = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_UseClassesFlags.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_UseClassesFlags_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_UseClassesFlags, 1, 1)
    #################################

    #################################
    if USE_GUI_FLAG_ARGV_OVERRIDE != -1:
        USE_GUI_FLAG = USE_GUI_FLAG_ARGV_OVERRIDE
    else:
        USE_GUI_FLAG = PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG", ParametersToBeLoaded_UseClassesFlags_Dict["USE_GUI_FLAG"])
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_GUIsettings():
    global ParametersToBeLoaded_GUIsettings_Dict

    print("Calling LoadAndParseJSONfile_GUIsettings().")

    #################################
    JSONfilepathFull_GUIsettings = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_GUIsettings.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_GUIsettings_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_GUIsettings, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_RoboteqBLDCcontroller_0():
    global ParametersToBeLoaded_RoboteqBLDCcontroller_Dict_0

    print("Calling LoadAndParseJSONfile_RoboteqBLDCcontroller_0().")

    #################################
    JSONfilepathFull_RoboteqBLDCcontroller_0 = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_RoboteqBLDCcontroller_0.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_RoboteqBLDCcontroller_Dict_0 = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_RoboteqBLDCcontroller_0, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_RoboteqBLDCcontroller_1():
    global ParametersToBeLoaded_RoboteqBLDCcontroller_Dict_1

    print("Calling LoadAndParseJSONfile_RoboteqBLDCcontroller_1().")

    #################################
    JSONfilepathFull_RoboteqBLDCcontroller_1 = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_RoboteqBLDCcontroller_1.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_RoboteqBLDCcontroller_Dict_1 = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_RoboteqBLDCcontroller_1, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_WiFiVINTthumbstick():
    global ParametersToBeLoaded_WiFiVINTthumbstick_Dict

    print("Calling LoadAndParseJSONfile_WiFiVINTthumbstick().")

    #################################
    JSONfilepathFull_WiFiVINTthumbstick = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_WiFiVINTthumbstick.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_WiFiVINTthumbstick_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_WiFiVINTthumbstick, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_SpatialPrecision333():
    global ParametersToBeLoaded_SpatialPrecision333_Dict

    print("Calling LoadAndParseJSONfile_SpatialPrecision333().")

    #################################
    JSONfilepathFull_SpatialPrecision333 = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_SpatialPrecision333.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_SpatialPrecision333_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_SpatialPrecision333, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_DC30AmpCurrentSensor():
    global ParametersToBeLoaded_DC30AmpCurrentSensor_Dict
    global DC30AmpCurrentSensor_AxisHatButtonOrBallTo6DOFposeMapping_ListOfDicts_FormattedAsNicelyPrintedString

    print("Calling LoadAndParseJSONfile_DC30AmpCurrentSensor().")

    #################################
    JSONfilepathFull_DC30AmpCurrentSensor = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_DC30AmpCurrentSensor.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_DC30AmpCurrentSensor_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_DC30AmpCurrentSensor, 1, 1)
    #################################
    
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_MyPlotterPureTkinterStandAloneProcess():
    global ParametersToBeLoaded_MyPlotterPureTkinterStandAloneProcess_Dict

    print("Calling LoadAndParseJSONfile_MyPlotterPureTkinterStandAloneProcess().")

    #################################
    JSONfilepathFull_MyPlotterPureTkinterStandAloneProcess = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_MyPlotterPureTkinterStandAloneProcess.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_MyPlotterPureTkinterStandAloneProcess_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_MyPlotterPureTkinterStandAloneProcess, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_Keyboard():
    global ParametersToBeLoaded_Keyboard_Dict
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts

    print("Calling LoadAndParseJSONfile_Keyboard().")

    #################################
    JSONfilepathFull_Keyboard = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_Keyboard.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_Keyboard_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_Keyboard, 1, 1)
    #################################

    Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString = ConvertDictToProperlyFormattedStringForPrinting(Keyboard_KeysToTeleopControlsMapping_DictOfDicts, NumberOfDecimalsPlaceToUse = 2, NumberOfEntriesPerLine = 1, NumberOfTabsBetweenItems = 1)

    Keyboard_KeysToTeleopControlsMapping_DictOfDicts = Keyboard_KeysToTeleopControlsMapping_DictOfDicts

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_ControlLawParameters():
    global ParametersToBeLoaded_ControlLawParameters_Dict

    print("Calling LoadAndParseJSONfile_ControlLawParameters().")

    #################################
    JSONfilepathFull_ControlLawParameters = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_ControlLawParameters.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_ControlLawParameters_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_ControlLawParameters, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_RobotModelParameters():
    global ParametersToBeLoaded_RobotModelParameters_Dict

    print("Calling LoadAndParseJSONfile_RobotModelParameters().")

    #################################
    JSONfilepathFull_RobotModelParameters = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_RobotModelParameters.json"

    #def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):
    ParametersToBeLoaded_RobotModelParameters_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_RobotModelParameters, 1, 1)
    #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LoadAndParseJSONfile_AddDictKeysToGlobalsDict(GlobalsDict, JSONfilepathFull, USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS = 0, PrintResultsFlag = 0):

    try:
        #################################

        ##############
        with open(JSONfilepathFull) as ParametersToBeLoaded_JSONfileObject:
            ParametersToBeLoaded_JSONfileParsedIntoDict = json.load(ParametersToBeLoaded_JSONfileObject)

        ParametersToBeLoaded_JSONfileObject.close()
        ##############

        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        ##############
        for key, value in ParametersToBeLoaded_JSONfileParsedIntoDict.items():
            if USE_PassThrough0and1values_ExitProgramOtherwise_FOR_FLAGS == 1:
                if key.upper().find("_FLAG") != -1:
                    GlobalsDict[key] = PassThrough0and1values_ExitProgramOtherwise(key, value)
                else:
                    GlobalsDict[key] = value
            else:
                GlobalsDict[key] = value

            if PrintResultsFlag == 1:
                print(key + ": " + str(value))

        ##############
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        return ParametersToBeLoaded_JSONfileParsedIntoDict
        #################################
    except:
        #################################
        exceptions = sys.exc_info()[0]
        print("LoadAndParseJSONfile_Advanced Error, Exceptions: %s" % exceptions)
        traceback.print_exc()
        return dict()
        #################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ParseColonCommaSeparatedVariableString(line, print_line_flag = 0, numeric_values_only = 0):

    if print_line_flag == 1:
        print("ParseColonCommaSeparatedVariableString input: " + line)

    line_as_dict = dict()

    if len(line) > 0:
        try:
            line = line.replace("\n", "").replace("\r", "")
            line_as_list = filter(None, re.split("[,:]+", line))
            #print(line_as_list)

            toggle_counter = 0
            key = ""
            for element in line_as_list:
                if toggle_counter == 0:  # Every other element is a key, every other element is the value
                    key = element.strip()
                    toggle_counter = 1
                else:
                    if numeric_values_only == 1:
                        try:
                            line_as_dict[key] = float(element)
                            #print(key + " , " + element)
                        except:
                            line_as_dict[key] = "ERROR"
                    else:
                        line_as_dict[key] = element
                    toggle_counter = 0

            return line_as_dict
        except:
            exceptions = sys.exc_info()[0]
            print("ParseColonCommaSeparatedVariableString ERROR: Exceptions: %s" % exceptions)
            traceback.print_exc()
            return line_as_dict
    else:
        print("ParseColonCommaSeparatedVariableString WARNING: input string was zero-length")
        return line_as_dict
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
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

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
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

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
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
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def getTimeStampString():

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%m_%d_%Y---%H_%M_%S')

    return st
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def PassThrough0and1values_ExitProgramOtherwise(InputNameString, InputNumber):

    try:
        InputNumber_ConvertedToFloat = float(InputNumber)
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error. InputNumber for variable_name '" + InputNameString + "' must be a float value, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

    try:
        if InputNumber_ConvertedToFloat == 0.0 or InputNumber_ConvertedToFloat == 1:
            return InputNumber_ConvertedToFloat
        else:
            input("PassThrough0and1values_ExitProgramOtherwise Error. '" + InputNameString + "' must be 0 or 1 (value was " + str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")
            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThrough0and1values_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def PassThroughFloatValuesInRange_ExitProgramOtherwise(InputNameString, InputNumber, RangeMinValue, RangeMaxValue):

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
            input("PassThroughFloatValuesInRange_ExitProgramOtherwise Error. '" + InputNameString + "' must be in the range [" + str(RangeMinValue) + ", " + str(RangeMaxValue) + "] (value was " + str(InputNumber_ConvertedToFloat) + "). Press any key (and enter) to exit.")
            sys.exit()
    except:
        exceptions = sys.exc_info()[0]
        print("PassThroughFloatValuesInRange_ExitProgramOtherwise Error, Exceptions: %s" % exceptions)
        input("Press any key to continue")
        sys.exit()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction):

    TimerObject = threading.Timer(CallbackAfterDeltaTseconds, FunctionToCall_NoParenthesesAfterFunctionName, ArgumentListToFunction) #Must pass arguments to callback-function via list as the third argument to Timer call
    TimerObject.daemon = True #Without the daemon=True, this recursive function won't terminate when the main program does.
    TimerObject.start()

    print("TimerCallbackFunctionWithFunctionAsArgument_SingleShot_NoParenthesesAfterFunctionName event fired to call function: '" + str(FunctionToCall_NoParenthesesAfterFunctionName.__name__) + "' at time " + str(getPreciseSecondsTimeStampString()))

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateFrequencyCalculation(LoopCounter, CurrentTime, LastTime, DataStreamingFrequency, DataStreamingDeltaT):

    try:

        DataStreamingDeltaT = CurrentTime - LastTime

        ##########################
        if DataStreamingDeltaT != 0.0:
            DataStreamingFrequency = 1.0/DataStreamingDeltaT
        ##########################

        LastTime = CurrentTime

        LoopCounter = LoopCounter + 1

        return [LoopCounter, LastTime, DataStreamingFrequency, DataStreamingDeltaT]

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation, exceptions: %s" % exceptions)
        return [-11111.0]*4
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LimitNumber_FloatOutputOnly(min_val, max_val, test_val):
    if test_val > max_val:
        test_val = max_val

    elif test_val < min_val:
        test_val = min_val

    else:
        test_val = test_val

    test_val = float(test_val)

    return test_val
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LimitNumber_IntOutputOnly(min_val, max_val, test_val):
    if test_val > max_val:
        test_val = max_val

    elif test_val < min_val:
        test_val = min_val

    else:
        test_val = test_val

    test_val = int(test_val)

    return test_val
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def LimitTextEntryInput(min_val, max_val, test_val, TextEntryObject):

    test_val = float(test_val)  # MUST HAVE THIS LINE TO CATCH STRINGS PASSED INTO THE FUNCTION

    if test_val > max_val:
        test_val = max_val
    elif test_val < min_val:
        test_val = min_val
    else:
        test_val = test_val

    if TextEntryObject != "":
        if isinstance(TextEntryObject, list) == 1:  # Check if the input 'TextEntryObject' is a list or not
            TextEntryObject[0].set(str(test_val))  # Reset the text, overwriting the bad value that was entered.
        else:
            TextEntryObject.set(str(test_val))  # Reset the text, overwriting the bad value that was entered.

    return test_val
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GetMyPlatform():
    my_platform = "other"

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

    return my_platform
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ParseARGV_USE_GUI_and_SOFTWARE_LAUNCH_METHOD():

    try:
        USE_GUI_FLAG_ARGV_OVERRIDE = -1
        SOFTWARE_LAUNCH_METHOD = -1

        if len(sys.argv) >= 2:
            ARGV_1 = sys.argv[1].strip().lower()

            print("ARGV_1: " + str(ARGV_1))
            ARGV_1_ParsedDict = ParseColonCommaSeparatedVariableString(ARGV_1)

            if "use_gui_flag" in ARGV_1_ParsedDict:
                USE_GUI_FLAG_ARGV_OVERRIDE = PassThrough0and1values_ExitProgramOtherwise("USE_GUI_FLAG_ARGV_OVERRIDE", int(ARGV_1_ParsedDict["use_gui_flag"]))

            if "software_launch_method" in ARGV_1_ParsedDict:
                SOFTWARE_LAUNCH_METHOD = ARGV_1_ParsedDict["software_launch_method"]

    except:
        exceptions = sys.exc_info()[0]
        print("Parsing ARGV_1, exceptions: %s" % exceptions)
        traceback.print_exc()
        time.sleep(0.25)

    #print("ARGV_1, USE_GUI_FLAG_ARGV_OVERRIDE: " + str(USE_GUI_FLAG_ARGV_OVERRIDE))
    #print("ARGV_1, SOFTWARE_LAUNCH_METHOD: " + str(SOFTWARE_LAUNCH_METHOD))

    return [USE_GUI_FLAG_ARGV_OVERRIDE, SOFTWARE_LAUNCH_METHOD]

#######################################################################################################################
#######################################################################################################################

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
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyboardMapKeysToCallbackFunctions():

    keyboard.unhook_all() #Remove all current mappings

    ###############################################
    for AxisNameAsKey in Keyboard_KeysToTeleopControlsMapping_DictOfDicts:

            KeyToTeleopControlsMappingDict = Keyboard_KeysToTeleopControlsMapping_DictOfDicts[AxisNameAsKey]

            KeyName = KeyToTeleopControlsMappingDict["KeyName"]
            OnPressCallbackFunctionNameString = KeyToTeleopControlsMappingDict["OnPressCallbackFunctionNameString"]
            OnReleaseCallbackFunctionNameString = KeyToTeleopControlsMappingDict["OnReleaseCallbackFunctionNameString"]

            if OnPressCallbackFunctionNameString in globals():
                keyboard.on_press_key(KeyName, globals()[OnPressCallbackFunctionNameString])

            if OnReleaseCallbackFunctionNameString in globals():
                keyboard.on_release_key(KeyName, globals()[OnReleaseCallbackFunctionNameString])

    ###############################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def DedicatedKeyboardListeningThread():

    ###############################################
    global EXIT_PROGRAM_FLAG

    global DedicatedKeyboardListeningThread_StillRunningFlag
    global CurrentTime_CalculatedFromDedicatedKeyboardListeningThread
    global StartingTime_CalculatedFromDedicatedKeyboardListeningThread
    global LastTime_CalculatedFromDedicatedKeyboardListeningThread
    global DataStreamingFrequency_CalculatedFromDedicatedKeyboardListeningThread
    global DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread
    global DedicatedKeyboardListeningThread_TimeToSleepEachLoop
    global BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace
    global BeepNeedsToBePlayedFlag_RecordNewWaypoint_CartesianSpace
    global KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag
    global KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag
    global KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag
    global KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag
    global KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag
    global KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag
    global Keyboard_AddToUR5armCurrentPositionList
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts
    global Keyboard_OPEN_FLAG
    ###############################################

    print("Started DedicatedKeyboardListeningThread for SelfBalancingRobot1.")
    DedicatedKeyboardListeningThread_StillRunningFlag = 1

    Keyboard_OPEN_FLAG = 1

    StartingTime_CalculatedFromDedicatedKeyboardListeningThread = getPreciseSecondsTimeStampString()

    ###############################################
    while EXIT_PROGRAM_FLAG == 0:
        try:
            ###############################################
            CurrentTime_CalculatedFromDedicatedKeyboardListeningThread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromDedicatedKeyboardListeningThread
            ###############################################

            ###############################################
            if BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace == 1:
                if platform.system() == "Windows":
                    winsound.Beep(int(4000), int(500))
                else:
                    try:
                        shell_response = subprocess.check_output("paplay //home//pi//Desktop//SelfBalancingRobot1_PythonDeploymentFiles//ParametersToBeLoaded//point.wav", shell=True)
                    except:
                        exceptions = sys.exc_info()[0]
                        print("ERROR BEEPING ON RASPBERRY PI, Exceptions: %s" % exceptions)

                BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace = 0
            ###############################################

            ###############################################
            if BeepNeedsToBePlayedFlag_RecordNewWaypoint_CartesianSpace == 1:
                if platform.system() == "Windows":
                    winsound.Beep(int(8000), int(500))
                else:
                    try:
                        shell_response = subprocess.check_output("paplay //home//pi//Desktop//SelfBalancingRobot1_PythonDeploymentFiles//ParametersToBeLoaded//point.wav", shell=True)
                    except:
                        exceptions = sys.exc_info()[0]
                        print("ERROR BEEPING ON RASPBERRY PI, Exceptions: %s" % exceptions)

                BeepNeedsToBePlayedFlag_RecordNewWaypoint_CartesianSpace = 0
            ###############################################

            ############################################### USE THE TIME.SLEEP() TO SET THE LOOP FREQUENCY
            ###############################################
            ###############################################
            if DedicatedKeyboardListeningThread_TimeToSleepEachLoop > 0.0:
                time.sleep(DedicatedKeyboardListeningThread_TimeToSleepEachLoop)
            ###############################################
            ###############################################
            ###############################################

        except:
            exceptions = sys.exc_info()[0]
            print("DedicatedKeyboardListeningThread, Exceptions: %s" % exceptions)
            traceback.print_exc()
    ###############################################

    print("Exited DedicatedKeyboardListeningThread.")
    DedicatedKeyboardListeningThread_StillRunningFlag = 0
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_RecordNewWaypoint_JointSpace(event):

    NewWaypointNumberToPrint = 99999.0 #CHANGE THIS TO SOMETHING USEFUL
    KeyPressResponse_RecordNewWaypoint_JointSpace_TextToPrint = ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(NewWaypointNumberToPrint, 0, 5)
    KeyPressResponse_RecordNewWaypoint_JointSpace_TextToPrint = KeyPressResponse_RecordNewWaypoint_JointSpace_TextToPrint.replace("+","")
    print(KeyPressResponse_RecordNewWaypoint_JointSpace_TextToPrint)

    BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace = 1

    print("KeyPressResponse_RecordNewWaypoint_JointSpace event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInX_START(event):

    KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_IncrementURtoolTipInX_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInX_STOP(event):

    KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_IncrementURtoolTipInX_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInX_START(event):

    KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_DecrementURtoolTipInX_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInX_STOP(event):

    KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_DecrementURtoolTipInX_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInY_START(event):

    KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_IncrementURtoolTipInY_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInY_STOP(event):

    KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_IncrementURtoolTipInY_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInY_START(event):

    KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_DecrementURtoolTipInY_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInY_STOP(event):

    KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_DecrementURtoolTipInY_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInZ_START(event):

    KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_IncrementURtoolTipInZ_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_IncrementURtoolTipInZ_STOP(event):

    KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_IncrementURtoolTipInZ_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInZ_START(event):

    KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_DecrementURtoolTipInZ_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_DecrementURtoolTipInZ_STOP(event):

    KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_DecrementURtoolTipInZ_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global USE_GUI_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global TKinter_LightRedColor
    global TKinter_LightGreenColor
    global TKinter_LightBlueColor
    global TKinter_LightYellowColor
    global TKinter_DefaultGrayColor
    global GreenCheckmarkPhotoImage
    global RedXphotoImage
    global TabControlObject
    global GUItabObjectsOrderedDict

    global CurrentTime_CalculatedFromMainThread
    global DataStreamingFrequency_CalculatedFromMainThread

    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0
    global RoboteqBLDCcontroller_OPEN_FLAG_0
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0
    global RoboteqBLDCcontroller_MostRecentDict_0

    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1
    global RoboteqBLDCcontroller_OPEN_FLAG_1
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1
    global RoboteqBLDCcontroller_MostRecentDict_1

    global PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject
    global WiFiVINTthumbstick_OPEN_FLAG
    global SHOW_IN_GUI_WiFiVINTthumbstick_FLAG
    global WiFiVINTthumbstick_MostRecentDict

    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject
    global SpatialPrecision333_OPEN_FLAG
    global SHOW_IN_GUI_SpatialPrecision333_FLAG
    global SpatialPrecision333_MostRecentDict

    global PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject
    global DC30AmpCurrentSensor_OPEN_FLAG
    global SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG
    global DC30AmpCurrentSensor_MostRecentDict

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global KeyboardInfo_Label
    #global Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString

    global DebuggingInfo_Label

    global ControlType

    global ControlType_StartingValue
    global ControlType_AcceptableValues

    #global SharedGlobals_SelfBalancingRobot1_MainThread_TimeToSleepEachLoop
    #global WiFiVINTthumbstick_PositionList_ScalingFactorList
    #global WiFiVINTthumbstick_RollPitchYaw_AbtXYZ_List_ScalingFactorList

    global LoopCounter_CalculatedFromGUIthread
    global CurrentTime_CalculatedFromGUIthread
    global StartingTime_CalculatedFromGUIthread
    global LastTime_CalculatedFromGUIthread
    global DataStreamingFrequency_CalculatedFromGUIthread
    global DataStreamingDeltaT_CalculatedFromGUIthread

    global LQR_PitchControl_GainVectorElement_Ktheta_0
    global LQR_PitchControl_GainVectorElement_Ktheta_1
    global LQR_PitchControl_GainVectorElement_Ktheta_2
    global LQR_PitchControl_GainVectorElement_Ktheta_3
    global LQR_YawControl_GainVectorElement_Kdelta_0
    global LQR_YawControl_GainVectorElement_Kdelta_1
    global Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION

    global Theta_RL_Actual
    global Theta_RR_Actual
    global Omega_RL_Actual
    global Omega_RL_Actual
    global Position_X_RM_Meters_Actual
    global Position_X_RMC_Meters_Commanded
    global Velocity_V_RM_MetersPerSec_Actual
    global Velocity_V_RMC_MetersPerSec_Commanded
    global PitchAngle_Theta_Deg_Actual
    global PitchAngle_Theta_Radians_Actual
    global PitchAngle_Theta_Deg_Commanded
    global PitchAngle_Theta_Radians_Commanded
    global PitchAngularRate_ThetaDot_DegPerSec_Actual
    global PitchAngularRate_ThetaDot_RadiansPerSec_Actual
    global PitchAngularRate_ThetaDot_DegPerSec_Commanded
    global PitchAngularRate_ThetaDot_RadiansPerSec_Commanded
    global YawAngle_Delta_Deg_Actual
    global YawAngle_Delta_Radians_Actual
    global YawAngle_Delta_Deg_Commanded
    global YawAngle_Delta_Radians_Commanded
    global YawAngularRate_DeltaDot_RadiansPerSec_Actual
    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded
    global TorqueToBeCommanded_Motor0
    global TorqueToBeCommanded_Motor1

    global EnableMotors_Button
    global EnableMotors_State

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            #########################################################
            CurrentTime_CalculatedFromGUIthread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromGUIthread

            [LoopCounter_CalculatedFromGUIthread, LastTime_CalculatedFromGUIthread, DataStreamingFrequency_CalculatedFromGUIthread, DataStreamingDeltaT_CalculatedFromGUIthread] = UpdateFrequencyCalculation(LoopCounter_CalculatedFromGUIthread, CurrentTime_CalculatedFromGUIthread, LastTime_CalculatedFromGUIthread, DataStreamingFrequency_CalculatedFromGUIthread, DataStreamingDeltaT_CalculatedFromGUIthread)
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            DebuggingInfo_Label["text"] = "MainThread, Time: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(CurrentTime_CalculatedFromMainThread, 0, 3) +\
                            "\t\t\tFrequency: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DataStreamingFrequency_CalculatedFromMainThread, 0, 3) +\
                            "\nGUIthread, Time: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(CurrentTime_CalculatedFromGUIthread, 0, 3) +\
                            "\t\t\tFrequency: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DataStreamingFrequency_CalculatedFromGUIthread, 0, 3) +\
                            "\nControlType: " + ControlType + \
                            "\n\n\n" +\
                            "\nTheta_RL_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Theta_RL_Actual, 3, 3) + \
                            "\nTheta_RR_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Theta_RR_Actual, 3, 3) + \
                            "\nOmega_RL_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Omega_RL_Actual, 3, 3) + \
                            "\nOmega_RR_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Omega_RR_Actual, 3, 3) + \
                            "\nPosition_X_RM_Meters_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Position_X_RM_Meters_Actual, 3, 3) + \
                            "\t\tPosition_X_RMC_Meters_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Position_X_RMC_Meters_Commanded, 3, 3) + \
                            "\nVelocity_V_RM_MetersPerSec_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Velocity_V_RM_MetersPerSec_Actual, 3, 3) + \
                            "\t\tVelocity_V_RMC_MetersPerSec_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Velocity_V_RMC_MetersPerSec_Commanded, 3, 3) + \
                            "\nPitchAngle_Theta_Deg_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PitchAngle_Theta_Deg_Actual, 3, 3) + \
                            "\t\tPitchAngle_Theta_Deg_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PitchAngle_Theta_Deg_Commanded, 3, 3) + \
                            "\nYawAngle_Delta_Deg_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngle_Delta_Deg_Actual, 3, 3) + \
                            "\t\tYawAngle_Delta_Deg_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngle_Delta_Deg_Commanded, 3, 3) + \
                            "\nLQR Ktheta_0: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_PitchControl_GainVectorElement_Ktheta_0, 3, 3) + \
                            "\t\tLQR Ktheta_1: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_PitchControl_GainVectorElement_Ktheta_1, 3, 3) + \
                            "\t\tLQR Ktheta_2: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_PitchControl_GainVectorElement_Ktheta_2, 3, 3) + \
                            "\t\tLQR Ktheta_3: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_PitchControl_GainVectorElement_Ktheta_3, 3, 3) + \
                            "\nLQR Kdelta_0: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_YawControl_GainVectorElement_Kdelta_0, 3, 3) + \
                            "\t\tLQR Kdelta_1: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(LQR_YawControl_GainVectorElement_Kdelta_1, 3, 3) + \
                            "\nPosition_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, 3, 3) + \
                            "\nTorqueToBeCommanded_Motor0: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(TorqueToBeCommanded_Motor0, 0, 3) + \
                            "\nTorqueToBeCommanded_Motor1: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(TorqueToBeCommanded_Motor1, 0, 3)
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if EnableMotors_State == 1:
                EnableMotors_Button["bg"] = TKinter_LightGreenColor
                EnableMotors_Button["text"] = "Motors enabled"
            else:
                EnableMotors_Button["bg"] = TKinter_LightRedColor
                EnableMotors_Button["text"] = "Motors disabled"
            #########################################################
            #########################################################

            ###########################################################
            ###########################################################
            for TabNameStringAsKey in GUItabObjectsOrderedDict:

                #########################################################
                if "IsTabCreatedFlag" in GUItabObjectsOrderedDict[TabNameStringAsKey]:
                    if GUItabObjectsOrderedDict[TabNameStringAsKey]["IsTabCreatedFlag"] == 1:

                        if GUItabObjectsOrderedDict[TabNameStringAsKey]["OpenFlag"] == 1:
                            TabControlObject.tab(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"], state='normal')
                            TabControlObject.tab(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"], image=GreenCheckmarkPhotoImage)
                        else:
                            TabControlObject.tab(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"], state='disabled')
                            TabControlObject.tab(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"], image=RedXphotoImage)
                #########################################################

            ###########################################################
            ###########################################################

            #########################################################
            #########################################################
            '''
            KeyboardInfo_Label["text"] = "Keyboard flags: " + str([KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag,
                                                        KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag,
                                                        KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag,
                                                        KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag,
                                                        KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag,
                                                        KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag,
                                                        KeyPressResponse_OpenRobotiqGripper2F85_NeedsToBeChangedFlag,
                                                        KeyPressResponse_CloseRobotiqGripper2F85_NeedsToBeChangedFlag]) + \
                            "\nKeyboard_AddToUR5armCurrentPositionList: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Keyboard_AddToUR5armCurrentPositionList, 0, 3) +\
                            "\nKeyboard_KeysToTeleopControlsMapping_DictOfDicts: " + \
                            "\n" + Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString
            '''
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            '''
            WiFiVINTthumbstick_Label["text"] = "\nWiFiVINTthumbstick_PositionList_ScalingFactorList: " + str(WiFiVINTthumbstick_PositionList_ScalingFactorList) + \
                            "\nWiFiVINTthumbstick_RollPitchYaw_AbtXYZ_List_ScalingFactorList: " + str(WiFiVINTthumbstick_RollPitchYaw_AbtXYZ_List_ScalingFactorList)

            '''
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if RoboteqBLDCcontroller_OPEN_FLAG_0 == 1 and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if RoboteqBLDCcontroller_OPEN_FLAG_1 == 1 and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if WiFiVINTthumbstick_OPEN_FLAG == 1 and SHOW_IN_GUI_WiFiVINTthumbstick_FLAG == 1:
                PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if SpatialPrecision333_OPEN_FLAG == 1 and SHOW_IN_GUI_SpatialPrecision333_FLAG == 1:
                PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if DC30AmpCurrentSensor_OPEN_FLAG == 1 and SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG == 1:
                PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
            #########################################################
            #########################################################
        
        #########################################################
        #########################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def GUI_Thread():
    global my_platform
    global root
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUItitleString
    global GUI_RootAfterCallbackInterval_Milliseconds
    global GUIbuttonWidth
    global GUIbuttonPadX
    global GUIbuttonPadY
    global GUIbuttonFontSize
    global USE_GUI_FLAG
    global TKinter_LightRedColor
    global TKinter_LightGreenColor
    global TKinter_LightBlueColor
    global TKinter_LightYellowColor
    global TKinter_DefaultGrayColor
    global SHOW_IN_GUI_UR5arm_MostRecentDict_FLAG

    global USE_Keyboard_FLAG
    global USE_WiFiVINTthumbstick_FLAG

    global ParametersToBeLoaded_Directory_TO_BE_USED
    global GreenCheckmarkPhotoImage
    global RedXphotoImage
    global GUItabObjectsOrderedDict
    global TabControlObject

    ########################################################### KEY GUI LINE
    ###########################################################
    root = Tk()
    ###########################################################
    ###########################################################

    ###########################################################SET THE DEFAULT FONT FOR ALL WIDGETS CREATED AFTTER/BELOW THIS CALL
    ###########################################################
    default_font = tkFont.nametofont("TkDefaultFont")
    default_font.configure(size=8)
    root.option_add("*Font", default_font)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150)  # RGB
    TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150)  # RGB
    TKinter_LightBlueColor = '#%02x%02x%02x' % (150, 150, 255)  # RGB
    TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150)  # RGB
    TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240)  # RGB
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    GreenCheckmarkPhotoImage = PhotoImage(file=ParametersToBeLoaded_Directory_TO_BE_USED + "//GreenCheckmark.gif")
    RedXphotoImage = PhotoImage(file=ParametersToBeLoaded_Directory_TO_BE_USED + "//RedXmark.gif")
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################

    ###########################################################
    TabControlObject = ttk.Notebook(root)
    ###########################################################

    ###########################################################
    TabCounter = 0
    for TabNameStringAsKey in GUItabObjectsOrderedDict:

        #############
        if GUItabObjectsOrderedDict[TabNameStringAsKey]["UseFlag"] == 1:
            GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject"] = ttk.Frame(TabControlObject)
            TabControlObject.add(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject"], text=GUItabObjectsOrderedDict[TabNameStringAsKey]["GUItabNameToDisplay"])

            if TabCounter == 0:
                GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"] = ".!notebook.!frame"
            else:
                GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"] = ".!notebook.!frame" + str(TabCounter + 1)

            TabControlObject.tab(GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject_InternalStringName"], compound='top')
            GUItabObjectsOrderedDict[TabNameStringAsKey]["IsTabCreatedFlag"] = 1
            TabCounter = TabCounter + 1
        else:
            GUItabObjectsOrderedDict[TabNameStringAsKey]["TabObject"] = None
        #############

    ###########################################################

    ###########################################################
    TabControlObject.pack(expand=1, fill="both") #CANNOT MIX PACK AND GRID IN THE SAME FRAME/TAB, SO ALL .GRID'S MUST BE CONTAINED WITHIN THEIR OWN FRAME/TAB.

    ############# #Set the tab header font
    TabStyle = ttk.Style()
    TabStyle.configure('TNotebook.Tab', font=('Helvetica', '12', 'bold'))
    #############

    ###########################################################

    ###########################################################
    ###########################################################
  
    ###########################################################
    ###########################################################
    global ExtraProgramControlGuiFrame
    ExtraProgramControlGuiFrame = Frame(GUItabObjectsOrderedDict["MainControls"]["TabObject"])
    ExtraProgramControlGuiFrame["borderwidth"] = 2
    ExtraProgramControlGuiFrame["relief"] = "ridge"
    ExtraProgramControlGuiFrame.grid(row=0, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, rowspan=1, columnspan=1, sticky='w')
    ###########################################################
    ###########################################################

    ############################################
    ############################################
    global ExitProgramButton
    ExitProgramButton = Button(ExtraProgramControlGuiFrame, text="Exit Program", state="normal", width=GUIbuttonWidth, command=lambda i=1: ExitProgram_Callback())
    ExitProgramButton.grid(row=0, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1,)
    ExitProgramButton.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global JSONfiles_NeedsToBeLoadedFlagButton
    JSONfiles_NeedsToBeLoadedFlagButton = Button(ExtraProgramControlGuiFrame, text="Load JSON files", state="normal", width=GUIbuttonWidth, command=lambda i=1: JSONfiles_NeedsToBeLoadedFlag_ButtonResponse())
    JSONfiles_NeedsToBeLoadedFlagButton.grid(row=0, column=1, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1,)
    JSONfiles_NeedsToBeLoadedFlagButton.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global EnableMotors_Button
    EnableMotors_Button = Button(ExtraProgramControlGuiFrame, text="Enable Motors", state="normal", width=GUIbuttonWidth, command=lambda i=1: EnableMotors_ButtonResponse())
    EnableMotors_Button.grid(row=0, column=2, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1,)
    EnableMotors_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ###########################################################
    ###########################################################
    global DebuggingInfo_Label
    DebuggingInfo_Label = Label(ExtraProgramControlGuiFrame, text="DebuggingInfo_Label", width=120, font=("Helvetica", 10))  #
    DebuggingInfo_Label.grid(row=1, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=10, rowspan=1)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global KeyboardInfo_Label
    KeyboardInfo_Label = Label(GUItabObjectsOrderedDict["Keyboard"]["TabObject"], text="KeyboardInfo_Label", width=120, font=("Helvetica", 10))
    if USE_Keyboard_FLAG == 1:
        KeyboardInfo_Label.grid(row=0, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=10, rowspan=1)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global WiFiVINTthumbstick_Label
    WiFiVINTthumbstick_Label = Label(GUItabObjectsOrderedDict["WiFiVINTthumbstick"]["TabObject"], text="WiFiVINTthumbstick_Label", width=120, font=("Helvetica", 10))
    if USE_WiFiVINTthumbstick_FLAG == 1:
        WiFiVINTthumbstick_Label.grid(row=1, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=10, rowspan=1)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ActuatorsControlGuiFrame
    ActuatorsControlGuiFrame = Frame(GUItabObjectsOrderedDict["MainControls"]["TabObject"])
    ActuatorsControlGuiFrame["borderwidth"] = 2
    ActuatorsControlGuiFrame["relief"] = "ridge"
    ActuatorsControlGuiFrame.grid(row=2, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, rowspan=1, columnspan=1, sticky='w')
    ActuatorsControlGuiFrame_ButtonWidth = 22
    ActuatorsControlGuiFrame_FontSize = 20
    ActuatorsControlGuiFrame_CheckbuttonWidth = 20
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlTypeGuiFrame
    ControlTypeGuiFrame = Frame(ExtraProgramControlGuiFrame)
    ControlTypeGuiFrame.grid(row=2, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, rowspan=1, columnspan=1, sticky='w')
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlType_Radiobutton_SelectionVar
    ControlType_Radiobutton_SelectionVar = StringVar()

    ControlType_Radiobutton_SelectionVar.set(ControlType_StartingValue)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlType_AcceptableValues

    global ControlType_RadioButtonObjectsList
    ControlType_RadioButtonObjectsList = list()
    for Index, ControlTypeString in enumerate(ControlType_AcceptableValues):
        ControlType_RadioButtonObjectsList.append(Radiobutton(ControlTypeGuiFrame,
                                                      text=ControlTypeString,
                                                      state="normal",
                                                      width=15,
                                                      anchor="w",
                                                      variable=ControlType_Radiobutton_SelectionVar,
                                                      value=ControlTypeString,
                                                      command=lambda name=ControlTypeString: ControlType_Radiobutton_Response(name)))
        ControlType_RadioButtonObjectsList[Index].grid(row=0, column=Index, padx=1, pady=1, columnspan=1, rowspan=1)
        #if ControlType_StartingValue == "ControlTypeString":
        #    ControlType_RadioButtonObjectsList[Index].select()
    ###########################################################
    ###########################################################

    ########################################################### THIS BLOCK MUST COME 2ND-TO-LAST IN def  GUI_Thread() IF USING TABS.
    ###########################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title(GUItitleString)
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.geometry('%dx%d+%d+%d' % (
    root_width, root_height, root_Xpos, root_Ypos))  # set the dimensions of the screen and where it is placed
    root.mainloop()
    ###########################################################
    ###########################################################

    ###########################################################
    ########################################################### THIS BLOCK MUST COME LAST IN def  GUI_Thread() REGARDLESS OF CODE.
    root.quit()  # Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy()  # Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
    ###########################################################
    ###########################################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ControlType_Radiobutton_Response(name):
    global ControlType_Radiobutton_SelectionVar
    global ControlType
    global ControlType_NeedsToBeChangedFlag

    #print("name: " + name)

    ControlType = ControlType_Radiobutton_SelectionVar.get()
    ControlType_NeedsToBeChangedFlag = 1
    print("ControlType set to: " + ControlType)
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def JSONfiles_NeedsToBeLoadedFlag_ButtonResponse():
    global JSONfiles_NeedsToBeLoadedFlag

    JSONfiles_NeedsToBeLoadedFlag = 1

    MyPrint_ReubenPython2and3ClassObject.my_print("JSONfiles_NeedsToBeLoadedFlag_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def EnableMotors_ButtonResponse():
    global EnableMotors_State

    if EnableMotors_State == 1:
        EnableMotors_State = 0
    else:
        EnableMotors_State = 1

    #MyPrint_ReubenPython2and3ClassObject.my_print("EnableMotors_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def SetAllActuatorsStatesOnOrOffCleanlyFromMainLoop():
    global MyPrint_ReubenPython2and3ClassObject
    #global UR5arm_StopMotion_State_NeedsToBeChangedFlag

    #UR5arm_StopMotion_State_NeedsToBeChangedFlag = 1

    MyPrint_ReubenPython2and3ClassObject.my_print("SetAllActuatorsStatesOnOrOffCleanlyFromMainLoop event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateGUItabObjectsOrderedDict():

    global USE_WiFiVINTthumbstick_FLAG
    global WiFiVINTthumbstick_OPEN_FLAG
    global SHOW_IN_GUI_WiFiVINTthumbstick_FLAG

    global USE_RoboteqBLDCcontroller_FLAG_0
    global RoboteqBLDCcontroller_OPEN_FLAG_0
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0

    global USE_RoboteqBLDCcontroller_FLAG_1
    global RoboteqBLDCcontroller_OPEN_FLAG_1
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1

    global USE_SpatialPrecision333_FLAG
    global SpatialPrecision333_OPEN_FLAG
    global SHOW_IN_GUI_SpatialPrecision333_FLAG

    global USE_Keyboard_FLAG
    global Keyboard_OPEN_FLAG
    global SHOW_IN_GUI_Keyboard_FLAG

    global USE_DC30AmpCurrentSensor_FLAG
    global DC30AmpCurrentSensor_OPEN_FLAG
    global SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG

    global USE_MyPrint_FLAG
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global GUItabObjectsOrderedDict

    try:

        ###########################################################
        ###########################################################
        if len(GUItabObjectsOrderedDict) == 0: #Not yet populated
            GUItabObjectsOrderedDict = OrderedDict([("MainControls", dict([("UseFlag", 1), ("ShowFlag", 1), ("GUItabObjectName", "MainControls"), ("GUItabNameToDisplay", "MainControls"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                    ("WiFiVINTthumbstick", dict([("UseFlag", USE_WiFiVINTthumbstick_FLAG), ("ShowFlag", SHOW_IN_GUI_WiFiVINTthumbstick_FLAG), ("GUItabObjectName", "WiFiVINTthumbstick"), ("GUItabNameToDisplay", "Joystick"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("RoboteqBLDCcontroller_0", dict([("UseFlag", USE_RoboteqBLDCcontroller_FLAG_0), ("ShowFlag", SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0), ("GUItabObjectName", "RoboteqBLDCcontroller_0"), ("GUItabNameToDisplay", "Roboteq0"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("RoboteqBLDCcontroller_1", dict([("UseFlag", USE_RoboteqBLDCcontroller_FLAG_1), ("ShowFlag", SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1), ("GUItabObjectName", "RoboteqBLDCcontroller_1"), ("GUItabNameToDisplay", "Roboteq1"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("SpatialPrecision333", dict([("UseFlag", USE_SpatialPrecision333_FLAG), ("ShowFlag", SHOW_IN_GUI_SpatialPrecision333_FLAG), ("GUItabObjectName", "SpatialPrecision333"), ("GUItabNameToDisplay", "Spatial"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("Keyboard", dict([("UseFlag", USE_Keyboard_FLAG), ("ShowFlag", SHOW_IN_GUI_Keyboard_FLAG), ("GUItabObjectName", "Keyboard"), ("GUItabNameToDisplay", "Keyboard"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("DC30AmpCurrentSensor", dict([("UseFlag", USE_DC30AmpCurrentSensor_FLAG),  ("ShowFlag", SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG), ("GUItabObjectName", "DC30AmpCurrentSensor"), ("GUItabNameToDisplay", "Current"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("MyPrint", dict([("UseFlag", USE_MyPrint_FLAG), ("ShowFlag", SHOW_IN_GUI_MyPrint_FLAG), ("GUItabObjectName", "MyPrint"), ("GUItabNameToDisplay", "MyPrint"), ("IsTabCreatedFlag", 0), ("TabObject", None)]))])
        ###########################################################
        ###########################################################

        ###########################################################
        ###########################################################
        GUItabObjectsOrderedDict["MainControls"]["OpenFlag"] = 1
        GUItabObjectsOrderedDict["WiFiVINTthumbstick"]["OpenFlag"] = WiFiVINTthumbstick_OPEN_FLAG
        GUItabObjectsOrderedDict["RoboteqBLDCcontroller_0"]["OpenFlag"] = RoboteqBLDCcontroller_OPEN_FLAG_0
        GUItabObjectsOrderedDict["RoboteqBLDCcontroller_1"]["OpenFlag"] = RoboteqBLDCcontroller_OPEN_FLAG_1
        GUItabObjectsOrderedDict["SpatialPrecision333"]["OpenFlag"] = SpatialPrecision333_OPEN_FLAG
        GUItabObjectsOrderedDict["Keyboard"]["OpenFlag"] = Keyboard_OPEN_FLAG
        GUItabObjectsOrderedDict["DC30AmpCurrentSensor"]["OpenFlag"] = DC30AmpCurrentSensor_OPEN_FLAG
        GUItabObjectsOrderedDict["MyPrint"]["OpenFlag"] = MyPrint_OPEN_FLAG
        ###########################################################
        ###########################################################

        print("UpdateGUItabObjectsOrderedDict, GUItabObjectsOrderedDict: " + str(GUItabObjectsOrderedDict))

    except:
        exceptions = sys.exc_info()[0]
        print("UpdateGUItabObjectsOrderedDict, exceptions: %s" % exceptions)
        traceback.print_exc()

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
if __name__ == '__main__':

    ################################################
    ################################################
    global EXIT_PROGRAM_FLAG
    EXIT_PROGRAM_FLAG = 0
    ################################################
    ################################################

    ################################################
    ################################################
    global my_platform
    global ParametersToBeLoaded_Directory_TO_BE_USED
    global LogFile_Directory_TO_BE_USED

    my_platform = GetMyPlatform()

    if my_platform == "windows":
        ParametersToBeLoaded_Directory_TO_BE_USED = ParametersToBeLoaded_Directory_Windows
        LogFile_Directory_TO_BE_USED = LogFile_Directory_Windows

    elif my_platform == "pi":
        ParametersToBeLoaded_Directory_TO_BE_USED = ParametersToBeLoaded_Directory_RaspberryPi
        LogFile_Directory_TO_BE_USED = LogFile_Directory_RaspberryPi

    elif my_platform == "linux":
        ParametersToBeLoaded_Directory_TO_BE_USED = ParametersToBeLoaded_Directory_LinuxNonRaspberryPi
        LogFile_Directory_TO_BE_USED = LogFile_Directory_LinuxNonRaspberryPi

    elif my_platform == "mac":
        ParametersToBeLoaded_Directory_TO_BE_USED = ParametersToBeLoaded_Directory_Mac
        LogFile_Directory_TO_BE_USED = LogFile_Directory_Mac

    else:
        "SelfBalancingRobot1.py: ERROR, OS must be Windows, LinuxNonRaspberryPi, or Mac!"
        ExitProgram_Callback()

    print("ParametersToBeLoaded_Directory_TO_BE_USED: " + ParametersToBeLoaded_Directory_TO_BE_USED)
    print("LogFile_Directory_TO_BE_USED: " + LogFile_Directory_TO_BE_USED)
    ################################################
    ################################################

    ################################################
    ################################################
    global USE_GUI_FLAG_ARGV_OVERRIDE
    global SOFTWARE_LAUNCH_METHOD

    [USE_GUI_FLAG_ARGV_OVERRIDE, SOFTWARE_LAUNCH_METHOD] =  ParseARGV_USE_GUI_and_SOFTWARE_LAUNCH_METHOD()

    print("SelfBalancingRobot1, USE_GUI_FLAG_ARGV_OVERRIDE: " + str(USE_GUI_FLAG_ARGV_OVERRIDE) + ", SOFTWARE_LAUNCH_METHOD: " + str(SOFTWARE_LAUNCH_METHOD))

    '''
    if SOFTWARE_LAUNCH_METHOD == -1:
        print("SelfBalancingRobot1 ERROR, must launch software via command terminal/BAT-file, not IDE!")
        time.sleep(5.0)
        sys.exit()
    '''
    ################################################
    ################################################

    ################################################
    ################################################
    AMflag = IsTheTimeCurrentlyAM()
    if AMflag == 1:
        AMorPMstring = "AM"
    else:
        AMorPMstring = "PM"

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print("Starting 'SelfBalancingRobot1.py' at " + getTimeStampString() + AMorPMstring)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    ################################################
    ################################################

    #################################################
    #################################################
    global JSONfiles_NeedsToBeLoadedFlag
    JSONfiles_NeedsToBeLoadedFlag = 0

    #################################################
    global UseAndShowFlags_Directions
    global USE_RoboteqBLDCcontroller_FLAG_0
    global USE_RoboteqBLDCcontroller_FLAG_1
    global USE_WiFiVINTthumbstick_FLAG
    global USE_SpatialPrecision333_FLAG
    global USE_DC30AmpCurrentSensor_FLAG
    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    global USE_MyPrint_FLAG
    global USE_Keyboard_FLAG
    global USE_GUI_FLAG
    global USE_SINUSOIDAL_CONTROL_INPUT_FLAG
    global USE_PITCH_PID_FLAG
    global USE_PITCH_LQR_FLAG
    global ENABLE_MOTORS_AT_STARTUP_FLAG
    global SAVE_PROGRAM_LOGS_FLAG

    LoadAndParseJSONfile_UseClassesFlags()
    #################################################

    #################################################
    global GUIsettings_Directions

    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0
    global SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1
    global SHOW_IN_GUI_WiFiVINTthumbstick_FLAG
    global SHOW_IN_GUI_SpatialPrecision333_FLAG
    global SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG
    global SHOW_IN_GUI_Keyboard_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG
    global SHOW_IN_GUI_MyPlotterPureTkinterStandAloneProcess_FLAG
    global SHOW_IN_GUI_PID_TUNING_ENTRIES_FLAG

    global GUItitleString
    global GUI_RootAfterCallbackInterval_Milliseconds
    global root_Xpos
    global root_Ypos
    global root_width
    global root_height
    global GUIbuttonWidth
    global GUIbuttonPadX
    global GUIbuttonPadY
    global GUIbuttonFontSize

    global GUI_ROW_RoboteqBLDCcontroller_0
    global GUI_COLUMN_RoboteqBLDCcontroller_0
    global GUI_PADX_RoboteqBLDCcontroller_0
    global GUI_PADY_RoboteqBLDCcontroller_0
    global GUI_ROWSPAN_RoboteqBLDCcontroller_0
    global GUI_COLUMNSPAN_RoboteqBLDCcontroller_0

    global GUI_ROW_RoboteqBLDCcontroller_1
    global GUI_COLUMN_RoboteqBLDCcontroller_1
    global GUI_PADX_RoboteqBLDCcontroller_1
    global GUI_PADY_RoboteqBLDCcontroller_1
    global GUI_ROWSPAN_RoboteqBLDCcontroller_1
    global GUI_COLUMNSPAN_RoboteqBLDCcontroller_1

    global GUI_ROW_WiFiVINTthumbstick
    global GUI_COLUMN_WiFiVINTthumbstick
    global GUI_PADX_WiFiVINTthumbstick
    global GUI_PADY_WiFiVINTthumbstick
    global GUI_ROWSPAN_WiFiVINTthumbstick
    global GUI_COLUMNSPAN_WiFiVINTthumbstick

    global GUI_ROW_SpatialPrecision333
    global GUI_COLUMN_SpatialPrecision333
    global GUI_PADX_SpatialPrecision333
    global GUI_PADY_SpatialPrecision333
    global GUI_ROWSPAN_SpatialPrecision333
    global GUI_COLUMNSPAN_SpatialPrecision333

    global GUI_ROW_DC30AmpCurrentSensor
    global GUI_COLUMN_DC30AmpCurrentSensor
    global GUI_PADX_DC30AmpCurrentSensor
    global GUI_PADY_DC30AmpCurrentSensor
    global GUI_ROWSPAN_DC30AmpCurrentSensor
    global GUI_COLUMNSPAN_DC30AmpCurrentSensor

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint

    LoadAndParseJSONfile_GUIsettings()
    #################################################

    #################################################
    global MyPlotterPureTkinterStandAloneProcess_Directions
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict
    global MyPlotterPureTkinterStandAloneProcess_RefreshDurationInSeconds

    LoadAndParseJSONfile_MyPlotterPureTkinterStandAloneProcess()
    #################################################

    #################################################
    global RoboteqBLDCcontroller_Directions_0
    global RoboteqBLDCcontroller_NameToDisplay_UserSet_0
    global RoboteqBLDCcontroller_DesiredSerialNumber_USBtoSerialConverter_0
    global RoboteqBLDCcontroller_ControlMode_Starting_0
    global RoboteqBLDCcontroller_Position_Target_Min_UserSet_0
    global RoboteqBLDCcontroller_Position_Target_Max_UserSet_0
    global RoboteqBLDCcontroller_Position_Target_Starting_0
    global RoboteqBLDCcontroller_Speed_Target_Min_UserSet_0
    global RoboteqBLDCcontroller_Speed_Target_Max_UserSet_0
    global RoboteqBLDCcontroller_Speed_Target_Starting_0
    global RoboteqBLDCcontroller_Acceleration_Target_Min_UserSet_0
    global RoboteqBLDCcontroller_Acceleration_Target_Max_UserSet_0
    global RoboteqBLDCcontroller_Acceleration_Target_Starting_0
    global RoboteqBLDCcontroller_Current_Amps_Min_UserSet_0
    global RoboteqBLDCcontroller_Current_Amps_Max_UserSet_0
    global RoboteqBLDCcontroller_Current_Amps_Starting_0
    global RoboteqBLDCcontroller_Torque_Amps_Min_UserSet_0
    global RoboteqBLDCcontroller_Torque_Amps_Max_UserSet_0
    global RoboteqBLDCcontroller_Torque_Amps_Starting_0
    global RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_0
    global RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_0
    global RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_0
    global RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_0
    global RoboteqBLDCcontroller_NumberOfMagnetsInMotor_0
    global RoboteqBLDCcontroller_PID_Kp_0
    global RoboteqBLDCcontroller_PID_Ki_0
    global RoboteqBLDCcontroller_PID_Kd_0
    global RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_0
    global RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_0

    LoadAndParseJSONfile_RoboteqBLDCcontroller_0()
    #################################################

    #################################################
    global RoboteqBLDCcontroller_Directions_1
    global RoboteqBLDCcontroller_NameToDisplay_UserSet_1
    global RoboteqBLDCcontroller_DesiredSerialNumber_USBtoSerialConverter_1
    global RoboteqBLDCcontroller_ControlMode_Starting_1
    global RoboteqBLDCcontroller_Position_Target_Min_UserSet_1
    global RoboteqBLDCcontroller_Position_Target_Max_UserSet_1
    global RoboteqBLDCcontroller_Position_Target_Starting_1
    global RoboteqBLDCcontroller_Speed_Target_Min_UserSet_1
    global RoboteqBLDCcontroller_Speed_Target_Max_UserSet_1
    global RoboteqBLDCcontroller_Speed_Target_Starting_1
    global RoboteqBLDCcontroller_Acceleration_Target_Min_UserSet_1
    global RoboteqBLDCcontroller_Acceleration_Target_Max_UserSet_1
    global RoboteqBLDCcontroller_Acceleration_Target_Starting_1
    global RoboteqBLDCcontroller_Current_Amps_Min_UserSet_1
    global RoboteqBLDCcontroller_Current_Amps_Max_UserSet_1
    global RoboteqBLDCcontroller_Current_Amps_Starting_1
    global RoboteqBLDCcontroller_Torque_Amps_Min_UserSet_1
    global RoboteqBLDCcontroller_Torque_Amps_Max_UserSet_1
    global RoboteqBLDCcontroller_Torque_Amps_Starting_1
    global RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_1
    global RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_1
    global RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_1
    global RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_1
    global RoboteqBLDCcontroller_NumberOfMagnetsInMotor_1
    global RoboteqBLDCcontroller_PID_Kp_1
    global RoboteqBLDCcontroller_PID_Ki_1
    global RoboteqBLDCcontroller_PID_Kd_1
    global RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_1
    global RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_1

    LoadAndParseJSONfile_RoboteqBLDCcontroller_1()
    #################################################

    #################################################
    global WiFiVINTthumbstick_Directions
    global WiFiVINTthumbstick_VINT_DesiredSerialNumber
    global WiFiVINTthumbstick_VINT_DesiredPortNumber
    global WiFiVINTthumbstick_DesiredDeviceID
    global WiFiVINTthumbstick_WaitForAttached_TimeoutDuration_Milliseconds
    global WiFiVINTthumbstick_NameToDisplay_UserSet
    global WiFiVINTthumbstick_UsePhidgetsLoggingInternalToThisClassObjectFlag
    global WiFiVINTthumbstick_MainThread_TimeToSleepEachLoop
    global WiFiVINTthumbstick_UpdateDeltaT_ms
    global WiFiVINTthumbstick_WirelessVINThub_ServerName_Str
    global WiFiVINTthumbstick_WirelessVINThub_Address_Str
    global WiFiVINTthumbstick_WirelessVINThub_Port_Int
    global WiFiVINTthumbstick_WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str
    global WiFiVINTthumbstick_WirelessVINThub_Flags_Int
    global WiFiVINTthumbstick_VoltageRatioInput0Object_SteadyStateOffset
    global WiFiVINTthumbstick_VoltageRatioInput1Object_SteadyStateOffset
    global WiFiVINTthumbstick_VoltageRatioInput0Object_LowPassFilter_Lambda
    global WiFiVINTthumbstick_VoltageRatioInput1Object_LowPassFilter_Lambda

    LoadAndParseJSONfile_WiFiVINTthumbstick()
    #################################################

    #################################################
    global SpatialPrecision333_Directions
    global SpatialPrecision333_DesiredSerialNumber
    global SpatialPrecision333_WaitForAttached_TimeoutDuration_Milliseconds
    global SpatialPrecision333_NameToDisplay_UserSet
    global SpatialPrecision333_UsePhidgetsLoggingInternalToThisClassObjectFlag
    global SpatialPrecision333_SpatialAlgorithm
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_Spatial_CallbackUpdateDeltaTmilliseconds
    global SpatialPrecision333_DataCollectionDurationInSecondsForSnapshottingAndZeroing
    global SpatialPrecision333_MainThread_TimeToSleepEachLoop
    global SpatialPrecision333_HeatingEnabledToStabilizeSensorTemperature

    LoadAndParseJSONfile_SpatialPrecision333()
    #################################################

    #################################################
    global Keyboard_Directions
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts

    LoadAndParseJSONfile_Keyboard()
    KeyboardMapKeysToCallbackFunctions()
    #################################################

    #################################################
    global DC30AmpCurrentSensor_Directions
    global DC30AmpCurrentSensor_VINT_DesiredSerialNumber
    global DC30AmpCurrentSensor_VINT_DesiredPortNumber
    global DC30AmpCurrentSensor_DesiredDeviceID
    global DC30AmpCurrentSensor_WaitForAttached_TimeoutDuration_Milliseconds
    global DC30AmpCurrentSensor_NameToDisplay_UserSet
    global DC30AmpCurrentSensor_UsePhidgetsLoggingInternalToThisClassObjectFlag
    global DC30AmpCurrentSensor_DataCallbackUpdateDeltaT_ms
    global DC30AmpCurrentSensor_CurrentSensorList_Current_Amps_ExponentialFilterLambda
    
    LoadAndParseJSONfile_DC30AmpCurrentSensor()
    #################################################

    #################################################
    global ControlType_StartingValue
    global ControlType_AcceptableValues
    global SelfBalancingRobot1_MainThread_TimeToSleepEachLoop

    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseMedianFilterFlag
    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseExponentialSmoothingFilterFlag
    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda

    global LQR_ParametersToBeLoaded_Directions
    global LQR_PitchControl_GainVectorElement_Ktheta_0
    global LQR_PitchControl_GainVectorElement_Ktheta_1
    global LQR_PitchControl_GainVectorElement_Ktheta_2
    global LQR_PitchControl_GainVectorElement_Ktheta_3
    global LQR_YawControl_GainVectorElement_Kdelta_0
    global LQR_YawControl_GainVectorElement_Kdelta_1
    global Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION

    global Pitch_ParametersToBeLoaded_Directions
    global Pitch_PosControl_PID_gain_Kp
    global Pitch_PosControl_PID_gain_Ki
    global Pitch_PosControl_PID_gain_Kd
    global Pitch_PosControl_PID_ErrorSum_Max

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    global SINUSOIDAL_MOTION_INPUT_MinValue
    global SINUSOIDAL_MOTION_INPUT_MaxValue

    LoadAndParseJSONfile_ControlLawParameters()

    if ControlType_StartingValue not in ControlType_AcceptableValues:
        print("ERROR: ControlType_StartingValue but be in " + str(ControlType_AcceptableValues))
    #################################################

    #################################################
    global RobotModelParameters_UserNotes
    global RobotModelParameters_Mp_MassOfChassisBodyInKG
    global RobotModelParameters_Mr_MassOfRotatingMassesConnecetedToLeftAndRightWheelsInKG
    global RobotModelParameters_L_DistanceBetweenAxisAndCGofChassisOrHeightOfCGaboveWheelAxisInMeters
    global RobotModelParameters_D_LateralDistanceBetweenWheelContactPatchesInMeters
    global RobotModelParameters_R_RadiusOfWheelInMeters
    global RobotModelParameters_g_GravityInMetersPerSecondSquared

    LoadAndParseJSONfile_RobotModelParameters()
    #################################################

    #################################################
    #################################################
    global root
    root = None

    global ControlType
    ControlType = ControlType_StartingValue

    global ControlType_NeedsToBeChangedFlag
    ControlType_NeedsToBeChangedFlag = 0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0

    global RoboteqBLDCcontroller_OPEN_FLAG_0
    RoboteqBLDCcontroller_OPEN_FLAG_0 = -1

    global RoboteqBLDCcontroller_MostRecentDict_0
    RoboteqBLDCcontroller_MostRecentDict_0 = dict()

    global RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_0
    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_0
    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_0 = -11111.0

    '''
    global RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_0
    RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_0
    RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_0
    RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_0 = -11111.0
    '''

    global RoboteqBLDCcontroller_MostRecentDict_FaultFlags_0
    RoboteqBLDCcontroller_MostRecentDict_FaultFlags_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0
    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Radians_0
    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_0
    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Time_0
    RoboteqBLDCcontroller_MostRecentDict_Time_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_0
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_0
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Kp_0
    RoboteqBLDCcontroller_MostRecentDict_PID_Kp_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Ki_0
    RoboteqBLDCcontroller_MostRecentDict_PID_Ki_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Kd_0
    RoboteqBLDCcontroller_MostRecentDict_PID_Kd_0 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_0
    RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_0 = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_0
    RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_0 = -11111

    global RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_0
    RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_0 = "unknown"
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1

    global RoboteqBLDCcontroller_OPEN_FLAG_1
    RoboteqBLDCcontroller_OPEN_FLAG_1 = -1

    global RoboteqBLDCcontroller_MostRecentDict_1
    RoboteqBLDCcontroller_MostRecentDict_1 = dict()

    global RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_1
    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1
    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1 = -11111.0

    '''
    global RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_1
    RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_1
    RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_1
    RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_1 = -11111.0
    '''

    global RoboteqBLDCcontroller_MostRecentDict_FaultFlags_1
    RoboteqBLDCcontroller_MostRecentDict_FaultFlags_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1
    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1
    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1
    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Time_1
    RoboteqBLDCcontroller_MostRecentDict_Time_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_1
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_1
    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Kp_1
    RoboteqBLDCcontroller_MostRecentDict_PID_Kp_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Ki_1
    RoboteqBLDCcontroller_MostRecentDict_PID_Ki_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_Kd_1
    RoboteqBLDCcontroller_MostRecentDict_PID_Kd_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_1
    RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_1 = -11111.0
    
    global RoboteqBLDCcontroller_MostRecentDict_ControlModeOfOperationIntegerValue_1
    RoboteqBLDCcontroller_MostRecentDict_ControlModeOfOperationIntegerValue_1 = -11111.0

    global RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_1
    RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_1 = -11111

    global RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_1
    RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_1 = "unknown"
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject

    global WiFiVINTthumbstick_OPEN_FLAG
    WiFiVINTthumbstick_OPEN_FLAG = -1

    global WiFiVINTthumbstick_MostRecentDict
    WiFiVINTthumbstick_MostRecentDict = dict()

    global WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio
    WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio
    WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_DigitalInput0Object_State
    WiFiVINTthumbstick_MostRecentDict_DigitalInput0Object_State = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback
    WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback
    WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = -11111.0

    global WiFiVINTthumbstick_MostRecentDict_Time
    WiFiVINTthumbstick_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject

    global SpatialPrecision333_OPEN_FLAG
    SpatialPrecision333_OPEN_FLAG = -1

    global SpatialPrecision333_MostRecentDict
    SpatialPrecision333_MostRecentDict = dict()

    global SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler
    SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler = [-11111.0]*4

    global SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict
    SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict = dict([("RollPitchYaw_AbtXYZ_List_Degrees",[-11111.0]*3),("RollPitchYaw_AbtXYZ_List_Radians",[-11111.0]*3)])

    global SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict
    SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict = dict([("RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond",[-11111.0]*3),("RollPitchYaw_Rate_AbtXYZ_List_RadiansPerSecond",[-11111.0]*3)])

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0

    global SpatialPrecision333_MostRecentDict_Time
    SpatialPrecision333_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject

    global DC30AmpCurrentSensor_OPEN_FLAG
    DC30AmpCurrentSensor_OPEN_FLAG = -1

    global DC30AmpCurrentSensor_MostRecentDict
    DC30AmpCurrentSensor_MostRecentDict = dict()

    global DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Raw
    DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Raw = [-11111.0]*1

    global DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Filtered
    DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Filtered = [-11111.0]*1

    global DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag
    DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag = [-1]*1

    global DC30AmpCurrentSensor_MostRecentDict_Time
    DC30AmpCurrentSensor_MostRecentDict_Time = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject

    global MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG
    MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = -1

    global MyPlotterPureTkinterStandAloneProcess_MostRecentDict
    MyPlotterPureTkinterStandAloneProcess_MostRecentDict = dict()

    global MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = -1

    global LastTime_CalculatedFromMainThread_PLOTTER
    LastTime_CalculatedFromMainThread_PLOTTER = -11111.0
    #################################################
    #################################################

    #################################################
    #################################################
    global Keyboard_OPEN_FLAG
    Keyboard_OPEN_FLAG = 0

    global DedicatedKeyboardListeningThread_StillRunningFlag
    DedicatedKeyboardListeningThread_StillRunningFlag = 0

    global CurrentTime_CalculatedFromDedicatedKeyboardListeningThread
    CurrentTime_CalculatedFromDedicatedKeyboardListeningThread = -11111.0

    global StartingTime_CalculatedFromDedicatedKeyboardListeningThread
    StartingTime_CalculatedFromDedicatedKeyboardListeningThread = -11111.0

    global LastTime_CalculatedFromDedicatedKeyboardListeningThread
    LastTime_CalculatedFromDedicatedKeyboardListeningThread = -11111.0

    global DataStreamingFrequency_CalculatedFromDedicatedKeyboardListeningThread
    DataStreamingFrequency_CalculatedFromDedicatedKeyboardListeningThread = -11111.0

    global DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread
    DataStreamingDeltaT_CalculatedFromDedicatedKeyboardListeningThread = -11111.0

    global DedicatedKeyboardListeningThread_TimeToSleepEachLoop
    DedicatedKeyboardListeningThread_TimeToSleepEachLoop = 0.020

    global BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace
    BeepNeedsToBePlayedFlag_RecordNewWaypoint_JointSpace = 0

    global BeepNeedsToBePlayedFlag_RecordNewWaypoint_CartesianSpace
    BeepNeedsToBePlayedFlag_RecordNewWaypoint_CartesianSpace = 0

    global KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag
    KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag = 0

    global KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag
    KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag = 0

    global KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag
    KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag = 0

    global KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag
    KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag = 0

    global KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag
    KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag = 0

    global KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag
    KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag = 0

    global Keyboard_AddToUR5armCurrentPositionList
    Keyboard_AddToUR5armCurrentPositionList = [-11111.0] * 6

    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts
    Keyboard_KeysToTeleopControlsMapping_DictOfDicts = dict()
    #################################################
    #################################################

    #################################################
    #################################################
    global LoopCounter_CalculatedFromMainThread
    LoopCounter_CalculatedFromMainThread = 0

    global CurrentTime_CalculatedFromMainThread
    CurrentTime_CalculatedFromMainThread = -11111.0

    global StartingTime_CalculatedFromMainThread
    StartingTime_CalculatedFromMainThread = -11111.0

    global LastTime_CalculatedFromMainThread
    LastTime_CalculatedFromMainThread = -11111.0

    global DataStreamingFrequency_CalculatedFromMainThread
    DataStreamingFrequency_CalculatedFromMainThread = -1

    global DataStreamingDeltaT_CalculatedFromMainThread
    DataStreamingDeltaT_CalculatedFromMainThread = -1
    #################################################
    #################################################
    
    #################################################
    #################################################
    global LoopCounter_CalculatedFromGUIthread
    LoopCounter_CalculatedFromGUIthread = 0

    global CurrentTime_CalculatedFromGUIthread
    CurrentTime_CalculatedFromGUIthread = -11111.0

    global StartingTime_CalculatedFromGUIthread
    StartingTime_CalculatedFromGUIthread = -11111.0

    global LastTime_CalculatedFromGUIthread
    LastTime_CalculatedFromGUIthread = -11111.0

    global DataStreamingFrequency_CalculatedFromGUIthread
    DataStreamingFrequency_CalculatedFromGUIthread = -1

    global DataStreamingDeltaT_CalculatedFromGUIthread
    DataStreamingDeltaT_CalculatedFromGUIthread = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global SINUSOIDAL_INPUT_TO_COMMAND
    SINUSOIDAL_INPUT_TO_COMMAND = 0.0

    global Theta_RL_Actual
    Theta_RL_Actual = -11111

    global Theta_RR_Actual
    Theta_RR_Actual = -11111

    global Omega_RL_Actual
    Omega_RL_Actual = -11111

    global Omega_RR_Actual
    Omega_RR_Actual = -11111

    global Position_X_RM_Meters_Actual
    Position_X_RM_Meters_Actual = 0.0

    global Position_X_RMC_Meters_Commanded
    Position_X_RMC_Meters_Commanded = 0.0

    global Velocity_V_RM_MetersPerSec_Actual
    Velocity_V_RM_MetersPerSec_Actual = -11111

    global Velocity_V_RM_MetersPerSec_Actual_UNFILTERED
    Velocity_V_RM_MetersPerSec_Actual_UNFILTERED = -11111

    global Velocity_V_RMC_MetersPerSec_Commanded
    Velocity_V_RMC_MetersPerSec_Commanded = 0.0

    global YawAngle_Delta_Deg_Actual
    YawAngle_Delta_Deg_Actual = -11111

    global YawAngle_Delta_Deg_Commanded
    YawAngle_Delta_Deg_Commanded = 0.0

    global YawAngle_Delta_Radians_Actual
    YawAngle_Delta_Radians_Actual = -11111

    global YawAngle_Delta_Radians_Commanded
    YawAngle_Delta_Radians_Commanded = 0.0

    global YawAngularRate_DeltaDot_RadiansPerSec_Actual
    YawAngularRate_DeltaDot_RadiansPerSec_Actual = -11111

    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded
    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0

    global PitchAngle_Theta_Deg_Actual
    PitchAngle_Theta_Deg_Actual = -11111.0

    global PitchAngle_Theta_Radians_Actual
    PitchAngle_Theta_Radians_Actual = -11111.0

    global PitchAngle_Theta_Deg_Commanded
    PitchAngle_Theta_Deg_Commanded = 0.0

    global PitchAngle_Theta_Radians_Commanded
    PitchAngle_Theta_Radians_Commanded = 0.0

    global PitchAngularRate_ThetaDot_DegPerSec_Actual
    PitchAngularRate_ThetaDot_DegPerSec_Actual = -11111.0

    global PitchAngularRate_ThetaDot_RadiansPerSec_Actual
    PitchAngularRate_ThetaDot_RadiansPerSec_Actual = -11111.0

    global PitchAngularRate_ThetaDot_RadiansPerSec_Commanded
    PitchAngularRate_ThetaDot_RadiansPerSec_Commanded = 0.0

    global C_L
    C_L = -11111.0

    global C_R
    C_R = -11111.0

    global C_Theta
    C_Theta = -11111.0

    global C_Delta
    C_Delta = -11111.0

    global TorqueToBeCommanded_Motor0
    TorqueToBeCommanded_Motor0 = 0.0

    global TorqueToBeCommanded_Motor1
    TorqueToBeCommanded_Motor1 = 0.0

    global Odrive_DifferentiatingPositionEstimateRxFromOdriveToGiveJointAngularVelocity_RevPerSec_Motor0
    Odrive_DifferentiatingPositionEstimateRxFromOdriveToGiveJointAngularVelocity_RevPerSec_Motor0 = -11111.0

    global Odrive_DifferentiatingPositionEstimateRxFromOdriveToGiveJointAngularVelocity_RevPerSec_Motor1
    Odrive_DifferentiatingPositionEstimateRxFromOdriveToGiveJointAngularVelocity_RevPerSec_Motor1 = -11111.0

    global Pitch_PosControl_PID_Error
    Pitch_PosControl_PID_Error = 0

    global Pitch_PosControl_PID_Error_last
    Pitch_PosControl_PID_Error_last = 0

    global Pitch_PosControl_PID_ErrorSum
    Pitch_PosControl_PID_ErrorSum = 0

    global Pitch_PosControl_PID_ErrorD
    Pitch_PosControl_PID_ErrorD = 0

    global Pitch_PID_CommandToMotor
    Pitch_PID_CommandToMotor = 0

    global EnableMotors_State
    EnableMotors_State = ENABLE_MOTORS_AT_STARTUP_FLAG
    #################################################
    #################################################

    #################################################
    #################################################
    global GUItabObjectsOrderedDict
    GUItabObjectsOrderedDict = OrderedDict()

    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_Keyboard_FLAG == 1:
        DedicatedKeyboardListeningThread_ThreadingObject = threading.Thread(target=DedicatedKeyboardListeningThread, args=())
        DedicatedKeyboardListeningThread_ThreadingObject.setDaemon(True) #Means that thread is destroyed automatically when the main thread is destroyed.
        DedicatedKeyboardListeningThread_ThreadingObject.start()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################  KEY GUI LINE
    #################################################
    if USE_GUI_FLAG == 1:
        StartingTime_CalculatedFromGUIthread = getPreciseSecondsTimeStampString()
        print("Starting GUI thread...")

        global GUI_Thread_ThreadingObject
        GUI_Thread_ThreadingObject = threading.Thread(target=GUI_Thread)
        GUI_Thread_ThreadingObject.setDaemon(True)  # Should mean that the GUI thread is destroyed automatically when the main thread is destroyed.
        GUI_Thread_ThreadingObject.start()
        time.sleep(0.5)  # Allow enough time for 'root' to be created that we can then pass it into other classes.
    else:
        pass

    #################################################
    #################################################

    #################################################
    #################################################
    global MyPrint_ReubenPython2and3ClassObject_GUIparametersDict
    MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                    ("root", GUItabObjectsOrderedDict["MyPrint"]["TabObject"]),
                                                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                    ("GUI_ROW", GUI_ROW_MyPrint),
                                                                    ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                    ("GUI_PADX", GUI_PADX_MyPrint),
                                                                    ("GUI_PADY", GUI_PADY_MyPrint),
                                                                    ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint),
                                                                    ("GUI_STICKY", "W")])

    global MyPrint_ReubenPython2and3ClassObject_LogFile_Directory_TO_BE_USED
    if SAVE_PROGRAM_LOGS_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject_LogFile_Directory_TO_BE_USED = LogFile_Directory_TO_BE_USED + "//SelfBalancingRobot1_MyPrint_LogFile_" + str(int(round(getPreciseSecondsTimeStampString()))) +  ".txt"
    else:
        MyPrint_ReubenPython2and3ClassObject_LogFile_Directory_TO_BE_USED = "" #Meanings that no log will be save.

    global MyPrint_ReubenPython2and3ClassObject_setup_dict
    MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 20),
                                                            ("WidthOfPrintingLabel", 150),
                                                            ("PrintToConsoleFlag", 1),
                                                            ("LogFileNameFullPath", MyPrint_ReubenPython2and3ClassObject_LogFile_Directory_TO_BE_USED),
                                                            ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

    if USE_MyPrint_FLAG == 1:
        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_0
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_0 = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0),
                                    ("root", GUItabObjectsOrderedDict["RoboteqBLDCcontroller_0"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_RoboteqBLDCcontroller_0),
                                    ("GUI_COLUMN", GUI_COLUMN_RoboteqBLDCcontroller_0),
                                    ("GUI_PADX", GUI_PADX_RoboteqBLDCcontroller_0),
                                    ("GUI_PADY", GUI_PADY_RoboteqBLDCcontroller_0),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_RoboteqBLDCcontroller_0),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_RoboteqBLDCcontroller_0)])

    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_0
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_0 = dict([("GUIparametersDict", RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_0),
                                                                        ("DesiredSerialNumber_USBtoSerialConverter", RoboteqBLDCcontroller_DesiredSerialNumber_USBtoSerialConverter_0),
                                                                        ("NameToDisplay_UserSet", RoboteqBLDCcontroller_NameToDisplay_UserSet_0),
                                                                        ("ControlMode_Starting", RoboteqBLDCcontroller_ControlMode_Starting_0),
                                                                        ("Position_Target_Min_UserSet", RoboteqBLDCcontroller_Position_Target_Min_UserSet_0),
                                                                        ("Position_Target_Max_UserSet", RoboteqBLDCcontroller_Position_Target_Max_UserSet_0),
                                                                        ("Position_Target_Starting", RoboteqBLDCcontroller_Position_Target_Starting_0),
                                                                        ("Speed_Target_Min_UserSet", RoboteqBLDCcontroller_Speed_Target_Min_UserSet_0),
                                                                        ("Speed_Target_Max_UserSet", RoboteqBLDCcontroller_Speed_Target_Max_UserSet_0),
                                                                        ("Speed_Target_Starting", RoboteqBLDCcontroller_Speed_Target_Starting_0),
                                                                        ("Acceleration_Target_Min_UserSet", RoboteqBLDCcontroller_Acceleration_Target_Min_UserSet_0),
                                                                        ("Acceleration_Target_Max_UserSet", RoboteqBLDCcontroller_Acceleration_Target_Max_UserSet_0),
                                                                        ("Acceleration_Target_Starting", RoboteqBLDCcontroller_Acceleration_Target_Starting_0),
                                                                        ("Current_Amps_Min_UserSet", RoboteqBLDCcontroller_Current_Amps_Min_UserSet_0),
                                                                        ("Current_Amps_Max_UserSet", RoboteqBLDCcontroller_Current_Amps_Max_UserSet_0),
                                                                        ("Current_Amps_Starting", RoboteqBLDCcontroller_Current_Amps_Starting_0),
                                                                        ("Torque_Amps_Min_UserSet", RoboteqBLDCcontroller_Torque_Amps_Min_UserSet_0),
                                                                        ("Torque_Amps_Max_UserSet", RoboteqBLDCcontroller_Torque_Amps_Max_UserSet_0),
                                                                        ("Torque_Amps_Starting", RoboteqBLDCcontroller_Torque_Amps_Starting_0),
                                                                        ("DedicatedRxThread_TimeToSleepEachLoop", RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_0),
                                                                        ("DedicatedTxThread_TimeToSleepEachLoop", RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_0),
                                                                        ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_0),
                                                                        ("HeartbeatTimeIntervalMilliseconds", RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_0),
                                                                        ("NumberOfMagnetsInMotor", RoboteqBLDCcontroller_NumberOfMagnetsInMotor_0),
                                                                        ("RoboteqBLDCcontroller_PID_Kp_0", RoboteqBLDCcontroller_PID_Kp_0),
                                                                        ("RoboteqBLDCcontroller_PID_Ki_0", RoboteqBLDCcontroller_PID_Ki_0),
                                                                        ("RoboteqBLDCcontroller_PID_Kd_0", RoboteqBLDCcontroller_PID_Kd_0),
                                                                        ("RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_0", RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_0),
                                                                        ("SetBrushlessCounterTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_0)])

    if USE_RoboteqBLDCcontroller_FLAG_0 == 1:
        try:
            RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0 = RoboteqBLDCcontroller_ReubenPython2and3Class(RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_0)
            RoboteqBLDCcontroller_OPEN_FLAG_0 = RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0 __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_1
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_1 = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1),
                                    ("root", GUItabObjectsOrderedDict["RoboteqBLDCcontroller_1"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_RoboteqBLDCcontroller_1),
                                    ("GUI_COLUMN", GUI_COLUMN_RoboteqBLDCcontroller_1),
                                    ("GUI_PADX", GUI_PADX_RoboteqBLDCcontroller_1),
                                    ("GUI_PADY", GUI_PADY_RoboteqBLDCcontroller_1),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_RoboteqBLDCcontroller_1),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_RoboteqBLDCcontroller_1)])

    global RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_1
    RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_1 = dict([("GUIparametersDict", RoboteqBLDCcontroller_ReubenPython2and3ClassObject_GUIparametersDict_1),
                                                                        ("DesiredSerialNumber_USBtoSerialConverter", RoboteqBLDCcontroller_DesiredSerialNumber_USBtoSerialConverter_1),
                                                                        ("NameToDisplay_UserSet", RoboteqBLDCcontroller_NameToDisplay_UserSet_1),
                                                                        ("ControlMode_Starting", RoboteqBLDCcontroller_ControlMode_Starting_1),
                                                                        ("Position_Target_Min_UserSet", RoboteqBLDCcontroller_Position_Target_Min_UserSet_1),
                                                                        ("Position_Target_Max_UserSet", RoboteqBLDCcontroller_Position_Target_Max_UserSet_1),
                                                                        ("Position_Target_Starting", RoboteqBLDCcontroller_Position_Target_Starting_1),
                                                                        ("Speed_Target_Min_UserSet", RoboteqBLDCcontroller_Speed_Target_Min_UserSet_1),
                                                                        ("Speed_Target_Max_UserSet", RoboteqBLDCcontroller_Speed_Target_Max_UserSet_1),
                                                                        ("Speed_Target_Starting", RoboteqBLDCcontroller_Speed_Target_Starting_1),
                                                                        ("Acceleration_Target_Min_UserSet", RoboteqBLDCcontroller_Acceleration_Target_Min_UserSet_1),
                                                                        ("Acceleration_Target_Max_UserSet", RoboteqBLDCcontroller_Acceleration_Target_Max_UserSet_1),
                                                                        ("Acceleration_Target_Starting", RoboteqBLDCcontroller_Acceleration_Target_Starting_1),
                                                                        ("Current_Amps_Min_UserSet", RoboteqBLDCcontroller_Current_Amps_Min_UserSet_1),
                                                                        ("Current_Amps_Max_UserSet", RoboteqBLDCcontroller_Current_Amps_Max_UserSet_1),
                                                                        ("Current_Amps_Starting", RoboteqBLDCcontroller_Current_Amps_Starting_1),
                                                                        ("Torque_Amps_Min_UserSet", RoboteqBLDCcontroller_Torque_Amps_Min_UserSet_1),
                                                                        ("Torque_Amps_Max_UserSet", RoboteqBLDCcontroller_Torque_Amps_Max_UserSet_1),
                                                                        ("Torque_Amps_Starting", RoboteqBLDCcontroller_Torque_Amps_Starting_1),
                                                                        ("DedicatedRxThread_TimeToSleepEachLoop", RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_1),
                                                                        ("DedicatedTxThread_TimeToSleepEachLoop", RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_1),
                                                                        ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_1),
                                                                        ("HeartbeatTimeIntervalMilliseconds", RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_1),
                                                                        ("NumberOfMagnetsInMotor", RoboteqBLDCcontroller_NumberOfMagnetsInMotor_1),
                                                                        ("RoboteqBLDCcontroller_PID_Kp_1", RoboteqBLDCcontroller_PID_Kp_1),
                                                                        ("RoboteqBLDCcontroller_PID_Ki_1", RoboteqBLDCcontroller_PID_Ki_1),
                                                                        ("RoboteqBLDCcontroller_PID_Kd_1", RoboteqBLDCcontroller_PID_Kd_1),
                                                                        ("RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_1", RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_1),
                                                                        ("SetBrushlessCounterTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_1)])

    if USE_RoboteqBLDCcontroller_FLAG_1 == 1:
        try:
            RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1 = RoboteqBLDCcontroller_ReubenPython2and3Class(RoboteqBLDCcontroller_ReubenPython2and3ClassObject_setup_dict_1)
            RoboteqBLDCcontroller_OPEN_FLAG_1 = RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1 __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_WiFiVINTthumbstick_FLAG),
                                    ("root", GUItabObjectsOrderedDict["WiFiVINTthumbstick"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_WiFiVINTthumbstick),
                                    ("GUI_COLUMN", GUI_COLUMN_WiFiVINTthumbstick),
                                    ("GUI_PADX", GUI_PADX_WiFiVINTthumbstick),
                                    ("GUI_PADY", GUI_PADY_WiFiVINTthumbstick),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_WiFiVINTthumbstick),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_WiFiVINTthumbstick)])

    global PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_setup_dict
    PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                ("VINT_DesiredSerialNumber", WiFiVINTthumbstick_VINT_DesiredSerialNumber),
                                                                                ("VINT_DesiredPortNumber", WiFiVINTthumbstick_VINT_DesiredPortNumber),
                                                                                ("DesiredDeviceID", WiFiVINTthumbstick_DesiredDeviceID),
                                                                                ("WaitForAttached_TimeoutDuration_Milliseconds", WiFiVINTthumbstick_WaitForAttached_TimeoutDuration_Milliseconds),
                                                                                ("NameToDisplay_UserSet", WiFiVINTthumbstick_NameToDisplay_UserSet),
                                                                                ("UsePhidgetsLoggingInternalToThisClassObjectFlag", WiFiVINTthumbstick_UsePhidgetsLoggingInternalToThisClassObjectFlag),
                                                                                ("MainThread_TimeToSleepEachLoop", WiFiVINTthumbstick_MainThread_TimeToSleepEachLoop),
                                                                                ("UpdateDeltaT_ms", WiFiVINTthumbstick_UpdateDeltaT_ms),
                                                                                ("WirelessVINThub_ServerName_Str", WiFiVINTthumbstick_WirelessVINThub_ServerName_Str),
                                                                                ("WirelessVINThub_Address_Str", WiFiVINTthumbstick_WirelessVINThub_Address_Str),
                                                                                ("WirelessVINThub_Port_Int", WiFiVINTthumbstick_WirelessVINThub_Port_Int),
                                                                                ("WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str", WiFiVINTthumbstick_WirelessVINThub_ServerNotWiFiAccessPointNetworkPassword_Str),
                                                                                ("WirelessVINThub_Flags_Int", WiFiVINTthumbstick_WirelessVINThub_Flags_Int),
                                                                                ("VoltageRatioInput0Object_SteadyStateOffset", WiFiVINTthumbstick_VoltageRatioInput0Object_SteadyStateOffset),
                                                                                ("VoltageRatioInput1Object_SteadyStateOffset", WiFiVINTthumbstick_VoltageRatioInput1Object_SteadyStateOffset),
                                                                                ("VoltageRatioInput0Object_LowPassFilter_Lambda", WiFiVINTthumbstick_VoltageRatioInput0Object_LowPassFilter_Lambda),
                                                                                ("VoltageRatioInput1Object_LowPassFilter_Lambda", WiFiVINTthumbstick_VoltageRatioInput1Object_LowPassFilter_Lambda)])

    if USE_WiFiVINTthumbstick_FLAG == 1:
        try:
            PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject = PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class(PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject_setup_dict)
            WiFiVINTthumbstick_OPEN_FLAG = PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_SpatialPrecision333_FLAG),
                                    ("root", GUItabObjectsOrderedDict["SpatialPrecision333"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_SpatialPrecision333),
                                    ("GUI_COLUMN", GUI_COLUMN_SpatialPrecision333),
                                    ("GUI_PADX", GUI_PADX_SpatialPrecision333),
                                    ("GUI_PADY", GUI_PADY_SpatialPrecision333),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_SpatialPrecision333),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_SpatialPrecision333)])

    global PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict
    PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                        ("DesiredSerialNumber", SpatialPrecision333_DesiredSerialNumber),
                                                                                        ("WaitForAttached_TimeoutDuration_Milliseconds", SpatialPrecision333_WaitForAttached_TimeoutDuration_Milliseconds),
                                                                                        ("NameToDisplay_UserSet", SpatialPrecision333_NameToDisplay_UserSet),
                                                                                        ("UsePhidgetsLoggingInternalToThisClassObjectFlag", SpatialPrecision333_UsePhidgetsLoggingInternalToThisClassObjectFlag),
                                                                                        ("SpatialAlgorithm", SpatialPrecision333_SpatialAlgorithm),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseMedianFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_UseExponentialSmoothingFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegPerSec_ExponentialSmoothingFilterLambda),
                                                                                        ("Spatial_CallbackUpdateDeltaTmilliseconds", SpatialPrecision333_Spatial_CallbackUpdateDeltaTmilliseconds),
                                                                                        ("DataCollectionDurationInSecondsForSnapshottingAndZeroing", SpatialPrecision333_DataCollectionDurationInSecondsForSnapshottingAndZeroing),
                                                                                        ("MainThread_TimeToSleepEachLoop", SpatialPrecision333_MainThread_TimeToSleepEachLoop),
                                                                                        ("HeatingEnabledToStabilizeSensorTemperature", SpatialPrecision333_HeatingEnabledToStabilizeSensorTemperature)])

    if USE_SpatialPrecision333_FLAG == 1:
        try:
            PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class(PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject_setup_dict)
            SpatialPrecision333_OPEN_FLAG = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    global PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_GUIparametersDict
    PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG),
                                    ("root", GUItabObjectsOrderedDict["DC30AmpCurrentSensor"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_DC30AmpCurrentSensor),
                                    ("GUI_COLUMN", GUI_COLUMN_DC30AmpCurrentSensor),
                                    ("GUI_PADX", GUI_PADX_DC30AmpCurrentSensor),
                                    ("GUI_PADY", GUI_PADY_DC30AmpCurrentSensor),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_DC30AmpCurrentSensor),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_DC30AmpCurrentSensor)])

    global PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_setup_dict
    PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                                ("VINT_DesiredSerialNumber", DC30AmpCurrentSensor_VINT_DesiredSerialNumber),
                                                                                ("VINT_DesiredPortNumber", DC30AmpCurrentSensor_VINT_DesiredPortNumber),
                                                                                ("DesiredDeviceID", DC30AmpCurrentSensor_DesiredDeviceID),
                                                                                ("WaitForAttached_TimeoutDuration_Milliseconds", DC30AmpCurrentSensor_WaitForAttached_TimeoutDuration_Milliseconds),
                                                                                ("NameToDisplay_UserSet", DC30AmpCurrentSensor_NameToDisplay_UserSet),
                                                                                ("UsePhidgetsLoggingInternalToThisClassObjectFlag", DC30AmpCurrentSensor_UsePhidgetsLoggingInternalToThisClassObjectFlag),
                                                                                ("DataCallbackUpdateDeltaT_ms", DC30AmpCurrentSensor_DataCallbackUpdateDeltaT_ms),
                                                                                ("CurrentSensorList_Current_Amps_ExponentialFilterLambda", DC30AmpCurrentSensor_CurrentSensorList_Current_Amps_ExponentialFilterLambda)])

    if USE_DC30AmpCurrentSensor_FLAG == 1:
        try:
            PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject = PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class(PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject_setup_dict)
            DC30AmpCurrentSensor_OPEN_FLAG = PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict["GUIparametersDict"] = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_GUIparametersDict
    MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict["ParentPID"] = os.getpid()

    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1:
        try:
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3Class(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject, exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    try:
        Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject_setup_dict = dict([("UseMedianFilterFlag", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseMedianFilterFlag),
                                                                    ("UseExponentialSmoothingFilterFlag", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseExponentialSmoothingFilterFlag),
                                                                    ("ExponentialSmoothingFilterLambda", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda)])

        Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject = LowPassFilter_ReubenPython2and3Class(Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject_setup_dict)
        Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_OPEN_FLAG = Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

    except:
        exceptions = sys.exc_info()[0]
        print("SelfBalancingRobot1.py, LowPassFilter_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_RoboteqBLDCcontroller_FLAG_0 == 1 and RoboteqBLDCcontroller_OPEN_FLAG_0 != 1:
        print("SelfBalancingRobot1.py, failed to open RoboteqBLDCcontroller_ReubenPython2and3Class for motor 0.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_RoboteqBLDCcontroller_FLAG_1 == 1 and RoboteqBLDCcontroller_OPEN_FLAG_1 != 1:
        print("SelfBalancingRobot1.py, failed to open RoboteqBLDCcontroller_ReubenPython2and3Class for motor 0.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_WiFiVINTthumbstick_FLAG == 1 and WiFiVINTthumbstick_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_SpatialPrecision333_FLAG == 1 and SpatialPrecision333_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_DC30AmpCurrentSensor_FLAG == 1 and DC30AmpCurrentSensor_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open LowPassFilter_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Starting main loop of SelfBalancingRobot1.py")
    else:
        print("Starting main loop of SelfBalancingRobot1.py")
    #################################################
    #################################################

    #################################################
    #################################################
    StartingTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString()
    #################################################
    #################################################

    while(EXIT_PROGRAM_FLAG == 0):
        ###################################################################################################### Start GET's
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ################################################### GET's
        ###################################################
        CurrentTime_CalculatedFromMainThread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromMainThread
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if JSONfiles_NeedsToBeLoadedFlag == 1:
            LoadAndParseJSONfile_GUIsettings()

            LoadAndParseJSONfile_RoboteqBLDCcontroller_0()
            LoadAndParseJSONfile_RoboteqBLDCcontroller_1()
            LoadAndParseJSONfile_WiFiVINTthumbstick()
            LoadAndParseJSONfile_SpatialPrecision333()
            LoadAndParseJSONfile_DC30AmpCurrentSensor()
            
            LoadAndParseJSONfile_ControlLawParameters()
            LoadAndParseJSONfile_RobotModelParameters()

            LoadAndParseJSONfile_Keyboard()
            KeyboardMapKeysToCallbackFunctions()

            '''
            UPDATE PARAMETERS HERE UPON RELOADING JSON FILE
            '''

            JSONfiles_NeedsToBeLoadedFlag = 0
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_0 == 1:
            try:

                RoboteqBLDCcontroller_MostRecentDict_0 = RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.GetMostRecentDataDict()

                if "Time" in RoboteqBLDCcontroller_MostRecentDict_0:
                    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_0 = RoboteqBLDCcontroller_MostRecentDict_0["AbsoluteBrushlessCounter"]
                    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_0 = RoboteqBLDCcontroller_MostRecentDict_0["SpeedRPM"]
                    #RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_0 = RoboteqBLDCcontroller_MostRecentDict_0["TorqueTarget"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_0 = RoboteqBLDCcontroller_MostRecentDict_0["BatteryCurrentInAmps"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_0 = RoboteqBLDCcontroller_MostRecentDict_0["BatteryVoltsX10"]
                    RoboteqBLDCcontroller_MostRecentDict_FaultFlags_0 = RoboteqBLDCcontroller_MostRecentDict_0["FaultFlags"]
    
                    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 = RoboteqBLDCcontroller_MostRecentDict_0["Position_Rev"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_0 = RoboteqBLDCcontroller_MostRecentDict_0["Position_Radians"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_0 = RoboteqBLDCcontroller_MostRecentDict_0["Position_Degrees"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_0 = RoboteqBLDCcontroller_MostRecentDict_0["Speed_RPM"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0 = RoboteqBLDCcontroller_MostRecentDict_0["Speed_RPS"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_0 = RoboteqBLDCcontroller_MostRecentDict_0["Speed_RadiansPerSec"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_0 = RoboteqBLDCcontroller_MostRecentDict_0["Speed_DegreesPerSec"]
    
                    RoboteqBLDCcontroller_MostRecentDict_Time_0 = RoboteqBLDCcontroller_MostRecentDict_0["Time"]
                    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_0 = RoboteqBLDCcontroller_MostRecentDict_0["DataStreamingFrequency_CalculatedFromDedicatedRxThread"]
                    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_0 = RoboteqBLDCcontroller_MostRecentDict_0["DataStreamingFrequency_CalculatedFromDedicatedTxThread"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Kp_0 = RoboteqBLDCcontroller_MostRecentDict_0["PID_Kp"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Ki_0 = RoboteqBLDCcontroller_MostRecentDict_0["PID_Ki"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Kd_0 = RoboteqBLDCcontroller_MostRecentDict_0["PID_Kd"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_0 = RoboteqBLDCcontroller_MostRecentDict_0["PID_IntegratorCap1to100percent"]
                    RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_0 = RoboteqBLDCcontroller_MostRecentDict_0["ControlMode_IntegerValue"]
                    RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_0 = RoboteqBLDCcontroller_MostRecentDict_0["ControlMode_EnglishString"]
                    #print("RoboteqBLDCcontroller_MostRecentDict_Time_0: " + str(RoboteqBLDCcontroller_MostRecentDict_Time_0))

            except:
                exceptions = sys.exc_info()[0]
                print("SelfBalancingRobot1, RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0 GET's, exceptions: %s" % exceptions)
                #traceback.print_exc()
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_1 == 1:
            try:

                RoboteqBLDCcontroller_MostRecentDict_1 = RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.GetMostRecentDataDict()

                if "Time" in RoboteqBLDCcontroller_MostRecentDict_1:
                    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_1 = RoboteqBLDCcontroller_MostRecentDict_1["AbsoluteBrushlessCounter"]
                    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1 = RoboteqBLDCcontroller_MostRecentDict_1["SpeedRPM"]
                    #RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_1 = RoboteqBLDCcontroller_MostRecentDict_1["TorqueTarget"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_1 = RoboteqBLDCcontroller_MostRecentDict_1["BatteryCurrentInAmps"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_1 = RoboteqBLDCcontroller_MostRecentDict_1["BatteryVoltsX10"]
                    RoboteqBLDCcontroller_MostRecentDict_FaultFlags_1 = RoboteqBLDCcontroller_MostRecentDict_1["FaultFlags"]
    
                    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 = RoboteqBLDCcontroller_MostRecentDict_1["Position_Rev"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1 = RoboteqBLDCcontroller_MostRecentDict_1["Position_Radians"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1 = RoboteqBLDCcontroller_MostRecentDict_1["Position_Degrees"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1 = RoboteqBLDCcontroller_MostRecentDict_1["Speed_RPM"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 = RoboteqBLDCcontroller_MostRecentDict_1["Speed_RPS"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1 = RoboteqBLDCcontroller_MostRecentDict_1["Speed_RadiansPerSec"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1 = RoboteqBLDCcontroller_MostRecentDict_1["Speed_DegreesPerSec"]
    
                    RoboteqBLDCcontroller_MostRecentDict_Time_1 = RoboteqBLDCcontroller_MostRecentDict_1["Time"]
                    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedRxThread_1 = RoboteqBLDCcontroller_MostRecentDict_1["DataStreamingFrequency_CalculatedFromDedicatedRxThread"]
                    RoboteqBLDCcontroller_MostRecentDict_DataStreamingFrequency_CalculatedFromDedicatedTxThread_1 = RoboteqBLDCcontroller_MostRecentDict_1["DataStreamingFrequency_CalculatedFromDedicatedTxThread"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Kp_1 = RoboteqBLDCcontroller_MostRecentDict_1["PID_Kp"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Ki_1 = RoboteqBLDCcontroller_MostRecentDict_1["PID_Ki"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_Kd_1 = RoboteqBLDCcontroller_MostRecentDict_1["PID_Kd"]
                    RoboteqBLDCcontroller_MostRecentDict_PID_IntegratorCap1to100percent_1 = RoboteqBLDCcontroller_MostRecentDict_1["PID_IntegratorCap1to100percent"]
                    RoboteqBLDCcontroller_MostRecentDict_ControlMode_IntegerValue_1 = RoboteqBLDCcontroller_MostRecentDict_0["ControlMode_IntegerValue"]
                    RoboteqBLDCcontroller_MostRecentDict_ControlMode_EnglishString_1 = RoboteqBLDCcontroller_MostRecentDict_0["ControlMode_EnglishString"]
                    #print("RoboteqBLDCcontroller_MostRecentDict_Time_1: " + str(RoboteqBLDCcontroller_MostRecentDict_Time_1))

            except:
                exceptions = sys.exc_info()[0]
                print("SelfBalancingRobot1, RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1 GET's, exceptions: %s" % exceptions)
                #traceback.print_exc()
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if WiFiVINTthumbstick_OPEN_FLAG == 1:

            WiFiVINTthumbstick_MostRecentDict = PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in WiFiVINTthumbstick_MostRecentDict:
                WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio = WiFiVINTthumbstick_MostRecentDict["VoltageRatioInput0Object_VoltageRatio"]
                WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio = WiFiVINTthumbstick_MostRecentDict["VoltageRatioInput1Object_VoltageRatio"]
                WiFiVINTthumbstick_MostRecentDict_DigitalInput0Object_State = WiFiVINTthumbstick_MostRecentDict["DigitalInput0Object_State"]
                WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = WiFiVINTthumbstick_MostRecentDict["DataStreamingFrequency_CalculatedFromMainThread"]
                WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback = WiFiVINTthumbstick_MostRecentDict["DataStreamingFrequency_TimestampFromVoltageRatioInput0DataCallback"]
                WiFiVINTthumbstick_MostRecentDict_DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback = WiFiVINTthumbstick_MostRecentDict["DataStreamingFrequency_TimestampFromVoltageRatioInput1DataCallback"]
                WiFiVINTthumbstick_MostRecentDict_Time = WiFiVINTthumbstick_MostRecentDict["Time"]

                #print("WiFiVINTthumbstick_MostRecentDict_Time: " + str(WiFiVINTthumbstick_MostRecentDict_Time))
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if SpatialPrecision333_OPEN_FLAG == 1:

            SpatialPrecision333_MostRecentDict = PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in SpatialPrecision333_MostRecentDict:
                SpatialPrecision333_MostRecentDict_Quaternions_DirectFromDataEventHandler = SpatialPrecision333_MostRecentDict["Quaternions_DirectFromDataEventHandler"]
                SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict = SpatialPrecision333_MostRecentDict["RollPitchYaw_AbtXYZ_Dict"]
                SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict = SpatialPrecision333_MostRecentDict["RollPitchYaw_Rate_AbtXYZ_Dict"]
                SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = SpatialPrecision333_MostRecentDict["DataStreamingFrequency_CalculatedFromMainThread"]
                SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = SpatialPrecision333_MostRecentDict["DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions"]
                SpatialPrecision333_MostRecentDict_Time = SpatialPrecision333_MostRecentDict["Time"]

                #print("SpatialPrecision333_MostRecentDict_Time: " + str(SpatialPrecision333_MostRecentDict_Time))
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if DC30AmpCurrentSensor_OPEN_FLAG == 1:

            DC30AmpCurrentSensor_MostRecentDict = PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "Time" in DC30AmpCurrentSensor_MostRecentDict:
                DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Raw = DC30AmpCurrentSensor_MostRecentDict["CurrentSensorList_Current_Amps_Raw"]
                DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_Current_Amps_Filtered = DC30AmpCurrentSensor_MostRecentDict["CurrentSensorList_Current_Amps_Filtered"]
                DC30AmpCurrentSensor_MostRecentDict_CurrentSensorList_ErrorCallbackFiredFlag = DC30AmpCurrentSensor_MostRecentDict["CurrentSensorList_ErrorCallbackFiredFlag"]
                DC30AmpCurrentSensor_MostRecentDict_Time = DC30AmpCurrentSensor_MostRecentDict["Time"]

                #print("DC30AmpCurrentSensor_MostRecentDict_Time: " + str(DC30AmpCurrentSensor_MostRecentDict_Time))
        ###################################################
        ###################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End GET's

        ###################################################################################################### Start Control Law
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ###################################################
        ###################################################
        ###################################################
        if ControlType_NeedsToBeChangedFlag == 1:
            dummy = 0
            ControlType_NeedsToBeChangedFlag = 0
        ###################################################
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        ###################################################
        #We can include JoystickControl here because the joystick-->robotiq code will overwrite these keyboard-generated values later.
        #However, if 'ParametersToBeLoaded_Joystick.json' doesn't map anything to the Robotiq (like with the SpaceMouse), then this keyboard code's values will still map to the Robotiq.
        if ControlType == "KeyboardControl" or ControlType == "JoystickControl":

            pass

            '''
            ###################################################
            ###################################################
            if KeyPressResponse_OpenRobotiqGripper2F85_NeedsToBeChangedFlag  == 1:
                RobotiqGripper2F85_Position_ToBeSet = LimitNumber_FloatOutputOnly(0.0, 255.0, RobotiqGripper2F85_Position_ToBeSet + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["OpenRobotiqGripper2F85"]["IncrementSize"])

                RobotiqGripper2F85_PositionSpeedOrForce_NeedsToBeChangedFlag = 1
                #KeyPressResponse_OpenRobotiqGripper2F85_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            if KeyPressResponse_CloseRobotiqGripper2F85_NeedsToBeChangedFlag  == 1:
                RobotiqGripper2F85_Position_ToBeSet = LimitNumber_FloatOutputOnly(0.0, 255.0, RobotiqGripper2F85_Position_ToBeSet + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["CloseRobotiqGripper2F85"]["IncrementSize"])

                RobotiqGripper2F85_PositionSpeedOrForce_NeedsToBeChangedFlag = 1
                #KeyPressResponse_CloseRobotiqGripper2F85_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS
            ###################################################
            ###################################################
            '''

        ###################################################
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        ###################################################
        if ControlType == "KeyboardControl":

            pass

            '''
            if 1:#UR5arm_MostRecentDict_ToolVectorActual_IsItInitializedFlag == 1:

                if KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[0] = UR5arm_ToolVectorActual_ToBeSet[0] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Xincrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_IncrementURtoolTipInX_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[0] = UR5arm_ToolVectorActual_ToBeSet[0] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Xdecrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_DecrementURtoolTipInX_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[1] = UR5arm_ToolVectorActual_ToBeSet[1] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Yincrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_IncrementURtoolTipInY_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[1] = UR5arm_ToolVectorActual_ToBeSet[1] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Ydecrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_DecrementURtoolTipInY_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[2] = UR5arm_ToolVectorActual_ToBeSet[2] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Zincrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_IncrementURtoolTipInZ_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag == 1:
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
                    UR5arm_ToolVectorActual_ToBeSet[2] = UR5arm_ToolVectorActual_ToBeSet[2] + Keyboard_KeysToTeleopControlsMapping_DictOfDicts["Zdecrement"]["IncrementSize"]
                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1
                    #KeyPressResponse_DecrementURtoolTipInZ_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS
            '''

        ###################################################
        ###################################################
        ###################################################

        ###################################################
        ###################################################
        ###################################################
        if ControlType == "KeyboardControl" or ControlType == "JoystickControl":

            #################################################
            #################################################
            if USE_WiFiVINTthumbstick_FLAG == 1:
                Velocity_V_RMC_MetersPerSec_Commanded = WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio
            #################################################
            #################################################

            ################################################# dragon
            #################################################
            #OdriveRoboticsBLDCcontroller_MostRecentDict_1_PositionEstimateRxFromOdrive_Rev_Motor1
            #self.PositionEstimateRxFromOdrive_Rev_Motor0 = self.OdriveBoardObject.axis0.encoder.pos_estimate
            #I think this is supposed to be in radians?
            Theta_RL_Actual = RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 * 2.0 * math.pi #THE ENCODERS BOTH SHOW POSITIVE DESPITE OPPOSITE MOUNTING
            Theta_RR_Actual = RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 * 2.0 * math.pi

            #OdriveRoboticsBLDCcontroller_MostRecentDict_1_VelocityEstimateRxFromOdrive_RevPerSec_Motor1
            Omega_RL_Actual = RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 * 2.0 * math.pi
            Omega_RR_Actual = RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0 * 2.0 * math.pi

            Position_X_RM_Meters_Actual = RobotModelParameters_R_RadiusOfWheelInMeters * (Theta_RL_Actual + Theta_RR_Actual) / 2.0

            Position_X_RMC_Meters_Commanded = Position_X_RMC_Meters_Commanded + Velocity_V_RMC_MetersPerSec_Commanded*DataStreamingDeltaT_CalculatedFromMainThread #NUMERICALLY INTEGRATE
            Position_X_RMC_Meters_Commanded = LimitNumber_FloatOutputOnly(Position_X_RM_Meters_Actual - Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, Position_X_RM_Meters_Actual + Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, Position_X_RMC_Meters_Commanded) #Cap it

            Velocity_V_RM_MetersPerSec_Actual_UNFILTERED = RobotModelParameters_R_RadiusOfWheelInMeters * (Omega_RL_Actual + Omega_RR_Actual) / 2.0

            Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject.AddDataPointFromExternalProgram(Velocity_V_RM_MetersPerSec_Actual_UNFILTERED)
            Velocity_V_RM_MetersPerSec_Actual = Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ReubenPython2and3ClassObject.GetMostRecentDataDict()["SignalOutSmoothed"]

            PitchAngle_Theta_Deg_Actual = SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][1]#spatial333_Pitch_AbtYaxis_Degrees_1
            PitchAngle_Theta_Radians_Actual = PitchAngle_Theta_Deg_Actual*math.pi/180.0
            PitchAngle_Theta_Deg_Commanded = 0.0
            PitchAngle_Theta_Radians_Commanded = PitchAngle_Theta_Deg_Commanded*math.pi/180.0

            ###NEED TO SMOOTH HERE.
            PitchAngularRate_ThetaDot_DegPerSec_Actual = SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict["RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond"][1]#spatial333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegPerSec_SMOOTHED_1
            PitchAngularRate_ThetaDot_RadiansPerSec_Actual = PitchAngularRate_ThetaDot_DegPerSec_Actual*math.pi/180.0
            PitchAngularRate_ThetaDot_RadiansPerSec_Commanded = 0.0

            YawAngle_Delta_Radians_Actual = -1.0*RobotModelParameters_R_RadiusOfWheelInMeters * (Theta_RL_Actual - Theta_RR_Actual) / RobotModelParameters_D_LateralDistanceBetweenWheelContactPatchesInMeters #NOT SURE WHY WE NEED MINUS SIGN TO GET YAW IN CORRECT DIRECTION
            YawAngle_Delta_Deg_Actual = YawAngle_Delta_Radians_Actual * 180.0 / math.pi
            YawAngle_Delta_Radians_Commanded = 0.0

            YawAngularRate_DeltaDot_RadiansPerSec_Actual = RobotModelParameters_R_RadiusOfWheelInMeters * (Omega_RL_Actual - Omega_RR_Actual) / RobotModelParameters_D_LateralDistanceBetweenWheelContactPatchesInMeters
            YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0
            #################################################
            #################################################

            #################################################
            #################################################
            if USE_SINUSOIDAL_CONTROL_INPUT_FLAG == 1 and USE_PITCH_PID_FLAG == 0 and USE_PITCH_LQR_FLAG == 0:
                time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
                SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)*math.sin(time_gain*CurrentTime_CalculatedFromMainThread)

                TorqueToBeCommanded_Motor0 = SINUSOIDAL_INPUT_TO_COMMAND
                TorqueToBeCommanded_Motor1 = -1.0*SINUSOIDAL_INPUT_TO_COMMAND #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
            #################################################
            #################################################

            #################################################
            #################################################
            if USE_SINUSOIDAL_CONTROL_INPUT_FLAG == 0 and USE_PITCH_PID_FLAG == 1 and USE_PITCH_LQR_FLAG == 0:

                Pitch_PosControl_PID_Error = PitchAngle_Theta_Deg_Commanded - PitchAngle_Theta_Deg_Actual

                if abs(Pitch_PosControl_PID_ErrorSum + Pitch_PosControl_PID_Error) <= Pitch_PosControl_PID_ErrorSum_Max:
                    Pitch_PosControl_PID_ErrorSum = Pitch_PosControl_PID_ErrorSum + Pitch_PosControl_PID_Error

                # print Pitch_PosControl_PID_ErrorSum

                Pitch_PosControl_PID_ErrorD = (0 - PitchAngularRate_ThetaDot_DegPerSec_Actual)

                Pitch_PosControl_PID_CommandToMotor = -1.0 * Pitch_PosControl_PID_Error * Pitch_PosControl_PID_gain_Kp \
                                                      - Pitch_PosControl_PID_ErrorSum * Pitch_PosControl_PID_gain_Ki \
                                                      - Pitch_PosControl_PID_ErrorD * Pitch_PosControl_PID_gain_Kd

                TorqueToBeCommanded_Motor0 = Pitch_PosControl_PID_CommandToMotor
                TorqueToBeCommanded_Motor1 = -1.0*Pitch_PosControl_PID_CommandToMotor #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
            #################################################
            #################################################

            ################################################# unicorn
            #################################################
            if USE_SINUSOIDAL_CONTROL_INPUT_FLAG == 0 and USE_PITCH_PID_FLAG == 0 and USE_PITCH_LQR_FLAG == 1:

                #'''
                C_Theta = -1.0 * (1.0*LQR_PitchControl_GainVectorElement_Ktheta_0 * (Position_X_RM_Meters_Actual - Position_X_RMC_Meters_Commanded) +
                                    1.0 *LQR_PitchControl_GainVectorElement_Ktheta_1 * (Velocity_V_RM_MetersPerSec_Actual - Velocity_V_RMC_MetersPerSec_Commanded) +
                                    -1.0*LQR_PitchControl_GainVectorElement_Ktheta_2 * (PitchAngle_Theta_Radians_Actual - PitchAngle_Theta_Radians_Commanded) +
                                    -1.0 *LQR_PitchControl_GainVectorElement_Ktheta_3 * (PitchAngularRate_ThetaDot_RadiansPerSec_Actual - PitchAngularRate_ThetaDot_RadiansPerSec_Commanded))  #NOT SURE WHY WE HAD TO REMOVE PAPER'S MINUS SIGN

                C_Delta =  1.0 * (LQR_YawControl_GainVectorElement_Kdelta_0 * (YawAngle_Delta_Radians_Actual - YawAngle_Delta_Radians_Commanded) +
                                   LQR_YawControl_GainVectorElement_Kdelta_1 * (YawAngularRate_DeltaDot_RadiansPerSec_Actual - YawAngularRate_DeltaDot_RadiansPerSec_Commanded)) #NOT SURE WHY WE HAD TO REMOVE PAPER'S MINUS SIGN
                #'''

                C_Delta = 0

                C_L = 0.5*(C_Theta + C_Delta)

                C_R = 0.5*(C_Theta - C_Delta)

                TorqueToBeCommanded_Motor0 = 1.0*C_R #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
                TorqueToBeCommanded_Motor1 = -1.0*C_L

                #TorqueToBeCommanded_Motor0 = 1.0
                #TorqueToBeCommanded_Motor1 = -1.0
            #################################################
            #################################################


            '''
            ###################################################
            ###################################################
            if UR5arm_MostRecentDict_ToolVectorActual_IsItInitializedFlag == 1 and JOYSTICK_OPEN_FLAG == 1:

                ###################################################
                if Joystick_UseClutchFlag == 1:
                    Joystick_ClutchState = JOYSTICK_MostRecentDict_Joystick_Button_Value_List[Joystick_Clutch_Button_Index_ToDisplayAsDotColorOn2DdotDisplay]
                else:
                    Joystick_ClutchState = 1
                ###################################################

                if Joystick_ClutchState == 1:

                    ###################################################
                    for Index in range(0,6):
                        AxisHatButtonOrBallTo6DOFposeMappingDict = Joystick_AxisHatButtonOrBallTo6DOFposeMapping_ListOfDicts[Index]

                        IncrementSize = AxisHatButtonOrBallTo6DOFposeMappingDict["IncrementSize"]
                        PrimaryAxisHatButtonOrBallIndex = AxisHatButtonOrBallTo6DOFposeMappingDict["PrimaryAxisHatButtonOrBallIndex"]
                        SecondaryAxisHatButtonOrBallIndex = AxisHatButtonOrBallTo6DOFposeMappingDict["SecondaryAxisHatButtonOrBallIndex"]

                        if AxisHatButtonOrBallTo6DOFposeMappingDict["AxisHatButtonOrBallType"] == "AXIS":
                            Joystick_AddToUR5armCurrentPositionList[Index] = IncrementSize*JOYSTICK_MostRecentDict_Joystick_Axis_Value_List[PrimaryAxisHatButtonOrBallIndex]

                        elif AxisHatButtonOrBallTo6DOFposeMappingDict["AxisHatButtonOrBallType"] == "HAT":
                            Joystick_AddToUR5armCurrentPositionList[Index] = IncrementSize*JOYSTICK_MostRecentDict_Joystick_Hat_Value_List[PrimaryAxisHatButtonOrBallIndex][SecondaryAxisHatButtonOrBallIndex]

                        else:
                            print("In JoystickControl, only AXIS and HAT can be used to control the UR5.") #Nothing other than an axis or hat can be used as an input currently (no buttons or balls).

                    ###################################################

                    #We're NOT using UR5arm_MostRecentDict_ToolVectorActual_AtTimeOfClutchIn because the joystick inputs rate-control, not absolute position.
                    UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)

                    ################################################### unicorn dragon lorax goat

                    RotationObjectScipy = Rotation.from_rotvec(UR5arm_ToolVectorActual_ToBeSet[-3:])
                    RotationEulerList = RotationObjectScipy.as_euler('xyz', degrees=False)

                    RotationEulerList[0] = RotationEulerList[0] + Joystick_AddToUR5armCurrentPositionList[3]
                    RotationEulerList[1] = RotationEulerList[1] + Joystick_AddToUR5armCurrentPositionList[4]
                    RotationEulerList[2] = RotationEulerList[2] + Joystick_AddToUR5armCurrentPositionList[5]

                    #print("RotationEulerList: " + str(RotationEulerList))

                    RotationObjectScipy_Joystick_AddToUR5armCurrentPositionList = Rotation.from_euler('xyz', RotationEulerList, degrees=False)
                    RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList = RotationObjectScipy_Joystick_AddToUR5armCurrentPositionList.as_rotvec()
                    #print("RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList: " + str(RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList))

                    ################################################### goat

                    ###################################################
                    if Trigger_State == 0:
                        for Index in range(0,3):
                            UR5arm_ToolVectorActual_ToBeSet[Index] = UR5arm_ToolVectorActual_ToBeSet[Index]  + Joystick_AddToUR5armCurrentPositionList[Index]

                    if Trigger_State == 1:
                        #print("Trigger_State: " + str(Trigger_State))
                        UR5arm_ToolVectorActual_ToBeSet[3] = RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList[0]
                        UR5arm_ToolVectorActual_ToBeSet[4] = RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList[1]
                        UR5arm_ToolVectorActual_ToBeSet[5] = RotationAxisAngleList_Joystick_AddToUR5armCurrentPositionList[2]
                    ###################################################

                    UR5arm_PositionControl_NeedsToBeChangedFlag = 1

            else:
                UR5arm_ToolVectorActual_ToBeSet = list(UR5arm_MostRecentDict_ToolVectorActual)
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            if RobotiqGripper2F85_OPEN_FLAG == 1:

                ###################################################
                if len(Joystick_AxisHatButtonOrBallTo6DOFposeMapping_ListOfDicts) >= 7: #If 'ParametersToBeLoaded_Joystick.json' includes mapping to the Robotiq.
                    AxisHatButtonOrBallTo6DOFposeMappingDict = Joystick_AxisHatButtonOrBallTo6DOFposeMapping_ListOfDicts[6]

                    IncrementSize = AxisHatButtonOrBallTo6DOFposeMappingDict["IncrementSize"]
                    PrimaryAxisHatButtonOrBallIndex = AxisHatButtonOrBallTo6DOFposeMappingDict["PrimaryAxisHatButtonOrBallIndex"]
                    SecondaryAxisHatButtonOrBallIndex = AxisHatButtonOrBallTo6DOFposeMappingDict["SecondaryAxisHatButtonOrBallIndex"]

                    if AxisHatButtonOrBallTo6DOFposeMappingDict["AxisHatButtonOrBallType"] == "AXIS":
                        RobotiqGripper2F85_Position_ToBeSet = RobotiqGripper2F85_Position_ToBeSet + IncrementSize*JOYSTICK_MostRecentDict_Joystick_Axis_Value_List[PrimaryAxisHatButtonOrBallIndex]

                    elif AxisHatButtonOrBallTo6DOFposeMappingDict["AxisHatButtonOrBallType"] == "HAT":
                        RobotiqGripper2F85_Position_ToBeSet = RobotiqGripper2F85_Position_ToBeSet + IncrementSize*JOYSTICK_MostRecentDict_Joystick_Hat_Value_List[PrimaryAxisHatButtonOrBallIndex][SecondaryAxisHatButtonOrBallIndex]

                    elif AxisHatButtonOrBallTo6DOFposeMappingDict["AxisHatButtonOrBallType"] == "BUTTON":
                        #PrimaryAxisHatButtonOrBallIndex is 1 button (for opening), and SecondaryAxisHatButtonOrBallIndex is another button (for closing).
                        #If both are pressed at once, then nothing will happen as they cancel eachother out.
                        RobotiqGripper2F85_Position_ToBeSet = RobotiqGripper2F85_Position_ToBeSet + IncrementSize*JOYSTICK_MostRecentDict_Joystick_Button_Value_List[PrimaryAxisHatButtonOrBallIndex] - IncrementSize*JOYSTICK_MostRecentDict_Joystick_Button_Value_List[SecondaryAxisHatButtonOrBallIndex]

                    else:
                        print("In JoystickControl, only AXIS, HAT, and BUTTON can be specified to control the RobotiqGripper2F85.") #Nothing other than an axis or hat can be used as an input currently (no buttons or balls).

                    RobotiqGripper2F85_Position_ToBeSet = LimitNumber_FloatOutputOnly(0.0, 255.0, RobotiqGripper2F85_Position_ToBeSet)
                    RobotiqGripper2F85_PositionSpeedOrForce_NeedsToBeChangedFlag = 1
                ###################################################

            ###################################################
            ###################################################
            
            '''

        ###################################################
        ###################################################
        ###################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End Control Law

        ###################################################################################################### Start SET's
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_0 == 1:
            if EnableMotors_State == 1:
                #TorqueToBeCommanded_Motor0 = 20
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.SendCommandToMotor_ExternalClassFunction(TorqueToBeCommanded_Motor0, RoboteqBLDCcontroller_ControlMode_Starting_0)
            else:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.SendCommandToMotor_ExternalClassFunction(0.0, RoboteqBLDCcontroller_ControlMode_Starting_0)

        ###################################################
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_1 == 1:
            if EnableMotors_State == 1:
                #TorqueToBeCommanded_Motor1 = -20
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.SendCommandToMotor_ExternalClassFunction(TorqueToBeCommanded_Motor1, RoboteqBLDCcontroller_ControlMode_Starting_1)
            else:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.SendCommandToMotor_ExternalClassFunction(0.0, RoboteqBLDCcontroller_ControlMode_Starting_1)

        ###################################################
        ###################################################
        ###################################################

        ################################################### SETs
        ###################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread_PLOTTER >= MyPlotterPureTkinterStandAloneProcess_RefreshDurationInSeconds:
                        pass
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0"], [CurrentTime_CalculatedFromMainThread], [Tension_ActualValue_grams])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread], [PIDcontroller_Tension_MostRecentDict_ActualValueDot_ActualValueDot_Raw, PIDcontroller_Tension_MostRecentDict_ActualValueDot_ActualValueDot_Filtered])

                        LastTime_CalculatedFromMainThread_PLOTTER = CurrentTime_CalculatedFromMainThread
            ####################################################

        ###################################################
        ###################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End SET's

        ###################################################################################################### Update "last" values, calculate frequency, and sleep
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        #PLACE TO UPDATE LAST_ VARIABLES

        [LoopCounter_CalculatedFromMainThread, LastTime_CalculatedFromMainThread, DataStreamingFrequency_CalculatedFromMainThread, DataStreamingDeltaT_CalculatedFromMainThread] = UpdateFrequencyCalculation(LoopCounter_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread, LastTime_CalculatedFromMainThread, DataStreamingFrequency_CalculatedFromMainThread, DataStreamingDeltaT_CalculatedFromMainThread)
        time.sleep(SelfBalancingRobot1_MainThread_TimeToSleepEachLoop)

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

    ###################################################
    ###################################################
    ###################################################

    #################################################### THIS IS THE EXIT ROUTINE!
    ###################################################
    ###################################################
    print("Exiting main program 'SelfBalancingRobot1'.")

    #################################################
    if RoboteqBLDCcontroller_OPEN_FLAG_0 == 1:
        RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.ExitProgram_Callback()
    #################################################

    #################################################
    if RoboteqBLDCcontroller_OPEN_FLAG_1 == 1:
        RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.ExitProgram_Callback()
    #################################################

    #################################################
    if WiFiVINTthumbstick_OPEN_FLAG == 1:
        PhidgetsWirelessVINThubWithThumbstick_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if SpatialPrecision333_OPEN_FLAG == 1:
        PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if DC30AmpCurrentSensor_OPEN_FLAG == 1:
        PhidgetsCurrentSensor30ampDConlyVCP1100_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    ###################################################
    ###################################################
    ###################################################

#######################################################################################################################
#######################################################################################################################