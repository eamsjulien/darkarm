"""
Main handler for the EOP_Sockets server component.

Usage: python3 main.py [--sleep SLEEP]
"""

import argparse

import socks
import dark

def main(): # pylint: disable=too-many-statements
    """Main function for server loop."""

    # PYTHON PARSER VIA ARGPARSE #

    parser = argparse.ArgumentParser(description="DarkArm Client Main.")
    parser.add_argument("-l", "--label", help="Label string.",
                        nargs='?', default='person', type=str)
    args = vars(parser.parse_args())

    label = args['label']

    # DARKARM SERVER #

    print(" ------------------")
    print("| DARKARM - SERVER |")
    print(" ------------------")

    print("\n Initializing ENV variables...", end='')
    darkarm_loc, inbox_loc = socks.init_environ_folder()
    print("Done!")

    print("\n Initializing server socket...", end='')
    server_socket = socks.init_server_socket()
    print("Done!")

    server_socket.listen(5)
    print("\nWaiting for incoming connection...")
    client, addr = server_socket.accept()
    print("Incoming connection from " + str(addr))

    print("\n **** RECEIVING FRAME ****")

    frame_size = int(socks.receive_bytes_to_string(client))
    socks.send_msg(client, 'OK FRAME')
    socks.receive_frame(client, frame_size, inbox_loc)
    print("Frame  received.")

    print("Label detection...")
    vect = {}
    output = dark.get_detection_output(darkarm_loc, inbox_loc, label, 'frame')
    rect_center = dark.compute_center(dark.parse_detection_output(output))
    coord = dark.get_translation_vec(inbox_loc + "frame.jpg", rect_center)
    vect['xval'] = coord[0]
    vect['yval'] = coord[1]

    print("Sending ack...", end='')
    socks.send_msg(client, 'OK FRAME')
    print("Sent.")

    print("\nFrame processing completed!")

    print("\n **** SENDING VECTOR ****")
    socks.send_msg(client, vect)

    print("\nVector sent!")

    print("Closing sockets...", end='')
    client.close()
    server_socket.close()
    print("Done!")

    print("\n ------------------------")
    print("| DARKARM SERVER - GOODBYE |")
    print(" --------------------------")

if __name__ == '__main__':
    main()
