import os
import sys
import string
import argparse
import time
import subprocess
import shutil
import string

def get_info(input_dir,data_file,backslh):
	#print "Arquivos RASTER encontrados!"
	return os.system('gdalinfo ' + input_dir + backslh + data_file + ' -stats> NUL 2> NUL')