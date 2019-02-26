#!/usr/bin/python
# coding: utf-8

# A python script to cycle all available colors the Lego USB Pad can create.
import usb.core
import usb.util
import signal
import random
import sys
from time import sleep

TOYPAD_INIT = [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

OFF   = [0,0,0]
RED   = [255,0,0]
GREEN = [0,255,0]
BLUE  = [0,0,255]
PURPLE = [255,0,255]
LBLUE = [255,255,255]
OLIVE = [128,128,0]

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

def switch_pad(pad, colour):
    send_command(dev,[0x55, 0x06, 0xc0, 0x02, pad, colour[0], colour[1], colour[2],])
    return

def rand_number(maxint):
    print random.randint(0, maxint)
    return

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

    init_usb()
    
    try:
        signal.signal(signal.SIGTERM, signal_term_handler)
        while True:
            switch_pad(ALL_PADS,RED)
            sleep(0.2)
            switch_pad(CENTER_PAD,GREEN)
            sleep(0.2)
            switch_pad(LEFT_PAD,BLUE)
            sleep(0.2)
            switch_pad(RIGHT_PAD,PURPLE)
            sleep(0.2)
            switch_pad(ALL_PADS,PURPLE)
            sleep(0.2)
            switch_pad(ALL_PADS,OLIVE)
            sleep(0.2)
            switch_pad(CENTER_PAD,OFF)
            switch_pad(LEFT_PAD,BLUE)
            switch_pad(RIGHT_PAD,GREEN)
            sleep(0.2)
            switch_pad(ALL_PADS,OLIVE)
            sleep(0.2)
            switch_pad(LEFT_PAD,LBLUE)
            switch_pad(RIGHT_PAD,PURPLE)
            sleep(0.2)
            switch_pad(ALL_PADS,OLIVE)
            sleep(0.2)
            switch_pad(ALL_PADS,PURPLE)
    except KeyboardInterrupt:
       print 'interrupted'
    finally:
       switch_pad(ALL_PADS,OFF)
    

if __name__ == '__main__':
    main()
  
