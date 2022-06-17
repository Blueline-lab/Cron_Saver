import hashlib
import os
import config
import csv


def racine():
    racine = os.popen(f"ls /home/{config.username}").read()
    return str(racine)



def generate_hash_path(str_os):
    hash1 = hashlib.sha256(str(str_os).encode(encoding="UTF-8"))
    return hash1.digest()

def write_csv(value):
     with open('key.csv', 'a', newline='') as s:
            write = csv.DictWriter(s, fieldnames=value)
            write.writeheader()
            write.writerow({"hash_tree":value})

def read_csv():
      with open('key.csv', 'r') as key:
        hash = str()
        read = csv.DictReader(key)
        for i in read:
            hash = i
        return hash
       


        



def explorer():
    base = str(racine())
    if read_csv() == "":
        print(base)


explorer()