"""
Main handler for the client component.

Usage: python3 main_client.py --address ADDRESS [--frames FRAMES]
                             [--sleep SLEEP] [--rate RATE]
"""


import os
import argparse
import time

import socks
import dark
import mymath
import PID
from camera import Camera
# from dynamixel_sdk import *


Z_AXIS = 150
X_ROT = 0
Y_ROT = 0
Z_ROT = 0
STEPINCREMENT = 5
STARTINVX = True


def main(): #pylint: disable=too-many-locals, too-many-statements
    """Main function for client loop."""

    # PYTHON PARSER VIA ARGPARSE #

    parser = argparse.ArgumentParser(description="DarkArm Client Main.")
    parser.add_argument("-a", "--address", required=True,
                        help="Address to connect to.", type=str)
    args = vars(parser.parse_args())

    server_addr = args['address']

    # PID / ROBOT PARAMS

    pid_x = PID.PID(0.1, 0, 0.02)
    pid_x.SetPoint = 0
    pid_x.setWindup = 1

    mymath.RobotArmAwake()
    mymath.StandByPos()
    mymath.MoveRobot(100, 250)

    # DARKARM CLIENT #

    print(" ------------------")
    print("| DARKARM - CLIENT |")
    print(" ------------------")

    print("\n Initializing ENV variables...", end='')
    capture_loc = socks.init_environ_folder()
    print("Done!")

    print("\n Initializing instance variables...", end='')
    cam = Camera(path=capture_loc)
    print("Done!")

    print("| ITERATION LOOP |")

    for _count in range(2):

        print("\n Initializing server socket...", end='')
        client_socket = socks.init_client_socket(server_addr)
        print("Done!")

        print("\n **** CAPTURING FRAME ****")
        cam.capture()
        print("Frame captured!")

        print("\n **** SENDING FRAME ****")
        frame_loc = capture_loc + "frame.jpg"
        socks.send_frame_size(client_socket, frame_loc)
        socks.waiting_for_ack(client_socket)
        socks.send_frame(client_socket, frame_loc)
        print("Done.")
        print("Waiting for frame reception...", end='')
        socks.waiting_for_ack(client_socket)
        print("ACK")

        print("\nFrame sent!")

        print("\n **** RECEIVING VECTOR ****")

        socks.send_msg(client_socket, "OK VECT")
        recv_string = socks.receive_bytes_to_string(client_socket)
        recv_string = recv_string.replace(", ", " ").replace(": ", ":")
        recv_string = recv_string.strip("{}").replace("'", "")
        os.remove(frame_loc)

        print("\nVector received!")

        if recv_string != "":
            vector = dark.parse_detection_output(recv_string)
            print("Received vector: " + str(recv_string))

            error = vector['xval']
            pid_x.update(error)
            output = pid_x.output
            print("Engine movement: " + str(output))
            mymath.MoveRobot(100, 250)
        else:
            print("No output detected from classifier.")

        time.sleep(2) # Give some air for the arm to replace itself.

    mymath.RobotArmGoHome() # Put the arm in its original position.

    print("\n ------------------------")
    print("| DARKARM CLIENT - GOODBYE |")
    print(" --------------------------")


if __name__ == '__main__':
    main()
