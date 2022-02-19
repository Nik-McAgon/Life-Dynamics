# import the opencv library
import cv2
  
def get_imgs_from_cam(camID):

    # define a video capture object
    vid = cv2.VideoCapture(camID,cv2.CAP_V4L2)
    vid.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    width = 1920
    height = 1080
    vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    img=[]

    for i in range(0,200):
        
        # Capture the video frame
        # by frame
        ret, frame = vid.read()
        frame=cv2.GaussianBlur(frame,[3,3],2)
        img.append(crop(frame))
    
        # Display the resulting frame
        #cv2.imshow('frame', frame,)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if 0xFF == ord('q'):
            break
    
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    #cv2.destroyAllWindows()
    
    return(img)

def crop(img):
    x=450
    y=300
    r=400
    rectX = (x - r) 
    rectY = (y - r)
    crop_img = img
    return(crop_img)
