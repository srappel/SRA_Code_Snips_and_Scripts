@echo off
cls

::Make the directory for the logs

MKDIR C:\Workspace\RobocopyLogs\SEWRPC\


:::::GeoTIFF:::::

::Kenosha TIFF
color 02

robocopy E:\Kenosha_pictometry R:\Aerial_Photos\Kenosha_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Kenosha_TIFF.txt" /tee

color 03

::Milwaukee TIFF
robocopy E:\Milwaukee_pictometry R:\Aerial_Photos\Milwaukee\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Milwaukee_TIFF.txt" /tee

color 04

::Ozaukee TIFF
robocopy E:\Ozaukee R:\Aerial_Photos\Ozaukee_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Ozaukee_TIFF.txt" /tee

color 05

::Racine TIFF
robocopy E:\Racine R:\Aerial_Photos\Racine_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Racine_TIFF.txt" /tee

color 06

::Walworth TIFF
robocopy E:\Walworth R:\Aerial_Photos\Walworth_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Walworth_TIFF.txt" /tee

color 07

::Washington TIFF
robocopy E:\Washington R:\Aerial_Photos\Washington_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Washington_TIFF.txt" /tee

color 09

::Waukesha TIFF
robocopy E:\Waukesha R:\Aerial_Photos\Waukesha_Co\2015_SEWRPC_UWM\GeoTIFF /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Waukesha_TIFF.txt" /tee

:::::MrSID::::::

color f1

::Kenosha MrSID
robocopy E:\MrSID_NAD27_MG3\Kenosha_MrSID_MG3 R:\Aerial_Photos\Kenosha_Co\2015_SEWRPC_UWM\MrSID /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Kenosha_MrSID.txt" /tee

color f2

::Ozaukee MrSID
robocopy E:\MrSID_NAD27_MG3\Ozaukee_MrSID_MG3 R:\Aerial_Photos\Ozaukee_Co\2015_SEWRPC_UWM\MrSID /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Ozaukee_MrSID.txt" /tee

color f3

::Racine MrSID
robocopy E:\MrSID_NAD27_MG3\Racine_MrSID_MG3 R:\Aerial_Photos\Racine_Co\2015_SEWRPC_UWM\MrSID /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Racine_MrSID.txt" /tee

color f4

::Walworth MrSID
robocopy E:\MrSID_NAD27_MG3\Walworth_MrSID_MG3 R:\Aerial_Photos\Walworth_Co\2015_SEWRPC_UWM\MrSID /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Walworth_MrSID.txt" /tee

color f5

::Washington MrSID
robocopy E:\MrSID_NAD27_MG3\Washington_MrSID_MG3 R:\Aerial_Photos\Washington_Co\2015_SEWRPC_UWM\MrSID /E /Z /r:3 /w:0 /log:"C:\Workspace\RobocopyLogs\SEWRPC\Washington_MrSID.txt" /tee

color af
echo The Transfer is complete 

pause
