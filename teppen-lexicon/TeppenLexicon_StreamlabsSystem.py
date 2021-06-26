#!/usr/bin/python
# -*- coding: utf-8 -*-
# pylint: disable=invalid-name
"""TEPPEN Lexicon Streamlabs Chatbot script"""
#---------------------------------------
# Libraries and references
#---------------------------------------
import codecs
import json
import os
import re
#---------------------------------------
# [Required] Script information
#---------------------------------------
ScriptName = "TEPPENLexicon"
Website = "https://www.twitch.tv/neoncraze_"
Creator = "@neoncraze_"
Version = "1.0.0"
Description = "API for interacting with TEPPEN Lexicon"
#---------------------------------------
# Versions
#---------------------------------------
""" 
1.0.0 - Initial Release
"""
#---------------------------------------
# Variables
#---------------------------------------
settingsFile = os.path.join(os.path.dirname(__file__), "settings.json")
#---------------------------------------
# Classes
#---------------------------------------
class Settings:
    """" Loads settings from file if file is found if not uses default values"""

    # The 'default' variable names need to match UI_Config
    def __init__(self, settingsFile=None):
        if settingsFile and os.path.isfile(settingsFile):
            with codecs.open(settingsFile, encoding='utf-8-sig', mode='r') as f:
                self.__dict__ = json.load(f, encoding='utf-8-sig')

        else: #set variables if no custom settings file is found
            self.MessageInvalidInput = "$user usage: !teppen <card name>"
            self.Commands = "!teppen lexicon"
            

    # Reload settings on save through UI
    def ReloadSettings(self, data):
        """Reload settings on save through UI"""
        Parent.SendStreamMessage(json.dumps(data))
        self.__dict__ = json.loads(data, encoding='utf-8-sig')
        return

    # Save settings to files (json and js)
    def SaveSettings(self, settingsFile):
        """Save settings to files (json and js)"""
        with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
            json.dump(self.__dict__, f, encoding='utf-8-sig')
        with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
            f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
        return

#---------------------------------------
# Settings functions
#---------------------------------------
def ReloadSettings(jsondata):
    """Reload settings on Save"""
    # Reload saved settings
    MySet.ReloadSettings(jsondata)
    # End of ReloadSettings

def SaveSettings(self, settingsFile):
    """Save settings to files (json and js)"""
    with codecs.open(settingsFile, encoding='utf-8-sig', mode='w+') as f:
        json.dump(self.__dict__, f, encoding='utf-8-sig')
    with codecs.open(settingsFile.replace("json", "js"), encoding='utf-8-sig', mode='w+') as f:
        f.write("var settings = {0};".format(json.dumps(self.__dict__, encoding='utf-8-sig')))
    return

#---------------------------------------
# System functions
#---------------------------------------

#---------------------------------------
# [Required] functions
#---------------------------------------
def Init():
    global MySet
    # Load in saved settings
    MySet = Settings(settingsFile)
    # End of Init
    global firstcommand 
    firstcommand = MySet.Commands.lower().split()    
    return

def Execute(data):
    """Required Execute data function"""
    if data.IsChatMessage():
        split = data.Message.split(' ');
        if split[0][0] == '!':
            if split[0][1:] in MySet.Commands:
                if len(split) > 1:
                    SendResp(data, "Stream Chat", "@$user http://teppenlexicon.com/en/cards/?name_contains=" + str('+'.join(split[1:])))
                else:
                    SendResp(data, "Stream Chat", MySet.MessageInvalidInput)
    return

def Tick():
    """Required tick function"""
    return

#---------------------------------------
# Parse functions
#---------------------------------------

def SendResp(data, Usage, Message):
    """Sends message to Stream or discord chat depending on settings"""
    Message = Message.replace("$user", data.UserName)

    l = ["Stream Chat", "Chat Both", "All", "Stream Both"]
    if not data.IsFromDiscord() and (Usage in l) and not data.IsWhisper():
        Parent.SendStreamMessage(Message)
