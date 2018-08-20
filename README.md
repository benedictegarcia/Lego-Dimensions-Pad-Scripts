# Lego-Dimensions-Pad-Scripts
Scripts to interact with your Lego Dimensions pad
<br>

* Python dependencies :
- libusb1
- libusb
- pyusb

Run the install script located in folder ```install_prerequisties/``` to install all the required packages.

* How to use it :
Plug your Lego Dimensions Pad to a USB port, run the example script using the python cmd :
 ```python legousb-colorcycle.py```

It should enlight your pad. If not, try again with sudo mode :
 ```sudo python legousb-colorcycle.py```

The Pad is powered off at the end of the script. If you want to make it do a cycle without powering it off, you can disable the last instruction ```switch_pad(ALL_PADS,OFF) ``` and make it do a light cycle with the ```watch``` command :  
 ```watch python legousb-colorcycle.py```
When you want to power if off, cancel the script execution and use the ```legousb-poweroff.py``` script.

I will try to do it in a better way in future releases. 


/!\ Warning : tested on Debian / Ubuntu only /!\
/!\ Warning : tested with Wii U version only /!\

* TODO : 
- Better install scripts
- Create cycles functions
- Randomize cycles
- Create interface to manage pad enlightment

