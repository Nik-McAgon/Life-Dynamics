import Daphny_counter
import argparse
import os
import cv2

parser = argparse.ArgumentParser(description='Process video files from a folder and detect daphnias')
parser.add_argument(
    '-p', '--path',
    default='.',
    help='folder where the videos are')
parser.add_argument(
    '-o', '--out',
    default='output.txt',
    help='path to file where to write the results')
parser.add_argument(
    '-st', '--start',
    default=0,
    help='start frame')
parser.add_argument(
    '-sp', '--stop',
    default=200,
    help='stop frame')

args = vars(parser.parse_args())

debug=False
daph_stat=[]
##img=get_imgList("/home/nmakagonov/Desktop/")
if (args['path']!='0'):
    nb=args['path']
else:
    nb = input('Choose a folder with daphny dataset')
if (nb=="cam"):
    img=get_imgs_from_cam()
else:
    if (len(nb)==0):
        nb="/media/nmakagonov/DiskD/NN_DATA/daphniacounter/DataForTraining/DataForTraining/Cohort15/Cohort15_1_RawImage/"
    print ('folder%s \n' % (nb))
    img=Daphny_counter.get_imgList(nb)
    if(len(img)==0):
        img=Daphny_counter.get_Simple_imgList(nb)
imgs=img[int(args['start']):int(args['stop'])]
diffImg=Daphny_counter.RA_BackGround_Extraction(imgs)
cv2.imwrite("/media/nmakagonov/DiskD/NN_DATA/daphniacounter/rez/rez.jpeg", diffImg)
pimg=Daphny_counter.prepareImg(imgs,diffImg)

[mean,min,max,boxs]=Daphny_counter.countDaph(pimg)
print(len(boxs))
print (len(imgs))
for i in range(0, len(imgs)):
    for j in range(0, len(boxs[i])):
        cv2.rectangle(imgs[i], (boxs[i][j][0], boxs[i][j][1]), (boxs[i][j][2],boxs[i][j][3]), (255, 0, 200), 2)

    cv2.imwrite("/media/nmakagonov/DiskD/NN_DATA/daphniacounter/rez/"+str(i)+".jpeg",imgs[i])
    cv2.imshow("dcss", imgs[i])
    #cv2.waitKey()
Daphny_counter.printSave(mean,min,max,args)
