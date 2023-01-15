import requests
from bs4 import BeautifulSoup
import os
import time
import numpy as np
time_splits = np.linspace(10.129, 30.256, num=40)
counter = 0
skips = 0
url="https://zhuanlan.zhihu.com/p/361341288"
header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
html=requests.get(url).content
soup=BeautifulSoup(html,"html.parser")

def mk_dir(soup):
    mydivs = soup.find_all("h2")
    dir_lst=[]
    for tag in mydivs:
        str_tag=tag.text
        if "." in str_tag:
            str_tag=str_tag.split(".")
            name=str_tag[1]
            if "/" in name:
                name=name.replace("/","_")
            if not os.path.exists(name):
                os.mkdir(name)
            dir_lst.append(name)
    return dir_lst


def mk_sub_dir(soup,dir_lst):
    mydivs = soup.find_all("p")
    sub_dir_lst=initializ_lst(dir_lst)
    for k in mydivs:
        if "." in k.text :
            title_lst=k.text.split(" ")[1:]
            index=k.text.split(" ")[0].split(".")
            if len(index)==2 and index[1]!="":
                index_float=float(k.text.split(" ")[0])
                sub_dir=(''.join(title_lst))
                parent_dir=dir_lst[int(index[0])-1]
                if "/" in sub_dir:
                    sub_dir=sub_dir.replace("/","_")
                mk_path="C:\\PythonProgram\\IRR_spider\\"+parent_dir+"\\"+sub_dir
                if not os.path.exists(mk_path):
                    os.mkdir(mk_path)
                sub_dir_lst[int(index[0])-1].append(sub_dir)
            else:
                index=int(index[0])
    return sub_dir_lst

def initializ_lst(dir_lst):
    sub_dir_lst=[]
    for i in range(len(dir_lst)):
        sub_dir_lst.append([])
    return sub_dir_lst
