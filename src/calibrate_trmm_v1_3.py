import os
import sys
import string
import argparse
import time
import subprocess
import shutil
import string

def calibrate_trmm(input_dir,out_dir,data_file,backslh):
	print ("Processando", data_file)
	
	if (int(data_file[5:9]) % 4) == 0:
				if (data_file[9:11]) == '02':
					print ('Ano bissexto: fevereiro com 29 dias')
					
					return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*696)) + (((A.astype(float))< 0)*((A.astype(float))*(-1))))" --co TFW=YES --NoDataValue=-1')
					#return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*696)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')
					
				elif (data_file[9:11]) in ['01','03','05','07','08','10','12']:
					print ('Ano bissexto: mes com 31 dias')
					return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*744)) + (((A.astype(float))< 0)*((A.astype(float))*(-1))))" --co TFW=YES --NoDataValue=-1')
					#return os.system("gdal_calc.py -A " + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*744)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')
				
				else:
					print ('Ano bissexto: mes com 30 dias')
					return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*720)) + (((A.astype(float))< 0)*((A.astype(float))*(-1))))" --co TFW=YES --NoDataValue=-1')
					#return os.system("gdal_calc.py -A " + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*720)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')
	
	elif (data_file[9:11]) == '02': 
		print ('Ano comum: fevereiro com 28 dias')
		return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*672)) + (((A.astype(float))< 0)*((A.astype(float))*(-1))))" --co TFW=YES --NoDataValue=-1')
		#return os.system("gdal_calc.py -A " + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*672)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')
	
	elif (data_file[9:11]) in ['01','03','05','07','08','10','12']:
		print ('Ano comum: mes com 31 dias')
		return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*744)) + (((A.astype(float))< 0)*((A.astype(float))*-1)))" --co TFW=YES --NoDataValue=-1')
		#return os.system("gdal_calc.py -A " + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*744)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')
			
	else:
		print ('Ano comum: mes com 30 dias')
		return os.system('gdal_calc.py -A ' + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*720)) + (((A.astype(float))< 0)*((A.astype(float))*-1)))" --co TFW=YES --NoDataValue=-1')
		#return os.system("gdal_calc.py -A " + input_dir + backslh + data_file + ' --type=Float32 --outfile=' + out_dir + backslh + data_file + ' --cal="((((A.astype(float))> 0)*((A.astype(float))*720)) + (((A.astype(float))< 0)*((A.astype(float))*0)))" --co TFW=YES --NoDataValue=0')