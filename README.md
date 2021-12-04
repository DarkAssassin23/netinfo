# Netinfo
**Version:** 1.0<br />
**Published Date:** 12/3/2021

GENERAL USAGE NOTES
----------------------
- This is a CLI tool to give you information about your network settings such as your
hostname, local ip, default gateway, DNS Servers, and global ip

---------

System Requirenments 
----------
- Python 3
- Pip3
________

Before you in install
---------
If you don't already have Python3 installed you need to do that before you can install
Netinfo. A link to download Python3 can be found [here](https://www.python.org/downloads/)

Similarly, if you don't already have Pip3 installed you need to install that first. 
Information on how to do that can be found [here](https://pip.pypa.io/en/stable/installation/)
_______

Windows Installation
----------
To install Netinfo on Windows, simply run the `install.bat` file 
and you will be good to go.

One thing to note, can install the program perfectly fine without admin privileges, 
however, it is not recommended since if you do not run the installer with admin 
privileges you will then have to do one of the follwoing:

1. Log out and log back in
2. Open 'Advanced System Settings' -> Environment Variables, then select 'OK' and 'OK' again
3. Restart your device

Since you did run the installer as administrator, the registry environment variables were 
not able to automatically propogate throughout the OS, which is why you need to do one of 
the three options listed above in order to trigger it.

If you ran the `install.bat` file as an administrator, however, you are good to go.
Just close out of any open command prompt windows (if applicable) for their environment 
variables to reset.

If you run into an error on Windows, during the install process trying to install netifaces,
make sure you have Microsoft C++ Build Tools installed.  

If you don't have Microsoft C++ Build Tools installed, a link to the installer can be found 
[here](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

When you download the installer make sure select the C++ Build Tools check box
see [this](https://docs.microsoft.com/en-us/answers/questions/136595/error-microsoft-visual-c-140-or-greater-is-require.html) forum post for reference 

Once you have Microsoft C++ Build Tools installed, run the install.bat program again and it
should work.

______

macOS/Linux Installation
------------------------

To install Netinfo on macOS/Linux run the install script
```bash
./install
```

------------------------

Utilizing Netinfo
----------------------

Once the installation is complete, run the program from your command line

	netinfo

You will then see an ouput similar to this:
```
Hostname:	        Home-PC
Local IP:	        192.168.1.63
Default Gateway:    192.168.1.1
DNS Servers			1.1.1.1
					1.0.0.1
Global IP:	        118.9.215.87
```
_________


Windows Uninstall
----------
To uninstall Netinfo on Windows run the `uninstall.bat` file as 
Administrator. 

______

macOS/Linux Uninstall
------------------------

To uninstall Netinfo on macOS/Linux run the uninstall script
```bash
./uninstall
```
_______________