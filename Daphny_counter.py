import cv2
import numpy as np
import os
from connect_to_camera import get_imgs_from_cam
from numpy.core.fromnumeric import shape
import argparse

size = 1
kernal = {
    'rect':cv2.getStructuringElement(cv2.MORPH_RECT, (size,size)),
    'cross':cv2.getStructuringElement(cv2.MORPH_CROSS, (size,size)),
    'ell':cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size,size)),
    'diamond':np.array([
        [0,0,0],
        [0,4,0],
        [0,0,0]        
    ], dtype=np.uint8)
}

def RA_BackGround_Extraction(img_s):

    fora=70
    avg1 = np.float32(np.zeros(img_s[0].shape))
    avg2 = np.float64(np.zeros(img_s[0].shape))
    grey_new=np.int32(np.zeros(img_s[0].shape))
    num=len(img_s)
    for f in img_s:
        #cv2.accumulateWeighted(f,avg1,0.1)
        cv2.accumulateWeighted(f,avg2,1/num)

        #res1 = cv2.convertScaleAbs(avg1)
        res2 = cv2.convertScaleAbs(avg2)

    delta=np.mean(img_s[0])/np.mean(res2)

    grey_new = cv2.convertScaleAbs(res2*delta)

    return(grey_new)

def get_imgList(path_to_folder):
    img=[]
    img1=[]
    img2=[]
    img3=[]
    img4=[]
    relevant_path = path_to_folder
    
    included_extensions = ['_1_.png']
    file_names = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    for file in file_names:
        img1.append(cv2.imread(path_to_folder+file))

    included_extensions = ['_2_.png']
    file_names = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    for file in file_names:
        img2.append(cv2.imread(path_to_folder+file))

    included_extensions = ['_3_.png']
    file_names = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    for file in file_names:
        img3.append(cv2.imread(path_to_folder+file))

    included_extensions = ['_4_.png']
    file_names = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    for file in file_names:
        img4.append(cv2.imread(path_to_folder+file))

    for i in range(0,len(img3)-1):
        crop_img = img
        up=cv2.hconcat([img1[i],img2[i]])
        down=cv2.hconcat([img3[i],img4[i]])
        #[0:img3[i].shape[0], 50:img3[i].shape[1]+img4[i].shape[1]-50]
        img.append(cv2.GaussianBlur((cv2.vconcat([up,down])[20:up.shape[1]+up.shape[1],50:img3[i].shape[1]+img4[i].shape[1]-20]),[3,3],5))
    return(img)

def get_Simple_imgList(path_to_folder):
    img=[]

    relevant_path = path_to_folder
    included_extensions = ['.jpg']
    file_names = [fn for fn in os.listdir(relevant_path) if any(fn.endswith(ext) for ext in included_extensions)]
    file_names.sort()
    for file in file_names:
        frame=cv2.GaussianBlur(cv2.imread(path_to_folder+file),[3,3],5)
        img.append(frame[0:frame.shape[0],0:frame.shape[1]-0])

    print("files find :", len(img))

    return(img)

def RGB2GRAY(img):
    return(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


def maxiSobelGrads(im,kernal):
    kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]])
    gray = cv2.filter2D(im, -1, kernel)
    ksize=3
    gX = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=1, dy=0, ksize=ksize)
    gY = cv2.Sobel(gray, ddepth=cv2.CV_32F, dx=0, dy=1, ksize=ksize)

    # the gradient magnitude images are now of the floating point data
    # type, so we need to take care to convert them back a to unsigned
    # 8-bit integer representation so other OpenCV functions can operate
    # on them and visualize them
    gX = cv2.convertScaleAbs(gX)
    gY = cv2.convertScaleAbs(gY)

    # combine the gradient representations into a single image
    combined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)
    cv2.threshold(combined,100,255,0,combined)
    erodeIm=cv2.dilate(combined,kernal)
    erodeIm=cv2.dilate(erodeIm,kernal)
    diffImg=erodeIm-combined

    return(diffImg)

def equalMean(target_im,change_im):

    delta=-np.mean(change_im)+np.mean(target_im)
    change_im=cv2.convertScaleAbs( np.where((255 - change_im) < delta,255,change_im+delta))

    return(change_im)

def prepareImg(img,background):

    rez=[]
    for i in range(0,len(img)):

        difference=30
        img[i]=equalMean(img[0],img[i])

        gdimg = RGB2GRAY(background)-RGB2GRAY(img[i])-difference
        BWImg=cv2.threshold(gdimg,150,255,cv2.THRESH_BINARY_INV )[1]

        #ret, bw = cv2.threshold(gray,a,255,cv2.THRESH_BINARY_INV )
        # bw=cv2.erode(BWImg,kernal["cross"])
        # bw=cv2.dilate(bw,kernal["cross"])

        rez.append(BWImg)
    return(rez)

def countDaph(imgs):
    daph_stat=[]
    boxs = []
    for i in range(0,len(imgs)):
        BWImg = imgs[i]
        frame = imgs[i]
        contours, hierarchy = cv2.findContours(BWImg, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        cv2.drawContours(frame, contours, contourIdx=-1, color=(100, 255, 90), thickness=1, lineType=cv2.LINE_AA)
        for contour in contours:
            print(cv2.contourArea(contour))
        print(" ")
        cv2.imwrite("/media/nmakagonov/DiskD/NN_DATA/daphniacounter/rez/contur"+str(i)+".jpeg", frame)

        try: hierarchy = hierarchy[0]
        except: hierarchy = []

        height, width = BWImg.shape
        min_x, min_y = width, height
        max_x = max_y = 0
        boxs.append([])

        # computes the bounding box for the contour, and draws it on the frame,
        for contour, hier in zip(contours, hierarchy):
            (x,y,w,h) = cv2.boundingRect(contour)
            min_x, max_x = min(x, min_x), max(x+w, max_x)
            min_y, max_y = min(y, min_y), max(y+h, max_y)
            if w > 1 and h > 1:
                cv2.rectangle(frame, (x-round(w/4),y-round(h/4)), (x+w+round(w/4),y+h+round(h/4)), (255, 0, 200), 2)
                boxs[i].append([x-round(w/4),y-round(h/4),x+w+round(w/4),y+h+round(h/4)])

        count = len(contours)
        daph_stat.append(count)
        print(count)

    mean=(np.mean(daph_stat))
    diff=daph_stat[:]-mean
    sort_diff=sorted(diff,key=abs)
    
    half_amplitude= abs(sort_diff[int(len(sort_diff)*0.999)])
    return(round(mean), round(mean-half_amplitude), round(mean+half_amplitude), boxs)

def printSave(mean,min,max,args):
    print("mean: ", mean)
    print("confidence interval: ",min," - ",max)
    f = open(args['out'], 'w')
    f.write('%s: %.0f, [%.1f, %.1f]\n' % (args['path'], mean, min, max))
    f.flush()
    return('%s: %.0f, [%.1f, %.1f]\n' % (args['path'], mean, min, max))

