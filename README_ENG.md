# ckAnimation generator

[***RUSSIAN README.md || README.md НА РУССКОМ***](https://github.com/Felucca24/ckAnimation-generator/blob/master/README_ENG.md)

***Gif examples below!***  
These scripts allow you to generate backlight animation files for some A4 Bloody keyboards. I tested it on Bloody B975, it should work on similar models with RGB backlighting. By changing ckAnimation_algorithms.py, you can easily add your own animations, inheriting the Algorithm class.

***DISCLAIMER!***  
If you want to try out these scripts - YOU DO ALL AT YOUR OWN RISK! If suddenly something happens to your keyboard or computer, I am not responsible for it.

## How to use
You can continue without this, however, the automatic installation will not work:
Open the ckAnimation_generator.py script with notepad and make sure that the paths to the scripts folder and the Setting.ini KeyDominator file are correct. You can try to copy them and paste in the win+r window and press Enter. If the folder and file are opened, then everything is fine. If not, find out where KeyDominator is installed, namely the NumberPadAtRight folder and the NumberPadAtRight \ Setting.ini file and correct the paths in the script. Path separator is \\\\. After that you can continue.

Run ckAnimation_generator.py with Python 3.
With console or by dragging script to python.exe file 

    Shift+Right mouse key in folder -> Open command line
    
    python ckAnimation_generator.py

You will be prompted to enter a file path/name, but you can skip this by pressing Enter.
After that, you should choose which of the animation algorithms you want to use, to do this, enter the number - the algorithm number in the displayed list and press Enter.
After the animation has been generated, the script will offer to install animation. Enter a number from 0 to 9 to set the animation on the combination with Fn. The created file will be copied to the Bloody animations folder and the settings will be changed. You can skip this, then the file will simply remain on the path you have entered, or in the folder with the script.

## GIF - examples

![White waves](https://i.imgur.com/gO0a5b3.gif)

![Starfall](https://i.imgur.com/Og8kqrh.gif)
