#!/usr/bin/python
# coding: utf-8

# A python script to cycle and randomize all available colors the Lego USB Pad can create.
import usb.core
import usb.util
import signal
import random
import sys
from time import sleep

# Global vars
TOYPAD_INIT = [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Pad id
ALL_PADS   = 0
CENTER_PAD = 1
LEFT_PAD   = 2
RIGHT_PAD  = 3

# Init usb pad
# Detects if available or not, thanks to usb library
def init_usb():
    global dev

    dev = usb.core.find(idVendor=0x0e6f, idProduct=0x0241)

    if dev is None:
        print 'Device not found'
    else:
        if dev.is_kernel_driver_active(0):
            dev.detach_kernel_driver(0)

        print usb.util.get_string(dev, dev.iProduct)

        dev.set_configuration()
        dev.write(1,TOYPAD_INIT)

    return dev


# Send any order to pad
def send_command(dev,command):

    # calculate checksum
    checksum = 0
    for word in command:
        checksum = checksum + word
        if checksum >= 256:
            checksum -= 256
    message = command+[checksum]

    # pad message
    while(len(message) < 32):
        message.append(0x00)

    # send message
    dev.write(1, message)

    return

# Send color update to chosen pad
def switch_pad(pad, colour):
    send_command(dev,[0x55, 0x06, 0xc0, 0x02, pad, colour[0], colour[1], colour[2],])
    return

# Rand color or pad number
# 0 -> 3 : Pad number
# 0 -> 255 : Color
def rand_number(maxint):
    return random.randint(0, maxint)

# End systemctl service properly
def signal_term_handler(signal, frame):
    print 'got SIGTERM'
    exit(0)

def main():
    # --
    # Keywords references
    # -- Pads
    # ALL_PADS   = 0
    # CENTER_PAD = 1
    # LEFT_PAD   = 2
    # RIGHT_PAD  = 3
    # -- Colors
    # OFF   = [0,0,0]
    # RED   = [255,0,0]
    # GREEN = [0,255,0]
    # BLUE  = [0,0,255]
    # PURPLE = [255,0,255]
    # LBLUE = [255,255,255]
    # OLIVE = [128,128,0]

    # Connect to Lego USB Pad
    init_usb()
    
    try:
        # Init exit signal handler 
        signal.signal(signal.SIGTERM, signal_term_handler)

        while True:
            # Rand color and pad number
            pad=rand_number(3)
            color=rand_number(255)

            # Switch color
            switch_pad(ALL_PADS,GREEN)

            # Debug output
            #print 'pad : ',pad
            #print 'color : ',color 
            sleep(0.5)

    except KeyboardInterrupt:
       print 'interrupted'
    finally:
       switch_pad(ALL_PADS,OFF)
    

if __name__ == '__main__':
    main()
  