def generate_url_paper_file(soup,dir_lst,sub_dir_lst):
    paper=soup.select("ol")[1:]
    temp=[]
    for name in paper:
        temp.append(name.select("li"))
    count=0
    for i in range(len(dir_lst)):
            dir_name=dir_lst[i]
            sub_dir_lst_name=sub_dir_lst[i]
            paper_lst=temp[count]
            if len(sub_dir_lst_name)!=0:
                for name in sub_dir_lst_name:
                        paper_lst=temp[count]
        
                        down_load_path_paper="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"paper.txt"
                        down_load_path_url="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"url.txt"
                        name_file=open(down_load_path_paper,"a",encoding="utf-8")
                        url_file=open(down_load_path_url,"a",encoding="utf-8")
                        if not os.path.exists("C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"paper"):
                                os.mkdir("C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"paper")
                        name_empty=os.stat(down_load_path_paper).st_size == 0
                        url_empty=os.stat(down_load_path_url).st_size == 0
                        count=count+1
                        if not (name_empty and url_empty ):
                            print(name+" Finished")
                            continue
                        print("Downloading "+name)
                        for paper_name in paper_lst:
                            url="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="+paper_name.text.split(".")[0]
                            header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","Cookie":"CONSENT=PENDING+390; SOCS=CAISHAgCEhJnd3NfMjAyMjEyMDUtMF9SQzMaAmVuIAEaBgiAgpmdBg; SEARCH_SAMESITE=CgQImJcB; SID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOpuuDhxfBABfPdBeksXl1NMQ.; __Secure-1PSID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOpM-dHmkPXKrb6Al1UzYxSLg.; __Secure-3PSID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOp2Jr0lT9ycMXI84nPmUJseQ.; HSID=AXWWdzYUCaYjNwHHl; SSID=AFaAZI4W1D4ceYzXn; APISID=yY253SnM0N1PzPkJ/AtgyPj7u3XK2TQSnT; SAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; __Secure-1PAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; __Secure-3PAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; OGPC=19022519-1:19022622-1:; OGP=-19022622:; AEC=ARSKqsLvSR3ZVb5NZvnM8tyi8ISu6XGd8A6-LQQyG8Dwbijmb0b7MIZjGoM; NID=511=nl3TtqSEae5g-t5f_GmKzedhT82Ou_Opk-IMNPEn43PfgrDDxewjbieUklzHipt4LGCB6VNfWt2ytcICoi1wRuZWYv3BXj4KthYb4U3q32VaYcJrpATYTAouus4ebGd_EA01dAMB3zn4ofUIDi3pCaf2VvwhH19czBq_mOK1w8oxuHDtUPF91fuQaUsfKRSb3BWTp0Iq28m0PNc1micOGLt1MdEdBmlr0DKsrYqEdliWVM7ooMF4Cw0rBp75BkDT3lY4RWksh34jUTVZpqQo3oMKkfW_i-bzI1MdXpkg2t55vtK8qmddNr7j6nluaKhWCVwZ; 1P_JAR=2023-1-11-23; GSP=A=PJmejQ:CPTS=1673481677:LM=1673481677:S=OUXewlI7IAFBWkjY; SIDCC=AIKkIs2xs70q8WlXz7osmghTgrihAHsjKg6GaHfwGLjownRyimRDjqq9mzT6IeJ_DMo84fzfow; __Secure-1PSIDCC=AIKkIs2OWLVeke0MRwgjwvnHMZDqsOy5MLAjY4czY6LSZyv-dFX_9dv1Spu38wTSoMP-5EVRzSo; __Secure-3PSIDCC=AIKkIs2E_L0FIclbJkRRkby4_7yDQtEjxEWt7dTXgx74i6a4ozLW2rsC1vOa2JmhPKxRXS-PmQ"}
                            html=requests.get(url,headers=header).content
                            soup=BeautifulSoup(html,"html.parser")
                            mydivs = soup.find("div", {"class": "gs_or_ggsm"})
                            if mydivs is not None:
                                    print(mydivs.select('a')[0].get("href"))
                                    url_file.write(mydivs.select('a')[0].get("href"))
                                    url_file.write("\n")
                                    name_file.write(paper_name.text.split(".")[0])
                                    name_file.write("\n")
                            else:
                                    print(paper_name.text.split(".")[0]+"  download failed")
                            alarm = np.random.choice(time_splits)
                            rounding = np.random.choice(list(range(2,6)))
                            print(f'Sleeping {round(alarm, 2)} seconds...')
                            time.sleep(round(alarm, rounding))
                        print("\n")
                    
            
            # else:
                # down_load_path_paper="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+"paper.txt"
                # down_load_path_url="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+"url.txt"
                # name_file=open(down_load_path_paper,"a",encoding="utf-8")
                # url_file=open(down_load_path_url,"a",encoding="utf-8")
                # if not os.path.exists("C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+"paper"):
                #     os.mkdir("C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+"paper")
                # name_empty=os.stat(down_load_path_paper).st_size == 0
                # url_empty=os.stat(down_load_path_url).st_size == 0
                # count=count+1
                # if not (name_empty and url_empty ):
                #     print(dir_name+" Finished")
                #     continue
                # print("Downloading "+dir_name)
                # for paper_name in paper_lst:
                #     url="https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q="+paper_name.text.split(".")[0]
                #     header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36","Cookie":"CONSENT=PENDING+390; SOCS=CAISHAgCEhJnd3NfMjAyMjEyMDUtMF9SQzMaAmVuIAEaBgiAgpmdBg; SEARCH_SAMESITE=CgQImJcB; SID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOpuuDhxfBABfPdBeksXl1NMQ.; __Secure-1PSID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOpM-dHmkPXKrb6Al1UzYxSLg.; __Secure-3PSID=SAi7d4yZ7LYOtSjhvsZpmkW-u2XPHzsjV5zQYwO-Ivj4CvOp2Jr0lT9ycMXI84nPmUJseQ.; HSID=AXWWdzYUCaYjNwHHl; SSID=AFaAZI4W1D4ceYzXn; APISID=yY253SnM0N1PzPkJ/AtgyPj7u3XK2TQSnT; SAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; __Secure-1PAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; __Secure-3PAPISID=oDTaBhUMJURZW6XD/AlB4yVx3vPJ1buea_; OGPC=19022519-1:19022622-1:; OGP=-19022622:; AEC=ARSKqsLvSR3ZVb5NZvnM8tyi8ISu6XGd8A6-LQQyG8Dwbijmb0b7MIZjGoM; NID=511=nl3TtqSEae5g-t5f_GmKzedhT82Ou_Opk-IMNPEn43PfgrDDxewjbieUklzHipt4LGCB6VNfWt2ytcICoi1wRuZWYv3BXj4KthYb4U3q32VaYcJrpATYTAouus4ebGd_EA01dAMB3zn4ofUIDi3pCaf2VvwhH19czBq_mOK1w8oxuHDtUPF91fuQaUsfKRSb3BWTp0Iq28m0PNc1micOGLt1MdEdBmlr0DKsrYqEdliWVM7ooMF4Cw0rBp75BkDT3lY4RWksh34jUTVZpqQo3oMKkfW_i-bzI1MdXpkg2t55vtK8qmddNr7j6nluaKhWCVwZ; 1P_JAR=2023-1-11-23; GSP=A=PJmejQ:CPTS=1673481677:LM=1673481677:S=OUXewlI7IAFBWkjY; SIDCC=AIKkIs2xs70q8WlXz7osmghTgrihAHsjKg6GaHfwGLjownRyimRDjqq9mzT6IeJ_DMo84fzfow; __Secure-1PSIDCC=AIKkIs2OWLVeke0MRwgjwvnHMZDqsOy5MLAjY4czY6LSZyv-dFX_9dv1Spu38wTSoMP-5EVRzSo; __Secure-3PSIDCC=AIKkIs2E_L0FIclbJkRRkby4_7yDQtEjxEWt7dTXgx74i6a4ozLW2rsC1vOa2JmhPKxRXS-PmQ"}
                #     html=requests.get(url,headers=header).content
                #     soup=BeautifulSoup(html,"html.parser")
                #     mydivs = soup.find("div", {"class": "gs_or_ggsm"})
                #     print(mydivs)
                #     if mydivs is not None:
                #                     print(mydivs.select('a')[0].get("href"))
                #                     url_file.write(mydivs.select('a')[0].get("href"))
                #                     url_file.write("\n")
                #                     name_file.write(paper_name.text.split(".")[0])
                #                     name_file.write("\n")
                #     else:
                #                     print(paper_name.text.split(".")[0]+"  download failed")
                #     alarm = np.random.choice(time_splits)
                #     rounding = np.random.choice(list(range(2,6)))
                #     print(f'Sleeping {round(alarm, 2)} seconds...')
                #     time.sleep(round(alarm, rounding))
def spider():
    dir_lst=mk_dir(soup)
    sub_dir_lst=mk_sub_dir(soup,dir_lst)
    generate_url_paper_file(soup,dir_lst,sub_dir_lst)
    down_load_paper(dir_lst,sub_dir_lst)
def down_load_paper(dir_lst,sub_dir_lst):
    print("\n\n")
    print("Downloading PDF........")
    for i in range(len(dir_lst)):
            dir_name=dir_lst[i]
            sub_dir_lst_name=sub_dir_lst[i]
            if len(sub_dir_lst_name)!=0:
               for name in sub_dir_lst_name:
                   down_load_path_url="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"url.txt"
                   down_load_path_paper="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"paper.txt"
                   url_file=open(down_load_path_url,"r",encoding="utf-8")
                   name_file=open(down_load_path_paper,"r",encoding="utf-8")
                   url_lst=url_file.readlines()
                   name_lst=name_file.readlines()
                   for i in range(len(url_lst)):
                     url=url_lst[i]
                     print(url)
                     paper_name=name_lst[i]
                     html=requests.get(url)
                     path="C:\\PythonProgram\\IRR_spider\\"+dir_name+"\\"+name+"\\"+"paper"+"\\"+paper_name.replace("\n","")+".pdf"
                     with open(path, 'wb') as f:
                        f.write(html.content)
                     
if __name__=="__main__":
    
    
     
    