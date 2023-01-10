from pytesseract import *
import cv2
import os


def Conversion(file):
    multiple = 4
    image = cv2.resize(cv2.imread(file),(0,0),fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)
    text = image_to_string(image,lang="eng",config='--psm 1 -c preserve_interword_spaces=1')
    return text

def ParseText(text, cnt_row, cnt_col):
    text = text.replace('\n\n','\n')
    list = text.split('\n') 
    list.remove("")
    result=[]
    for i in range(cnt_row):
        temp=[]
        for j in range(cnt_col):
            temp.append(list[i + j*cnt_row])
        result.append(temp)
    return result
    
def ConfigDict():
    this_program_directory = os.path.dirname(os.path.abspath(__file__))
    path = f'{this_program_directory}\\Path_Capture_Folder.ini'
    dic = {}
    with open(path, 'r') as f:
        for linetext in f.readlines():
            dic[linetext.split("=")[0]]=linetext.strip().split("=")[1]            
        f.close
    return dic


if __name__ == '__main__':
    
    config = ConfigDict().copy()
    folder = config['Folder_Pictures']
    row_cnt = config['Row_Count']
    col_cnt = config['Column_Count']
    fileext = tuple(config['File_Extensions'])
    photos = [os.path.join(folder,file) for file in os.listdir(folder) if file.endswith(fileext)]
    
    for photo in photos:
        print('Converting "{}" in progress...'.format(os.path.basename(photo)))
        result_file = os.path.splitext(photo)[0] + '.csv'

        multiple=3.35
        src = cv2.imread(photo)
        dst = src[205:448, 725:1125].copy()
        print("Photo={}".format(photo))
        image = cv2.resize(dst,(0,0),fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)
        
        text = image_to_string(image,lang="eng",config='--psm 1 -c preserve_interword_spaces=1')
        print(text)

        # print(Conversion())
        # result = ParseText(Conversion(photo),row_cnt,col_cnt)
        # print(result)
        # r = open(result_file,'w')
        # for row in result:
        #     string = ",".join(row)
        #     r.write(string + '\n')
        # r.close
    
    input('Press Enter to Finish.')




