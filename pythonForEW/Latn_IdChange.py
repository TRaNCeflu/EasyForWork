import re

def changeLatn_Id(oldString,oldLatn,newLatn):
    oldLatn = oldLatn.lower()
    newLatn = newLatn.lower()
    oldasc = ord(oldLatn)
    newasc = ord(newLatn)
    for i in range(len(oldString)):
        iasc = ord(oldString[i])
        # print(iasc)
        if(i == len(oldString) - 1):
            if(iasc == oldasc):
                if(oldString[i-1] == '_'):
                    oldString = oldString[:i]+chr(newasc)
            elif(iasc == oldasc - 32):
                if(oldString[i-1] == '_'):
                    oldString = oldString[:i]+chr(newasc-32)
            break
        if(iasc == oldasc):
            if(oldString[i-1] == '_' and (oldString[i+1] == ' ' or oldString[i+1] == '_')):
                oldString = oldString[:i]+chr(newasc)+oldString[i+1:]
        elif(iasc == oldasc - 32):
            if(oldString[i-1] == '_' and (oldString[i+1] == ' ' or oldString[i+1] == '_')):
                oldString = oldString[:i]+chr(newasc-32)+oldString[i+1:]
        else:    
            continue
    return oldString
                
def changeLatn_IdForAll(oldString,oldLatn):
    oldLatn = oldLatn.lower()
    strList = []
    for i in range(ord('a'),ord('k')+1):
        strList.append(changeLatn_Id(oldString,oldLatn,chr(i)))
    return strList

if __name__ == "__main__":
    line ='''VA_OFR_ASSET_EXI_HIST_J'''
    # line = changeLatn_Id(line,'a','k')
    strList = changeLatn_IdForAll(line,'J')
    #   mode = 'a' append  mode = 'w' 覆盖原先内容
    outFile = open(r'd:\code\python\11.txt',mode='w',encoding='utf-8')
    for i in strList:
        print(i,file=outFile)
    outFile.close()
        
