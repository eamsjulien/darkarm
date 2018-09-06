"""
Main handler for the client component.

Usage: python3 main_client.py --address ADDRESS [--frames FRAMES]
                             [--sleep SLEEP] [--rate RATE]
"""


import argparse

import socks
import dark
from camera import Camera

def main(): #pylint: disable=too-many-locals, too-many-statements
    """Main function for client loop."""

    # PYTHON PARSER VIA ARGPARSE #

    parser = argparse.ArgumentParser(description="AWS FaceDetect Client Main.")
    parser.add_argument("-a", "--address", required=True,
                        help="Address to connect to.", type=str)
    args = vars(parser.parse_args())

    server_addr = args['address']

    # FACEDETECT CLIENT #

    print(" ------------------")
    print("| DARKARM - CLIENT |")
    print(" ------------------")

    print("\n Initializing ENV variables...", end='')
    capture_loc = socks.init_environ_folder()
    print("Done!")

    print("\n Initializing server socket...", end='')
    client_socket = socks.init_client_socket(server_addr)
    print("Done!")

    print("\n **** CAPTURING FRAME ****")
    cam = Camera(path=capture_loc)
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

    recv_string = socks.receive_bytes_to_string(client_socket)
    vector = dark.parse_detection_output(recv_string)

    print("\nVector received!")

    print("Vector is: " + str(vector))

    print("\n ------------------------")
    print("| DARKARM CLIENT - GOODBYE |")
    print(" --------------------------")


if __name__ == '__main__':
    main()
