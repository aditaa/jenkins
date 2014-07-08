#!/usr/bin/env python

import tarfile , argparse, os
from datetime import date 

"""Backup a dir

usage: Backup.py [-h] source_dir dest_dir
""" 

__author__ = "Daniel Shirley"
__credits__ = ["Daniel Shirley"]
__license__ = "GPL v.2"
__version__ = "0.1"
__maintainer__ = "Daniel Shirley"
__email__ = "aditaa@ig2ad.com"
__status__ = "Production"






def Get_vars():
    global opts, args, backupdir, destination
    parser = argparse.ArgumentParser(
        description=__doc__)
    parser.add_argument("BACKUPDIR", help="Specify the directory to backup.")
    parser.add_argument("DESTINATION", help="Specify the location where the backup is sent.")

    args    = parser.parse_args()
    
    backupdir = args.BACKUPDIR
    destination = args.DESTINATION
    
def Check_dir(os_dir):
    if not os.path.exists(os_dir):
            print os_dir, "does not exist."
            exit(1)
    
def Exclusions():
    exclusions = []
    if args.exclude:
        for argument in args.exclude:
            exclusions.append("--exclude={}".format(argument))
    return exclusions

def Make_tar(source_dir, destination):
    fileName=destination+"Backup-"+str(date.today())+".tar"
    with tarfile.open(fileName, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
        
def Main():
    Get_vars()
    Check_dir(backupdir)
    Make_tar(backupdir, destination)


if __name__ == '__main__':
    Main()


