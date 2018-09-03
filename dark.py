# pylint: disable=missing-docstring
import subprocess


def get_detection_output(darkarm_loc, label, img_name):
    # Invoke darknet and retrieve the left/right/up/bot
    # coordinates of the detect rectangle.
    data_loc = darkarm_loc + "inbox/"
    darknet_loc = darkarm_loc + "darknet/"
    dark_cmd = ("./darknet " + "detector test " + label + " " +
                "cfg/coco.data " + "cfg/yolov3.cfg " +
                "weights/yolov3.weights " + data_loc + img_name + ".jpg")

    output = subprocess.check_output(dark_cmd.split(), cwd=darknet_loc)

    return output


def parse_detection_output(output):
    # Parse output items and put them in a dictionary
    str_output = output.decode('utf-8')
    item_list = str_output.split()
    dic = {}
    for items in item_list:
        dic[items.split(":")[0]] = int(items.split(":")[1])

    return dic


def compute_center(cord):
    # From the coordinates, get the rectangle center
    rect_center = []
    rect_center.append(cord['left'] + int((cord['right'] - cord['left'])/2))
    rect_center.append(cord['top'] + int((cord['bot'] - cord['top'])/2))

    return rect_center


def get_translation_vec(img, rect_center):
    # Get the translation vector from center
    height, width, _chan = img.shape
    transl_x = int(width / 2) - rect_center[0]
    transl_y = int(height / 2) - rect_center[1]

    return transl_x, transl_y
