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

from test import explorer


class Saver:

    def __init__(self):
        self.dest = config.destination_path


    def logs(self, value):
        with open("LOGS.txt", "w") as logs:
            logs.write(value)
            logs.close()

    def copy_machine(self):
        try:
            copytree(f"/home/{config.username}\Musique", self.dest)
            self.logs(f"Saving copy on {self.dest}")
        except:
            print("Error in copy")
            self.logs(f"Error in copy {self.dest}")

    def replace_old_copy(self, day_past):
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

    def new_device(self):
        if str(os.system("hostname")) != config.hostname:
            copytree(self.dest, "/home")
            config.hostname = os.system("hostname")
            self.logs(f"Changing device on {config.date} new device is {config.hostname}")




    def racine(self):
        racine = os.popen(f"ls /home/{config.username}").read()
        return str(racine)

    def tree(self):
        tree = os.popen(f"tree /home/{config.username}/Musique").read()
        return str(tree)


    def generate_hash_path(self,str_os):
        hash1 = hashlib.sha256(str(str_os).encode(encoding="UTF-8"))
        return str(hash1.digest())

    def write_csv(self,value):
        with open('key.csv', 'w', newline='') as s:
            field = ['hash = ']
            write = csv.DictWriter(s, fieldnames=field)
            write.writeheader()
            write.writerow({'hash = ':str(value)})

    def read_csv(self):
      with open('key.csv', 'r') as key:
        hash = str()
        read = csv.DictReader(key)
        for i in read:
            hash = i['hash = ']
        return str(hash)
       

    def explorer(self):
        tree = self.tree()
        hasher= str(self.generate_hash_path(tree))
        read = str(self.read_csv())
        if read == "" or read != hasher:
            self.write_csv(hasher)
            self.copy_machine()
       
            

S = Saver()
#a = S.tree()
#S.write_csv(S.generate_hash_path(a))
#e = S.read_csv()
#z = S.generate_hash_path(a)

#if e == z : 
    #print("ok")

S.explorer()
    
        



        





    






