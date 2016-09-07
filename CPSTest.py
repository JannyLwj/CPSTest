import os
import time
import shutil

def copyfile():
    date = time.strftime("%Y%m%d", time.localtime(time.time()))
    print(date)
    source_dir = "\\\\10.193.236.88\\dropfolder\\RM2.0CI_CDC\\RM2.0CI_CDC_" + date + ".1\\Install\\Suite\\PCR_NA"
    target_dir = "D:\Target\CPS"
    if os.path.exists(target_dir):
        os.remove(target_dir)
    shutil.copytree(source_dir, target_dir)


if __name__ == '__main__':
    copyfile()







