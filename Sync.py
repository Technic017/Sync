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
import shutil

# STALE
FOLDERY = ("./TEST_PC", "./TEST_DYSK")

class FolderComparer:

    def __init__(self, folder0, folder1):
        self.folder0 = folder0
        self.folder1 = folder1

    def get_files_to_sync(self):
        files_to_sync = []

        for file_d in os.listdir(self.folder1):
            if file_d not in os.listdir(self.folder0):
                files_to_sync.append((0, file_d))

        for file_p in os.listdir(self.folder0):
            if file_p not in os.listdir(self.folder1):
                files_to_sync.append((1, file_p))
        
            if file_p in os.listdir(self.folder1):
                files_to_sync.append((2, file_p))

        return files_to_sync

    def exists_folder(self):
        return os.path.exists(self.folder1)
    
    def folder_synchronisation(self):
        copiedFromPc = []
        copiedFromDrive = []
        missing_files = self.get_files_to_sync()
        for file_info in missing_files:
            if file_info[0] == 1:
                source_file = os.path.join(self.folder0, file_info[1])
                destination_file = os.path.join(self.folder1, file_info[1])
                shutil.copy(source_file, destination_file)
                copiedFromPc.append(file_info)
                
            if file_info[0] == 0:
                source_file = os.path.join(self.folder1, file_info[1])
                destination_file = os.path.join(self.folder0, file_info[1])
                shutil.copy(source_file, destination_file)
                copiedFromDrive.append(file_info)
        return copiedFromPc, copiedFromDrive


if __name__ == "__main__":
    comparer = FolderComparer(FOLDERY[0], FOLDERY[1])
    if comparer.exists_folder():
        files_to_sync = comparer.get_files_to_sync()
        print(files_to_sync)
