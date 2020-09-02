import os
import shutil
import queue

# shutil.copytree(r'D:\work\8.04\20200804-其他辅助工作-邮件-互联网卡标识标签确认',r'D:\work\aa\20200804-其他辅助工作-邮件-互联网卡标识标签确认')
# # 将旧的文件目录按层级复制到新的目录  
# bfs 层级按文件路径中的'\\'出现次数判断
def oldCopyToNewDirByLayers(oldfileDir,newfileDir,layer):
    oldLayer = oldfileDir.count('\\')
    layer += oldLayer
    q = queue.Queue()
    q.put(oldfileDir)
    while(q.empty() != True):
        oldtmp = q.get()
        for filename in os.listdir(oldtmp):
            file_path = os.path.join(oldtmp,filename)
            if(file_path.count('\\') < layer):
                q.put(file_path)
            elif(file_path.count('\\') == layer):
                if(os.path.isdir(file_path)):
                    shutil.copytree(file_path,os.path.join(newfileDir,filename))
                else:
                    shutil.copyfile(file_path,os.path.join(newfileDir,filename))
            else:
                return False
    return True

if __name__ == "__main__":
    oldfileDir = 'D:\\work'
    newfileDir = 'D:\\works\\张洪豪'
    for file in os.listdir(oldfileDir):
        file_path = os.path.join(oldfileDir,file)
        print(file_path)
    oldCopyToNewDirByLayers(oldfileDir,newfileDir,2)

