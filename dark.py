# pylint: disable=missing-docstring
import subprocess


def get_detection_square(darknet_loc, darkarm_loc, label, img_name):
    # Invoke darknet and retrieve the left/right/up/bot
    # coordinates of the detect rectangle.
    cfg_loc = darknet_loc + "cfg/"
    weights_loc = darknet_loc + "weights/"
    data_loc = darkarm_loc + "inbox/"
    dark_cmd = (darknet_loc + "darknet detector test " + label + " " +
                cfg_loc + "coco.data " + cfg_loc + "yolov3.cfg " +
                weights_loc + "yolov3.weights " + data_loc + img_name + ".jpg")

    process = subprocess.Popen(dark_cmd.split(), stdout=subprocess.PIPE)
    output, _err = process.communicate()

    return output # Need to test the ouput to see what it looks like, then parse.


def compute_center(cord):
    # From the coordinates, get the rectangle center
    rect_center = []
    rect_center.append(cord['xlft'] + int((cord['xrght'] - cord['xlft'])/2))
    rect_center.append(cord['ylft'] + int((cord['yrght'] - cord['ylft'])/2))
    return rect_center


def get_translation_vec(img, rect_center):
    # Get the translation vector from center
    height, width, _chan = img.shape
    transl_x = int(width / 2) - rect_center[0]
    transl_y = int(height / 2) - rect_center[1]
    return transl_x, transl_y
