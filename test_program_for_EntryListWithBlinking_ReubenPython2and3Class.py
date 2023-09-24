# -*- coding: utf-8 -*-

'''
Reuben Brewer, Ph.D.
reuben.brewer@gmail.com
www.reubotics.com

Apache 2 License
Software Revision F, 09/24/2023

Verified working on: Python 2.7, 3.8 for Windows 8.1, 10 64-bit and Raspberry Pi Buster (no Mac testing yet).
'''

__author__ = 'reuben.brewer'

#########################################################
from EntryListWithBlinking_ReubenPython2and3Class import *
from MyPrint_ReubenPython2and3Class import *
#########################################################

#########################################################
import os
import sys
import platform
import time
import datetime
import threading
import collections
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

###########################################################################################################
##########################################################################################################
def getPreciseSecondsTimeStampString():
    ts = time.time()

    return ts
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def TestButtonResponse():
    global MyPrint_ReubenPython2and3ClassObject
    global USE_MyPrint_FLAG

    if USE_MyPrint_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.my_print("Test Button was Pressed!")
    else:
        print("Test Button was Pressed!")
##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def GUI_update_clock():
    global root
    global EXIT_PROGRAM_FLAG
    global GUI_RootAfterCallbackInterval_Milliseconds
    global USE_GUI_FLAG

    global EntryListWithBlinking_ReubenPython2and3ClassObject
    global EntryListWithBlinking_OPEN_FLAG
    global SHOW_IN_GUI_EntryListWithBlinking_FLAG

    global MyPrint_ReubenPython2and3ClassObject
    global MyPrint_OPEN_FLAG
    global SHOW_IN_GUI_MyPrint_FLAG

    if USE_GUI_FLAG == 1:
        if EXIT_PROGRAM_FLAG == 0:
        #########################################################
        #########################################################

            #########################################################
            if EntryListWithBlinking_OPEN_FLAG == 1 and SHOW_IN_GUI_EntryListWithBlinking_FLAG == 1:
                EntryListWithBlinking_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            #########################################################
            if MyPrint_OPEN_FLAG == 1 and SHOW_IN_GUI_MyPrint_FLAG == 1:
                MyPrint_ReubenPython2and3ClassObject.GUI_update_clock()
            #########################################################

            root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
        #########################################################
        #########################################################

##########################################################################################################
##########################################################################################################

