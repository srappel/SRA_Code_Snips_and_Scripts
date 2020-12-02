@echo off
:start
cls
title Geodex Update Pusher

set /p userinput=Are you sure you want to update the current Geodex build?(Y or N)

::if user says Y 
if %userinput% == Y robocopy H:\Departments\AGSL\GIS\Projects\GEODEX\Project\gdx_editor_tools\gdx_editor_tools\bin\Release H:\Departments\AGSL\GIS\Projects\GEODEX\gdx_editor_tools /is /e /r:2 /w:0
	pause
	exit

::this one captures lower case
if %userinput% == y robocopy H:\Departments\AGSL\GIS\Projects\GEODEX\Project\gdx_editor_tools\gdx_editor_tools\bin\Release H:\Departments\AGSL\GIS\Projects\GEODEX\gdx_editor_tools /is /e /r:2 /w:0
	pause
	exit

::This will capture anything else and restart the script
if not %userinput% == Y echo update has been canceled
	pause
	goto start


