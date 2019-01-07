import os
import sys
import string
#import commands
import argparse
import time
import shutil
import string
import re
import numpy
import tkinter
from tkinter import filedialog
import string
import platform
import argparse
import datetime


#GPM MONTH

from gpm_download_v1_4_for_V05 import gpm_month_download
from calibrate_gpm_v1_3 import calibrate_gpm

#GPM DAY

#from gpm_download_day_edition_v3 import gpm_day_download
from gpm_download_day_edition_v3_1_for_V05 import gpm_day_download
#from gpm_download_dayL_edition_v3_forV04 import gpm_day_download
#from gpm_download_day_Late_edition_v3 import gpm_day_download
from calibrate_gpm_day import calibrate_gpm_day

#TRMM MONTH

from trmm_download_v1_3 import trmm_month_download
from calibrate_trmm_v1_3 import calibrate_trmm #calibrate_gpm

#TRMM DAY

from trmm_download_day_edition_v3 import trmm_day_download
from calibrate_gpm_day import calibrate_gpm_day #calibrate_gpm

#AncillaryData
from image_flip_v1 import flipper
from get_info_v1_1 import get_info
from data_geolocation_v1 import geolocation #nc_2_tiff
from raster_cut_v1_1a import raster_cut

def system_os():
	if platform.system() == 'Windows':
		return 1
	else:
		return 2
		
global backslh
global input_dir_data

if system_os() == 1:
	backslh = '\\'

else:
	backslh = '/'

#print 'O seu sistema operacional e %s' % platform.system()

#DIRECTORIE INFOS

#ARGS GET_OPT

#GET ARGUMENTS FOR DATA PROCESSING
def parseArguments():

	parser = argparse.ArgumentParser(prog='Precipitation Processing Tool')
	parser.add_argument('--ProdTP',choices= ['GPM_M','GPM_D','TRMM_M','TRMM_D'],default='GPM_M',dest='ProdTP', help='GPM_M: GPM Monthly (IMERGM v4);\n GPM_D: GPM Daily (IMERGDF v4);\n TRMM_M: TRMM Monthly (TRMM 3B43 v7);\n TRMM_D: TRMM Daily (TRMM 3B42 v7).\n')
	StartDF = '12-03-2014'# if ProdTP == 'GPM_M' or ProdTP == 'GPM_D' else '01-01-1998'
	EndDF = str((datetime.datetime.now()).strftime('%Y-%m-%d'))
	parser.add_argument('--StartDate',dest='StartDate', help='Insert the start date',default=StartDF,type=str)
	parser.add_argument('--EndDate',dest='EndDate', help='Insert the end date',default=EndDF,type=str)
	parser.add_argument('--ProcessDir',dest='ProcessDir', help='Insert the processing directory path',type=str)
	parser.add_argument('--SptSlc',dest='SptSlc', nargs="?", help='Insert the slice feature path',type=str)
	parser.add_argument('--OP', dest='OP',action="store_true", help='Call this argument if you wanna Only Process the data. Make sure you have a directory with a raw files subfolder!!!!')

	args = parser.parse_args();
	return args

args = parseArguments()

if args.OP == '':
	args.OP == False

helios = [args.ProdTP,args.StartDate,args.EndDate,args.ProcessDir,args.SptSlc,args.OP]
print(helios)

# Chamar funcoes do Tkinter e invocar janela de selecao de diretorio
tkinter.Tk().withdraw()

#DIR CHECK
if helios[3] == None:
		
	try:
		input_dir_data = filedialog.askdirectory(initialdir="/",title='Por favor selecione o diretorio de saida dos dados!')
		if len(input_dir_data) == 0:
			raise IOError
		if system_os() == 1:
			input_dir_data = str(input_dir_data).replace('/', '\\')

		else:
			input_dir_data = input_dir_data

	except:
		print ("ERROUUUUUUU! Voce nao inseriu o diretorio de entrada")
		sys.exit(2)
else:

	if system_os() == 1:
		input_dir_data = str(helios[3])

		input_dir_data = input_dir_data.replace('/','\\')
	else:
		input_dir_data = str(helios[3])

#PROCESS METHOD CHECK
#global OnlyProcess
#OnlyProcess = False
#
#if helios[4] == True:
#	OnlyProcess = True

############################################################### - INTEGRATION
	
download_dir = None
DirEnd = None
	
#MONTH
if helios[0] == 'GPM_M':
	#GPM

	#Criacao de diretorio de download para GPM Month
	
	try:
		os.mkdir(input_dir_data + backslh + 'GPM_BRUTO_MONTH')
	except:
		pass
	
	# Diretorio de saida dos dados baixados - organizar para o algoritmo pai
	download_dir = input_dir_data + backslh + 'GPM_BRUTO_MONTH'

	print(download_dir,backslh,helios[1],helios[2])

	if helios[5] == False:
		gpm_month_download(download_dir,backslh=backslh,Start_Date = helios[1],End_Date = helios[2])
	
	DirEnd = 'GPM_BRUTO_MONTH'
	
	#TRMM

	#Criacao de diretorio de download para TRMM Month
