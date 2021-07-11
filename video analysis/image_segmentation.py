import pixellib
from pixellib.instance import custom_segmentation

segment_image = custom_segmentation()
segment_image.inferConfig(num_classes= 2, class_names= ["BG", "butterfly", "squirrel"])
segment_image.load_model("mask_rcnn_model.005-0.443756.h5")
segment_image.segmentImage("butterfly (1).jpg", show_bboxes=True, output_image_name="sample_out.jpg")