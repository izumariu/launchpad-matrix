1. Set up your cloud

To get this thing to work, you have to create 3 files in your cloud: 'sccontrol.txt'(without the quotes), 'sendstring.txt'(without the quotes) 
and 'color.txt'(also without the quotes). I recommend to put them in a seperated folder. In sccontrol.txt, you can type 'Off', 'On' or 
'sendstring'(everything without the quotes).
Cases for sccontrol.txt:

Off       : The script will do nothing.
On        : The script will send a screensaver to the device.
sendstring: The script will send 'sendstring.txt' in the color of 'color.txt' to the device.

In sendstring.txt, you can type a line of text which will be sent to the device if the text in 'sccontrol.txt' is 'sendstring'.

In color.txt, you can define a color. This color will be applied to the string in 'sendstring.txt'.

Syntax:

color=<color>

Vaild colors:

red
orange
light_orange
yellow
light_yellow
green
light_green
-------------------------------------------------------------------------------------------------------
2. Configure the folder

Open the folder config/ and enter the download links of the text files. If you use dropbox, please make sure that there is no '?dl=0' 
behind the name of the file, else the script won't do it's work. Make ALWAYS sure that the file you download doesn't change it's name. 
By example, if you use dropbox(yes, I unfortunately do), then delete the '?dl=0' behind the file's name, else it will be named like
'blabla.txt?dl=0'. Got it?
-------------------------------------------------------------------------------------------------------
3. Enjoy!

Yeah, just navigate to the folder and execute the script 'screensaver-sh.py'(...no quotes :D). You can go to your cloud and edit the files now. Every time the script cycle completed, it will download the files and do things based on the strings from the files.
--------------------------------------------------------------------------------------------------------
Credit to the guy who made the
Launchpad library: https://github.com/FMMT666/launchpad.py