elif helios[0] == 'TRMM_M':	
	try:
		os.mkdir(input_dir_data + backslh + 'TRMM_BRUTO_MONTH')
	except:
		pass

	# Diretorio de saida dos dados baixados - organizar para o algoritmo pai
	download_dir = input_dir_data + backslh + 'TRMM_BRUTO_MONTH'

	if helios[5] == False:
		trmm_month_download(download_dir,backslh = backslh,Start_Date=helios[1],End_Date=helios[2])
	
	DirEnd = 'TRMM_BRUTO_MONTH'

#DAY
	
	#GPM

	#Criacao de diretorio de download para GPM Day
elif helios[0] == 'GPM_D':		
	try:
		os.mkdir(input_dir_data + backslh + 'GPM_BRUTO_DAY')
	except:
		pass
	
	# Diretorio de saida dos dados baixados - organizar para o algoritmo pai
	download_dir = input_dir_data + backslh + 'GPM_BRUTO_DAY'
	
	if helios[5] == False:
		gpm_day_download(download_dir,backslh=backslh,Start_Date = helios[1],End_Date = helios[2])
	
	DirEnd = 'GPM_BRUTO_DAY'

	#TRMM

	#Criacao de diretorio de download para TRMM Day
elif helios[0] == 'TRMM_D':		
	try:
		os.mkdir(input_dir_data + backslh + 'TRMM_BRUTO_DAY')
	except:
		pass

	# Diretorio de saida dos dados baixados - organizar para o algoritmo pai
	download_dir = input_dir_data + backslh + 'TRMM_BRUTO_DAY'
	
	if helios[5] == False:
		trmm_day_download(download_dir,Start_Date=helios[1],End_Date=helios[2])
	
	DirEnd = 'TRMM_BRUTO_DAY'

else:
	print ("UQ TA CONTESSENO??")
	sys.exit(2)

############################################################### - INTEGRATION


zero_dir = download_dir#[:-1]

try:
	os.mkdir(input_dir_data + backslh + '1')
except:
	print ("Esse diretorio ja existe")

try:
	os.mkdir(input_dir_data + backslh + '2')
except:
	print ("Esse diretorio ja existe")

try:
	os.mkdir(input_dir_data + backslh + '3')
except:
	print ("Esse diretorio ja existe")

try:
	os.mkdir(input_dir_data + backslh + DirEnd + "_processed")
except:
	print ("Esse diretorio ja existe")

fst_dir = input_dir_data + backslh + '1'
scd_dir = input_dir_data + backslh + '2'
thd_dir = input_dir_data + backslh + '3'


fth_dir = input_dir_data + backslh + DirEnd + "_processed"

#====================================================================================LIST ZERO==========================================================================================

zero_list = os.listdir(zero_dir)

zero_list = sorted(zero_list, key = lambda x: x.rsplit('.', 1)[0])

if helios[0] == 'GPM_M':

	for n in range(0,len(zero_list),1):
		if zero_list[n].endswith('.HDF5') > -1 and zero_list[n].find('.xml') == -1 and zero_list[n].find('.aux') == -1 and zero_list[n].find('.tfw') == -1:
			if 	zero_list[n].find('.HDF5') > -1:
				extract_subdata = 'HDF5:"%s%s%s"://Grid/precipitation' % (zero_dir,backslh,zero_list[n])
				outfile = '%s%s%s.tif' % (fst_dir,backslh,zero_list[n][:-5])
				flipper(outfile,extract_subdata)
				extract_subdata = outfile = None
			else:
				print(zero_list[n])

elif helios[0] == 'TRMM_M':

	for n in range(0,len(zero_list),1) :
		if zero_list[n].endswith('.HDF') > -1 and zero_list[n].find('.xml') == -1 and zero_list[n].find('.aux') == -1 and zero_list[n].find('.tfw') == -1:
			extract_subdata = 'HDF4_SDS:UNKNOWN:"%s%s%s":0' % (zero_dir,backslh,zero_list[n])
			outfile = '%s%s%s.tif' % (fst_dir,backslh,zero_list[n][:-4])
			flipper(outfile,extract_subdata)
			extract_subdata = outfile = None
		else:
			print(zero_list[n])

elif helios[0] == 'GPM_D':
	print('hu3')
	for n in range(0,len(zero_list),1):
		if zero_list[n].endswith('.nc4') > -1 and zero_list[n].find('.xml') == -1 and zero_list[n].find('.aux') == -1 and zero_list[n].find('.tfw') == -1:
			extract_subdata2 = 'HDF5:"%s%s%s"://precipitationCal' % (zero_dir, backslh, zero_list[n])
			outfile2 = '%s%s%s_precipitationCal.tif' % (fst_dir,backslh, zero_list[n][:-4])
			flipper(outfile2,extract_subdata2)
			extract_subdata2 = outfile2 = None
		else:
			print (zero_list[n])


