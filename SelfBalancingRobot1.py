# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision J, 09/24/2024

Verified working on: Python 3.8 for Windows 10 64-bit (not yet tested on Raspberry Pi, Ubuntu, or Mac).
'''

__author__ = 'reuben.brewer'

#########################################################
#https://github.com/Reuben-Brewer/BarGraphDisplay_ReubenPython3Class
from BarGraphDisplay_ReubenPython3Class import *

#https://github.com/Reuben-Brewer/CSVdataLogger_ReubenPython3Class
from CSVdataLogger_ReubenPython3Class import *

#https://github.com/Reuben-Brewer/EntryListWithBlinking_ReubenPython2and3Class
from EntryListWithBlinking_ReubenPython2and3Class import *

#https://github.com/Reuben-Brewer/LowPassFilterForDictsOfLists_ReubenPython2and3Class
from LowPassFilterForDictsOfLists_ReubenPython2and3Class import *

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
from scipy.spatial.transform import Rotation #'sudo pip install scipy' (*AFTER* 'sudo apt install -y python3-scipy' if on Raspberry Pi)
#########################################################

#########################################################
from tkinter import *
import tkinter.font as tkFont
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
def LoadAndParseJSONfile_SavingSettings():
    global ParametersToBeLoaded_SavingSettings_Dict

    print("Calling LoadAndParseJSONfile_SavingSettings().")

    #################################
    JSONfilepathFull_SavingSettings = ParametersToBeLoaded_Directory_TO_BE_USED + "//ParametersToBeLoaded_SavingSettings.json"

    ParametersToBeLoaded_SavingSettings_Dict = LoadAndParseJSONfile_AddDictKeysToGlobalsDict(globals(), JSONfilepathFull_SavingSettings, 1, 1)
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
                                                 str(Key) + ":\n" + \
                                                 ConvertDictToProperlyFormattedStringForPrinting(DictToPrint[Key], NumberOfDecimalsPlaceToUse, NumberOfEntriesPerLine, NumberOfTabsBetweenItems)

        else:
            ProperlyFormattedStringForPrinting = ProperlyFormattedStringForPrinting + \
                                                 str(Key) + ": " + \
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
def UpdateFrequencyCalculation_MainThread_Filtered():

    global CurrentTime_CalculatedFromMainThread
    global LastTime_CalculatedFromMainThread
    global LoopCounter_CalculatedFromMainThread
    global DataStreamingDeltaT_CalculatedFromMainThread
    global DataStreamingFrequency_CalculatedFromMainThread_Filtered
    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject

    try:
        DataStreamingDeltaT_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread

        if DataStreamingDeltaT_CalculatedFromMainThread != 0.0:
            DataStreamingFrequency_CalculatedFromMainThread = 1.0/DataStreamingDeltaT_CalculatedFromMainThread
            VariablesDict_Temp = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("DataStreamingFrequency_CalculatedFromMainThread", [DataStreamingFrequency_CalculatedFromMainThread])]))
            DataStreamingFrequency_CalculatedFromMainThread_Filtered = VariablesDict_Temp["DataStreamingFrequency_CalculatedFromMainThread"]["Filtered_MostRecentValuesList"][0]

            if DataStreamingFrequency_CalculatedFromMainThread_Filtered <= 0.0:
                DataStreamingFrequency_CalculatedFromMainThread_Filtered = 0.001

        LastTime_CalculatedFromMainThread = CurrentTime_CalculatedFromMainThread
        LoopCounter_CalculatedFromMainThread = LoopCounter_CalculatedFromMainThread + 1
        
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_MainThread_Filtered, exceptions: %s" % exceptions)
        traceback.print_exc()
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def UpdateFrequencyCalculation_GUIthread_Filtered():

    global CurrentTime_CalculatedFromGUIthread
    global LastTime_CalculatedFromGUIthread
    global LoopCounter_CalculatedFromGUIthread
    global DataStreamingDeltaT_CalculatedFromGUIthread
    global DataStreamingFrequency_CalculatedFromGUIthread_Filtered
    global LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject
    
    try:
        DataStreamingDeltaT_CalculatedFromGUIthread = CurrentTime_CalculatedFromGUIthread - LastTime_CalculatedFromGUIthread

        if DataStreamingDeltaT_CalculatedFromGUIthread != 0.0:
            DataStreamingDeltaT_CalculatedFromGUIthread = 1.0/DataStreamingDeltaT_CalculatedFromGUIthread
            VariablesDict_Temp = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("DataStreamingFrequency_CalculatedFromGUIthread", [DataStreamingDeltaT_CalculatedFromGUIthread])]))
            DataStreamingFrequency_CalculatedFromGUIthread_Filtered = VariablesDict_Temp["DataStreamingFrequency_CalculatedFromGUIthread"]["Filtered_MostRecentValuesList"][0]

            if DataStreamingFrequency_CalculatedFromGUIthread_Filtered <= 0.0:
                DataStreamingFrequency_CalculatedFromGUIthread_Filtered = 0.001

        LastTime_CalculatedFromGUIthread = CurrentTime_CalculatedFromGUIthread
        LoopCounter_CalculatedFromGUIthread = LoopCounter_CalculatedFromGUIthread + 1
        
    except:
        exceptions = sys.exc_info()[0]
        print("UpdateFrequencyCalculation_GUIthread_Filtered, exceptions: %s" % exceptions)
        traceback.print_exc()
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
  
    global KeyPressResponse_FWD_NeedsToBeChangedFlag
    global KeyPressResponse_REV_NeedsToBeChangedFlag
    global KeyPressResponse_RIGHT_NeedsToBeChangedFlag
    global KeyPressResponse_LEFT_NeedsToBeChangedFlag
    global KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag
    global KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag

    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString
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
def KeyPressResponse_FWD_START(event):
    global KeyPressResponse_FWD_NeedsToBeChangedFlag

    KeyPressResponse_FWD_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_FWD_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_FWD_STOP(event):
    global KeyPressResponse_FWD_NeedsToBeChangedFlag

    KeyPressResponse_FWD_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_FWD_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_REV_START(event):
    global KeyPressResponse_REV_NeedsToBeChangedFlag

    KeyPressResponse_REV_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_REV_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_REV_STOP(event):
    global KeyPressResponse_REV_NeedsToBeChangedFlag

    KeyPressResponse_REV_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_REV_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_RIGHT_START(event):
    global KeyPressResponse_RIGHT_NeedsToBeChangedFlag

    KeyPressResponse_RIGHT_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_RIGHT_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_RIGHT_STOP(event):
    global KeyPressResponse_RIGHT_NeedsToBeChangedFlag

    KeyPressResponse_RIGHT_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_RIGHT_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_LEFT_START(event):
    global KeyPressResponse_LEFT_NeedsToBeChangedFlag

    KeyPressResponse_LEFT_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_LEFT_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_LEFT_STOP(event):
    global KeyPressResponse_LEFT_NeedsToBeChangedFlag

    KeyPressResponse_LEFT_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_LEFT_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_TorqueEnable_START(event):
    global KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag

    KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_TorqueEnable_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_TorqueEnable_STOP(event):
    global KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag

    dummy = 0
    #KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_TorqueEnable_STOP event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_ZeroLQR_START(event):
    global KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag

    KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag = 1

    #print("KeyPressResponse_ZeroLQR_START event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def KeyPressResponse_ZeroLQR_STOP(event):
    global KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag

    dummy = 0
    #KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag = 0

    #print("KeyPressResponse_ZeroLQR_STOP event fired!")
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
    global DataStreamingFrequency_CalculatedFromMainThread_Filtered

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

    global EntryListWithBlinking_ReubenPython2and3ClassObject
    global EntryListWithBlinking_OPEN_FLAG
    global SHOW_IN_GUI_EntryListWithBlinking_FLAG

    global CSVdataLogger_ReubenPython3ClassObject
    global CSVdataLogger_OPEN_FLAG
    global SHOW_IN_GUI_CSVdataLogger_FLAG

    global BarGraphDisplay_ReubenPython3ClassObject
    global BarGraphDisplay_OPEN_FLAG
    global SHOW_IN_GUI_BarGraphDisplay_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global KeyboardInfo_Label
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString
    global Keyboard_KeysToTeleopControlsMapping_DictOfDicts
    global KeyPressResponse_FWD_NeedsToBeChangedFlag
    global KeyPressResponse_REV_NeedsToBeChangedFlag
    global KeyPressResponse_LEFT_NeedsToBeChangedFlag
    global KeyPressResponse_RIGHT_NeedsToBeChangedFlag
    global KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag
    global KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag

    global DebuggingInfo_Label

    global ControlInput
    global ControlInput_StartingValue
    global ControlInput_AcceptableValues

    global ControlAlgorithm
    global ControlAlgorithm_StartingValue
    global ControlAlgorithm_AcceptableValues
    
    #global SharedGlobals_SelfBalancingRobot1_MainThread_TimeToSleepEachLoop
    #global WiFiVINTthumbstick_PositionList_ScalingFactorList
    #global WiFiVINTthumbstick_RollPitchYaw_AbtXYZ_List_ScalingFactorList

    global LoopCounter_CalculatedFromGUIthread
    global CurrentTime_CalculatedFromGUIthread
    global StartingTime_CalculatedFromGUIthread
    global LastTime_CalculatedFromGUIthread
    global DataStreamingFrequency_CalculatedFromGUIthread_Filtered
    global DataStreamingDeltaT_CalculatedFromGUIthread

    global LQR_PitchControl_GainVectorElement_Ktheta_0
    global LQR_PitchControl_GainVectorElement_Ktheta_1
    global LQR_PitchControl_GainVectorElement_Ktheta_2
    global LQR_PitchControl_GainVectorElement_Ktheta_3
    global LQR_YawControl_GainVectorElement_Kdelta_0
    global LQR_YawControl_GainVectorElement_Kdelta_1
    global Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION
    global Pitch_PosControl_PID_CommandToMotor_Term_1
    global Pitch_PosControl_PID_CommandToMotor_Term_2
    global Pitch_PosControl_PID_CommandToMotor_Term_3
    global Pitch_PosControl_PID_CommandToMotor_Term_5
    global Pitch_PosControl_PID_CommandToMotor_Term_6
    global LQR_ControlLaw_Term_1
    global LQR_ControlLaw_Term_2
    global LQR_ControlLaw_Term_3
    global LQR_ControlLaw_Term_4
    global LQR_ControlLaw_Term_5
    global LQR_ControlLaw_Term_6

    global Wheel_Theta_RL_Radians_Actual
    global Wheel_Theta_RR_Radians_Actual

    global Wheel_Omega_Theta_RL_RadiansPerSec_Actual
    global Wheel_Omega_Theta_RL_RadiansPerSec_Actual

    global Position_X_RM_Meters_Actual
    global Position_X_RMC_Meters_Commanded

    global Velocity_V_RM_MetersPerSec_Actual
    global Velocity_V_RMC_MetersPerSec_Commanded

    global PitchAngle_Theta_Deg_Actual
    global PitchAngle_Theta_Radians_Actual

    global PitchAngle_Theta_Deg_Commanded
    global PitchAngle_Theta_Radians_Commanded

    global PitchAngularRate_ThetaDot_DegreesPerSecond_Actual
    global PitchAngularRate_ThetaDot_RadiansPerSec_Actual

    global PitchAngularRate_ThetaDot_DegreesPerSecond_Commanded
    global PitchAngularRate_ThetaDot_RadiansPerSec_Commanded

    global YawAngle_Delta_Deg_Actual
    global YawAngle_Delta_Radians_Actual

    global YawAngle_Delta_Deg_Commanded
    global YawAngle_Delta_Radians_Commanded

    global YawAngularRate_DeltaDot_RadiansPerSec_Actual
    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded

    global YawAngularRate_DeltaDot_DegreesPerSecond_Actual
    global YawAngularRate_DeltaDot_DegreesPerSecond_Commanded

    global TorqueToBeCommanded_Motor0
    global TorqueToBeCommanded_Motor1

    global EnableMotors_Button
    global EnableMotorState_0
    global EnableMotorState_1

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            #########################################################
            CurrentTime_CalculatedFromGUIthread = getPreciseSecondsTimeStampString() - StartingTime_CalculatedFromGUIthread
            UpdateFrequencyCalculation_GUIthread_Filtered()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            DebuggingInfo_Label["text"] = "MainThread, Time: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(CurrentTime_CalculatedFromMainThread, 0, 3) +\
                            "\t\t\tFrequency: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DataStreamingFrequency_CalculatedFromMainThread_Filtered, 0, 3) +\
                            "\nGUIthread, Time: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(CurrentTime_CalculatedFromGUIthread, 0, 3) +\
                            "\t\t\tFrequency: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(DataStreamingFrequency_CalculatedFromGUIthread_Filtered, 0, 3) +\
                            "\nControlInput: " + ControlInput + \
                            "\nControlAlgorithm: " + ControlAlgorithm + \
                            "\n\n\n" +\
                            "" +\
                            "\nWheel_Theta_RL_Radians_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Wheel_Theta_RL_Radians_Actual, 3, 3) + \
                            "\nWheel_Theta_RR_Radians_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Wheel_Theta_RR_Radians_Actual, 3, 3) + \
                            "\n" +\
                            "\nWheel_Wheel_Omega_Theta_RL_RadiansPerSec_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Wheel_Omega_Theta_RL_RadiansPerSec_Actual, 3, 3) + \
                            "\nWheel_Wheel_Omega_Theta_RR_RadiansPerSec_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Wheel_Omega_Theta_RR_RadiansPerSec_Actual, 3, 3) + \
                            "\n" +\
                            "\nPosition_X_RM_Meters_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Position_X_RM_Meters_Actual, 3, 3) + \
                            "\t\tPosition_X_RMC_Meters_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Position_X_RMC_Meters_Commanded, 3, 3) + \
                            "\n" +\
                            "\nVelocity_V_RM_MetersPerSec_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Velocity_V_RM_MetersPerSec_Actual, 3, 3) + \
                            "\t\t\t\tVelocity_V_RMC_MetersPerSec_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(Velocity_V_RMC_MetersPerSec_Commanded, 3, 3) + \
                            "\n" +\
                            "\nPitchAngle_Theta_Deg_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PitchAngle_Theta_Deg_Actual, 3, 3) + \
                            "\t\tPitchAngle_Theta_Deg_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(PitchAngle_Theta_Deg_Commanded, 3, 3) + \
                            "\n" +\
                            "\nYawAngle_Delta_Deg_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngle_Delta_Deg_Actual, 3, 3) + \
                            "\t\tYawAngle_Delta_Deg_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngle_Delta_Deg_Commanded, 3, 3) + \
                            "\n" +\
                            "\nYawAngularRate_DeltaDot_DegreesPerSecond_Actual: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngularRate_DeltaDot_DegreesPerSecond_Actual, 3, 3) + \
                            "\t\tYawAngularRate_DeltaDot_DegreesPerSecond_Commanded: " + ConvertFloatToStringWithNumberOfLeadingNumbersAndDecimalPlaces_NumberOrListInput(YawAngularRate_DeltaDot_DegreesPerSecond_Commanded, 3, 3) + \
                            "\n" +\
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
            if EnableMotorState_0 == 1 and EnableMotorState_1 == 1:
                EnableMotors_Button["bg"] = TKinter_LightGreenColor
                EnableMotors_Button["text"] = "2 Motors enabled"

            elif EnableMotorState_0 == 1 or EnableMotorState_1 == 1:
                EnableMotors_Button["bg"] = TKinter_LightYellowColor
                EnableMotors_Button["text"] = "1 Motor enabled"

            else:
                EnableMotors_Button["bg"] = TKinter_LightRedColor
                EnableMotors_Button["text"] = "2 Motors disabled"
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
            KeyboardInfo_Label["text"] = "Keyboard flags: " + str([KeyPressResponse_FWD_NeedsToBeChangedFlag,
                                                                    KeyPressResponse_REV_NeedsToBeChangedFlag,
                                                                    KeyPressResponse_LEFT_NeedsToBeChangedFlag,
                                                                    KeyPressResponse_RIGHT_NeedsToBeChangedFlag,
                                                                    KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag,
                                                                    KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag]) + \
                            "\nKeyboard_KeysToTeleopControlsMapping_DictOfDicts: " + \
                            "\n" + Keyboard_KeysToTeleopControlsMapping_DictOfDicts_FormattedAsNicelyPrintedString
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
            if EntryListWithBlinking_OPEN_FLAG == 1 and SHOW_IN_GUI_EntryListWithBlinking_FLAG == 1:
                EntryListWithBlinking_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if CSVdataLogger_OPEN_FLAG == 1 and SHOW_IN_GUI_CSVdataLogger_FLAG == 1:
                CSVdataLogger_ReubenPython3ClassObject.GUI_update_clock()
            #########################################################
            #########################################################

            #########################################################
            #########################################################
            if BarGraphDisplay_OPEN_FLAG == 1:

                if ControlAlgorithm == "PID":
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_1", Pitch_PosControl_PID_CommandToMotor_Term_1) #Too slow to update from non-GUI loop.
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_2", Pitch_PosControl_PID_CommandToMotor_Term_2)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_3", Pitch_PosControl_PID_CommandToMotor_Term_3)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_4", 0.0)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_5", Pitch_PosControl_PID_CommandToMotor_Term_5)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_6", Pitch_PosControl_PID_CommandToMotor_Term_6)

                elif ControlAlgorithm == "LQR":
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_1", LQR_ControlLaw_Term_1) #Too slow to update from non-GUI loop.
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_2", LQR_ControlLaw_Term_2)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_3", LQR_ControlLaw_Term_3)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_4", LQR_ControlLaw_Term_4)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_5", LQR_ControlLaw_Term_5)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_6", LQR_ControlLaw_Term_6)
                else:
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_1", 0.0) #Too slow to update from non-GUI loop.
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_2", 0.0)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_3", 0.0)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_4", 0.0)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_5", 0.0)
                    BarGraphDisplay_ReubenPython3ClassObject.UpdateValue("LQR_6", 0.0)

                BarGraphDisplay_ReubenPython3ClassObject.GUI_update_clock()
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
    ExtraProgramControlGuiFrame.grid(row=GUI_ROW_ExtraProgramControlGuiFrame,
                                     column=GUI_COLUMN_ExtraProgramControlGuiFrame,
                                     padx=GUI_PADX_ExtraProgramControlGuiFrame,
                                     pady=GUI_PADY_ExtraProgramControlGuiFrame,
                                     rowspan=GUI_ROWSPAN_ExtraProgramControlGuiFrame,
                                     columnspan=GUI_COLUMNSPAN_ExtraProgramControlGuiFrame,
                                     sticky='w')
    ###########################################################
    ###########################################################

    ############################################
    ############################################
    global ExitProgramButton
    ExitProgramButton = Button(ExtraProgramControlGuiFrame, text="Exit Program", state="normal", width=GUIbuttonWidth, command=lambda i=1: ExitProgram_Callback())
    ExitProgramButton.grid(row=0, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    ExitProgramButton.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global JSONfiles_NeedsToBeLoadedFlagButton
    JSONfiles_NeedsToBeLoadedFlagButton = Button(ExtraProgramControlGuiFrame, text="Load JSON files", state="normal", width=GUIbuttonWidth, command=lambda i=1: JSONfiles_NeedsToBeLoadedFlag_ButtonResponse())
    JSONfiles_NeedsToBeLoadedFlagButton.grid(row=1, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    JSONfiles_NeedsToBeLoadedFlagButton.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global ZeroSpatialPrecision333Gyros_Button
    ZeroSpatialPrecision333Gyros_Button = Button(ExtraProgramControlGuiFrame, text="Zero Spatial Gyros", state="normal", width=GUIbuttonWidth, command=lambda i=1: ZeroSpatialPrecision333Gyros_ButtonResponse())
    ZeroSpatialPrecision333Gyros_Button.grid(row=0, column=1, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    ZeroSpatialPrecision333Gyros_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global ZeroSpatialPrecision333Algorithm_Button
    ZeroSpatialPrecision333Algorithm_Button = Button(ExtraProgramControlGuiFrame, text="Zero Spatial Alg", state="normal", width=GUIbuttonWidth, command=lambda i=1: ZeroSpatialPrecision333Algorithm_ButtonResponse())
    ZeroSpatialPrecision333Algorithm_Button.grid(row=0, column=2, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    ZeroSpatialPrecision333Algorithm_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ############################################
    ############################################
    global ZeroLQR_Button
    ZeroLQR_Button = Button(ExtraProgramControlGuiFrame, text="ZeroLQR", state="normal", width=GUIbuttonWidth, command=lambda i=1: ZeroLQR_ButtonResponse())
    ZeroLQR_Button.grid(row=0, column=3, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    ZeroLQR_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    '''
    ############################################
    ############################################
    global ZeroPitch_Button
    ZeroPitch_Button = Button(ExtraProgramControlGuiFrame, text="ZeroPitch", state="normal", width=GUIbuttonWidth, command=lambda i=1: ZeroPitch_ButtonResponse())
    ZeroPitch_Button.grid(row=0, column=4, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    ZeroPitch_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################
    '''

    ############################################
    ############################################
    global EnableMotors_Button
    EnableMotors_Button = Button(ExtraProgramControlGuiFrame, text="Enable Motors", state="normal", width=GUIbuttonWidth, command=lambda i=1: EnableMotors_ButtonResponse())
    EnableMotors_Button.grid(row=1, column=1, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=1, rowspan=1)
    EnableMotors_Button.config(font=("Helvetica", GUIbuttonFontSize))
    ############################################
    ############################################

    ###########################################################
    ###########################################################
    global DebuggingInfo_Label
    DebuggingInfo_Label = Label(ExtraProgramControlGuiFrame, text="DebuggingInfo_Label", width=120, font=("Helvetica", 10))  #
    DebuggingInfo_Label.grid(row=3, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, columnspan=10, rowspan=1)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlGuiFrame
    ControlGuiFrame = Frame(ExtraProgramControlGuiFrame)
    ControlGuiFrame.grid(row=2, column=0, padx=GUIbuttonPadX, pady=GUIbuttonPadY, rowspan=1, columnspan=1, sticky='w')
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlInput_Radiobutton_SelectionVar
    ControlInput_Radiobutton_SelectionVar = StringVar()

    ControlInput_Radiobutton_SelectionVar.set(ControlInput_StartingValue)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlInput_AcceptableValues

    global ControlInput_RadioButtonObjectsList
    ControlInput_RadioButtonObjectsList = list()
    for Index, ControlInputString in enumerate(ControlInput_AcceptableValues):
        ControlInput_RadioButtonObjectsList.append(Radiobutton(ControlGuiFrame,
                                                      text=ControlInputString,
                                                      state="normal",
                                                      width=15,
                                                      anchor="w",
                                                      variable=ControlInput_Radiobutton_SelectionVar,
                                                      value=ControlInputString,
                                                      command=lambda name=ControlInputString: ControlInput_Radiobutton_Response(name)))
        ControlInput_RadioButtonObjectsList[Index].grid(row=0, column=Index, padx=1, pady=1, columnspan=1, rowspan=1)
        #if ControlInput_StartingValue == "ControlInputString":
        #    ControlInput_RadioButtonObjectsList[Index].select()
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlAlgorithm_Radiobutton_SelectionVar
    ControlAlgorithm_Radiobutton_SelectionVar = StringVar()

    ControlAlgorithm_Radiobutton_SelectionVar.set(ControlAlgorithm_StartingValue)
    ###########################################################
    ###########################################################

    ###########################################################
    ###########################################################
    global ControlAlgorithm_AcceptableValues

    global ControlAlgorithm_RadioButtonObjectsList
    ControlAlgorithm_RadioButtonObjectsList = list()
    for Index, ControlAlgorithmString in enumerate(ControlAlgorithm_AcceptableValues):
        ControlAlgorithm_RadioButtonObjectsList.append(Radiobutton(ControlGuiFrame,
                                                      text=ControlAlgorithmString,
                                                      state="normal",
                                                      width=15,
                                                      anchor="w",
                                                      variable=ControlAlgorithm_Radiobutton_SelectionVar,
                                                      value=ControlAlgorithmString,
                                                      command=lambda name=ControlAlgorithmString: ControlAlgorithm_Radiobutton_Response(name)))
        ControlAlgorithm_RadioButtonObjectsList[Index].grid(row=1, column=Index, padx=1, pady=1, columnspan=1, rowspan=1)
        #if ControlAlgorithm_StartingValue == "ControlAlgorithmString":
        #    ControlAlgorithm_RadioButtonObjectsList[Index].select()
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

    ########################################################### THIS BLOCK MUST COME 2ND-TO-LAST IN def  GUI_Thread() IF USING TABS.
    ###########################################################
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title(GUItitleString)
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos))  # set the dimensions of the screen and where it is placed
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
def ControlInput_Radiobutton_Response(name):
    global ControlInput_Radiobutton_SelectionVar
    global ControlInput
    global ControlInput_NeedsToBeChangedFlag

    #print("name: " + name)

    ControlInput = ControlInput_Radiobutton_SelectionVar.get()
    ControlInput_NeedsToBeChangedFlag = 1
    print("ControlInput set to: " + ControlInput)
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ControlAlgorithm_Radiobutton_Response(name):
    global ControlAlgorithm_Radiobutton_SelectionVar
    global ControlAlgorithm
    global ControlAlgorithm_NeedsToBeChangedFlag

    #print("name: " + name)

    ControlAlgorithm = ControlAlgorithm_Radiobutton_SelectionVar.get()
    ControlAlgorithm_NeedsToBeChangedFlag = 1
    print("ControlAlgorithm set to: " + ControlAlgorithm)
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
    global ToggleEnableForBothMotors_EventNeedsToBeFiredFlag

    ToggleEnableForBothMotors_EventNeedsToBeFiredFlag = 1
    
    #MyPrint_ReubenPython2and3ClassObject.my_print("EnableMotors_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ToggleEnableForBothMotors():
    global EnableMotorState_0
    global EnableMotorState_1

    ####################################
    if EnableMotorState_0 == 1:
        EnableMotor(0, 0)
    else:
        EnableMotor(0, 1)
    ####################################

    ####################################
    if EnableMotorState_1 == 1:
        EnableMotor(1, 0)
    else:
        EnableMotor(1, 1)
    ####################################

#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def EnableMotor(MotorNumber_Input, EnableMotorState_Input):
    global EnableMotorState_0
    global EnableMotorState_NeedsToBeChangedFlag_0
    global EnableMotorState_1
    global EnableMotorState_NeedsToBeChangedFlag_1

    MotorNumber_Input = int(MotorNumber_Input)
    EnableMotorState_Input = int(EnableMotorState_Input)

    if MotorNumber_Input in [0, 1]:

        if EnableMotorState_Input in [0, 1]:
            
            if MotorNumber_Input == 0:
                EnableMotorState_0 = EnableMotorState_Input
                EnableMotorState_NeedsToBeChangedFlag_0 = 1
                
            if MotorNumber_Input == 1:
                EnableMotorState_1 = EnableMotorState_Input
                EnableMotorState_NeedsToBeChangedFlag_1 = 1
    
        else:
            MyPrint_ReubenPython2and3ClassObject.my_print("EnableMotors 'EnableMotorState_Input' input must be in [0, 1]")

    else:
        MyPrint_ReubenPython2and3ClassObject.my_print("EnableMotors 'MotorNumber_Input' input must be in [0, 1]")
        
    #MyPrint_ReubenPython2and3ClassObject.my_print("EnableMotors event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ZeroSpatialPrecision333Gyros_ButtonResponse():
    global SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag

    SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag = 1

    #MyPrint_ReubenPython2and3ClassObject.my_print("ZeroSpatialPrecision333Gyros_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ZeroSpatialPrecision333Algorithm_ButtonResponse():
    global SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag

    SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag = 1

    #MyPrint_ReubenPython2and3ClassObject.my_print("ZeroSpatialPrecision333Algorithm_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ZeroLQR_ButtonResponse():
    global ZeroLQR_EventNeedsToBeFiredFlag

    ZeroLQR_EventNeedsToBeFiredFlag = 1

    #MyPrint_ReubenPython2and3ClassObject.my_print("ZeroLQR_ButtonResponse event fired!")
#######################################################################################################################
#######################################################################################################################

#######################################################################################################################
#######################################################################################################################
def ZeroPitch_ButtonResponse():
    global SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag
    global SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag

    #SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag = 1
    #SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag = 1
    pass

    #MyPrint_ReubenPython2and3ClassObject.my_print("ZeroPitch_ButtonResponse event fired!")
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

    global USE_BarGraphDisplay_FLAG
    global BarGraphDisplay_OPEN_FLAG
    global SHOW_IN_GUI_BarGraphDisplay_FLAG

    global USE_CSVdataLogger_FLAG
    global CSVdataLogger_OPEN_FLAG
    global SHOW_IN_GUI_CSVdataLogger_FLAG

    global USE_MyPrint_FLAG
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    global GUItabObjectsOrderedDict

    try:

        ###########################################################
        ###########################################################
        if len(GUItabObjectsOrderedDict) == 0: #Not yet populated
            GUItabObjectsOrderedDict = OrderedDict([("MainControls", dict([("UseFlag", 1), ("ShowFlag", 1), ("GUItabObjectName", "MainControls"), ("GUItabNameToDisplay", "MainControls"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                    ("CSVdataLogger", dict([("UseFlag", USE_CSVdataLogger_FLAG), ("ShowFlag", SHOW_IN_GUI_CSVdataLogger_FLAG), ("GUItabObjectName", "CSVdataLogger"), ("GUItabNameToDisplay", "CSVdataLogger"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                    ("WiFiVINTthumbstick", dict([("UseFlag", USE_WiFiVINTthumbstick_FLAG), ("ShowFlag", SHOW_IN_GUI_WiFiVINTthumbstick_FLAG), ("GUItabObjectName", "WiFiVINTthumbstick"), ("GUItabNameToDisplay", "Joystick"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("RoboteqBLDCcontroller_0", dict([("UseFlag", USE_RoboteqBLDCcontroller_FLAG_0), ("ShowFlag", SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_0), ("GUItabObjectName", "RoboteqBLDCcontroller_0"), ("GUItabNameToDisplay", "Roboteq0"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("RoboteqBLDCcontroller_1", dict([("UseFlag", USE_RoboteqBLDCcontroller_FLAG_1), ("ShowFlag", SHOW_IN_GUI_RoboteqBLDCcontroller_FLAG_1), ("GUItabObjectName", "RoboteqBLDCcontroller_1"), ("GUItabNameToDisplay", "Roboteq1"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("SpatialPrecision333", dict([("UseFlag", USE_SpatialPrecision333_FLAG), ("ShowFlag", SHOW_IN_GUI_SpatialPrecision333_FLAG), ("GUItabObjectName", "SpatialPrecision333"), ("GUItabNameToDisplay", "Spatial"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("Keyboard", dict([("UseFlag", USE_Keyboard_FLAG), ("ShowFlag", SHOW_IN_GUI_Keyboard_FLAG), ("GUItabObjectName", "Keyboard"), ("GUItabNameToDisplay", "Keyboard"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("DC30AmpCurrentSensor", dict([("UseFlag", USE_DC30AmpCurrentSensor_FLAG),  ("ShowFlag", SHOW_IN_GUI_DC30AmpCurrentSensor_FLAG), ("GUItabObjectName", "DC30AmpCurrentSensor"), ("GUItabNameToDisplay", "Current"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("BarGraphDisplay", dict([("UseFlag", USE_BarGraphDisplay_FLAG),  ("ShowFlag", SHOW_IN_GUI_BarGraphDisplay_FLAG), ("GUItabObjectName", "BarGraphDisplay"), ("GUItabNameToDisplay", "BarGraph"), ("IsTabCreatedFlag", 0), ("TabObject", None)])),
                                   ("MyPrint", dict([("UseFlag", USE_MyPrint_FLAG), ("ShowFlag", SHOW_IN_GUI_MyPrint_FLAG), ("GUItabObjectName", "MyPrint"), ("GUItabNameToDisplay", "MyPrint"), ("IsTabCreatedFlag", 0), ("TabObject", None)]))])
        ###########################################################
        ###########################################################

        ###########################################################
        ###########################################################
        GUItabObjectsOrderedDict["MainControls"]["OpenFlag"] = 1
        GUItabObjectsOrderedDict["CSVdataLogger"]["OpenFlag"] = CSVdataLogger_OPEN_FLAG
        GUItabObjectsOrderedDict["WiFiVINTthumbstick"]["OpenFlag"] = WiFiVINTthumbstick_OPEN_FLAG
        GUItabObjectsOrderedDict["RoboteqBLDCcontroller_0"]["OpenFlag"] = RoboteqBLDCcontroller_OPEN_FLAG_0
        GUItabObjectsOrderedDict["RoboteqBLDCcontroller_1"]["OpenFlag"] = RoboteqBLDCcontroller_OPEN_FLAG_1
        GUItabObjectsOrderedDict["SpatialPrecision333"]["OpenFlag"] = SpatialPrecision333_OPEN_FLAG
        GUItabObjectsOrderedDict["Keyboard"]["OpenFlag"] = Keyboard_OPEN_FLAG
        GUItabObjectsOrderedDict["DC30AmpCurrentSensor"]["OpenFlag"] = DC30AmpCurrentSensor_OPEN_FLAG
        GUItabObjectsOrderedDict["BarGraphDisplay"]["OpenFlag"] = BarGraphDisplay_OPEN_FLAG
        GUItabObjectsOrderedDict["MyPrint"]["OpenFlag"] = MyPrint_OPEN_FLAG
        ###########################################################
        ###########################################################

        #print("UpdateGUItabObjectsOrderedDict, GUItabObjectsOrderedDict: " + str(GUItabObjectsOrderedDict))

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
    global USE_EntryListWithBlinking_FLAG
    global USE_MyPlotterPureTkinterStandAloneProcess_FLAG
    global USE_MyPrint_FLAG
    global USE_CSVdataLogger_FLAG
    global USE_Keyboard_FLAG
    global USE_BarGraphDisplay_FLAG
    global USE_GUI_FLAG
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
    global SHOW_IN_GUI_EntryListWithBlinking_FLAG
    global SHOW_IN_GUI_Keyboard_FLAG
    global SHOW_IN_GUI_BarGraphDisplay_FLAG
    global SHOW_IN_GUI_CSVdataLogger_FLAG
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
    global EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth
    global EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth

    global GUI_ROW_ExtraProgramControlGuiFrame
    global GUI_COLUMN_ExtraProgramControlGuiFrame
    global GUI_PADX_ExtraProgramControlGuiFrame
    global GUI_PADY_ExtraProgramControlGuiFrame
    global GUI_ROWSPAN_ExtraProgramControlGuiFrame
    global GUI_COLUMNSPAN_ExtraProgramControlGuiFrame

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
    
    global GUI_ROW_EntryListWithBlinking
    global GUI_COLUMN_EntryListWithBlinking
    global GUI_PADX_EntryListWithBlinking
    global GUI_PADY_EntryListWithBlinking
    global GUI_ROWSPAN_EntryListWithBlinking
    global GUI_COLUMNSPAN_EntryListWithBlinking

    global GUI_ROW_CSVdataLogger
    global GUI_COLUMN_CSVdataLogger
    global GUI_PADX_CSVdataLogger
    global GUI_PADY_CSVdataLogger
    global GUI_ROWSPAN_CSVdataLogger
    global GUI_COLUMNSPAN_CSVdataLogger

    global GUI_ROW_BarGraphDisplay
    global GUI_COLUMN_BarGraphDisplay
    global GUI_PADX_BarGraphDisplay
    global GUI_PADY_BarGraphDisplay
    global GUI_ROWSPAN_BarGraphDisplay
    global GUI_COLUMNSPAN_BarGraphDisplay

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
    global RoboteqBLDCcontroller_VariableStreamingSendDataEveryDeltaT_MillisecondsInt_0
    global RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_0
    global RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_0
    global RoboteqBLDCcontroller_SerialRxBufferSize_0
    global RoboteqBLDCcontroller_SerialTxBufferSize_0
    global RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_0
    global RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_0
    global RoboteqBLDCcontroller_NumberOfMagnetsInMotor_0
    global RoboteqBLDCcontroller_PID_Kp_0
    global RoboteqBLDCcontroller_PID_Ki_0
    global RoboteqBLDCcontroller_PID_Kd_0
    global RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_0
    global RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_0
    global RoboteqBLDCcontroller_SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag_0

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
    global RoboteqBLDCcontroller_VariableStreamingSendDataEveryDeltaT_MillisecondsInt_1
    global RoboteqBLDCcontroller_DedicatedRxThread_TimeToSleepEachLoop_1
    global RoboteqBLDCcontroller_DedicatedTxThread_TimeToSleepEachLoop_1
    global RoboteqBLDCcontroller_SerialRxBufferSize_1
    global RoboteqBLDCcontroller_SerialTxBufferSize_1
    global RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_1
    global RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_1
    global RoboteqBLDCcontroller_NumberOfMagnetsInMotor_1
    global RoboteqBLDCcontroller_PID_Kp_1
    global RoboteqBLDCcontroller_PID_Ki_1
    global RoboteqBLDCcontroller_PID_Kd_1
    global RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_1
    global RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_1
    global RoboteqBLDCcontroller_SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag_1

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
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag
    global SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda
    global SpatialPrecision333_Spatial_CallbackUpdateDeltaTmilliseconds
    global SpatialPrecision333_DataCollectionDurationInSecondsForSnapshottingAndZeroing
    global SpatialPrecision333_MainThread_TimeToSleepEachLoop
    global SpatialPrecision333_HeatingEnabledToStabilizeSensorTemperature
    global SpatialPrecision333_ZeroGyrosAtStartOfProgramFlag
    global SpatialPrecision333_ZeroAlgorithmAtStartOfProgramFlag
    global SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset
    global SpatialPrecision333_AHRS_Parameters_angularVelocityThreshold
    global SpatialPrecision333_AHRS_Parameters_angularVelocityDeltaThreshold
    global SpatialPrecision333_AHRS_Parameters_accelerationThreshold
    global SpatialPrecision333_AHRS_Parameters_magTime
    global SpatialPrecision333_AHRS_Parameters_accelTime
    global SpatialPrecision333_AHRS_Parameters_biasTime

    LoadAndParseJSONfile_SpatialPrecision333()
    #################################################

    #################################################
    global SavingSettings_user_notes
    global CSVdataLogger_NameToDisplay_UserSet
    global CSVdataLogger_CSVfile_DirectoryPath
    global CSVdataLogger_FileNamePrefix
    global CSVdataLogger_VariableNamesForHeaderList
    global CSVdataLogger_MainThread_TimeToSleepEachLoop
    global CSVdataLogger_SaveOnStartupFlag

    LoadAndParseJSONfile_SavingSettings()
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
    global ControlInput_StartingValue
    global ControlInput_AcceptableValues
    
    global ControlAlgorithm_StartingValue
    global ControlAlgorithm_AcceptableValues
    
    global ENABLE_MOTORS_AT_STARTUP_FLAG

    global SelfBalancingRobot1_MainThread_TimeToSleepEachLoop
    global DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda

    global DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda_last #NOT imported from JSON file
    DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda_last = 1.0

    global DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda

    global DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda_last  # NOT imported from JSON file
    DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda_last = 1.0

    global Velocity_V_RMC_MetersPerSec_Commanded_DeadbandThreshold
    global Velocity_V_RMC_MetersPerSec_Commanded_JoystickToMetersPerSecGain

    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded_DeadbandThreshold
    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded_JoystickToRadiansPerSecGain

    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseMedianFilterFlag
    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_UseExponentialSmoothingFilterFlag
    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda

    global Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last  # NOT imported from JSON file
    Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last = 1.0

    global YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_UseMedianFilterFlag
    global YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_UseExponentialSmoothingFilterFlag
    global YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda

    global YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last  # NOT imported from JSON file
    YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last = 1.0

    global LQR_ParametersToBeLoaded_Directions
    global LQR_PitchControl_GainVectorElement_Ktheta_0
    global LQR_PitchControl_GainVectorElement_Ktheta_1
    global LQR_PitchControl_GainVectorElement_Ktheta_2
    global LQR_PitchControl_GainVectorElement_Ktheta_3
    global LQR_YawControl_GainVectorElement_Kdelta_0
    global LQR_YawControl_GainVectorElement_Kdelta_1
    global Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION
    global YawAngle_Delta_Radians_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION

    global Pitch_ParametersToBeLoaded_Directions
    global Pitch_PosControl_PID_gain_Kp
    global Pitch_PosControl_PID_gain_Ki
    global Pitch_PosControl_PID_gain_Kd
    global Pitch_PosControl_PID_ErrorSum_Max

    global MaxCommandFromControlLaw_Motor0
    global MaxCommandFromControlLaw_Motor1

    global SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle
    global SINUSOIDAL_MOTION_INPUT_MinValue
    global SINUSOIDAL_MOTION_INPUT_MaxValue

    LoadAndParseJSONfile_ControlLawParameters()

    if ControlInput_StartingValue not in ControlInput_AcceptableValues:
        print("ERROR: ControlInput_StartingValue but be in " + str(ControlInput_AcceptableValues))
        
    if ControlAlgorithm_StartingValue not in ControlAlgorithm_AcceptableValues:
        print("ERROR: ControlAlgorithm_StartingValue but be in " + str(ControlAlgorithm_AcceptableValues))
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

    global ControlInput
    ControlInput = ControlInput_StartingValue

    global ControlInput_NeedsToBeChangedFlag
    ControlInput_NeedsToBeChangedFlag = 0
    
    global ControlAlgorithm
    ControlAlgorithm = ControlAlgorithm_StartingValue

    global ControlAlgorithm_NeedsToBeChangedFlag
    ControlAlgorithm_NeedsToBeChangedFlag = 0
    
    global LQR_ControlLaw_Term_1
    LQR_ControlLaw_Term_1 = 0.0
    
    global LQR_ControlLaw_Term_2
    LQR_ControlLaw_Term_2 = 0.0
    
    global LQR_ControlLaw_Term_3
    LQR_ControlLaw_Term_3 = 0.0

    global LQR_ControlLaw_Term_4
    LQR_ControlLaw_Term_4 = 0.0

    global LQR_ControlLaw_Term_5
    LQR_ControlLaw_Term_5 = 0.0
    
    global LQR_ControlLaw_Term_6
    LQR_ControlLaw_Term_6 = 0.0
    #################################################
    #################################################

    #################################################
    #################################################
    global BarGraphDisplay_ReubenPython3ClassObject

    global BarGraphDisplay_OPEN_FLAG
    BarGraphDisplay_OPEN_FLAG = -1
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
    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_0
    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_0 = 0.0

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
    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Radians_0
    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_0
    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_0
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_0 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Time_0
    RoboteqBLDCcontroller_MostRecentDict_Time_0 = 0.0
    
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

    global RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_0
    RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_0 = 0
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
    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1
    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1 = 0.0

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
    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1
    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1
    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1
    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1 = 0.0
    
    global RoboteqBLDCcontroller_MostRecentDict_Time_1
    RoboteqBLDCcontroller_MostRecentDict_Time_1 = 0.0
    
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

    global RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_1
    RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_1 = 0
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
    SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict = dict([("RollPitchYaw_AbtXYZ_List_Degrees",[0.0]*3),("RollPitchYaw_AbtXYZ_List_Radians",[0.0]*3)])

    global SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict
    SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict = dict([("RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond",[0.0]*3),("RollPitchYaw_Rate_AbtXYZ_List_RadiansPerSecond",[0.0]*3)])

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions
    SpatialPrecision333_MostRecentDict_DataStreamingFrequency_TimestampFromPhidget_AlgorithmData_Quaternions = -11111.0

    global SpatialPrecision333_MostRecentDict_Time
    SpatialPrecision333_MostRecentDict_Time = -11111.0

    global SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag
    SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag = 0
    
    global SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag
    SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag = 0
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
    global EntryListWithBlinking_ReubenPython2and3ClassObject

    global EntryListWithBlinking_OPEN_FLAG
    EntryListWithBlinking_OPEN_FLAG = -1

    global EntryListWithBlinking_MostRecentDict
    EntryListWithBlinking_MostRecentDict = dict()

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber = 0

    global EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last
    EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global CSVdataLogger_ReubenPython3ClassObject

    global CSVdataLogger_OPEN_FLAG
    CSVdataLogger_OPEN_FLAG = -1

    global CSVdataLogger_MostRecentDict
    CSVdataLogger_MostRecentDict = dict()

    global CSVdataLogger_MostRecentDict_Time
    CSVdataLogger_MostRecentDict_Time = -11111.0

    global CSVdataLogger_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread
    CSVdataLogger_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = -11111.0

    global CSVdataLogger_MostRecentDict_AcceptNewDataFlag
    CSVdataLogger_MostRecentDict_AcceptNewDataFlag = -1

    global CSVdataLogger_MostRecentDict_SaveFlag
    CSVdataLogger_MostRecentDict_SaveFlag = -1

    global CSVdataLogger_MostRecentDict_DataQueue_qsize
    CSVdataLogger_MostRecentDict_DataQueue_qsize = -1

    global CSVdataLogger_MostRecentDict_VariableNamesForHeaderList
    CSVdataLogger_MostRecentDict_VariableNamesForHeaderList = []

    global CSVdataLogger_MostRecentDict_FilepathFull
    CSVdataLogger_MostRecentDict_FilepathFull = ""
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

    global KeyPressResponse_FWD_NeedsToBeChangedFlag
    KeyPressResponse_FWD_NeedsToBeChangedFlag = 0

    global KeyPressResponse_REV_NeedsToBeChangedFlag
    KeyPressResponse_REV_NeedsToBeChangedFlag = 0

    global KeyPressResponse_RIGHT_NeedsToBeChangedFlag
    KeyPressResponse_RIGHT_NeedsToBeChangedFlag = 0

    global KeyPressResponse_LEFT_NeedsToBeChangedFlag
    KeyPressResponse_LEFT_NeedsToBeChangedFlag = 0

    global KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag
    KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag = 0
    
    global KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag
    KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag = 0
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

    global DataStreamingFrequency_CalculatedFromMainThread_Filtered
    DataStreamingFrequency_CalculatedFromMainThread_Filtered = -1

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

    global DataStreamingFrequency_CalculatedFromGUIthread_Filtered
    DataStreamingFrequency_CalculatedFromGUIthread_Filtered = -1

    global DataStreamingDeltaT_CalculatedFromGUIthread
    DataStreamingDeltaT_CalculatedFromGUIthread = -1
    #################################################
    #################################################

    #################################################
    #################################################
    global SINUSOIDAL_INPUT_TO_COMMAND
    SINUSOIDAL_INPUT_TO_COMMAND = 0.0

    global Wheel_Theta_RL_Radians_Actual
    Wheel_Theta_RL_Radians_Actual = 0.0

    global Wheel_Theta_RR_Radians_Actual
    Wheel_Theta_RR_Radians_Actual = 0.0

    global Wheel_Omega_Theta_RL_RadiansPerSec_Actual
    Wheel_Omega_Theta_RL_RadiansPerSec_Actual = 0.0

    global Wheel_Omega_Theta_RR_RadiansPerSec_Actual
    Wheel_Omega_Theta_RR_RadiansPerSec_Actual = 0.0

    global Position_X_RM_Meters_Actual
    Position_X_RM_Meters_Actual = 0.0

    global Position_X_RMC_Meters_Commanded
    Position_X_RMC_Meters_Commanded = 0.0

    global Velocity_V_RM_MetersPerSec_Actual
    Velocity_V_RM_MetersPerSec_Actual = 0.0

    global Velocity_V_RM_MetersPerSec_Actual_UNFILTERED
    Velocity_V_RM_MetersPerSec_Actual_UNFILTERED = 0.0

    global Velocity_V_RMC_MetersPerSec_Commanded
    Velocity_V_RMC_MetersPerSec_Commanded = 0.0

    global YawAngle_Delta_Deg_Actual
    YawAngle_Delta_Deg_Actual = 0.0

    global YawAngle_Delta_Deg_Commanded
    YawAngle_Delta_Deg_Commanded = 0.0

    global YawAngle_Delta_Radians_Actual
    YawAngle_Delta_Radians_Actual = 0.0

    global YawAngle_Delta_Radians_Commanded
    YawAngle_Delta_Radians_Commanded = 0.0

    global YawAngularRate_DeltaDot_RadiansPerSec_Actual
    YawAngularRate_DeltaDot_RadiansPerSec_Actual = 0.0

    global YawAngularRate_DeltaDot_DegreesPerSecond_Actual
    YawAngularRate_DeltaDot_DegreesPerSecond_Actual = 0.0

    global YawAngularRate_DeltaDot_RadiansPerSec_Commanded
    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0

    global YawAngularRate_DeltaDot_DegreesPerSecond_Commanded
    YawAngularRate_DeltaDot_DegreesPerSecond_Commanded = 0.0

    global PitchAngle_Theta_Deg_Actual
    PitchAngle_Theta_Deg_Actual = 0.0

    global PitchAngle_Theta_Radians_Actual
    PitchAngle_Theta_Radians_Actual = 0.0

    global PitchAngle_Theta_Deg_Commanded
    PitchAngle_Theta_Deg_Commanded = 0.0

    global PitchAngle_Theta_Radians_Commanded
    PitchAngle_Theta_Radians_Commanded = 0.0

    global PitchAngularRate_ThetaDot_DegreesPerSecond_Actual
    PitchAngularRate_ThetaDot_DegreesPerSecond_Actual = 0.0

    global PitchAngularRate_ThetaDot_RadiansPerSec_Actual
    PitchAngularRate_ThetaDot_RadiansPerSec_Actual = 0.0

    global PitchAngularRate_ThetaDot_RadiansPerSec_Commanded
    PitchAngularRate_ThetaDot_RadiansPerSec_Commanded = 0.0

    global C_L
    C_L = 0.0

    global C_R
    C_R = 0.0

    global C_Theta
    C_Theta = 0.0

    global C_Delta
    C_Delta = 0.0

    global TorqueToBeCommanded_Motor0
    TorqueToBeCommanded_Motor0 = 0.0

    global TorqueToBeCommanded_Motor1
    TorqueToBeCommanded_Motor1 = 0.0

    global Pitch_PosControl_PID_Error
    Pitch_PosControl_PID_Error = 0

    global Pitch_PosControl_PID_Error_last
    Pitch_PosControl_PID_Error_last = 0

    global Pitch_PosControl_PID_ErrorSum
    Pitch_PosControl_PID_ErrorSum = 0

    global Pitch_PosControl_PID_ErrorD
    Pitch_PosControl_PID_ErrorD = 0

    global Pitch_PosControl_PID_CommandToMotor_Term_1
    Pitch_PosControl_PID_CommandToMotor_Term_1 = 0.0

    global Pitch_PosControl_PID_CommandToMotor_Term_2
    Pitch_PosControl_PID_CommandToMotor_Term_2 = 0.0

    global Pitch_PosControl_PID_CommandToMotor_Term_3
    Pitch_PosControl_PID_CommandToMotor_Term_3 = 0.0

    global Pitch_PosControl_PID_CommandToMotor_Term_5
    Pitch_PosControl_PID_CommandToMotor_Term_5 = 0.0

    global Pitch_PosControl_PID_CommandToMotor_Term_6
    Pitch_PosControl_PID_CommandToMotor_Term_6 = 0.0

    global Pitch_PID_CommandToMotor
    Pitch_PID_CommandToMotor = 0

    global EnableMotorState_0
    EnableMotorState_0 = ENABLE_MOTORS_AT_STARTUP_FLAG

    global EnableMotorState_NeedsToBeChangedFlag_0
    EnableMotorState_NeedsToBeChangedFlag_0 = 1

    global EnableMotorState_1
    EnableMotorState_1 = ENABLE_MOTORS_AT_STARTUP_FLAG

    global EnableMotorState_NeedsToBeChangedFlag_1
    EnableMotorState_NeedsToBeChangedFlag_1 = 1

    global ToggleEnableForBothMotors_EventNeedsToBeFiredFlag
    ToggleEnableForBothMotors_EventNeedsToBeFiredFlag = 0

    global ZeroLQR_EventNeedsToBeFiredFlag
    ZeroLQR_EventNeedsToBeFiredFlag = 0
    #################################################
    #################################################

    ####################################################
    ####################################################
    try:

        LowPassFilterForDictsOfLists_DictOfVariableFilterSettings = dict([("DataStreamingFrequency_CalculatedFromMainThread", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda)])),
                                                                          ("DataStreamingFrequency_CalculatedFromGUIthread", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda)])),
                                                                          ("Velocity_V_RM_MetersPerSec_Actual", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda)])),
                                                                          ("YawAngularRate_DeltaDot_RadiansPerSec_Actual", dict([("UseMedianFilterFlag", 0), ("UseExponentialSmoothingFilterFlag", 1),("ExponentialSmoothingFilterLambda", YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda)]))])

        LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject = LowPassFilterForDictsOfLists_ReubenPython2and3Class(dict([("DictOfVariableFilterSettings", LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)]))
        LowPassFilterForDictsOfLists_OPEN_FLAG = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

    except:
        exceptions = sys.exc_info()[0]
        print("LowPassFilterForDictsOfLists_ReubenPython2and3Class __init__: Exceptions: %s" % exceptions)
    ####################################################
    ####################################################

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
                                                                        ("SerialRxBufferSize", RoboteqBLDCcontroller_SerialRxBufferSize_0),
                                                                        ("SerialTxBufferSize", RoboteqBLDCcontroller_SerialTxBufferSize_0),
                                                                        ("DedicatedTxThread_TxMessageToSend_Queue_MaxSize", RoboteqBLDCcontroller_DedicatedTxThread_TxMessageToSend_Queue_MaxSize_0),
                                                                        ("HeartbeatTimeIntervalMilliseconds", RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_0),
                                                                        ("NumberOfMagnetsInMotor", RoboteqBLDCcontroller_NumberOfMagnetsInMotor_0),
                                                                        ("PID_Kp", RoboteqBLDCcontroller_PID_Kp_0),
                                                                        ("PID_Ki", RoboteqBLDCcontroller_PID_Ki_0),
                                                                        ("PID_Kd", RoboteqBLDCcontroller_PID_Kd_0),
                                                                        ("PID_IntegratorCap1to100percent", RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_0),
                                                                        ("VariableStreamingSendDataEveryDeltaT_MillisecondsInt", RoboteqBLDCcontroller_VariableStreamingSendDataEveryDeltaT_MillisecondsInt_0),
                                                                        ("SetBrushlessCounterTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_0),
                                                                        ("SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag_0)])

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
                                                                        ("SerialRxBufferSize", RoboteqBLDCcontroller_SerialRxBufferSize_1),
                                                                        ("SerialTxBufferSize", RoboteqBLDCcontroller_SerialTxBufferSize_1),
                                                                        ("HeartbeatTimeIntervalMilliseconds", RoboteqBLDCcontroller_HeartbeatTimeIntervalMilliseconds_1),
                                                                        ("NumberOfMagnetsInMotor", RoboteqBLDCcontroller_NumberOfMagnetsInMotor_1),
                                                                        ("PID_Kp", RoboteqBLDCcontroller_PID_Kp_1),
                                                                        ("PID_Ki", RoboteqBLDCcontroller_PID_Ki_1),
                                                                        ("PID_Kd", RoboteqBLDCcontroller_PID_Kd_1),
                                                                        ("PID_IntegratorCap1to100percent", RoboteqBLDCcontroller_PID_IntegratorCap1to100percent_1),
                                                                        ("VariableStreamingSendDataEveryDeltaT_MillisecondsInt", RoboteqBLDCcontroller_VariableStreamingSendDataEveryDeltaT_MillisecondsInt_1),
                                                                        ("SetBrushlessCounterTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterTo0atStartOfProgramFlag_1),
                                                                        ("SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag", RoboteqBLDCcontroller_SetBrushlessCounterSoftwareOffsetOnlyTo0atStartOfProgramFlag_1)])

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
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),
                                                                                        ("Spatial_CallbackUpdateDeltaTmilliseconds", SpatialPrecision333_Spatial_CallbackUpdateDeltaTmilliseconds),
                                                                                        ("DataCollectionDurationInSecondsForSnapshottingAndZeroing", SpatialPrecision333_DataCollectionDurationInSecondsForSnapshottingAndZeroing),
                                                                                        ("MainThread_TimeToSleepEachLoop", SpatialPrecision333_MainThread_TimeToSleepEachLoop),
                                                                                        ("HeatingEnabledToStabilizeSensorTemperature", SpatialPrecision333_HeatingEnabledToStabilizeSensorTemperature),
                                                                                        ("ZeroGyrosAtStartOfProgramFlag", SpatialPrecision333_ZeroGyrosAtStartOfProgramFlag),
                                                                                        ("ZeroAlgorithmAtStartOfProgramFlag", SpatialPrecision333_ZeroAlgorithmAtStartOfProgramFlag),
                                                                                        ("AHRS_Parameters_angularVelocityThreshold", SpatialPrecision333_AHRS_Parameters_angularVelocityThreshold),
                                                                                        ("AHRS_Parameters_angularVelocityDeltaThreshold", SpatialPrecision333_AHRS_Parameters_angularVelocityDeltaThreshold),
                                                                                        ("AHRS_Parameters_accelerationThreshold", SpatialPrecision333_AHRS_Parameters_accelerationThreshold),
                                                                                        ("AHRS_Parameters_magTime", SpatialPrecision333_AHRS_Parameters_magTime),
                                                                                        ("AHRS_Parameters_accelTime", SpatialPrecision333_AHRS_Parameters_accelTime),
                                                                                        ("AHRS_Parameters_biasTime", SpatialPrecision333_AHRS_Parameters_biasTime)])

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
    global EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict
    EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", GUItabObjectsOrderedDict["MainControls"]["TabObject"]),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_EntryListWithBlinking),
                                    ("GUI_COLUMN", GUI_COLUMN_EntryListWithBlinking),
                                    ("GUI_PADX", GUI_PADX_EntryListWithBlinking),
                                    ("GUI_PADY", GUI_PADY_EntryListWithBlinking),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_EntryListWithBlinking),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_EntryListWithBlinking)])

    global EntryListWithBlinking_Variables_ListOfDicts
    EntryListWithBlinking_Variables_ListOfDicts = [dict([("Name", "Pitch_PosControl_PID_gain_Kp"),("Type", "float"), ("StartingVal", Pitch_PosControl_PID_gain_Kp), ("MinVal", -1000000.0), ("MaxVal", 0.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "Pitch_PosControl_PID_gain_Ki"),("Type", "float"), ("StartingVal", Pitch_PosControl_PID_gain_Ki), ("MinVal", -1000000.0), ("MaxVal", 0.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "Pitch_PosControl_PID_gain_Kd"),("Type", "float"), ("StartingVal", Pitch_PosControl_PID_gain_Kd), ("MinVal", -1000000.0), ("MaxVal", 0.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "Pitch_PosControl_PID_ErrorSum_Max"),("Type", "float"), ("StartingVal", Pitch_PosControl_PID_ErrorSum_Max), ("MinVal", -1000000.0), ("MaxVal", 1000000.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_PitchControl_GainVectorElement_Ktheta_0"),("Type", "float"), ("StartingVal", LQR_PitchControl_GainVectorElement_Ktheta_0), ("MinVal", -1000000.0), ("MaxVal", 1000000.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_PitchControl_GainVectorElement_Ktheta_1"),("Type", "float"), ("StartingVal", LQR_PitchControl_GainVectorElement_Ktheta_1), ("MinVal", -1000000.0), ("MaxVal", 1000000.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_PitchControl_GainVectorElement_Ktheta_2"),("Type", "float"), ("StartingVal", LQR_PitchControl_GainVectorElement_Ktheta_2), ("MinVal", -1000000.0), ("MaxVal", 1000000.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_PitchControl_GainVectorElement_Ktheta_3"),("Type", "float"), ("StartingVal", LQR_PitchControl_GainVectorElement_Ktheta_3), ("MinVal", -1000000.0), ("MaxVal", 1000000.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_YawControl_GainVectorElement_Kdelta_0"),("Type", "float"), ("StartingVal", LQR_YawControl_GainVectorElement_Kdelta_0), ("MinVal", -1000000.0), ("MaxVal", 0.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "LQR_YawControl_GainVectorElement_Kdelta_1"),("Type", "float"), ("StartingVal", LQR_YawControl_GainVectorElement_Kdelta_1), ("MinVal", -1000000.0), ("MaxVal", 0.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset"),("Type", "float"), ("StartingVal", SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset), ("MinVal", -10.0), ("MaxVal", 10.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda"),("Type", "float"), ("StartingVal", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda), ("MinVal", -0.0), ("MaxVal", 1.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)]),
                                                dict([("Name", "YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda"),("Type", "float"), ("StartingVal", YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda), ("MinVal", 0.0), ("MaxVal", 1.0),("EntryBlinkEnabled", 0), ("EntryWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_EntryWidth), ("LabelWidth", EntryListWithBlinking_ReubenPython2and3ClassObject_LabelWidth)])]

    global EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict
    EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict = dict([("GUIparametersDict", EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict),
                                                                          ("EntryListWithBlinking_Variables_ListOfDicts", EntryListWithBlinking_Variables_ListOfDicts),
                                                                          ("DebugByPrintingVariablesFlag", 0),
                                                                          ("LoseFocusIfMouseLeavesEntryFlag", 0)])

    if USE_EntryListWithBlinking_FLAG == 1:

        try:
            EntryListWithBlinking_ReubenPython2and3ClassObject = EntryListWithBlinking_ReubenPython2and3Class(EntryListWithBlinking_ReubenPython2and3ClassObject_setup_dict)
            EntryListWithBlinking_OPEN_FLAG = EntryListWithBlinking_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, EntryListWithBlinking_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()

    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    ##################################################
    #################################################
    global CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict
    CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_CSVdataLogger_FLAG),
                                    ("root", GUItabObjectsOrderedDict["CSVdataLogger"]["TabObject"]),
                                    ("EnableInternal_MyPrint_Flag", 1),
                                    ("NumberOfPrintLines", 10),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_CSVdataLogger),
                                    ("GUI_COLUMN", GUI_COLUMN_CSVdataLogger),
                                    ("GUI_PADX", GUI_PADX_CSVdataLogger),
                                    ("GUI_PADY", GUI_PADY_CSVdataLogger),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_CSVdataLogger),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_CSVdataLogger)])

    global CSVdataLogger_ReubenPython3ClassObject_setup_dict
    CSVdataLogger_ReubenPython3ClassObject_setup_dict = dict([("GUIparametersDict", CSVdataLogger_ReubenPython3ClassObject_GUIparametersDict),
                                                                                ("NameToDisplay_UserSet", CSVdataLogger_NameToDisplay_UserSet),
                                                                                ("CSVfile_DirectoryPath", CSVdataLogger_CSVfile_DirectoryPath),
                                                                                ("FileNamePrefix", CSVdataLogger_FileNamePrefix),
                                                                                ("VariableNamesForHeaderList", CSVdataLogger_VariableNamesForHeaderList),
                                                                                ("MainThread_TimeToSleepEachLoop", CSVdataLogger_MainThread_TimeToSleepEachLoop),
                                                                                ("SaveOnStartupFlag", CSVdataLogger_SaveOnStartupFlag)])

    if USE_CSVdataLogger_FLAG == 1:
        try:
            CSVdataLogger_ReubenPython3ClassObject = CSVdataLogger_ReubenPython3Class(CSVdataLogger_ReubenPython3ClassObject_setup_dict)
            CSVdataLogger_OPEN_FLAG = CSVdataLogger_ReubenPython3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, CSVdataLogger_ReubenPython3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    UpdateGUItabObjectsOrderedDict()
    #################################################
    #################################################

    ##################################################
    #################################################
    global BarGraphDisplay_Variables_ListOfDicts
    BarGraphDisplay_Variables_ListOfDicts = [dict([("Name", "LQR_1"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)]),
                                             dict([("Name", "LQR_2"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)]),
                                             dict([("Name", "LQR_3"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)]),
                                             dict([("Name", "LQR_4"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)]),
                                             dict([("Name", "LQR_5"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)]),
                                             dict([("Name", "LQR_6"), ("StartingValue", 0.0), ("MinValue", -100.0), ("MaxValue", 100.0)])]

    global BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict
    BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict = dict([("root", GUItabObjectsOrderedDict["MainControls"]["TabObject"]),
                                    ("GUI_ROW", GUI_ROW_BarGraphDisplay),
                                    ("GUI_COLUMN", GUI_COLUMN_BarGraphDisplay),
                                    ("GUI_PADX", GUI_PADX_BarGraphDisplay),
                                    ("GUI_PADY", GUI_PADY_BarGraphDisplay),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_BarGraphDisplay),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_BarGraphDisplay)])

    global BarGraphDisplay_ReubenPython3ClassObject_setup_dict
    BarGraphDisplay_ReubenPython3ClassObject_setup_dict = dict([("GUIparametersDict", BarGraphDisplay_ReubenPython3ClassObject_GUIparametersDict),
                                                                ("Variables_ListOfDicts", BarGraphDisplay_Variables_ListOfDicts),
                                                                ("Canvas_Width", 600),
                                                                ("Canvas_Height", 250),
                                                                ("BarWidth",90),
                                                                ("BarPadX", 5),
                                                                ("FontSize", 12),
                                                                ("NegativeColor", TKinter_LightRedColor),
                                                                ("PositiveColor", TKinter_LightGreenColor)])

    if USE_BarGraphDisplay_FLAG == 1:

        try:
            BarGraphDisplay_ReubenPython3ClassObject = BarGraphDisplay_ReubenPython3Class(BarGraphDisplay_ReubenPython3ClassObject_setup_dict)
            BarGraphDisplay_OPEN_FLAG = BarGraphDisplay_ReubenPython3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("SelfBalancingRobot1.py, BarGraphDisplay_ReubenPython3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            #traceback.print_exc()

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
            print("SelfBalancingRobot1.py, MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
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

    ####################################################
    ####################################################
    if LowPassFilterForDictsOfLists_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, Failed to open LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    ####################################################
    ####################################################

    #################################################
    #################################################
    if USE_MyPlotterPureTkinterStandAloneProcess_FLAG == 1 and MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, failed to open MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_CSVdataLogger_FLAG == 1 and CSVdataLogger_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, Failed to open CSVdataLogger_ReubenPython3Class.")
        #ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if BarGraphDisplay_OPEN_FLAG != 1:
        print("SelfBalancingRobot1.py, Failed to open BarGraphDisplay_ReubenPython3Class.")
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
        ###################################################
        if JSONfiles_NeedsToBeLoadedFlag == 1:

            ###################################################
            ###################################################
            LoadAndParseJSONfile_GUIsettings()
            LoadAndParseJSONfile_RoboteqBLDCcontroller_0()
            LoadAndParseJSONfile_RoboteqBLDCcontroller_1()
            LoadAndParseJSONfile_WiFiVINTthumbstick()
            LoadAndParseJSONfile_SpatialPrecision333()
            LoadAndParseJSONfile_DC30AmpCurrentSensor()
            LoadAndParseJSONfile_SavingSettings()
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            LoadAndParseJSONfile_ControlLawParameters()

            ################################################### SET's
            if EntryListWithBlinking_OPEN_FLAG == 1:    
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("Pitch_PosControl_PID_gain_Kp", Pitch_PosControl_PID_gain_Kp)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("Pitch_PosControl_PID_gain_Ki", Pitch_PosControl_PID_gain_Ki)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("Pitch_PosControl_PID_gain_Kd", Pitch_PosControl_PID_gain_Kd)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("Pitch_PosControl_PID_ErrorSum_Max", Pitch_PosControl_PID_ErrorSum_Max)

                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_PitchControl_GainVectorElement_Ktheta_0", LQR_PitchControl_GainVectorElement_Ktheta_0)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_PitchControl_GainVectorElement_Ktheta_1", LQR_PitchControl_GainVectorElement_Ktheta_1)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_PitchControl_GainVectorElement_Ktheta_2", LQR_PitchControl_GainVectorElement_Ktheta_2)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_PitchControl_GainVectorElement_Ktheta_3", LQR_PitchControl_GainVectorElement_Ktheta_3)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_YawControl_GainVectorElement_Kdelta_0", LQR_YawControl_GainVectorElement_Kdelta_0)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("LQR_YawControl_GainVectorElement_Kdelta_1", LQR_YawControl_GainVectorElement_Kdelta_1)

                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset", SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda", Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda)
                    EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda", YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda)
            ###################################################

            ###################################################
            PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.UpdateDifferentiatedAngularVelocityFilterParameters(dict([("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_RollRate_AbtXaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_PitchRate_AbtYaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseMedianFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_UseExponentialSmoothingFilterFlag),
                                                                                        ("YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda", SpatialPrecision333_YawRate_AbtZaxis_DifferentiatedAngularVelocity_DegreesPerSecond_ExponentialSmoothingFilterLambda),]))

            ###################################################

            ###################################################
            ###################################################

            ###################################################
            ###################################################
            LoadAndParseJSONfile_RobotModelParameters()
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            LoadAndParseJSONfile_Keyboard()

            KeyboardMapKeysToCallbackFunctions()
            ###################################################
            ###################################################

            ###################################################
            ###################################################
            LoadAndParseJSONfile_MyPlotterPureTkinterStandAloneProcess()

            if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalUpdateSetupDict(MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_setup_dict)
            ###################################################
            ###################################################

            JSONfiles_NeedsToBeLoadedFlag = 0
        ###################################################
        ###################################################
        ###################################################

        ################################################### GET's
        ###################################################
        if EntryListWithBlinking_OPEN_FLAG == 1:

            EntryListWithBlinking_MostRecentDict = EntryListWithBlinking_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:
                EntryListWithBlinking_MostRecentDict_DataUpdateNumber = EntryListWithBlinking_MostRecentDict["DataUpdateNumber"]

                Pitch_PosControl_PID_gain_Kp = EntryListWithBlinking_MostRecentDict["Pitch_PosControl_PID_gain_Kp"]
                Pitch_PosControl_PID_gain_Ki = EntryListWithBlinking_MostRecentDict["Pitch_PosControl_PID_gain_Ki"]
                Pitch_PosControl_PID_gain_Kd = EntryListWithBlinking_MostRecentDict["Pitch_PosControl_PID_gain_Kd"]
                Pitch_PosControl_PID_ErrorSum_Max = EntryListWithBlinking_MostRecentDict["Pitch_PosControl_PID_ErrorSum_Max"]

                LQR_PitchControl_GainVectorElement_Ktheta_0 = EntryListWithBlinking_MostRecentDict["LQR_PitchControl_GainVectorElement_Ktheta_0"] 
                LQR_PitchControl_GainVectorElement_Ktheta_1 = EntryListWithBlinking_MostRecentDict["LQR_PitchControl_GainVectorElement_Ktheta_1"]
                LQR_PitchControl_GainVectorElement_Ktheta_2 = EntryListWithBlinking_MostRecentDict["LQR_PitchControl_GainVectorElement_Ktheta_2"]
                LQR_PitchControl_GainVectorElement_Ktheta_3 = EntryListWithBlinking_MostRecentDict["LQR_PitchControl_GainVectorElement_Ktheta_3"]
                LQR_YawControl_GainVectorElement_Kdelta_0 = EntryListWithBlinking_MostRecentDict["LQR_YawControl_GainVectorElement_Kdelta_0"]
                LQR_YawControl_GainVectorElement_Kdelta_1 = EntryListWithBlinking_MostRecentDict["LQR_YawControl_GainVectorElement_Kdelta_1"]

                SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset = EntryListWithBlinking_MostRecentDict["SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset"]
                Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda = EntryListWithBlinking_MostRecentDict["Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda"]
                YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda = EntryListWithBlinking_MostRecentDict["YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda"]
                
                #print("EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
                #print("DataUpdateNumber = " + str(EntryListWithBlinking_MostRecentDict_DataUpdateNumber) + ", EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
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
                    RoboteqBLDCcontroller_MostRecentDict_AbsoluteBrushlessCounter_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["AbsoluteBrushlessCounter"]
                    RoboteqBLDCcontroller_MostRecentDict_SpeedRPM_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["SpeedRPM"]
                    #RoboteqBLDCcontroller_MostRecentDict_TorqueTarget_1 = RoboteqBLDCcontroller_MostRecentDict_1["TorqueTarget"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryCurrentInAmps_1 = RoboteqBLDCcontroller_MostRecentDict_1["BatteryCurrentInAmps"]
                    #RoboteqBLDCcontroller_MostRecentDict_BatteryVoltsX10_1 = RoboteqBLDCcontroller_MostRecentDict_1["BatteryVoltsX10"]
                    RoboteqBLDCcontroller_MostRecentDict_FaultFlags_1 = RoboteqBLDCcontroller_MostRecentDict_1["FaultFlags"]
    
                    RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Position_Rev"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Radians_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Position_Radians"]
                    RoboteqBLDCcontroller_MostRecentDict_Position_Degrees_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Position_Degrees"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPM_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Speed_RPM"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Speed_RPS"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_RadiansPerSec_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Speed_RadiansPerSec"]
                    RoboteqBLDCcontroller_MostRecentDict_Speed_DegreesPerSec_1 = -1.0*RoboteqBLDCcontroller_MostRecentDict_1["Speed_DegreesPerSec"]
    
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

        #################################################### GET's
        ####################################################
        if CSVdataLogger_OPEN_FLAG == 1:

            CSVdataLogger_MostRecentDict = CSVdataLogger_ReubenPython3ClassObject.GetMostRecentDataDict()

            if "Time" in CSVdataLogger_MostRecentDict:
                CSVdataLogger_MostRecentDict_Time = CSVdataLogger_MostRecentDict["Time"]
                CSVdataLogger_MostRecentDict_DataStreamingFrequency_CalculatedFromMainThread = CSVdataLogger_MostRecentDict["DataStreamingFrequency_CalculatedFromMainThread"]
                CSVdataLogger_MostRecentDict_AcceptNewDataFlag = CSVdataLogger_MostRecentDict["AcceptNewDataFlag"]
                CSVdataLogger_MostRecentDict_SaveFlag = CSVdataLogger_MostRecentDict["SaveFlag"]
                CSVdataLogger_MostRecentDict_DataQueue_qsize = CSVdataLogger_MostRecentDict["DataQueue_qsize"]
                CSVdataLogger_MostRecentDict_VariableNamesForHeaderList = CSVdataLogger_MostRecentDict["VariableNamesForHeaderList"]
                CSVdataLogger_MostRecentDict_FilepathFull = CSVdataLogger_MostRecentDict["FilepathFull"]

                #print("CSVdataLogger_MostRecentDict: " + str(CSVdataLogger_MostRecentDict))

        ####################################################
        ####################################################

        ####################################################
        ####################################################
        if LowPassFilterForDictsOfLists_OPEN_FLAG == 1:

            if DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda != DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda_last or \
                DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda != DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda_last or \
                Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda != Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last or \
                YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda != YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last:

                LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["DataStreamingFrequency_CalculatedFromMainThread"]["ExponentialSmoothingFilterLambda"] = DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda
                LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["DataStreamingFrequency_CalculatedFromGUIthread"]["ExponentialSmoothingFilterLambda"] = DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda
                LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["Velocity_V_RM_MetersPerSec_Actual"]["ExponentialSmoothingFilterLambda"] = Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda
                LowPassFilterForDictsOfLists_DictOfVariableFilterSettings["YawAngularRate_DeltaDot_RadiansPerSec_Actual"]["ExponentialSmoothingFilterLambda"] = YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda

                if "DataStreamingFrequency_CalculatedFromMainThread" in LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.GetMostRecentDataDict(): #Wait until it's populated
                    LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddOrUpdateDictOfVariableFilterSettingsFromExternalProgram(LowPassFilterForDictsOfLists_DictOfVariableFilterSettings)
        ####################################################
        ####################################################

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

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        if ControlInput_NeedsToBeChangedFlag == 1:
            dummy = 0
            ControlInput_NeedsToBeChangedFlag = 0
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        if ControlAlgorithm_NeedsToBeChangedFlag == 1:
            dummy = 0
            ControlAlgorithm_NeedsToBeChangedFlag = 0
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ###################################################################################################### Start ControlInput section
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        if ControlInput == "KeyboardControl":

            ######################################################################################################
            ######################################################################################################
            if KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag == 1:
                ToggleEnableForBothMotors_EventNeedsToBeFiredFlag = 1
                KeyPressResponse_TorqueEnable_NeedsToBeChangedFlag = 0
            ######################################################################################################
            ######################################################################################################

            ######################################################################################################
            ######################################################################################################
            if KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag == 1:
                ZeroLQR_EventNeedsToBeFiredFlag = 1
                KeyPressResponse_ZeroLQR_NeedsToBeChangedFlag = 0
            ######################################################################################################
            ######################################################################################################

            ###################################################################################################### NEED A SEPARATE SECTION FROM PID DUE TO DIFFERENT COMMAND VALUES
            ######################################################################################################
            if ControlAlgorithm == "LQR":
                Velocity_V_RMC_MetersPerSec_Commanded = 0.0 #Default to 0 and only change if a key is depressed.
                YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0 #Default to 0 and only change if a key is depressed.

                PitchAngle_Theta_Deg_Commanded = 0.0

                if KeyPressResponse_FWD_NeedsToBeChangedFlag == 1:
                    Velocity_V_RMC_MetersPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["FWD"]["CommandedValue_LQR"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded FWD")
                    #KeyPressResponse_FWD_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_REV_NeedsToBeChangedFlag == 1:
                    Velocity_V_RMC_MetersPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["REV"]["CommandedValue_LQR"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded REV")
                    #KeyPressResponse_REV_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_RIGHT_NeedsToBeChangedFlag == 1:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["RIGHT"]["CommandedValue_LQR"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded RIGHT")
                    #KeyPressResponse_RIGHT_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_LEFT_NeedsToBeChangedFlag == 1:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["LEFT"]["CommandedValue_LQR"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded LEFT")
                    #KeyPressResponse_LEFT_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

            ######################################################################################################
            ######################################################################################################

            ###################################################################################################### NEED A SEPARATE SECTION FROM LQR DUE TO DIFFERENT COMMAND VALUES
            ######################################################################################################
            elif ControlAlgorithm == "PID":
                Velocity_V_RMC_MetersPerSec_Commanded = 0.0 #Default to 0 and only change if a key is depressed.
                YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0 #Default to 0 and only change if a key is depressed.

                PitchAngle_Theta_Deg_Commanded = 0.0

                if KeyPressResponse_FWD_NeedsToBeChangedFlag == 1:
                    PitchAngle_Theta_Deg_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["FWD"]["CommandedValue_PID"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded FWD")
                    #KeyPressResponse_FWD_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_REV_NeedsToBeChangedFlag == 1:
                    PitchAngle_Theta_Deg_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["REV"]["CommandedValue_PID"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded REV")
                    #KeyPressResponse_REV_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

                if KeyPressResponse_RIGHT_NeedsToBeChangedFlag == 1:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["RIGHT"]["CommandedValue_PID"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded RIGHT")
                    #KeyPressResponse_RIGHT_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS
    
                if KeyPressResponse_LEFT_NeedsToBeChangedFlag == 1:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = Keyboard_KeysToTeleopControlsMapping_DictOfDicts["LEFT"]["CommandedValue_PID"]
                    #print("Velocity_V_RMC_MetersPerSec_Commanded LEFT")
                    #KeyPressResponse_LEFT_NeedsToBeChangedFlag = 0 #HANDLED INSTEAD BY THE REVERSE KEY-PRESS

            ######################################################################################################
            ######################################################################################################

            ######################################################################################################
            ######################################################################################################
            else:
                dummy = 0
            ######################################################################################################
            ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        elif ControlInput == "JoystickControl":

            ######################################################################################################
            ######################################################################################################
            if USE_WiFiVINTthumbstick_FLAG == 1:

                #################################################
                Velocity_V_RMC_MetersPerSec_Commanded_TEMP = Velocity_V_RMC_MetersPerSec_Commanded_JoystickToMetersPerSecGain*WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput0Object_VoltageRatio

                if abs(Velocity_V_RMC_MetersPerSec_Commanded_TEMP) >= Velocity_V_RMC_MetersPerSec_Commanded_DeadbandThreshold:
                    Velocity_V_RMC_MetersPerSec_Commanded = Velocity_V_RMC_MetersPerSec_Commanded_TEMP
                else:
                    Velocity_V_RMC_MetersPerSec_Commanded = 0.0
                #################################################

                #################################################
                YawAngularRate_DeltaDot_RadiansPerSec_Commanded_TEMP = YawAngularRate_DeltaDot_RadiansPerSec_Commanded_JoystickToRadiansPerSecGain*WiFiVINTthumbstick_MostRecentDict_VoltageRatioInput1Object_VoltageRatio

                if abs(YawAngularRate_DeltaDot_RadiansPerSec_Commanded_TEMP) >= YawAngularRate_DeltaDot_RadiansPerSec_Commanded_DeadbandThreshold:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = YawAngularRate_DeltaDot_RadiansPerSec_Commanded_TEMP
                else:
                    YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0
                #################################################

            ######################################################################################################
            ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        else:
            pass
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End ControlInput section

        ###################################################################################################### Start "calculating states" section
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        if ZeroLQR_EventNeedsToBeFiredFlag == 1:

            Position_X_RMC_Meters_Commanded = 0.0
            Velocity_V_RMC_MetersPerSec_Commanded = 0.0
            YawAngle_Delta_Radians_Commanded = 0.0
            YawAngularRate_DeltaDot_RadiansPerSec_Commanded = 0.0

            RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_0 = 1 #Sets actual position to 0 during next loop
            RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 = 0.0

            RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_1 = 1 #Sets actual position to 0 during next loop
            RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 = 0.0

            #SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag = 1 #Perform this separatly via its own button.
            #SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag = 1 #Perform this separatly via its own button.

            ZeroLQR_EventNeedsToBeFiredFlag = 0
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        Wheel_Theta_RL_Radians_Actual = RoboteqBLDCcontroller_MostRecentDict_Position_Rev_1 * 2.0 * math.pi #THE ENCODERS BOTH SHOW POSITIVE DESPITE OPPOSITE MOUNTING
        Wheel_Theta_RR_Radians_Actual = RoboteqBLDCcontroller_MostRecentDict_Position_Rev_0 * 2.0 * math.pi

        Wheel_Omega_Theta_RL_RadiansPerSec_Actual = RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_1 * 2.0 * math.pi
        Wheel_Omega_Theta_RR_RadiansPerSec_Actual = RoboteqBLDCcontroller_MostRecentDict_Speed_RPS_0 * 2.0 * math.pi

        Position_X_RM_Meters_Actual = (RobotModelParameters_R_RadiusOfWheelInMeters * (Wheel_Theta_RL_Radians_Actual + Wheel_Theta_RR_Radians_Actual) / 2.0)

        if DataStreamingFrequency_CalculatedFromMainThread_Filtered > 0:
            Position_X_RMC_Meters_Commanded = Position_X_RMC_Meters_Commanded + Velocity_V_RMC_MetersPerSec_Commanded*(1.0/DataStreamingFrequency_CalculatedFromMainThread_Filtered)

        if Velocity_V_RMC_MetersPerSec_Commanded != 0.0: #So that we're not integrating while commanding nothing via keyboard
            Position_X_RMC_Meters_Commanded = LimitNumber_FloatOutputOnly(Position_X_RM_Meters_Actual - Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, Position_X_RM_Meters_Actual + Position_X_RMC_Meters_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, Position_X_RMC_Meters_Commanded) #Cap it

        Velocity_V_RM_MetersPerSec_Actual_UNFILTERED = RobotModelParameters_R_RadiusOfWheelInMeters * (Wheel_Omega_Theta_RL_RadiansPerSec_Actual + Wheel_Omega_Theta_RR_RadiansPerSec_Actual) / 2.0
        VariablesDict_Temp = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("Velocity_V_RM_MetersPerSec_Actual", [Velocity_V_RM_MetersPerSec_Actual_UNFILTERED])]))
        Velocity_V_RM_MetersPerSec_Actual = VariablesDict_Temp["Velocity_V_RM_MetersPerSec_Actual"]["Filtered_MostRecentValuesList"][0]

        PitchAngle_Theta_Deg_Actual = SpatialPrecision333_MostRecentDict_RollPitchYaw_AbtXYZ_Dict["RollPitchYaw_AbtXYZ_List_Degrees"][1]#spatial333_Pitch_AbtYaxis_Degrees_1

        PitchAngle_Theta_Deg_Actual = PitchAngle_Theta_Deg_Actual + SpatialPrecision333_PitchAngle_Theta_Deg_Actual_Offset
        PitchAngle_Theta_Radians_Actual = PitchAngle_Theta_Deg_Actual*math.pi/180.0

        PitchAngle_Theta_Radians_Commanded = PitchAngle_Theta_Deg_Commanded*math.pi/180.0

        PitchAngularRate_ThetaDot_DegreesPerSecond_Actual = SpatialPrecision333_MostRecentDict_RollPitchYaw_Rate_AbtXYZ_Dict["RollPitchYaw_Rate_AbtXYZ_List_DegreesPerSecond"][1]
        PitchAngularRate_ThetaDot_RadiansPerSec_Actual = PitchAngularRate_ThetaDot_DegreesPerSecond_Actual*math.pi/180.0
        PitchAngularRate_ThetaDot_RadiansPerSec_Commanded = 0.0

        YawAngle_Delta_Radians_Actual = -1.0*RobotModelParameters_R_RadiusOfWheelInMeters * (Wheel_Theta_RL_Radians_Actual - Wheel_Theta_RR_Radians_Actual) / RobotModelParameters_D_LateralDistanceBetweenWheelContactPatchesInMeters #NOT SURE WHY WE NEED MINUS SIGN TO GET YAW IN CORRECT DIRECTION
        YawAngle_Delta_Deg_Actual = YawAngle_Delta_Radians_Actual * 180.0 / math.pi
        
        YawAngularRate_DeltaDot_RadiansPerSec_Actual_UNFILTERED = -1.0*RobotModelParameters_R_RadiusOfWheelInMeters * (Wheel_Omega_Theta_RL_RadiansPerSec_Actual - Wheel_Omega_Theta_RR_RadiansPerSec_Actual) / RobotModelParameters_D_LateralDistanceBetweenWheelContactPatchesInMeters #NOT SURE WHY WE NEED MINUS SIGN TO GET YAW IN CORRECT DIRECTION
        VariablesDict_Temp = LowPassFilterForDictsOfLists_ReubenPython2and3ClassObject.AddDataDictFromExternalProgram(dict([("YawAngularRate_DeltaDot_RadiansPerSec_Actual", [YawAngularRate_DeltaDot_RadiansPerSec_Actual_UNFILTERED])]))
        YawAngularRate_DeltaDot_RadiansPerSec_Actual = VariablesDict_Temp["YawAngularRate_DeltaDot_RadiansPerSec_Actual"]["Filtered_MostRecentValuesList"][0]

        YawAngularRate_DeltaDot_DegreesPerSecond_Actual = YawAngularRate_DeltaDot_RadiansPerSec_Actual * 180.0 / math.pi

        #YawAngularRate_DeltaDot_RadiansPerSec_Commanded = Set in above code by ControlInput
        YawAngularRate_DeltaDot_DegreesPerSecond_Commanded = YawAngularRate_DeltaDot_RadiansPerSec_Commanded * 180.0 / math.pi

        YawAngle_Delta_Radians_Commanded = YawAngle_Delta_Radians_Commanded + YawAngularRate_DeltaDot_RadiansPerSec_Commanded*(1.0/DataStreamingFrequency_CalculatedFromMainThread_Filtered)

        if YawAngularRate_DeltaDot_RadiansPerSec_Commanded != 0.0: #So that we're not integrating while commanding nothing via keyboard
            YawAngle_Delta_Radians_Commanded = LimitNumber_FloatOutputOnly(YawAngle_Delta_Radians_Actual - YawAngle_Delta_Radians_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, YawAngle_Delta_Radians_Actual + YawAngle_Delta_Radians_Commanded_MAX_ERROR_DISTANCE_LIMIT_FOR_LQR_CALCULATION, YawAngle_Delta_Radians_Commanded) #Cap it

        YawAngle_Delta_Deg_Commanded = YawAngle_Delta_Radians_Commanded * 180.0 / math.pi
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End "calculating states" section

        ###################################################################################################### Start ControlAlgorithm section
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        if ControlAlgorithm == "SinusoidalTest":
            time_gain = math.pi / (2.0 * SINUSOIDAL_MOTION_INPUT_ROMtestTimeToPeakAngle)
            SINUSOIDAL_INPUT_TO_COMMAND = (SINUSOIDAL_MOTION_INPUT_MaxValue + SINUSOIDAL_MOTION_INPUT_MinValue)/2.0 + 0.5*abs(SINUSOIDAL_MOTION_INPUT_MaxValue - SINUSOIDAL_MOTION_INPUT_MinValue)*math.sin(time_gain*CurrentTime_CalculatedFromMainThread)

            TorqueToBeCommanded_Motor0 = SINUSOIDAL_INPUT_TO_COMMAND
            TorqueToBeCommanded_Motor1 = -1.0*SINUSOIDAL_INPUT_TO_COMMAND #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        elif ControlAlgorithm == "PID":

            Pitch_PosControl_PID_Error = PitchAngle_Theta_Radians_Commanded - PitchAngle_Theta_Radians_Actual

            if abs(Pitch_PosControl_PID_ErrorSum + Pitch_PosControl_PID_Error) <= Pitch_PosControl_PID_ErrorSum_Max:
                Pitch_PosControl_PID_ErrorSum = Pitch_PosControl_PID_ErrorSum + Pitch_PosControl_PID_Error

            Pitch_PosControl_PID_ErrorD = (0.0 - PitchAngularRate_ThetaDot_RadiansPerSec_Actual)

            Pitch_PosControl_PID_CommandToMotor_Term_1 = -1.0 * Pitch_PosControl_PID_Error * Pitch_PosControl_PID_gain_Kp
            Pitch_PosControl_PID_CommandToMotor_Term_2 = -1.0 * Pitch_PosControl_PID_ErrorSum * Pitch_PosControl_PID_gain_Ki
            Pitch_PosControl_PID_CommandToMotor_Term_3 = -1.0 * Pitch_PosControl_PID_ErrorD * Pitch_PosControl_PID_gain_Kd

            Pitch_PosControl_PID_CommandToMotor_Term_5 = -1.0*LQR_YawControl_GainVectorElement_Kdelta_0 * (YawAngle_Delta_Radians_Actual - YawAngle_Delta_Radians_Commanded)
            Pitch_PosControl_PID_CommandToMotor_Term_6 = -1.0*LQR_YawControl_GainVectorElement_Kdelta_1 * (YawAngularRate_DeltaDot_RadiansPerSec_Actual - YawAngularRate_DeltaDot_RadiansPerSec_Commanded)



            ### Simple PID
            Pitch_PosControl_PID_CommandToMotor =  Pitch_PosControl_PID_CommandToMotor_Term_1 + Pitch_PosControl_PID_CommandToMotor_Term_2 + Pitch_PosControl_PID_CommandToMotor_Term_3
            ''' 
            TorqueToBeCommanded_Motor0 = Pitch_PosControl_PID_CommandToMotor
            TorqueToBeCommanded_Motor1 = -1.0*Pitch_PosControl_PID_CommandToMotor #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
            ###
            '''

            C_Theta = 1.0 * (Pitch_PosControl_PID_CommandToMotor_Term_1 + Pitch_PosControl_PID_CommandToMotor_Term_2 + Pitch_PosControl_PID_CommandToMotor_Term_3)

            C_Delta =  1.0 * (Pitch_PosControl_PID_CommandToMotor_Term_5 + Pitch_PosControl_PID_CommandToMotor_Term_6)
            #C_Delta = 0 #unicorn

            C_L = 0.5*(C_Theta + C_Delta)
            C_R = 0.5*(C_Theta - C_Delta)

            TorqueToBeCommanded_Motor0 = 1.0*C_R #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
            TorqueToBeCommanded_Motor1 = -1.0*C_L
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        elif ControlAlgorithm == "LQR":

            LQR_ControlLaw_Term_1 = 1.0*LQR_PitchControl_GainVectorElement_Ktheta_0 * (Position_X_RM_Meters_Actual - Position_X_RMC_Meters_Commanded)
            LQR_ControlLaw_Term_2 = 1.0*LQR_PitchControl_GainVectorElement_Ktheta_1 * (Velocity_V_RM_MetersPerSec_Actual - Velocity_V_RMC_MetersPerSec_Commanded)
            LQR_ControlLaw_Term_3 = 1.0*LQR_PitchControl_GainVectorElement_Ktheta_2 * (PitchAngle_Theta_Radians_Actual - PitchAngle_Theta_Radians_Commanded)
            LQR_ControlLaw_Term_4 = 1.0*LQR_PitchControl_GainVectorElement_Ktheta_3 * (PitchAngularRate_ThetaDot_RadiansPerSec_Actual - PitchAngularRate_ThetaDot_RadiansPerSec_Commanded)
            LQR_ControlLaw_Term_5 = -1.0*LQR_YawControl_GainVectorElement_Kdelta_0 * (YawAngle_Delta_Radians_Actual - YawAngle_Delta_Radians_Commanded)
            LQR_ControlLaw_Term_6 = -1.0*LQR_YawControl_GainVectorElement_Kdelta_1 * (YawAngularRate_DeltaDot_RadiansPerSec_Actual - YawAngularRate_DeltaDot_RadiansPerSec_Commanded)

            C_Theta = 1.0 * (LQR_ControlLaw_Term_1 + LQR_ControlLaw_Term_2 + LQR_ControlLaw_Term_3 + LQR_ControlLaw_Term_4)  #NOT SURE WHY WE HAD TO REMOVE PAPER'S MINUS SIGN

            C_Delta =  1.0 * (LQR_ControlLaw_Term_5 + LQR_ControlLaw_Term_6) #NOT SURE WHY WE HAD TO REMOVE PAPER'S MINUS SIGN
            #C_Delta = 0 #unicorn

            C_L = 0.5*(C_Theta + C_Delta)
            C_R = 0.5*(C_Theta - C_Delta)

            TorqueToBeCommanded_Motor0 = 1.0*C_R #Wheels are mounted opposite, so need a minus sign to get them both spinning in same direction.
            TorqueToBeCommanded_Motor1 = -1.0*C_L
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        else:
            pass
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################

        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        TorqueToBeCommanded_Motor0 = LimitNumber_FloatOutputOnly(-1.0*MaxCommandFromControlLaw_Motor0, MaxCommandFromControlLaw_Motor0, TorqueToBeCommanded_Motor0) #defined in ControlLawParameters.json
        TorqueToBeCommanded_Motor1 = LimitNumber_FloatOutputOnly(-1.0*MaxCommandFromControlLaw_Motor1, MaxCommandFromControlLaw_Motor1, TorqueToBeCommanded_Motor1) #defined in ControlLawParameters.json
        ######################################################################################################
        ######################################################################################################
        ######################################################################################################
        ###################################################################################################### End ControlAlgorithm section

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
        if ToggleEnableForBothMotors_EventNeedsToBeFiredFlag == 1:
            ToggleEnableForBothMotors()
            ToggleEnableForBothMotors_EventNeedsToBeFiredFlag = 0
        ###################################################
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_0 == 1:

            ###################################################
            if RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_0 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.SetCurrentPositionAsHomeSoftwareOffsetOnly()
                RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_0 = 0
            ###################################################

            ###################################################
            if EnableMotorState_NeedsToBeChangedFlag_0 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.EnableMotorsFromExternalProgram(EnableMotorState_0)
                EnableMotorState_NeedsToBeChangedFlag_0 = 0
            ###################################################

            ###################################################
            if EnableMotorState_0 == 1:
                #TorqueToBeCommanded_Motor0 = 20
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.SendCommandToMotor_ExternalClassFunction(TorqueToBeCommanded_Motor0, RoboteqBLDCcontroller_ControlMode_Starting_0)
            else:
                pass
                #RoboteqBLDCcontroller_ReubenPython2and3ClassObject_0.SendCommandToMotor_ExternalClassFunction(0.0, RoboteqBLDCcontroller_ControlMode_Starting_0)
            ###################################################

        ###################################################
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if RoboteqBLDCcontroller_OPEN_FLAG_1 == 1:

            ###################################################
            if RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_1 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.SetCurrentPositionAsHomeSoftwareOffsetOnly()
                RoboteqBLDCcontroller_NeedToHomeSoftwareOffsetOnlyFlag_1 = 0
            ###################################################

            ###################################################
            if EnableMotorState_NeedsToBeChangedFlag_1 == 1:
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.EnableMotorsFromExternalProgram(EnableMotorState_1)
                EnableMotorState_NeedsToBeChangedFlag_1 = 0
            ###################################################

            ###################################################
            if EnableMotorState_1 == 1:
                #TorqueToBeCommanded_Motor1 = -20
                RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.SendCommandToMotor_ExternalClassFunction(TorqueToBeCommanded_Motor1, RoboteqBLDCcontroller_ControlMode_Starting_1)
            else:
                pass
                #RoboteqBLDCcontroller_ReubenPython2and3ClassObject_1.SendCommandToMotor_ExternalClassFunction(0.0, RoboteqBLDCcontroller_ControlMode_Starting_1)
            ###################################################

        ###################################################
        ###################################################
        ###################################################

        ################################################### SET's
        ###################################################
        ###################################################
        if SpatialPrecision333_OPEN_FLAG == 1:

            ###################################################
            if SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag == 1:
                PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.ZeroGyrosFromExternalProgram()
                SpatialPrecision333_ZeroGyros_NeedsToBeChangedFlag = 0
            ###################################################

            ###################################################
            if SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag == 1:
                PhidgetsSpatialPrecision333AccelGyroCompass_ReubenPython2and3ClassObject.ZeroAlgorithmFromExternalProgram()
                SpatialPrecision333_ZeroAlgorithm_NeedsToBeChangedFlag = 0
            ###################################################

        ###################################################
        ###################################################
        ###################################################

        #################################################### SET's
        ####################################################
        ###################################################
        if CSVdataLogger_OPEN_FLAG == 1 and CSVdataLogger_MostRecentDict_AcceptNewDataFlag == 1:

            try:
                ListToWriteToCSV = []
                for VariableName in CSVdataLogger_VariableNamesForHeaderList:
                    ListToWriteToCSV.append(globals()[VariableName])

                CSVdataLogger_ReubenPython3ClassObject.AddDataToCSVfile_ExternalFunctionCall(ListToWriteToCSV)

            except:
                exceptions = sys.exc_info()[0]
                print("SelfBalancingRobot1, CSVdataLogger_ReubenPython3ClassObject SET's, exceptions: %s" % exceptions)
                traceback.print_exc()
        ####################################################
        ####################################################
        ###################################################

        ################################################### SETs
        ###################################################
        ###################################################
        if MyPlotterPureTkinterStandAloneProcess_OPEN_FLAG == 1:

            ####################################################
            MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "StandAlonePlottingProcess_ReadyForWritingFlag" in MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict:
                MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag = MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict["StandAlonePlottingProcess_ReadyForWritingFlag"]

                if MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject_MostRecentDict_StandAlonePlottingProcess_ReadyForWritingFlag == 1:
                    if CurrentTime_CalculatedFromMainThread - LastTime_CalculatedFromMainThread_PLOTTER >= MyPlotterPureTkinterStandAloneProcess_RefreshDurationInSeconds:
                        #pass
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0"], [CurrentTime_CalculatedFromMainThread], [PitchAngle_Theta_Deg_Actual])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread], [PitchAngle_Theta_Deg_Actual, PitchAngularRate_ThetaDot_DegreesPerSecond_Actual])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread], [YawAngle_Delta_Deg_Actual, YawAngularRate_DeltaDot_DegreesPerSecond_Actual])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread], [Wheel_Omega_Theta_RL_RadiansPerSec_Actual, Wheel_Omega_Theta_RR_RadiansPerSec_Actual])
                        #MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0"], [CurrentTime_CalculatedFromMainThread], [Velocity_V_RM_MetersPerSec_Actual])
                        MyPlotterPureTkinterStandAloneProcess_ReubenPython2and3ClassObject.ExternalAddPointOrListOfPointsToPlot(["Channel0", "Channel1"], [CurrentTime_CalculatedFromMainThread, CurrentTime_CalculatedFromMainThread], [Position_X_RM_Meters_Actual, Velocity_V_RM_MetersPerSec_Actual])

                        LastTime_CalculatedFromMainThread_PLOTTER = CurrentTime_CalculatedFromMainThread
            ####################################################

        ###################################################
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
        DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda_last = DataStreamingFrequency_CalculatedFromMainThread_LowPassFilter_ExponentialSmoothingFilterLambda
        DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda_last = DataStreamingFrequency_CalculatedFromGUIthread_LowPassFilter_ExponentialSmoothingFilterLambda
        Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last = Velocity_V_RM_MetersPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda
        YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda_last = YawAngularRate_DeltaDot_RadiansPerSec_Actual_LowPassFilter_ExponentialSmoothingFilterLambda

        UpdateFrequencyCalculation_MainThread_Filtered()
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
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if CSVdataLogger_OPEN_FLAG == 1:
        CSVdataLogger_ReubenPython3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if BarGraphDisplay_OPEN_FLAG == 1:
        BarGraphDisplay_ReubenPython3ClassObject.ExitProgram_Callback()
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