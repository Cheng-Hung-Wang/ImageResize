#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
from PIL import Image

width = 2048
height = 610


if __name__=='__main__':
    name = sys.argv[1].split(".")

    if(len(sys.argv)>2):
        width = int(sys.argv[2])
        height = int(sys.argv[3])
    if(len(sys.argv)>4):
        format = sys.argv[4]
    else:
        format = name[1]

    im = Image.open(sys.argv[1])
    im2 = im.resize((width, height), Image.BILINEAR)
    im2.save("{}_{}_{}.{}".format(name[0],width, height, format))
