@echo off
cls

::Set the destination path
set /p destpath=Enter a destination path: 
echo Destination Path: %destpath%

::Make the directory for the logs

MKDIR C:\Workspace\SanbornLogs

::1910 raw sanborns
robocopy "R:\Image_Archive\as - Sanborns\Milwaukee\as1910" %destpath% /E /Z /r:3 /w:0 /log:"C:\Workspace\SanbornLogs\1910RAW.txt" /tee

::belle's project folder
robocopy H:\Departments\AGSL\GIS\Projects\Belle\Georeferenced_Sanborns\1910 %destpath% /E /Z /r:3 /w:0 /log:"C:\Workspace\SanbornLogs\1910BELLE.txt" /tee

echo The Transfer is complete 

pause
