import os
import time
import shutil
import win32api
import win32con

def copyfile_from_server():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    print(date)
    source_dir = "\\\\10.193.236.88\\dropfolder\\RM2.0CI_CDC\\RM2.0CI_CDC_" + date + ".1\\Install\\Suite\\PCR_NA"
    target_dir = "D:\Target\CPS"+date
    if os.path.exists(target_dir):
        os.remove(target_dir)
    if not os.path.exists(source_dir):
        print("Source folder is not exist")
        return False
    shutil.copytree(source_dir, target_dir)
    print("Copy file finished")
    return True


def prepare_uninstall():
    # Kill CPS & RM
    lst_killprocess=["Motorola.CommonCPS.RadioManagement.Shell.exe",
                     "mototrbocps.exe"]

    tasklistrl = os.popen("tasklist").readlines()
    for task in tasklistrl:
        for process in lst_killprocess:
            if len(process) < 29:
                if process == task[0:len(process)]:
                    print(process)
                    pid=int(task[29:34])
                    print(pid)
                    try:
                        handle = win32api.OpenProcess(1, False, pid)
                        win32api.TerminateProcess(handle, 0)
                        win32api.CloseHandle(handle)
                        print("Successfully killed process %s on pid %d." % (task[0:len(process)], pid))
                    except:
                        pass
            else:
                if process[0:25]==task[0:25]:
                    print(process)
                    pid = int(task[29:34])
                    print(pid)
                    try:
                        handle = win32api.OpenProcess(1, False, pid)
                        win32api.TerminateProcess(handle, 0)
                        win32api.CloseHandle(handle)
                        print("Successfully killed process %s on pid %d." % (task[0:len(process)], pid))
                    except:
                        pass

def uninstall_cpsrm():
    #uninstall CPS from machine
    lst_uninstall = ['Motorola RM Device Programmer',
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
        try:
            display_uuid=win32api.RegEnumKey(registry_key, i)
            subkey = win32api.RegOpenKeyEx(registry_key, display_uuid, 0, win32con.KEY_READ)
            display_name, datatype = win32api.RegQueryValueEx(subkey, "DisplayName")
            if display_name in lst_uninstall:
                print(display_name)
                print(display_uuid)
                lst_displayname.append(display_uuid)
                lst_uuid.append(display_uuid)
                system_cmd="MsiExec.exe /X" +display_uuid+ " /quiet"
                print(system_cmd)
                os.system(system_cmd)
                print("uninstall successfully")
        except:
            pass
    print("End")


def clean_machine():
    # Remove folder
    remove_folder = r"C:\ProgramData\Motorola"
    if os.path.exists(remove_folder):
        motorola_files = os.listdir(remove_folder)
        # print(motorola_files)
        for file in motorola_files:
            remove_folder = r"C:\ProgramData\Motorola"
            remove_folder = os.path.join(remove_folder, file)
            remove_cmd = "rmdir \"" + remove_folder + "\" / S / Q"
            print(remove_cmd)
            os.system(remove_cmd)
            print("Remove motorola file successfully")

    # Run Drop DB
    try:
        process="sqlcmd -S .\\MOTORMSVR2 -Q \"IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'RMServer') ALTER DATABASE [RMServer] SET SINGLE_USER WITH ROLLBACK IMMEDIATE\""
        print(process)
        os.system(process)
        process="sqlcmd -S .\\MOTORMSVR2 -Q \"IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'RMServer') drop database [RMServer]\""
        print(process)
        os.system(process)
        process="sqlcmd -S .\\MOTORMSVR2 -Q \"IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'RMAuthorizationStore') ALTER DATABASE [RMAuthorizationStore] SET SINGLE_USER WITH ROLLBACK IMMEDIATE\""
        print(process)
        os.system(process)
        process="sqlcmd -S .\\MOTORMSVR2 -Q \"IF  EXISTS (SELECT name FROM sys.databases WHERE name = N'RMAuthorizationStore') drop database [RMAuthorizationStore]\""
        print(process)
        os.system(process)
    except:
        pass


def install_cpsrm():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    print(date)
    date="20160908"
    #install_path="D:\Target\CPS"+date+"\\Setup.exe"
    #CPS="D:\Target\CPS20160908\CPS\MOTOTRBO_CPS.msi"
    #os.system()



if __name__ == '__main__':
    copyfile_from_server()
    prepare_uninstall();
    uninstall_cpsrm()
    clean_machine()
    #install_cpsrm()







