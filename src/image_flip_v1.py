import os
import sys
import string
import argparse
import time
import subprocess
import shutil
import string
import numpy
import re
import numpy as np
from osgeo import gdal
from osgeo.gdalnumeric import *
from osgeo.gdalconst import *


def flipper(out_dir,data_file):
	print ("Preparando para converter", data_file)
	
	fname = str(data_file)
	outname = str(out_dir)
	ds = gdal.Open(fname, GA_ReadOnly)
	band = ds.GetRasterBand(1)
	#ar = BandReadAsArray(band)
	ar = band.ReadAsArray()
	# .T means transpose 2D array
	#TPSGPM = rot90(ar,2)
	TPSGPM = rot90(ar,1)
	driver = gdal.GetDriverByName("GTiff")
	dsOutGPM = driver.Create(outname , ds.RasterYSize, ds.RasterXSize, 1, band.DataType)
	CopyDatasetInfo(ds,dsOutGPM)
	bandOut=dsOutGPM.GetRasterBand(1)
	BandWriteArray(bandOut, TPSGPM)
	ds = band = None  # save, close
	
	#return os.system('gdal_translate -of GTiff -a_nodata -1 -stats ' + input_dir + '\\' + data_file + ' -a_ullr -180 90 180 -90 -a_srs EPSG:4326 ' + out_dir + '\\' + data_file[:-3] + '.tif -co TFW=YES')
	#return os.system('gdal_translate -of GTiff -a_nodata -1 -stats ' + input_dir + '\\' + data_file + ' -a_ullr -180 90 -90 180  -a_srs EPSG:4326 ' + out_dir + '\\' + data_file[:-3] + '.tif -co TFW=YES')
