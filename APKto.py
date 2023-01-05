import os
import xml.etree.ElementTree as ET
from keyboard import press


apks = os.listdir("apk")
# Extract the AndroidManifest.xml file using apktool
for i in apks:
    os.system(f"apktool d apk/{i} -o C:/Users/Segev/PycharmProjects/StackDroid/StackDroid/extracted_apk/{i[:-4]}")
    press('enter')
    # Open the AndroidManifest.xml file
    with open(f"C:/Users/Segev/PycharmProjects/StackDroid/StackDroid/extracted_apk/{i[:-4]}/AndroidManifest.xml", "r") as f:
        # Read the contents of the file
        try:
            manifest_xml = f.read()
        except:
            continue

        # print(manifest_xml)
    # Parse the XML data
    root = ET.fromstring(manifest_xml)

    # Initialize lists to store the extracted information
    permissions = []
    api_calls = []
    activities = []

    # Extract the permissions, API calls, and activities from the AndroidManifest.xml file
    for child in root:
        # Extract the permissions
        if child.tag == 'uses-permission':
            permissions.append(child.attrib['{http://schemas.android.com/apk/res/android}name'])
        for c in child:
            if c.tag == 'uses-library':
                api_calls.append(c.attrib['{http://schemas.android.com/apk/res/android}name'])
            # Extract the activities
            if c.tag == 'activity' and '{http://schemas.android.com/apk/res/android}name' in c.attrib:
                activities.append(c.attrib['{http://schemas.android.com/apk/res/android}name'][1:])

    # Open a new file for writing
    with open(f"ben/{i[:-4]}", "w") as f:
        # Write the permissions to the file
        for permission in permissions:
            f.write(f"permission::{permission}\n")

        # Write the API calls to the file
        for api_call in api_calls:
            f.write(f"api_call::{api_call}\n")

        # Write the activities to the file
        for activity in activities:
            f.write(f"activity::{activity}\n")
