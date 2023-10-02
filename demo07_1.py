#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo07_1.py
    Author: Shawn Hutchinson
    Description:  Demonstration script for GEOG 728 featuring CheckProduct and sys module.
    Date created: 10/02/2023
    Python Version: 3.9.16
"""

# Import arcpy and sys modules
import arcpy, sys

# Set geoprocessing environments
arcpy.env.workspace = "D:/GitHub/GitHub-TryExcept/DemoData.gdb"
arcpy.env.overwriteOutput = True

# Check for availability of ArcGIS Advanced and execute GP tool
if arcpy.CheckProduct("arcinfo") == "Available":
    arcpy.FeatureToPoint_management("Tiger2010_Census_County", "county_centroids2")

# If ArcGIS Advanced not available, print statement, and exit Python
else:
    msg = "ArcGIS for Desktop Advanced license is not available."
    print(msg)
    sys.exit(msg)    