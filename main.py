#  OWO is a minecraft trash resourcepack converter generator
#  Copyright (C) 2020 Konstantin Tolstoy & Stepan Gaidukevich
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
import random
import shutil
from PIL import Image

pinkOverlay_set=False
owoOverlay_set=False

inp = "./input/assets/minecraft/"
outp = "./output/assets/minecraft/"

def main():
    parseOptions()

    print(owoOverlay_set)
    print(pinkOverlay_set)
    
    if os.path.isdir("./output/"):
        shutil.rmtree("./output/")

    os.mkdir("./output/")
    os.mkdir("./output/assets/")
    os.mkdir("./output/assets/minecraft/")
    
    os.mkdir("./output/assets/minecraft/textures/")
    os.mkdir("./output/assets/minecraft/lang/")
    
    f = open("./output/pack.mcmeta", "w")
    
    f.write("{ \"pack\": { \"pack_format\": 1, \"description\": \"UwU\" } }")
    
    f.close()

    handle_localization()
    handle_blocks()

#############################################################################################



def handle_localization():
    i = inp + "lang/"
    o = outp + "lang/"

    if os.path.isfile(i + "en_US.lang"):
        f = open(i + "en_US.lang", "r")
    elif os.path.isfile("./en_US.lang"):
        print("United States English localization not found in input resourcepack. Trying to use built-in localization (1.8.9)")
        f = open("./en_US.lang")
    else:
        print("No localizations found")
        return

    endLines = []

    for line in f.readlines():
        ir = random.randint(0, 3)
        if ir == 0:
            a = "§d§lOwO§r"
        if ir == 1:
            a = "§d§lUwU§r"
        if ir == 2:
            a = "§d§lOWO§r"
        if ir == 3:
            a = "§d§lUWU§r"
            
        if "=" in line:
            x = line.split("=")
            y = x[1].replace("r", "w").replace("t", "h").replace("sh", "h").replace("Diamond", "OWO Cryftal")
            res = x[0] + "=" + y.rstrip("\n") + " " + a
            
        else:
            res = line
        
        endLines.append(res)

    f.close()

    f = open(o + "en_US.lang", "w")

    for x in endLines:
        f.write(x + "\n")
        
    print("yeah")
    
    
def handle_blocks():
    i = inp + "textures/blocks/"
    o = outp + "textures/blocks/"

    if not os.path.isdir(i):
        print("Block textures not found in input texturepack")
        return

    a = os.listdir(i)
    a2 = os.listdir("./uwus/")
    a3 = Image.open("./aatu/pink.png")
    
    os.mkdir(o)

    for x in a2:
        if x.endswith(".png") != True:
            a2.pop(a2.index(x))
            print("not png")


    for x in a:
        if x.endswith(".png"):
            a = Image.open(i + x).convert("RGBA")
            b = Image.open("./uwus/" + a2[random.randint(0, len(a2) - 1)]).convert("RGBA")
            
            b = b.resize(a.size)
            if owoOverlay_set==True:
                a = Image.alpha_composite(a, b)
            if pinkOverlay_set==True:
                a = Image.blend(a, a3, 0.45)
            
            a.save(o + x, "PNG")
            
            
    print('haha classic')
    
    
#############################################################################################

def parseOptions():

    f = open("./settings.txt", "r")

    for line in f.readlines():
        global pinkOverlay_set
        global owoOverlay_set
        x = line.split("=")
        
        if x[0] == "blockPink":
            if x[1].rstrip("\n") == "true":
                pinkOverlay_set=True
            else:
                pinkOverlay_set=False

        if x[0] == "blockUWU":
            if x[1].rstrip("\n") == "true":
                owoOverlay_set=True
            else:
                owoOverlay_set=False
    print(owoOverlay_set)
    print(pinkOverlay_set)
    f.close()







#############################################################################################

main()

