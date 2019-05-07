# PPTs
Precipitation Processing Tools (PPTs) it's an open source code developed by Vinícius Mesquita to download and process satellite precipitation data from NASA Tropical Rainfall Measuring Mission (TRMM) and Global Precipitation Measurement Mission (GPM)

Requisites:

  *Python 3.6 or above
  
  *PyQt5 python package
  
  *Gdal python package
  
  *wget package (If windows!, download Cygwin setup here http://cygwin.com/install.html, install with wget package and add C:\cygwin64\bin to variables of the system)
  
  
Recommendations: 
  *Install Anaconda Python 3.6 or above (https://www.anaconda.com/download/) and the Gdal package (https://anaconda.org/conda-forge/gdal)

#HOW TO RUN

You can use the **PPT_UI_RUN.py** to run an user-friendly interface or parse some arguments to ***Integration.py*** like:


***--ProdTP*** = 'GPM_M','GPM_D','TRMM_M','TRMM_D'

GPM_M: GPM Monthly (IMERGM v4)

GPM_D: GPM Daily (IMERGDF v4)

TRMM_M: TRMM Monthly (TRMM 3B43 v7)

TRMM_D: TRMM Daily (TRMM 3B42 v7)

***--StartDate*** = Insert the start date

***--EndDate*** = Insert the end date

***--ProcessDir*** = Insert the processing directory path

***--SptSlc*** = Insert the slice feature path (if not used, it assumes a Global product)

***--OP*** = Call this argument if you wanna Only Process the data. Make sure you have a directory with a raw files subfolder!!!!
 
 
 **E.G.***: python Integration.py --ProdTP GPM_M --StartDate 2018-01-01 --EndDate 2018-12-31 --ProcessDir ~./mydirectory --SptSlc ~./brazil_boundary.shp --OP
 
 
 ***UNDER CONSTRUCTION!***
 You may experience bugs and prints in brazilian portuguese
 
 
