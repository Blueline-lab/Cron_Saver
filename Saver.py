## This Python file uses the following encoding: utf-8
#Saver 07.06.2021
#saving files periodically

#--------------------------------------------

#modules
import os
from shutil import copytree
from filecmp import dircmp
import config
import hashlib
import csv



class Saving:

    def __init__(self):
        self.dest = config.destination_path
        #destination path from config file


    def logs(self, value):      #some logs, find it in LOGS.txt
        with open("LOGS.txt", "w") as logs:
            logs.write(value)
            logs.close()

    def copy_machine(self):         #Copy Fucntion
        try:
            copytree(f"/home/{str(config.username)}/Musique", self.dest)
            self.logs(f"Saving copy on {self.dest}")
        except:
            print("Error in copy")
            self.logs(f"Error in copy {self.dest}")

    def replace_old_copy(self, day_past):       #delete the copy of tommorow 
        string_dest = str(self.dest) 
        day = string_dest[-1]
        int_day = int(day) - day_past
        string_dest[-1] = str(int_day)
        try:
            os.system(f"rm -r {string_dest}")
            self.logs(f"Correctly rm{string_dest}")
        except:
            print("Cannot del last Save")
            self.logs(f"Cannot rm copy {string_dest}")

    def new_device(self):       #In case of new device detected this function copy the repo session on the profile of the new device
        command = str(os.popen("hostname").read())
        lift = command[0:4]
        if lift != config.hostname:
            copytree(self.dest, f"/home/{str(config.username)}/Musique")
            config.hostname = command
            self.logs(f"Changing device on {str(config.date)} new device is {str(config.hostname)}")




    def tree(self):     #tree command 
        tree = os.popen(f"tree /home/{config.username}/Musique").read()
        return str(tree)


    def generate_hash_path(self,str_os):        #generate hash 
        hash1 = hashlib.sha256(str(str_os).encode(encoding="UTF-8"))
        return str(hash1.digest())

    def write_csv(self,value):      #write the hash
        with open('key.csv', 'w', newline='') as s:
            field = ['hash = ']
            write = csv.DictWriter(s, fieldnames=field)
            write.writeheader()
            write.writerow({'hash = ':str(value)})

    def read_csv(self):         #read the last hash for compare
      with open('key.csv', 'r') as key:
        hash = str()
        read = csv.DictReader(key)
        for i in read:
            hash = i['hash = ']
        return str(hash)
       

    def explorer(self):     
        #MAIN function : make hash of the tree repo, compare it with the last hash, save and replace if there is change
        check_device = self.new_device() 
        tree = self.tree()
        hasher= str(self.generate_hash_path(tree))
        read = str(self.read_csv())
        if read == "" or read != hasher:
            self.write_csv(hasher)
            self.copy_machine()
            self.replace_old_copy(config.saving_duration)
       
            


    
        



        





    






