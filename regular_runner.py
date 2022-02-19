import config
import Daphny_counter 
import argparse
import cv2
import telebot
from datetime import datetime
import time


# Get the number of cameras available
def count_cameras():
    max_tested = 100
    for i in range(max_tested):
        temp_camera = cv2.VideoCapture(i)
        if temp_camera.isOpened():
            temp_camera.release()
            print(i)
            continue
        else :
            continue
        return i



def makeCount(img, cam_number):
    imgs=img[0:200]
    today = datetime.now()
    name = today.strftime("%d_%m_%Y-%H_%M_%S")
    i=0
    path=""
    for im in imgs:
        i=i+1
        path="/home/pi/sm3/"+name+"_"+str(cam_number)+"_"+str(i)+".jpeg"
        cv2.imwrite(path,im)
        diffImg=Daphny_counter.RA_BackGround_Extraction(imgs)
        pimg= Daphny_counter.prepareImg(imgs,diffImg)
        [mean,min,max]=Daphny_counter.countDaph(pimg)
        return([mean,min,max,path])


#print("the number of cameras available: "+ str(count_cameras()))
last_time = time.time()
period = 14400
period = 220
#from telebot import types
bot = telebot.TeleBot(config.token)
parser = argparse.ArgumentParser(description='Process video files from a folder and detect daphnias')
parser.add_argument(
    '-p', '--path',
    default='cam',
    help='folder where the videos are')
parser.add_argument(
    '-o', '--out',
    default='output.txt',
    help='path to file where to write the results')
args = vars(parser.parse_args())
while True:
    if(time.time()-last_time>period):
        last_time=time.time()
        
        img=Daphny_counter.get_imgs_from_cam(0)
        [mean, min, max, path] = makeCount(img, 0)
        bot.send_message(config.GrupID, Daphny_counter.printSave(mean,min,max,args)+"__DEV1__CAM0")
        bot.send_photo(config.GrupID,photo=open(path,"rb")) 

        img=Daphny_counter.get_imgs_from_cam(2)
        [mean, min, max, path] = makeCount(img, 1)
        bot.send_message(config.GrupID, Daphny_counter.printSave(mean,min,max,args)+"__DEV1__CAM1")
        bot.send_photo(config.GrupID,photo=open(path,"rb")) 
       

        
    

