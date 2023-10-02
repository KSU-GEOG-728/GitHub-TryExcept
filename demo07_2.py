#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo07_2.py
    Author: Shawn Hutchinson
    Description:  Demonstration script for GEOG 728 featuring CheckExtension and sys module.
    Date created: 10/02/2023
    Python Version: 3.9.16
"""

# Import arcpy and sys modules
import arcpy, sys

# Set geoprocessing environments
arcpy.env.workspace = "D:/GitHub/GitHub-TryExcept/DemoData.gdb"
arcpy.env.overwriteOutput = True

# Check for required extension, execute GP tool, and save raster result
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
    outSlope = arcpy.sa.Slope("KonzaDEM30")
    outSlope.save("KonzaDEM30_Slope")
    arcpy.CheckInExtension("Spatial")

# If extension not available, print a statement, and exit Python
else:
    msg = "The Spatial Analyst extension is not available."
    sys.exit(msg)