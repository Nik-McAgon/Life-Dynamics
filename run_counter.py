import Daphny_counter
import argparse
import os

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

pimg=Daphny_counter.prepareImg(imgs,diffImg)
[mean,min,max]=Daphny_counter.countDaph(pimg)
Daphny_counter.printSave(mean,min,max,args)
