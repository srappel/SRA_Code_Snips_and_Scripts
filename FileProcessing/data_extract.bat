::This batch file was created for a very specific purpose
::There were a bunch of directories named state by state (ie. CA, CO, CT)
::Inside each directory was a folder called data
::This script iterates through each directory, finds the "data" directory, and copies its contents into the parent folder for each state.
::It then deletes the data directory

::Setting up the env, if you change the path here, also change it at the end of the outer for loop
@echo off
cls
R:
cd R:\Image_Archive\Historic_Print_and_Map_Co\Panoramic_Maps

::Outer for loop loops through the parent folders
for /D %%s in (*) do (
	echo %%~fs
	cd %%~fs
	
	::loops through directories in the parent folders, but there is only one folder, data
	for /D %%f in (*) do (
		echo %%~ff
		cd %%~ff
		::copies the info
		robocopy %%~ff %%~ff\.. /e /z /r:2 /w:0 /tee
		cd ..
		::deletes the data folder
		rmdir /Q /S data
	)
	::bring the pwd back out to the main folder
	cd R:\Image_Archive\Historic_Print_and_Map_Co\Panoramic_Maps
)

pause
