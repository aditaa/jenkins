#!/usr/bin/env python

import tarfile , argparse, os
from datetime import date 
from shutil import copyfile

"""Backup a dir

usage: Backup.py [-h] source_dir dest_dir
""" 

__author__ = "Daniel Shirley"
__credits__ = ["Daniel Shirley"]
__license__ = "GPL v.2"
__version__ = "0.21"
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
    print "Checking directory"
    if not os.path.exists(os_dir):
            print os_dir, "does not exist."
            exit(1)
    else:
        print "directory is good"

def Make_tar(source_dir, destination):
    print "Starting backup"
    tar = tarfile.open(os.path.join(destination, 'Backup-'+str(date.today())+'.tar.gz'), 'w:gz')

    for item in os.listdir(backupdir):
        print "Adding " +item
        tar.add(os.path.join(backupdir, item),arcname="Backup/"+item)
        
    tar.close()
    print "Complete"

def Copy_to_current(destination):
    print "copying backup-date to backup-current"
    copyfile(os.path.join(destination, 'Backup-'+str(date.today())+'.tar.gz'), os.path.join(destination, 'Backup-Current.tar.gz'))
    print "Complete"
        
def Main():
    Get_vars()
    Check_dir(backupdir)
    Make_tar(backupdir, destination)
    Copy_to_current(destination)

if __name__ == '__main__':
    Main()


