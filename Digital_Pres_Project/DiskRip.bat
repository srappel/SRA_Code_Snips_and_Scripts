@echo off
:start
cls
title Disk Rip for AGSL

::Set the source path
set /p sourcepath=Enter Source Path: 
echo Source Path: %sourcepath%

::Set the destination path
set /p destpath=Enter a destination path: 
echo Destination Path: %destpath%

::Write out the command so that the user can see before approving
echo robocopy %sourcepath% %destpath% /E /Z /r:3 /w:0

::Ask for user to approve the script
set /p userinput=Run Robocopy (Y or N)?

::if user says Y 
if %userinput% == Y robocopy %sourcepath% %destpath% /E /Z /r:3 /w:0
::this one captures lower case
if %userinput% == y robocopy %sourcepath% %destpath% /E /Z /r:3 /w:0

::This will capture anything else and restart the script
if not %userinput% == Y echo Robocopy has been canceled
	pause
	goto start
	
pause
goto start