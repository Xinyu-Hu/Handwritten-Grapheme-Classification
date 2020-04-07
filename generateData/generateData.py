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
    roots = df.loc[0:167].loc[:, 'component'].values.tolist()
    # vowel: 11
    vowels = df.loc[168:178].loc[:, 'component'].values.tolist()
    # consonant: 7
    consonants = df.loc[179:].loc[:, 'component'].values.tolist()
    # print(roots)
    # print(consonants)

    i = 1
    for root in range(0, len(roots)):
        for vowel in range(0, len(vowels)):
            for consonant in range(0, len(consonants)):
                text = gen_grapheme(root, vowel, consonant, roots, vowels, consonants)
                trace(text, i)
                i = i + 1

    # i = 2
    # root = 14
    # vowel = 9
    # consonant = 3
    # text = gen_grapheme(root, vowel, consonant, roots, vowels, consonants)
    # trace(text, i)


def gen_grapheme(root, vowel, consonant, roots, vowels, consonants):
    if consonant == 0:
        if vowel == 0:
            return roots[root]
        else:
            return roots[root] + vowels[vowel]
    elif consonant == 1:
        if vowel == 0:
            return roots[root] + consonants[consonant]
        else:
            return roots[root] + vowels[vowel] + consonants[consonant]
    elif consonant == 2:
        if vowel == 0:
            return consonants[consonant] + roots[root]
        else:
            return consonants[consonant] + roots[root] + vowels[vowel]
    elif consonant == 3:
        if vowel == 0:
            return consonants[consonant][:2] + roots[root] + consonants[consonant][1:]
        else:
            return consonants[consonant][:2] + roots[root] + consonants[consonant][1:] + vowels[vowel]
    elif consonant == 4:
        if vowel == 0:
            return roots[root] + consonants[consonant]
        else:
            if root == 123 and vowel == 1:
                return roots[root] + '\u200d' + consonants[consonant] + vowels[vowel]
            return roots[root] + consonants[consonant] + vowels[vowel]
    elif consonant == 5 or 6:
        if vowel == 0:
            return roots[root] + consonants[consonant]
        else:
            return roots[root] + consonants[consonant] + vowels[vowel]
    elif consonant == 6:
        if vowel == 0:
            return consonants[2] + roots[root] + consonants[2][::-1]
        else:
            return consonants[2] + roots[root] + consonants[2][::-1] + vowels[vowel]


def trace(text, i):
    imgsize = random.randrange(180, 224)
    img = Image.new("RGB", (imgsize, imgsize), "white")
    draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype("./AponaLohit.ttf", 30, layout_engine=ImageFont.LAYOUT_RAQM)
    font = ImageFont.truetype("./kalpurush.ttf", 30, layout_engine=ImageFont.LAYOUT_RAQM)
    textsize = draw.textsize(text, font=font)
    # text = "অ"
    location = (imgsize - textsize[1]) / 2
    draw.text((location, imgsize / 2 - 10), text, (0, 0, 0), font=font)
    # img.save('./traceImg/' + str(i) + '.png')
    img.save('./' + str(i) + '.png')
    return


main()
