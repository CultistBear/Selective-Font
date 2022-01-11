import os
import sys
import re
from fontTools.subset import main as main_Thing

def Convert_Uni():
    global Unique_Uni
    Str=list(input("Enter string or letters you want to convert:\n"))
    Uni_Codes="".join(r"\u{:04X}".format(ord(chr)) for chr in Str)
    Uni_Codes_Split=re.findall("u....",Uni_Codes)
    Unique_Uni=[]
    [Unique_Uni.append("U+"+x[1:]) for x in Uni_Codes_Split if x not in Unique_Uni]
    TTF_Path()

def Final():
    try:
        sys.argv = [None, "%s"%Path_ttf, "--unicodes=U+0000-0020, %s"%(", ".join(map(str, Unique_Uni)))]
        main_Thing()
        print("\nCompleted!")
    except PermissionError:
        print("Insufficient Permissions to write at the Font File location.")
        sys.exit()
    except FileNotFoundError:
        print("File Not Found")
        TTF_Path()


def TTF_Path():
    global Path_ttf
    Path_ttf=input("\nPath to TTF File (path\\to\\file\\file.ttf):\n")
    if os.path.exists("%s"%Path_ttf)==False:
        print("File Not Found")
        TTF_Path()
    else:
        Final()

def Start():
    Convert_Uni()

Start()