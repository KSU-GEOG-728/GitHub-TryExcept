#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo07_4c.py
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
#clipFc = "county_centroids"
outFc = "clipped_rivers"

# Run a GP tool and print custom error messages
try:
	arcpy.Clip_analysis(inFc, clipFc, outFc)
except arcpy.ExecuteError:
	pass

severity = arcpy.GetMaxSeverity()

if severity == 2:
	print("Error occurred: \n{0}".format(arcpy.GetMessages(2)))
elif severity == 1:
	print("Warning raised: \n{0}".format(arcpy.GetMessages(1)))
else:
	print(arcpy.GetMessages())