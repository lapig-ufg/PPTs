#ttp://stackoverflow.com/questions/10875215/python-urllib-downloading-contents-of-an-online-directory
#ttp://stackoverflow.com/questions/4589241/downloading-files-from-an-http-server-in-python
#ttp://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
#ttp://stackoverflow.com/questions/34831770/download-a-file-in-python-with-urllib.request-instead-of-urllib
#ttp://stackoverflow.com/questions/25501090/how-to-get-wget-command-info-with-python

from urllib.request import urlopen

import http.cookiejar as cookielib

import sys
import os
import re
import string
import datetime
import urllib.request

from Login_UI import retrieveLogin

def trmm_day_download(input_dir, Start_Date = None,End_Date = None, backslh ='\\'):

    GetLoginInfo = list(retrieveLogin())

    #Get actual time
    try:
        Start_Date = list(map(int,Start_Date.split('-')))
        start_year = int(Start_Date[0])
        start_month = int(Start_Date[1])
        start_day = int(Start_Date[2])
    except:
        Start_Date = ['1998','01','01']
        start_year = '1998'
        start_month = '01'
        start_day = '01'
    try:
        End_Date =  list(map(int,(End_Date).split('-')))
        end_year = int(End_Date[0])
        end_month = int(End_Date[1])
        end_day = int(End_Date[2])
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


    #print str_Start_Date
    years = list(map(str,range(start_year,end_year+1)))

    #Download files
    try:
        for i in range(0,len(years),1):

            month = []
            months = []

            month = list(map(str,range(1,13)))

            months = list(map(lambda x: '0' + x if len(x)==1 else x,month))

            if years[i] == str_Start_Date[0]:
                try:
                    del months[:months.index(str_Start_Date[1])]
                except:
                    pass

            if years[i] == str_End_Date[0]:
                try:               
                    del months[months.index(str_End_Date[1])+1:]  
                except:
                    pass

            for j in range(0,len(months),1):
                #print months[j]
                url ='https://disc2.nascom.nasa.gov/data/TRMM_L3/TRMM_3B42_Daily.7/'+years[i]+'/'+months[j]+'/'    
                #print url
                #Acess the URL
                try:
                    urlpath =urlopen(url)
                except:
                    continue                
                #Decode the URL
                string = urlpath.read().decode('utf-8')
                
                #Extract HDF5 files and make an file list
                pattern = re.compile('3B.*?nc4.*?')
                filelist = list(set(list(map(str,pattern.findall(string)))))
                filelist.sort()

                #print filelist
    
                try:
                    startImg = filelist.index('3B42_Daily.'+str_Start_Date[0]+str_Start_Date[1]+str_Start_Date[2]+'.7.nc4')
                except:
                    startImg = None
                
                #DEL UNDER START
                if years[i] == str_Start_Date[0]:
                    if months[j] == str_Start_Date[1]:
                        #Start month
                        try:
                            del filelist[:startImg]
                        except:
                            pass
                    else:
                        pass
                else:
                    pass
                
                try:
                    endImg = filelist.index('3B42_Daily.'+str_End_Date[0]+str_End_Date[1]+str_End_Date[2]+'.7.nc4')
                except:
                    endImg = None
                
                #print endImg

                #DEL OVER END
                if years[i] == str_End_Date[0]:
                    if months[j] == str_End_Date[1]:    
                        #End month
                        try:
                            del filelist[endImg+1:]
                        except:
                            pass
                else:
                    pass
                
                filteredList = filelist #= list(filter(lambda x: x not in os.listdir(input_dir),filelist))

                for item in range(0,len(filteredList)):
                
                    os.system('wget --user=' + GetLoginInfo[0] + ' --password=' + GetLoginInfo[1] + ' --show-progress -c -q '+  url + filteredList[item] + ' -O ' + input_dir + backslh + filteredList[item])


    except:
        print ('\nDownloads finished')
    print ('\nDownloads finished')