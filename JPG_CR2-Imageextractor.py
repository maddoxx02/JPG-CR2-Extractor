import re
import os
import numpy as np
import pandas as pd
from tqdm import trange
import shutil

np.random.seed(1000)



def reader_JPG(): # Input is given as the Path of the Folder Where all Data is stored. 

    
    FILE_PATH = input("Enter Location of JPG files:") # W:\\Import 14\\JPG
    
    # Change Directory of the Kernel
    os.chdir(FILE_PATH)
    #os.getcwd()
    
    # Storing the Path of each file within the Folder
    file_paths = []    
    
    # Checking if all files are JPG or not, Read only JPG files
    for file in os.listdir(): 
        if file.endswith(".JPG"):
            file_paths.append(f"{FILE_PATH}\{file}")   

    # A Dictionary to store the Path of each File with an ID Number (assigned from 0 - max)
    a = {}  
    k = 0
    for ele in file_paths:
        a[k] = ele
        k+=1
    
    return a, FILE_PATH



def reader_CR2(): # Input is given as the Path of the Folder Where all Data is stored. 

    
    FILE_PATH = input("Enter Location of CR2 files:") # W:\\Import 14\\RAW
    
    # Change Directory of the Kernel
    os.chdir(FILE_PATH)
    #os.getcwd()
    
    # Storing the Path of each file within the Folder
    file_paths = []    
    
    # Checking if all files are JPG or not, Read only JPG files
    for file in os.listdir(): 
        if file.endswith(".CR2"):
            file_paths.append(f"{FILE_PATH}\{file}")   

    # A Dictionary to store the Path of each File with an ID Number (assigned from 0 - max)
    a = {}  
    k = 0
    for ele in file_paths:
        a[k] = ele
        k+=1
    
    return a, FILE_PATH



def extracter(JPG, CR2):
    
    SS = pd.DataFrame.from_dict(JPG[0], orient = 'index')
    GG = pd.DataFrame.from_dict(CR2[0], orient = 'index')
    
    for i in range(len(SS[0])):
        T1 = SS[0][i].replace(JPG[1], "") #JPG PATH
        T2 = T1.replace(".JPG", "")
        SS[0][i] = T2
    
    for i in range(len(GG[0])):
        T1 = GG[0][i].replace(CR2[1], "") #CR2 PATH
        T2 = T1.replace(".CR2", "")
        GG[0][i] = T2
    
    
    del_prep = np.setdiff1d(GG[0], SS[0]) # Finding the elements that need to be deleted
    
    for i in range(len(del_prep)):
        T1 = CR2[1] + "\\" + del_prep[i] + ".CR2"
        del_prep[i] = T1
    
    os.mkdir(CR2[1]+'\\TRASH')
    
    dest_path = CR2[1]+'\\TRASH'
    
    for i in trange(len(del_prep)):
        shutil.move(del_prep[i], dest_path)
        
    print("Operation Completed")
    print("JPG images from:", JPG[1], "have been cross verified with the RAW images in", CR2[1])
    print("The total number of JPG images present are:", len(JPG[0]))
    print("The total number of CR2 images present are:", len(CR2[0]))
    print("The total number of images deleted are:", len(del_prep))
    print("The Images to be permanently deleted are moved to location:", dest_path,"\n\n")
    
    print("_______oBBBBB8o______oBBBBBBB ")
    print("_____o8BBBBBBBBBBB__BBBBBBBBB8________o88o, ")
    print("___o8BBBBBB**8BBBB__BBBBBBBBBB_____oBBBBBBBo, ")
    print("__oBBBBBBB*___***___BBBBBBBBBB_____BBBBBBBBBBo, ")
    print("_8BBBBBBBBBBooooo___*BBBBBBB8______*BB*_8BBBBBBo, ")
    print("_8BBBBBBBBBBBBBBBB8ooBBBBBBB8___________8BBBBBBB8, ")
    print("__*BBBBBBBBBBBBBBBBBBBBBBBBBB8_o88BB88BBBBBBBBBBBB, ")
    print("____*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8, ")
    print("______**8BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB*, ")
    print("___________*BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB8*, ")
    print("____________*BBBBBBBBBBBBBBBBBBBBBBBB8888**, ")
    print("_____________BBBBBBBBBBBBBBBBBBBBBBB*, ")
    print("_____________*BBBBBBBBBBBBBBBBBBBBB*, ")
    print("______________*BBBBBBBBBBBBBBBBBB8, ")
    print("_______________*BBBBBBBBBBBBBBBB*, ")
    print("________________8BBBBBBBBBBBBBBB8, ")
    print("_________________8BBBBBBBBBBBBBBBo, ")
    print("__________________BBBBBBBBBBBBBBB8, ")
    print("__________________BBBBBBBBBBBBBBBB, ")
    print("__________________8BBBBBBBBBBBBBBB8, ")
    print("__________________*BBBBBBBBBBBBBBBB, ")
    print("__________________8BBBBBBBBBBBBBBBB8, ")
    print("_________________oBBBBBBBBBBBBBBBBBB, ")
    print("________________oBBBBBBBBBBBBBBBBBBB, ")
    print("________________BBBBBBBBBBBBBBBBBBBB, ")
    print("_______________8BBBBBBBBBBBBBBBBBBB8, ")
    print("______________oBBBBBBBBB88BBBBBBBBB8, ")
    print("______________8BBBBBBBBB*8BBBBBBBBB*, ")
    print("______________BBBBBBBBB*_BBBBBBBBB8, ")
    print("______________BBBBBBBB8_oBBBBBBBBB*, ")
    print("______________8BBBBBBB__oBBBBBBBB*, ")
    print("______________BBBBBBB*__8BBBBBBB*, ")
    print("_____________8BBBBBB*___BBBBBBB*, ")
    print("____________8BBBBBB8___oBBBBBB8, ")
    print("___________8BBBBBB8____8BBBBBB*, ")
    print("__________oBBBBBB8____BBBBBBB8, ")
    print("__________BBBBBBB8___BBBBBBBB*, ")
    print("_________oBBBBBBB8___BBBBBBBB, ")
    print("_________8BBBBBB8____BBBBBBB*, ")
    print("_________BBBBBB*_____8BBBBB*, ")
    print("________oBBBB8_______BBBBB*, ")
    print("________oBBB8________BBBB*, ")
    print("______8BBBB*_______*BBBBBBBB8o,") 
    print("______BBBBB*____________*88BBBo")
    
    exit()
    
    
JR = reader_JPG() # location & list of JPG Files are stored 
CR = reader_CR2() # location & list of CR2 Files are stored 
extracter(JR,CR)
    
    