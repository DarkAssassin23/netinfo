@echo off

net session >nul 2>&1
if %errorLevel% == 0 (
	echo Uninstalling Netinfo...
	set "UserPath="
	for /F "skip=2 tokens=1,2*" %%G in ('%SystemRoot%\System32\reg.exe query "HKCU\Environment" /v "Path" 2^>nul') do if /I "%%G" == "Path" (
    		if /I "%%H" == "REG_EXPAND_SZ" (call set "UserPath=%%I") else if /I "%%H" == "REG_SZ" set "UserPath=%%I"
    		if defined UserPath goto UserPathValid
	)

	goto end
) else (
	echo Error: You need Administrator Privileges to uninstall this program
	goto end
)

:UserPathValid
set NetinfoDirectory=%userprofile%\.netinfo\;

call set Replaced=%%UserPath:%NetinfoDirectory%=%%

If NOT "%UserPath%"=="%Replaced%" (
	REG ADD HKEY_CURRENT_USER\Environment /v Path /d "%Replaced%" /f
	echo Netinfo successfully removed from registry
	goto uninstall
) else (
	goto uninstall
)

:uninstall
echo Removing Files...
if exist "%userprofile%\.netinfo\" rmdir /s /q "%userprofile%\.netinfo\"
echo Netinfo was successfully uninstalled
goto end

:end
pause