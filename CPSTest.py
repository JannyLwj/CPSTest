import os
import win32file
import win32con
import time
import shutil
from os import listdir

ACTIONS = {
    1: "Created",
    2: "Deleted",
    3: "Updated",
    4: "Renamed from something",
    5: "Renamed to something"
}

FILE_LIST_DIRECTORY = win32con.GENERIC_READ
path_to_watch=r"\\zch49app08\CG546\8.Temp\Janny"
hDir = win32file.CreateFile(
    path_to_watch,
    FILE_LIST_DIRECTORY,
    win32con.FILE_SHARE_READ,
    None,
    win32con.OPEN_EXISTING,
    win32con.FILE_FLAG_BACKUP_SEMANTICS,
    None
)

if __name__ == '__main__':
    time=time.strftime("%Y%m%d",time.localtime(time.time()))
    print(time)
    sourceDir="\\\\10.193.236.88\\dropfolder\\RM2.0CI_CDC\\RM2.0CI_CDC_"+time+".1\\Install\\Suite\\PCR_NA"
    targetDir="D:\Target\CPS"
    copyFileCounts=0
    if os.path.exists(targetDir):
        os.remove(targetDir)
    shutil.copytree(sourceDir, targetDir)
    print("End")







