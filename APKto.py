import os
import re
import shutil
import time
import xml.etree.ElementTree as ET
import re
from androguard.misc import AnalyzeAPK
from androguard.cli import androlyze_main

from keyboard import press
from xml.dom import minidom  # mini Document Object Model for XML
import BasicBlockAttrBuilder as BasicBlockAttrBuilder
import PScoutMapping as PScoutMapping
import multiprocessing as mp
from dexparser import DEXParser

apks = os.listdir("F:/droid/ben/0/train")
# Extract the AndroidManifest.xml file using apktool

for i in apks:
    filename = i[:-4]
    os.system(f"apktool d {apks}/{i} -o apk/{filename}")
    time.sleep(10)
    press('enter')

    # Initialize lists to store the extracted information
    RequestedPermissionSet = set()
    ActivitySet = set()
    ServiceSet = set()
    ContentProviderSet = set()
    BroadcastReceiverSet = set()
    HardwareComponentsSet = set()
    IntentFilterSet = set()
    URLSet = set()

    try:
        f = open(f'apk/{filename}/AndroidManifest.xml', "r")
        Dom = minidom.parse(f)
        DomCollection = Dom.documentElement

        DomPermission = DomCollection.getElementsByTagName("uses-permission")
        for Permission in DomPermission:
            if Permission.hasAttribute("android:name"):
                RequestedPermissionSet.add(Permission.getAttribute("android:name"))

        DomActivity = DomCollection.getElementsByTagName("activity")
        for Activity in DomActivity:
            if Activity.hasAttribute("android:name"):
                ActivitySet.add(Activity.getAttribute("android:name"))

        DomService = DomCollection.getElementsByTagName("service")
        for Service in DomService:
            if Service.hasAttribute("android:name"):
                ServiceSet.add(Service.getAttribute("android:name"))

        DomContentProvider = DomCollection.getElementsByTagName("provider")
        for Provider in DomContentProvider:
            if Provider.hasAttribute("android:name"):
                ContentProviderSet.add(Provider.getAttribute("android:name"))

        DomBroadcastReceiver = DomCollection.getElementsByTagName("receiver")
        for Receiver in DomBroadcastReceiver:
            if Receiver.hasAttribute("android:name"):
                BroadcastReceiverSet.add(Receiver.getAttribute("android:name"))

        DomHardwareComponent = DomCollection.getElementsByTagName("uses-feature")
        for HardwareComponent in DomHardwareComponent:
            if HardwareComponent.hasAttribute("android:name"):
                HardwareComponentsSet.add(HardwareComponent.getAttribute("android:name"))

        DomIntentFilter = DomCollection.getElementsByTagName("intent-filter")
        DomIntentFilterAction = DomCollection.getElementsByTagName("action")
        for Action in DomIntentFilterAction:
            if Action.hasAttribute("android:name"):
                IntentFilterSet.add(Action.getAttribute("android:name"))

        f.close()
        shutil.rmtree(f'apk/{filename}')


    except Exception as e:
        print(e)
        continue

    try:
        os.system(f"apktool d -f -r -s {apks}/{i} -o apk/{filename}")
        dex = DEXParser(filedir=f"apk\{filename}\classes.dex")
        for s in dex.get_strings():
            print("//////////////////////")
            for encoding in ["utf-8", "latin-1", "utf-16"]:
                try:
                    # Decode the bytes object to a string using the current encoding
                    ss = s.decode(encoding)
                    if "http://" in ss:
                        URLSet.add(ss)
                except UnicodeDecodeError:
                    # If the current encoding is not supported, skip to the next one
                    continue

        # shutil.rmtree(f'apk/{filename}')

    except Exception as e:
        print(e)
        continue


    # Open a new file for writing
    with open(f"drebin/ben/{filename}", "w") as f:
        # Write the permissions to the file
        for permission in RequestedPermissionSet:
            f.write(f"permission::{permission}\n")

        # Write the service to the file
        for service in ServiceSet:
            f.write(f"service::{service}\n")

        # Write the activities to the file
        for activity in ActivitySet:
            f.write(f"activity::{activity[1:]}\n")

        # Write the Intent to the file
        for intent in IntentFilterSet:
            f.write(f"intent::{intent}\n")

        # Write the feature to the file
        for feature in HardwareComponentsSet:
            f.write(f"feature::{feature}\n")

        # Write the provider to the file
        for provider in ContentProviderSet:
            f.write(f"provider::{provider}\n")

        # Write the receiver to the file
        for receiver in BroadcastReceiverSet:
            f.write(f"receiver::{receiver[1:]}\n")

        # Write the URL to the file
        for url in URLSet:
            f.write(f"url::{url}\n")
        print("Saved")
