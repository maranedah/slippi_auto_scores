#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402

host = "localhost"
port = 4444
password = ""

def changeToScoreBoard():
    ws = obsws(host, port, password)
    ws.connect()

    try:
        # Automatically switch scenes between Players Info/ Vs Screen/ Stats
        ws.call(requests.SetCurrentProgramScene(sceneName="Training Arc - Current Match"))
        
    except KeyboardInterrupt:
        pass

    ws.disconnect()

def changeToVenueCam():
    ws = obsws(host, port, password)
    ws.connect()

    try:
        # Automatically switch scenes between Players Info/ Vs Screen/ Stats
        ws.call(requests.SetCurrentProgramScene(sceneName="Training Arc - Venue"))
        
    except KeyboardInterrupt:
        pass

    ws.disconnect()


def changeStats(url):
    ws = obsws(host, port, password)
    ws.connect()

    try:
        # Automatically switch scenes between Players Info/ Vs Screen/ Stats
        ws.call(requests.SetBrowserSourceProperties("Slippi Stats", url=url))
        time.sleep(1)
        ws.call(requests.SetCurrentScene("Training Arc - Stats"))
        time.sleep(25)
        
        
    except KeyboardInterrupt:
        pass

    ws.disconnect()

def startRecording():
    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.StartRecording())
        
    except KeyboardInterrupt:
        pass

    ws.disconnect()

def stopRecording():
    ws = obsws(host, port, password)
    ws.connect()

    try:
        ws.call(requests.StopRecording())
        
    except KeyboardInterrupt:
        pass

    ws.disconnect()