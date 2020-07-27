#    OWO is a minecraft trash resourcepack converter generator
#    Copyright (C) 2020 Konstantin Tolstoy & Stepan Gaidukevich
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import random

f = open("input.txt", "r")

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
        y = x[1].replace("r", "w").replace("t", "h")
        res = x[0] + "=" + y.rstrip("\n") + " " + a
        
    else:
        res = line
    
    endLines.append(res)

f.close()

f = open("en_US.lang", "w")

for x in endLines:
    f.write(x + "\n")
