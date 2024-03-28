This script adds a version file to the "include" folder of your project  

Available are following parameters 
* BUILD_NUMBER
* GitHash
* VERSION
* VERSION_SHORT

The versioning parameters are available after the inclusion of the version.h file  
like this: `#include <version.h>`  

To use this Script in your PlatformIO project you have to add  
this line: `extra_scripts = pre:PlatformIOVersionGenerator.py`  
to your platformio.ini file.