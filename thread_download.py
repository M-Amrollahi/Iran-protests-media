
from datetime import datetime
import pandas as pd
import requests
import os
from md_data import cls_data
from multiprocessing import Manager

path_image = "./mediaFiles/images/"
path_video = "./mediaFiles/videos/"

objdata = cls_data()

manager = Manager()
final_list = manager.dict({i:0 for i in objdata.f_getNotDLIndeces()})


def f_getIndeces():
    return objdata.f_getNotDLIndeces()

def f_updateStatus():
    objdata.f_updateStatus(final_list)

def f_saveData():
    objdata.f_saveDF()

def f_download(idx):
    
    url = objdata.f_getDF().loc[idx,"md_url"]
    try:
        data = requests.get(url, stream=True,timeout=4).content
    except:
        return

    #Get the file name out of url
    filename = url.split("/")[-1]
    pathf = os.path.join(path_image,filename)
    if "?" in filename:
        filename = filename.split("?")[0]
        pathf = os.path.join(path_video,filename)
    

    with open(pathf,"wb") as mfile:
        dt = datetime.strptime(objdata.f_getDF().loc[idx,"created_at"],"%Y-%m-%dT%H:%M:%S.%fZ")
        
        tformat = dt.strftime("%Y")+dt.strftime("%m")+dt.strftime("%d")+dt.strftime("%H")+dt.strftime("%M")
        mfile.write(data)
        # Change the metadata of the file to created_at datetime
        os.system("touch -t {} {}".format(str(int(tformat)),pathf))
    
    final_list[idx] = 1

    print("{}/{}  Downloaded.".format(idx,len(objdata.f_getDF())),end="",flush=True)
    