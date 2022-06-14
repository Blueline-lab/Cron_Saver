## This Python file uses the following encoding: utf-8
#Saver 07.06.2021
#saving files periodically

#--------------------------------------------

#modules
import os
from shutil import copytree
from filecmp import dircmp
import config


class Saver:

    def __init__(self):
        self.dest = config.destination_path


    def logs(self, value):
        with open("LOGS.txt", "w") as logs:
            logs.write(value)
            logs.close()

    def copy_machine(self):
        try:
            copytree("/home", self.dest)
            self.logs(f"Saving copy on {self.dest}")
        except:
            print("Error in copy")
            self.logs(f"Error in copy {self.dest}")

    def replace_old_copy(self):
        string_dest = str(self.dest) 
        day = string_dest[-1]
        int_day = int(day) - 3
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

    






