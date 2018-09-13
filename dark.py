"""
Module supporting various functions responsible for interacting with Darknet
and getting output results from it.

function get_detection_output: Get a string representing detection coordinates.

function parse_detection_output: Get a dict representing a parsed string.

function compute_center: With a rectangle, compute its center.

function get_translation_vec: Get the distance in px between a point and the
image center.
"""

import subprocess
import cv2


def get_detection_output(darkarm_loc, inbox_loc, label, img_name):
    """Invoke darknet and retrieve the left/right/up/bot coordinates of the
    detected rectangle.

    Relies on the external program darknet to function. Also needs a label to
    know what type of object to detect.

    Args:
        darkarm_loc: A string representing the project location.
        inbox_loc: A string representing the inbox location.
        label: A string representing a label name.
        img_name: A string representing an image name.

    Returns:
        A string representing the coordinate of the detection rectangle.
    """

    darknet_loc = darkarm_loc + "darknet/"
    dark_cmd = ("./darknet " + "detector test " + label + " " +
                "cfg/coco.data " + "cfg/yolov3.cfg " +
                "weights/yolov3.weights " + inbox_loc + img_name + ".jpg")

    output = subprocess.check_output(dark_cmd.split(), cwd=darknet_loc)

    return output


def parse_detection_output(output):
    """Parse output items and put them in a dictionary

    Args:
        output: A string representing rectangle coordinates.

    Returns:
        A dict representing rectangle coordinates.
    """

    str_output = output
    item_list = str_output.split()
    dic = {}
    for items in item_list:
        dic[items.split(":")[0]] = int(items.split(":")[1])

    return dic


def compute_center(cord):
    """From the coordinates dict, get the rectangle center.

    Args:
        cord: A dict representing the rectangle coordinates.

    Returns:
        A list representing the pixel coordinates of the rectangle center.
    """

    rect_center = []
    rect_center.append(cord['left'] + int((cord['right'] - cord['left'])/2))
    rect_center.append(cord['top'] + int((cord['bot'] - cord['top'])/2))

    return rect_center


def get_translation_vec(img_path, rect_center):
    """Get the translation vector from center.

    Args:
        img_path: A string representing the image path.
        rect_center: A list representing a point coordinates.

    Returns:
       A tuple representing the translation on x and y axis from the point
       coordinate to the image center.
    """

    img = cv2.imread(img_path)
    height, width, _chan = img.shape
    transl_x = int(width / 2) - rect_center[0]
    transl_y = int(height / 2) - rect_center[1]

    return transl_x, transl_y