##########################################################################################################
##########################################################################################################
def ExitProgram_Callback():
    global EXIT_PROGRAM_FLAG

    print("ExitProgram_Callback event fired!")

    EXIT_PROGRAM_FLAG = 1
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
    global Tab_EntryListWithBlinking
    global Tab_MyPrint

    if USE_TABS_IN_GUI_FLAG == 1:
        #################################################
        TabControlObject = ttk.Notebook(root)

        Tab_EntryListWithBlinking = ttk.Frame(TabControlObject)
        TabControlObject.add(Tab_EntryListWithBlinking, text='   EntryListWithBlinking   ')

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
        Tab_EntryListWithBlinking = root
        Tab_MyPrint = root
        #################################################

    #################################################
    #################################################

    #################################################
    TestButton = Button(Tab_MainControls, text='Test Button', state="normal", width=20, command=lambda i=1: TestButtonResponse())
    TestButton.grid(row=0, column=0, padx=1, pady=1)
    #################################################

    ################################################# THIS BLOCK MUST COME 2ND-TO-LAST IN def GUI_Thread() IF USING TABS.
    root.protocol("WM_DELETE_WINDOW", ExitProgram_Callback)  # Set the callback function for when the window's closed.
    root.title("test_program_for_EntryListWithBlinking_ReubenPython2and3Class")
    root.geometry('%dx%d+%d+%d' % (root_width, root_height, root_Xpos, root_Ypos)) # set the dimensions of the screen and where it is placed
    root.after(GUI_RootAfterCallbackInterval_Milliseconds, GUI_update_clock)
    root.mainloop()
    #################################################

    #################################################  THIS BLOCK MUST COME LAST IN def GUI_Thread() REGARDLESS OF CODE.
    root.quit() #Stop the GUI thread, MUST BE CALLED FROM GUI_Thread
    root.destroy() #Close down the GUI thread, MUST BE CALLED FROM GUI_Thread
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

    global USE_EntryListWithBlinking_FLAG
    USE_EntryListWithBlinking_FLAG = 1

    global USE_MyPrint_FLAG
    USE_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global SHOW_IN_GUI_EntryListWithBlinking_FLAG
    SHOW_IN_GUI_EntryListWithBlinking_FLAG = 1

    global SHOW_IN_GUI_MyPrint_FLAG
    SHOW_IN_GUI_MyPrint_FLAG = 1
    #################################################
    #################################################

    #################################################
    #################################################
    global GUI_ROW_EntryListWithBlinking
    global GUI_COLUMN_EntryListWithBlinking
    global GUI_PADX_EntryListWithBlinking
    global GUI_PADY_EntryListWithBlinking
    global GUI_ROWSPAN_EntryListWithBlinking
    global GUI_COLUMNSPAN_EntryListWithBlinking
    GUI_ROW_EntryListWithBlinking = 1

    GUI_COLUMN_EntryListWithBlinking = 0
    GUI_PADX_EntryListWithBlinking = 1
    GUI_PADY_EntryListWithBlinking = 1
    GUI_ROWSPAN_EntryListWithBlinking = 1
    GUI_COLUMNSPAN_EntryListWithBlinking = 1

    global GUI_ROW_MyPrint
    global GUI_COLUMN_MyPrint
    global GUI_PADX_MyPrint
    global GUI_PADY_MyPrint
    global GUI_ROWSPAN_MyPrint
    global GUI_COLUMNSPAN_MyPrint
    GUI_ROW_MyPrint = 2

    GUI_COLUMN_MyPrint = 0
    GUI_PADX_MyPrint = 1
    GUI_PADY_MyPrint = 1
    GUI_ROWSPAN_MyPrint = 1
    GUI_COLUMNSPAN_MyPrint = 1
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
    global Tab_EntryListWithBlinking
    global Tab_MyPrint

    global GUI_RootAfterCallbackInterval_Milliseconds
    GUI_RootAfterCallbackInterval_Milliseconds = 30

    TKinter_LightGreenColor = '#%02x%02x%02x' % (150, 255, 150) #RGB
    TKinter_LightRedColor = '#%02x%02x%02x' % (255, 150, 150) #RGB
    TKinter_LightYellowColor = '#%02x%02x%02x' % (255, 255, 150) #RGB
    TKinter_DefaultGrayColor = '#%02x%02x%02x' % (240, 240, 240) #RGB
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
    global MyPrint_ReubenPython2and3ClassObject

    global MyPrint_OPEN_FLAG
    MyPrint_OPEN_FLAG = -1
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
        Tab_EntryListWithBlinking = None
        Tab_MyPrint = None
    #################################################
    #################################################

    #################################################
    #################################################
    global EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict
    EntryListWithBlinking_ReubenPython2and3ClassObject_GUIparametersDict = dict([("root", Tab_EntryListWithBlinking),
                                    ("UseBorderAroundThisGuiObjectFlag", 0),
                                    ("GUI_ROW", GUI_ROW_EntryListWithBlinking),
                                    ("GUI_COLUMN", GUI_COLUMN_EntryListWithBlinking),
                                    ("GUI_PADX", GUI_PADX_EntryListWithBlinking),
                                    ("GUI_PADY", GUI_PADY_EntryListWithBlinking),
                                    ("GUI_ROWSPAN", GUI_ROWSPAN_EntryListWithBlinking),
                                    ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_EntryListWithBlinking)])

    global EntryListWithBlinking_Variables_ListOfDicts
    EntryListWithBlinking_Variables_ListOfDicts = [dict([("Name", "TestIntVariable"),("Type", "int"), ("StartingVal", 0), ("MinVal", -10), ("MaxVal", 10),("EntryBlinkEnabled", 1), ("EntryBlinkInactiveColor", TKinter_DefaultGrayColor), ("EntryBlinkActiveColor", TKinter_LightGreenColor)]),
                                                   dict([("Name", "TestFloatVariable"),("Type", "float"), ("StartingVal", 1.1), ("MinVal", -10.1), ("MaxVal", 10.1),("EntryBlinkEnabled", 0)]),
                                                   dict([("Name", "TestStrVariable"),("Type", "str"), ("StartingVal", "default"),("EntryBlinkEnabled", 1),("EntryWidth", 10),("LabelWidth", 25),("FontSize", 8)])]

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
            print("EntryListWithBlinking_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions, 0)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1:

        MyPrint_ReubenPython2and3ClassObject_GUIparametersDict = dict([("USE_GUI_FLAG", USE_GUI_FLAG and SHOW_IN_GUI_MyPrint_FLAG),
                                                                        ("root", Tab_MyPrint),
                                                                        ("UseBorderAroundThisGuiObjectFlag", 0),
                                                                        ("GUI_ROW", GUI_ROW_MyPrint),
                                                                        ("GUI_COLUMN", GUI_COLUMN_MyPrint),
                                                                        ("GUI_PADX", GUI_PADX_MyPrint),
                                                                        ("GUI_PADY", GUI_PADY_MyPrint),
                                                                        ("GUI_ROWSPAN", GUI_ROWSPAN_MyPrint),
                                                                        ("GUI_COLUMNSPAN", GUI_COLUMNSPAN_MyPrint)])

        MyPrint_ReubenPython2and3ClassObject_setup_dict = dict([("NumberOfPrintLines", 10),
                                                                ("WidthOfPrintingLabel", 200),
                                                                ("PrintToConsoleFlag", 1),
                                                                ("LogFileNameFullPath", os.getcwd() + "//TestLog.txt"),
                                                                ("GUIparametersDict", MyPrint_ReubenPython2and3ClassObject_GUIparametersDict)])

        try:
            MyPrint_ReubenPython2and3ClassObject = MyPrint_ReubenPython2and3Class(MyPrint_ReubenPython2and3ClassObject_setup_dict)
            time.sleep(0.25)
            MyPrint_OPEN_FLAG = MyPrint_ReubenPython2and3ClassObject.OBJECT_CREATED_SUCCESSFULLY_FLAG

        except:
            exceptions = sys.exc_info()[0]
            print("MyPrint_ReubenPython2and3ClassObject __init__: Exceptions: %s" % exceptions)
            traceback.print_exc()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_EntryListWithBlinking_FLAG == 1 and EntryListWithBlinking_OPEN_FLAG != 1:
        print("Failed to open EntryListWithBlinking_ReubenPython2and3Class.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    if USE_MyPrint_FLAG == 1 and MyPrint_OPEN_FLAG != 1:
        print("Failed to open MyPrint_ReubenPython2and3ClassObject.")
        ExitProgram_Callback()
    #################################################
    #################################################

    #################################################
    #################################################
    #EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryEnabledState("TestIntVariable", 0)

    print("Starting main loop 'test_program_for_EntryListWithBlinking_ReubenPython2and3Class.")
    StartingTime_MainLoopThread = getPreciseSecondsTimeStampString()

    ToggleVar = 0
    while(EXIT_PROGRAM_FLAG == 0):

        ###################################################
        CurrentTime_MainLoopThread = getPreciseSecondsTimeStampString() - StartingTime_MainLoopThread
        ###################################################

        ################################################### GET's
        if EntryListWithBlinking_OPEN_FLAG == 1:

            EntryListWithBlinking_MostRecentDict = EntryListWithBlinking_ReubenPython2and3ClassObject.GetMostRecentDataDict()

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:
                EntryListWithBlinking_MostRecentDict_DataUpdateNumber = EntryListWithBlinking_MostRecentDict["DataUpdateNumber"]

                print("EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
                #print("DataUpdateNumber = " + str(EntryListWithBlinking_MostRecentDict_DataUpdateNumber) + ", EntryListWithBlinking_MostRecentDict: " + str(EntryListWithBlinking_MostRecentDict))
        ###################################################

        ################################################### SET's
        if EntryListWithBlinking_OPEN_FLAG == 1:

            if "DataUpdateNumber" in EntryListWithBlinking_MostRecentDict and EntryListWithBlinking_MostRecentDict["DataUpdateNumber"] != EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last:

                #EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("TestIntVariable", EntryListWithBlinking_MostRecentDict["TestIntVariable"] + 1)
                EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("TestFloatVariable", EntryListWithBlinking_MostRecentDict["TestFloatVariable"] + 1.0)
                EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryValue("TestStrVariable", EntryListWithBlinking_MostRecentDict["TestStrVariable"] + "a")

                '''
                EntryListWithBlinking_ReubenPython2and3ClassObject.SetEntryEnabledState("TestIntVariable", ToggleVar)
                
                if ToggleVar == 0:
                    ToggleVar = 1
                else:
                    ToggleVar = 0
                '''
        ###################################################

        ###################################################
        EntryListWithBlinking_MostRecentDict_DataUpdateNumber_last = EntryListWithBlinking_MostRecentDict_DataUpdateNumber
        ###################################################

        time.sleep(0.1)
    #################################################
    #################################################

    ################################################# THIS IS THE EXIT ROUTINE!
    #################################################
    print("Exiting main program 'test_program_for_EntryListWithBlinking_ReubenPython2and3Class.")

    #################################################
    if EntryListWithBlinking_OPEN_FLAG == 1:
        EntryListWithBlinking_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    if MyPrint_OPEN_FLAG == 1:
        MyPrint_ReubenPython2and3ClassObject.ExitProgram_Callback()
    #################################################

    #################################################
    #################################################

##########################################################################################################
##########################################################################################################