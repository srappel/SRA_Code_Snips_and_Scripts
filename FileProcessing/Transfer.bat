@echo off
cls

::Make the directory for the logs

MKDIR C:\RobocopyLogs\

robocopy H:\Departments\AGSL\GIS\Projects\agsdisc_project\agsdisc\agsdisc0002 R:\Image_Archive\FAA_Aeronautical_Charts\Alaska /E /Z /r:3 /w:0 /log:"C:\RobocopyLogs\Alaska.txt" /tee

robocopy H:\Departments\AGSL\GIS\Projects\agsdisc_project\agsdisc\agsdisc0003 R:\Image_Archive\FAA_Aeronautical_Charts\East /E /Z /r:3 /w:0 /log:"C:\RobocopyLogs\East.txt" /tee

robocopy H:\Departments\AGSL\GIS\Projects\agsdisc_project\agsdisc\agsdisc0004 R:\Image_Archive\FAA_Aeronautical_Charts\West /E /Z /r:3 /w:0 /log:"C:\RobocopyLogs\West.txt" /tee

echo The Transfer is complete 

pause
