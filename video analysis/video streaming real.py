import pixellib
from pixellib.instance import custom_segmentation
import cv2

capture = cv2.VideoCapture(0)

while capture.isOpened():
    res,frame=capture.read()
    segment_camera = custom_segmentation()
    segment_camera.inferConfig(num_classes=2, class_names=["BG", "butterfly", "squirrel"])
    segment_camera.load_model("trained_model.h5")
    a=segment_camera.process_camera(capture, frames_per_second= 10, output_video_name="output_video.mp4",show_bboxes=True, show_frames= True,frame_name= "frame")
    image=a[1]
    cv2.imshow('Image Segmentation',image)

    if cv2.waitKey(10) & 0xFF==ord('q'):
        break

capture.release()
cv2.destroyAllWindows()


