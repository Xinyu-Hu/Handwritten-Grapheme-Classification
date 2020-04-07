#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pandas as pd
import random


def main():
    file_path = './class_map_corrected.csv'
    df = pd.read_csv(file_path)
    # root: 168
    roots = df.loc[0:167].loc[:, 'component']
    # vowel: 10
    vowels = df.loc[169:178].loc[:, 'component']
    # consonant: 6
    consonants = df.loc[180:].loc[:, 'component']
    # print(roots.size)

    i = 1
    for root in roots:
        for vowel in vowels:
            for consonant in consonants:
                trace(root + vowel + consonant, i)
                i = i + 1

    # i = 1
    # root=roots.loc[0]
    # vowel=vowels.loc[169]
    # for consonant in consonants:
    #     trace(root + vowel + consonant, i)
    #     i = i + 1


def trace(text, i):
    imgsize = random.randrange(180, 224)
    img = Image.new("RGB", (imgsize, imgsize), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("./kalpurush.ttf", 30, layout_engine=ImageFont.LAYOUT_RAQM)
    textsize = draw.textsize(text, font=font)
    # text = "অ"
    location = (imgsize - textsize[1])/2
    draw.text((location, imgsize/2-10), text, (0, 0, 0), font=font)
    img.save('./traceImg/' + str(i) + '.png')
    return


main()