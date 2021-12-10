import config
import Daphny_counter 
import argparse
import telebot
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
if(args["path"]!="cam"):
    img=Daphny_counter.get_imgList(args["path"])
else:
    img=Daphny_counter.get_imgs_from_cam()
imgs=img[0:200]
diffImg=Daphny_counter.RA_BackGround_Extraction(imgs)

pimg= Daphny_counter.prepareImg(imgs,diffImg)
[mean,min,max]=Daphny_counter.countDaph(pimg)
bot.send_message(config.GrupID, Daphny_counter.printSave(mean,min,max,args))
