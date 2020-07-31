#ttp://stackoverflow.com/questions/10875215/python-urllib-downloading-contents-of-an-online-directory
#ttp://stackoverflow.com/questions/4589241/downloading-files-from-an-http-server-in-python
#ttp://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
#ttp://stackoverflow.com/questions/34831770/download-a-file-in-python-with-urllib.request-instead-of-urllib
#ttp://stackoverflow.com/questions/25501090/how-to-get-wget-command-info-with-python

import sys
import os
import re
import string
import datetime
from urllib.request import urlopen

from Login_UI import retrieveLogin

def gpm_month_download(outputDir, Start_Date = None,End_Date = None, backslh ='\\'):

    GetLoginInfo = list(retrieveLogin())

    #Get actual time
    try:
        Start_Date = list(map(int,Start_Date.split('-')))
        start_year = int(Start_Date[0])
        start_month = int(Start_Date[1])
        start_day = 1
    except:
        Start_Date = ['2014','03','12']
        start_year = '2014'
        start_month = '03'
        start_day = '12'
    try:
        End_Date =  list(map(int,(End_Date).split('-')))
        end_year = int(End_Date[0])
        end_month = int(End_Date[1])
        end_day = 1
    except:
        End_Date = list(map(int,((datetime.datetime.now()).strftime('%Y-%m-%d')).split('-')))
        end_year = int(End_Date[0])
        end_month = int(End_Date[1])
        end_day = int(End_Date[2])

    
    str_Start_Date = list(map(str,Start_Date))
    str_End_Date = list(map(str,End_Date))

    #Start month
    if len(str_Start_Date[1]) == 1:
        str_Start_Date[1] = '0' + str_Start_Date[1]
    #End month
    if len(str_End_Date[1]) == 1:
        str_End_Date[1] = '0' + str_End_Date[1]

    #Start day
    if len(str_Start_Date[2]) == 1:
        str_Start_Date[2] = '0' + str_Start_Date[2]
    #End day
    if len(str_End_Date[2]) == 1:
       str_End_Date[2] = '0' + str_End_Date[2]


    
    years = list(map(str,range(start_year,end_year+1)))

    #Download files
    try:
        for i in range(0,len(years),1):
                    
            url ='https://gpm1.gesdisc.eosdis.nasa.gov/data/GPM_L3/GPM_3IMERGM.06/'+years[i]+'/'    
            
            #Acess the URL
            try:
                urlpath =urlopen(url)
            except:
                continue
            
            #Decode the URL
            string = urlpath.read().decode('utf-8')
            
            #Extract HDF5 files and make an file list
            pattern = re.compile('3B.*?HDF5.*?')
            filelist = list(set(list(map(str,pattern.findall(string)))))
            filelist.sort()

            try:
                try:
                    startImg = filelist.index('3B-MO.MS.MRG.3IMERG.'+str_Start_Date[0]+str_Start_Date[1]+'01'+'-S000000-E235959.'+ str_Start_Date[1] +'.V06B.HDF5')
                except:
                    startImg = filelist.index('3B-MO.MS.MRG.3IMERG.20140312-S000000-E235959.03.V06B.HDF5')
            except:
                startImg = None
            
            #DEL UNDER START
            if years[i] == str_Start_Date[0]:
                #Start month
                try:                    
                    del filelist[:startImg]
                except:
                    pass
            else:
                pass
            
            try:
                endImg = filelist.index('3B-MO.MS.MRG.3IMERG.'+str_End_Date[0]+str_End_Date[1]+'01'+'-S000000-E235959.'+str_End_Date[1]+'.V06B.HDF5')
            except:
                endImg = None
            
            #DEL OVER END
            if years[i] == str_End_Date[0]:
                #End month
                try:
                    del filelist[endImg+1:]
                except:
                    pass
            else:
                pass

            filteredList = filelist #= list(filter(lambda x: x not in os.listdir(outputDir),filelist))

            print(filteredList)
       
            for item in range(0,len(filteredList)):
                
                os.system('wget --user=' + GetLoginInfo[0] + ' --password=' + GetLoginInfo[1] + ' --show-progress -c -q '+  url + filteredList[item] + ' -O ' + outputDir + backslh + filteredList[item])

    except:
        print ('\nDownloads finished')
    
    print ('\nDownloads finished')
