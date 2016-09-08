import os
import time
import shutil
import win32api
import win32con



def copyfile():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    print(date)
    source_dir = "\\\\10.193.236.88\\dropfolder\\RM2.0CI_CDC\\RM2.0CI_CDC_" + date + ".1\\Install\\Suite\\PCR_NA"
    target_dir = "D:\Target\CPS"+date
    if os.path.exists(target_dir):
        os.remove(target_dir)
    if not os.path.exists(source_dir):
        exit()
        print("Source folder is not exist")
    shutil.copytree(source_dir, target_dir)
    print("Copy file finished")

def uninstall():
    lst_unistall = ['Motorola RM Device Programmer',
                  'Motorola RM Job Processor',
                  'Motorola RM MOTOTRBO Configuration Client',
                  'MOTOTRBO Customer Programming Software',
                  'Motorola RM Updater Service',
                  'Motorola RM Server']

    lst_uuid=[]
    lst_displayname=[]
    registry_key=win32api.RegOpenKeyEx(win32con.HKEY_LOCAL_MACHINE,'SOFTWARE\\WOW6432Node\\Microsoft\\Windows\\CurrentVersion\\Uninstall',0, win32con.KEY_READ)
    size=win32api.RegQueryInfoKey(registry_key)[0]
    for i in range(size):
        display_uuid=win32api.RegEnumKey(registry_key, i)
        subkey = win32api.RegOpenKeyEx(registry_key, display_uuid, 0, win32con.KEY_READ)
        try:
            display_name, datatype = win32api.RegQueryValueEx(subkey, "DisplayName")
            if display_name in lst_unistall:
                print(display_name)
                lst_displayname.append(display_uuid)
        except:
            pass


    print("aa")

if __name__ == '__main__':
    #copyfile()
    uninstall()







