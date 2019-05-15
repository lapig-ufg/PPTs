import os
import sys
import string
import argparse
import time
import subprocess
import shutil
import string
from osgeo import gdal

def geolocation(input_dir,out_dir,data_file,backslh):
	if data_file.find("IMERG") > -1:
		geo_ext = '-179.95 89.95 179.95 -89.95'
	elif data_file.find('3B43') > -1 or data_file.find('3B42') > -1:
		geo_ext = '-180.0 50 180.0 -50'

	#print ("Preparando para converter", data_file)
	#return os.system('gdal_translate -of GTiff -a_nodata -1 -stats ' + input_dir + '\\' + data_file + ' -a_ullr -180 90 180 -90 ' + out_dir + '\\' + data_file[:-3] + '.tif -co TFW=YES')
	return os.system('gdal_translate -of GTiff -a_nodata -1 -stats ' + input_dir + backslh + data_file + ' -a_srs EPSG:4326 -a_ullr ' + geo_ext + ' ' + out_dir + backslh + data_file + ' -co TFW=YES')
	#return os.system('gdal_translate -of GTiff -a_nodata -1 -stats ' + input_dir + '\\' + data_file + ' -a_srs EPSG:4326 -a_ullr -180 67 180 -67 ' + out_dir + '\\' + data_file + ' -co TFW=YES')
