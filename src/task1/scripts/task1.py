import rospy
import numpy as np
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from my_redmarkerdetection import *    # image processing by cython
sorted_ID = []

def img_callback(data):
    global sorted_ID
    result=[]
    try:
        cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as err:
        print(err)    
    seg_papram = np.array([0,15,125,180,46,80],dtype="uint8")
    cv2.imshow("img",cv_image)
    ID = sort_number_label(cv_image,seg_papram)  
    if ID != sorted_ID:
        for i in ID:
            result.append(i+1)
        rospy.loginfo(result)
        sorted_ID=ID
    cv2.waitKey(1)

if __name__=="__main__":
    rospy.init_node("task1")
    bridge = CvBridge()
    load_template()
    image_sub = rospy.Subscriber("/camera/color/image_raw", Image, img_callback)
    rospy.spin()