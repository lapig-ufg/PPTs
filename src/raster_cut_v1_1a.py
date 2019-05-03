import os
import sys
import string
import argparse
import time
import subprocess
import shutil
import string

def raster_cut(input_dir,output_dir,data_file,limite_cut,backslh,product):
	print("Preparando para recortar", data_file, "utilizando", limite_cut)
	#return os.system('gdalwarp -of ENVI -t_srs EPSG:4674 -cutline ' + limite_cut + ' ' + input_dir + backslh + data_file + ' -of Gtiff -crop_to_cutline ' + output_dir + backslh + data_file[:-3]  + '.bin -co TFW=YES')	
	
	if data_file.find("IMERG") > -1:
		if product.find('_M')>-1:
			year = data_file[20:24]
			month = data_file[24:26]
		else:
			year = data_file[21:25]
			month = data_file[25:27]
			day = data_file[27:29]
		data_type = 'gpm'
		scale = '1000'
	elif data_file.find('3B43') > -1:
		year = data_file[5:9]
		month = data_file[9:11]
		data_type = 'trmm'
		scale = '3000'
	
	nomen_lapig = str('pa_br_' + data_type + '_' + scale + '_' + year + 'M' + month + '_lapig.tif')
	if product.find('_D')>-1:
		nomen_lapig = str('pa_br_' + data_type + '_' + scale + '_' + year + 'M' + month +'D'+ day + '_lapig.tif')
	return os.system('gdalwarp -multi -wo NUM_THREADS=val/ALL_CPUS --config GDAL_CACHEMAX 512 -wm 4096 -overwrite -t_srs EPSG:4674 -cutline ' + limite_cut + ' ' + input_dir + backslh + data_file + ' -of Gtiff -crop_to_cutline ' + output_dir + backslh + nomen_lapig + ' -co TFW=YES -srcnodata -1 -dstnodata -1')	
	#return os.system('gdalwarp -t_srs EPSG:4674 -cutline ' + limite_cut + ' ' + input_dir + backslh + data_file + ' -of Gtiff -crop_to_cutline ' + output_dir + backslh + data_file + ' -co TFW=YES')