elif helios[0] == 'TRMM_D':

	for n in range(0,len(zero_list),1) :
		if zero_list[n].find('.nc4') > -1 and zero_list[n].find('.xml') == -1 and zero_list[n].find('.aux') == -1 and zero_list[n].find('.tfw') == -1:
			extract_subdata = 'HDF5:"%s%s%s"://precipitation' % (zero_dir,backslh,zero_list[n])
			outfile = '%s%s%s.tif' % (fst_dir,backslh,zero_list[n][:-6])
			flipper(outfile,extract_subdata)
			extract_subdata = outfile = None			
		else:
			print (zero_list[n])
else:
	print ("UQ TA CONTESSENO2??")
	sys.exit(2)

#====================================================================================LIST ONE==========================================================================================
fst_list = os.listdir(fst_dir)

fst_list = sorted(fst_list, key = lambda x: x.rsplit('.', 1)[0])

for n in range(0,len(fst_list),1):
	if fst_list[n].find('.tif') > -1 and fst_list[n].find('.xml') == -1 and fst_list[n].find('.aux') == -1 and fst_list[n].find('.tfw') == -1:
		print(fst_list[n])
		get_info(fst_dir,fst_list[n],backslh)
		
for n in range(0,len(fst_list),1):
	if fst_list[n].find('.tif') > -1 and fst_list[n].find('.xml') == -1 and fst_list[n].find('.aux') == -1 and fst_list[n].find('.tfw') == -1:
		print(fst_list[n])
		geolocation(fst_dir,scd_dir,fst_list[n],backslh)


#====================================================================================LIST TWO==========================================================================================		
shutil.rmtree(fst_dir)

scd_list = os.listdir(scd_dir)

scd_list = sorted(scd_list, key = lambda x: x.rsplit('.', 1)[0])		
		
		
for n in range(0,len(scd_list),1):
	if scd_list[n].find('.tif') > -1 and scd_list[n].find('.xml') == -1 and scd_list[n].find('.aux') == -1 and scd_list[n].find('.tfw') == -1:
		get_info(scd_dir,scd_list[n],backslh)
		
for n in range(0,len(scd_list),1):
	if scd_list[n].find('.tif') > -1 and scd_list[n].find('.xml') == -1 and scd_list[n].find('.aux') == -1 and scd_list[n].find('.tfw') == -1:
		
		if helios[0] == 'GPM_M':
			calibrate_gpm(scd_dir,thd_dir,scd_list[n],backslh)
		elif helios[0] == 'TRMM_M':
			calibrate_trmm(scd_dir,thd_dir,scd_list[n],backslh)
		elif helios[0] == 'GPM_D':
			calibrate_gpm_day(scd_dir,thd_dir,scd_list[n],backslh)
		elif helios[0] == 'TRMM_D':
			calibrate_gpm_day(scd_dir,thd_dir,scd_list[n],backslh)
		else:
			print ("UQ TA CONTESSENO3??")
			sys.exit(2)

#====================================================================================LIST THREE==========================================================================================		
shutil.rmtree(scd_dir)	

geek = '_processed'

if helios[4] == 'None':
	
	thd_list = os.listdir(thd_dir)
	
	thd_list = sorted(thd_list, key = lambda x: x.rsplit('.', 1)[0])
			
	for n in range(0,len(thd_list),1):
		if thd_list[n].find('.tif') > -1 and thd_list[n].find('.xml') == -1 and thd_list[n].find('.aux') == -1 and thd_list[n].find('.tfw') == -1:
			get_info(thd_dir,thd_list[n],backslh)

	try:
		os.rename(thd_dir,thd_dir[:-1] + "Global")
	except:
		pass
	
	DirEnd = "Global"
	geek = ""
	shutil.rmtree(fth_dir)

else:

	fft_dir = helios[4]

	thd_list = os.listdir(thd_dir)
	
	thd_list = sorted(thd_list, key = lambda x: x.rsplit('.', 1)[0])
			
	for n in range(0,len(thd_list),1):
		if thd_list[n].find('.tif') > -1 and thd_list[n].find('.xml') == -1 and thd_list[n].find('.aux') == -1 and thd_list[n].find('.tfw') == -1:
			pass
			#get_info(thd_dir,thd_list[n],backslh)
			
	for n in range(0,len(thd_list),1):
		if thd_list[n].find('.tif') > -1 and thd_list[n].find('.xml') == -1 and thd_list[n].find('.aux') == -1 and thd_list[n].find('.tfw') == -1:
			raster_cut(thd_dir,fth_dir,thd_list[n],fft_dir,backslh,helios[0])			
	
	#====================================================================================LIST FOUR==========================================================================================
	#shutil.rmtree(thd_dir)
	
	fth_list = os.listdir(fth_dir)
	
	fth_list = sorted(fth_list, key = lambda x: x.rsplit('.', 1)[0])
			
	for n in range(0,len(fth_list),1):
		if fth_list[n].find('.tif') > -1 and fth_list[n].find('.xml') == -1 and fth_list[n].find('.aux') == -1 and fth_list[n].find('.tfw') == -1:
			get_info(fth_dir,fth_list[n],backslh)

print ("Process done! All files are store in the subfolder " + DirEnd + geek + ". Thanks for using PPT")