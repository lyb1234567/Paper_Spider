import os 
import requests
import time
import shutil
from bs4 import BeautifulSoup
def download(url,filename,foldername):
        html=requests.get(url)
        path="C:\\PythonProgram\\IRR_spider"+"\\"+foldername+"\\"+filename.replace("\n","")+".pdf"
        with open(path, 'wb') as f:
            f.write(html.content)

def folder_empty(folder_name):
    dir = os.listdir(folder_name)
    if len(dir) == 0:
       return True
    else:
       return False


def run():
    for folder_name in os.listdir():
       if folder_name.endswith(".txt") or folder_name.endswith(".py"):
            continue
       if not folder_empty(folder_name):
          name_file=open(folder_name+"/name.txt",encoding="utf8").readlines()
          url_file=open(folder_name+"/url.txt",encoding="utf8").readlines()
          for i in range(len(name_file)):
            url=url_file[i]
            paper_name=name_file[i]
            paper_name=paper_name.split(".")[0]
            download(url,paper_name,folder_name)
          print(folder_name+" completed")

def mov_dir():
    for folder_name in os.listdir():
        if folder_name.endswith(".txt") or folder_name.endswith(".py"):
            continue
        if not folder_empty(folder_name):
           src_path = "C:/PythonProgram/IRR_spider"+"/"+folder_name
           dst_path = "C:/Users/15366/Nutstore/1/我的坚果云"
           shutil.move(src_path, dst_path)
if __name__=="__main__":
    mov_dir()
               

    
        