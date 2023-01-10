from pytesseract import *
import cv2
import os
import numpy as np
import pandas as pd
import re

def ConfigDict():
    this_program_directory = os.path.dirname(os.path.abspath(__file__))
    path = f'{this_program_directory}\\Path_Capture_Folder_Record.ini'
    dic = {}
    with open(path, 'r', encoding='UTF-8') as f:
        for linetext in f.readlines():
            dic[linetext.split("=")[0]] = linetext.strip().split("=")[1]
        f.close
    return dic


config = ConfigDict().copy()
folder = config['Folder_Pictures']
print(folder)
fileext = tuple(config['File_Extensions'])
photos = [os.path.join(folder, file) for file in os.listdir(folder) if file.endswith(fileext)]

# index = ['Function','V(AC)L-N','V(AC)L-L','Irms','Ipeak','Icrest','KW','KVA','PF','Frequency','Degrees']
Parameter = ['V(AC)L-N','V(AC)L-L','Irms','Ipeak','Icrest','KW','KVA','PF','Frequency','Degrees']

dx = 102
dy = 18
x_offset = 4
y_offset = 4
x_start = 4
x_end = 570
y_start = 4
y_end = 906
multiple = 5

writer = pd.ExcelWriter(folder+'\Test_Results.xlsx', engine='xlsxwriter')

for photo in photos:
    print('Converting "{}" in progress...'.format(os.path.basename(photo)))
    i = 0
    Col_1 = []
    Col_2 = []
    Col_3 = []
    Col_4 = []
    list = [Col_1 ,Col_2 , Col_3, Col_4]
    
    src = cv2.imread(photo, cv2.IMREAD_GRAYSCALE)
    dst2 = cv2.adaptiveThreshold(src,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,2)

    # cv2.imshow('dst',dst)
    # cv2.waitKey()
    p = re.compile('[+-]?\d+(\.?)+\d*')

    for x in range (x_start,x_end,dx+x_offset):
        for y in range(y_start,y_end,dy+y_offset):
            dst = dst2[y:y+dy, x:x+dx].copy()
            image = cv2.resize(dst, (0, 0), fx=multiple, fy=multiple, interpolation=cv2.INTER_LINEAR)
            
            cv2.imshow('image',image)
            cv2.waitKey()
            text = image_to_string(image, lang="eng", config='--psm 4 -c preserve_interword_spaces=1').strip()

            print('text=',text)
            print(p.search(text))
            value= p.search(text)[0]
            # if  value == 0:
            #     text = 0
            # elif float(text) >= 1000:
            #     text = str(float(text)/1000)
            
            list[i].append(text)
        i+=1
        x_offset = 20
        dx = 140
    
    # test_df = pd.DataFrame({'Phase_A':Phase_A, 'Phase_B':Phase_B, 'Phase_C':Phase_C},index=Parameter)
    test_df = pd.DataFrame({'온도':Col_1, '하한값':Col_2, '평균값':Col_3, '상한값':Col_4})
    test_df.to_excel(writer, sheet_name=os.path.basename(photo))

writer.save()

input("완료되었습니다. 종료하려면 Enter 키를 입력하세요.")