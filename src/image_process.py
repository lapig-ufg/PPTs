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


def process(out_dir,data_file,dataInfo):
	#print ("Preparando para converter", data_file)
	
	hourFactor = None

	if dataInfo in ['GPM_D','TRMM_D']:
		hourFactor = 1

	elif dataInfo == 'GPM_M':
		fileName = (str(data_file).split("\\")[-1]).split('"')[0]

		if str(fileName[20:28]) == '20140312':
			hourFactor = 456

		elif (int(fileName[20:24]) % 4) == 0:
					if (fileName[24:26]) == '02':
						hourFactor = 696

					elif (fileName[24:26]) in ['01','03','05','07','08','10','12']:
						hourFactor = 744

					elif (fileName[24:26]) in ['04','06','09','11']:
						hourFactor = 720

		elif (fileName[24:26]) == '02': 
			hourFactor = 672
			
		
		elif (fileName[24:26]) in ['01','03','05','07','08','10','12']:
			
			hourFactor = 744
				
		elif (fileName[24:26]) in ['04','06','09','11']:
			hourFactor = 720
	
	elif dataInfo == 'TRMM_M':

		fileName = data_file.split("\\")[-1][:-3]

		if (int(fileName[5:9]) % 4) == 0:
				
			if (fileName[9:11]) == '02':
				hourFactor = 696

			elif (fileName[9:11]) in ['01','03','05','07','08','10','12']:
				hourFactor = 744

			else:
				hourFactor = 720

		elif (fileName[9:11]) == '02':
			hourFactor = 672	
		elif (fileName[9:11]) in ['01','03','05','07','08','10','12']:
			hourFactor = 744
		else:
			hourFactor = 720

	fname = str(data_file)
	outname = str(out_dir)
	ds = gdal.Open(fname, GA_ReadOnly)
	band = ds.GetRasterBand(1)
	#ar = BandReadAsArray(band)
	ar = band.ReadAsArray()
	# .T means transpose 2D array
	#TPSGPM = rot90(ar,2)
	TPSGPM = rot90(ar,1)

	TPSGPM = ((TPSGPM.astype(float))> 0)*((TPSGPM.astype(float))*hourFactor) + ((TPSGPM.astype(float))< 0)*0

	driver = gdal.GetDriverByName("GTiff")
	dsOutGPM = driver.Create(outname , ds.RasterYSize, ds.RasterXSize, 1, band.DataType)
	CopyDatasetInfo(ds,dsOutGPM)
	bandOut=dsOutGPM.GetRasterBand(1)
	BandWriteArray(bandOut, TPSGPM)
	ds = band = None  # save, close