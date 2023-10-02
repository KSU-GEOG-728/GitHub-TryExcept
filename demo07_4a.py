#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo07_4a.py
    Author: Shawn Hutchinson
    Description:  Demonstration script for GEOG 728 in-class exercise.
    Date created: 10/02/2023
    Python Version: 3.9.16
"""

# Import arcpy and sys modules
import arcpy

# Set geoprocessing environments
arcpy.env.workspace = "D:/GitHub/GitHub-TryExcept/DemoData.gdb"
arcpy.env.overwriteOutput = True

# Declare local variables
inFc = "ks_major_rivers"
clipFc = "flint_hills"
outFc = "clipped_rivers"

# Run GP tool
arcpy.Clip_analysis(inFc, clipFc, outFc)

# Get and print all messages
print(arcpy.GetMessages())