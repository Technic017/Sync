#########################################
#   Name: Sync                          #
#   Version: 0.0.1 (alpha)              #
#   Author: Technic017                  #
#   Discription:                        #
#       Program do synchronizacji       #
#       dokumentow dysk <> PC           #
#   Date: 13/11/2023                    #
#########################################

import os

# Stale
FOLDERY = ("./TEST_PC", "./TEST_DYSK") # 0 - folder na PC, 1 - folder na dysku

def zawartoscFolderow():
    pass

def porownywanieFolderow(folder0, folder1):

    folder_dysk = os.listdir(folder1)
    folder_pc = os.listdir(folder0)

    pliki_to_sync = []

    for file_d in folder_dysk:
        if file_d not in folder_pc:
            pliki_to_sync.append([0,file_d])

    for file_p in folder_pc:
        if file_p not in folder_dysk:
            pliki_to_sync.append([1,file_p])
    
    return pliki_to_sync

print(porownywanieFolderow(FOLDERY[0], FOLDERY[1]))
