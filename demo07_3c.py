#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    File name: demo07_3c.py
    Author: Shawn Hutchinson
    Description:  Demonstration script for GEOG 728 featuring try-except blocks.
    Date created: 10/02/2023
    Python Version: 3.9.16
"""

# Import arcpy and sys modules
import arcpy

# Set geoprocessing environments
arcpy.env.workspace = "D:/GitHub/GitHub-TryExcept/DemoData.gdb"
arcpy.env.overwriteOutput = True

# Create local variables
regionExpression = "US_L3NAME = 'High Plains'"
outFcThiessen = "westks_thiessen"

# Select county seats from an ecoregion and calculate Thiessen polys
try:
    if arcpy.CheckProduct("arcinfo") == "Available":
        arcpy.Select_analysis("ks_ecoregions", "temp1", regionExpression)
        print(arcpy.GetMessages())
        arcpy.Select_analysis("ks_cities", "temp2", "STATUS = 'County Seat'")
        print(arcpy.GetMessages())
        arcpy.Intersect_analysis(["temp1", "temp2"], "temp3")
        print(arcpy.GetMessages())
        arcpy.CreateThiessenPolygons_analysis("temp3", "temp4", "ALL")
        print(arcpy.GetMessages())
        arcpy.Clip_analysis("temp4", "KansasBoundary", outFcThiessen)
        print(arcpy.GetMessages())
    
        deleteList = arcpy.ListFeatureClasses("temp*")
        for i in deleteList:
            arcpy.Delete_management(i)

    else:
        print("Your ArcGIS licensing level isn't sufficient.")

except arcpy.ExecuteError:
    print("A critical error occurred:  /n{0}".format(arcpy.GetMessages(2)))
    
finally:
    print("Script ran to completion.")