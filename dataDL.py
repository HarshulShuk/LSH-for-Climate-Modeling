import bz2
import os
import urllib.request
from time import time
from pathlib import Path
from multiprocessing.pool import ThreadPool
import subprocess
import shlex
from nco import Nco
#https://dzone.com/articles/simple-examples-of-downloading-files-using-python

# Roadblocks encountered:
# - Creating a multithreaded script to DL observation data of whole US
#     - Making this into a smaller subset of lon / lat 
# - Renaming latitude/longitude to lat / lon
# - Converting [0,360] to [-180,180]
# - Removing other variables to reduce data size
# - Changing units to kg m-2 d-1 from precip
# - Stitching all files together
# - R memory limitations for my laptop

#URL: ftp://192.12.137.7/pub/dcp/archive/OBS/livneh2014.1_16deg/netcdf/daily/


# ncatted -a units,pr,o,c,"kg m-2 d-1" Extraction_pr.nc
# ncrename -v lat,latitude NA1950_1959_pr.nc
# ncrename -v lon,longitude NA1950_1959_pr.nc
# ncrename -d longitude,lon -v longitude,lon in.nc out.nc

#Avergae out a degen dimension: ncwa -a projection in.nc out.nc

# ncks -O --msa -d lon,181.,360. -d lon,0.,180.0 in.nc out.nc
# ncap2 -O -s 'where(lon > 180) lon=lon-360' out.nc out.nc

# ncrcat *nc -o NA1950_1959pRECP.NC
downloadHeader2 = r"/mnt/c/Users/climateStuff/"
downloadHeader = r"/mnt/d/ClimateData/" #Download path
fileType = ".nc"
dropVarsOptions = ["-C -x -v Tmax,Tmin,wind"] #variables to remove

command = "ncks -x -v Tmax,Tmin,wind -d lat,32.0,40.0 -d lon,-110.0,-82.0"

header = "ftp://192.12.137.7/pub/dcp/archive/OBS/livneh2014.1_16deg/netcdf/daily/"#Download url path
fileStub = "livneh_NAmerExt_15Oct2014." 
years = list(range(1980,1990))#X to y-1 in list
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]


def url_response(url):
	item,header = url
	requestURL = header + item + fileType
	downloadPath = downloadHeader2 + item + fileType
	#Whole thing
	print(url)
	with urllib.request.urlopen(requestURL) as sourceFile:
		# This Path can be diff. Mine is like this because I am using
		# WSL and running from terminal, so must reference from /mnt onward
		with open(downloadPath, mode='wb') as destFile:
			for char in sourceFile:
				destFile.write(char)

	#Could you do into same file?
	newDownloadPath = downloadHeader2 + item + "_cleaned" + fileType
	thisCMD = command + " " + downloadPath + " " + newDownloadPath
	os.system(thisCMD)
	os.remove(downloadPath)

	return 1;


#ftp://192.12.137.7/pub/dcp/archive/OBS/livneh2014.1_16deg/netcdf/daily/livneh_NAmerExt_15Oct2014.195001.nc.bz2



print("Years: " + str(years))
print("Months: " + str(months))
print("Downloading zipped files")
urlList = list()
for year in years:
	for month in months:
		file = fileStub + str(year) + str(month)
		url = (file,header)
		urlList.append(url)
# for item in urlList:
# 	print(item)
processPool = ThreadPool()

for i in processPool.imap(url_response,urlList):
	pass

processPool.close()
processPool.join()
#cmdStr = "ncrcat *nc -o " + str(years[0]) + "-" years[-1]
