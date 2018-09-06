# pylint: disable=missing-docstring
import socket
import os
import inspect
import subprocess


def init_environ_folder():
    """Return necessary capture_loc based on environ.

    Variable capture_loc is used to determine where frames captured
    by the Camera class resides. It relies on an ENV parameter, called
    AWS_FACEDETECT_FOLDER.

    Args:
        capture_loc: Optional string defining the capture loc.

    Returns:
        The capture_loc string defining where frames taken by the Camera
        class reside.
    """

    stackp = inspect.stack()[1]
    module = inspect.getmodule(stackp[0])
    caller_filename = module.__file__

    if caller_filename == 'main_client.py':
        capture_loc = os.path.join(os.environ['DARKARM_CAPTURE_FOLDER'])
        return capture_loc

    darkarm_loc = os.environ['DARKARM_FOLDER']
    inbox_loc = os.environ['DARKARM_INBOX_FOLDER']

    return darkarm_loc, inbox_loc


def init_client_socket(address, port=5000):
    """Initialize client socket.

    Args:
        address: string representing the IP address to connect to.
        port: Optional int representing the port to connect to.

    Returns:
        A client socket where the program can start sending messages.
    """

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((address, port))

    return client_socket


def init_server_socket(address=None, port=5000):
    """Initialize server socket.

    Args:
        address: Optional string representing the IP address to bind to.
        port: Optional int representing the port to connect to.

    Returns:
        A server socket where the program can receive messages.
    """

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if address is None:
        cmd = (r"ip addr show | awk '$1 ~ /^inet$/ { print $2 }' "
               r"| sed 's/\/[0-9]*//g' | grep -v '127.0.0.1' -m1"
              )
        ip_raw = subprocess.check_output([cmd], shell=True)
        address = ip_raw.decode('utf-8')[:-1]
    server_socket.bind((address, port))

    return server_socket


def receive_bytes_to_string(client_sock):
    """Convert incoming messages from bytes to str.

    Receives message first, then do the byte to str translation.

    Args:
        client_sock: A socket instance representing the client socket.

    Returns:
        None
    """

    byte_msg = client_sock.recv(1024)
    str_msg = byte_msg.decode('utf-8').replace("\n", "")

    return str_msg


def send_frame_size(client_socket, frame_loc):
    """Send frame size to client.

    Function useful for the server since it will use this result to compute
    frame size and bytes reception accordingly. With this number, a
    server can exactly knows how many bytes to expect from a stream flow in
    order to fully receive a frame.

    Args:
        client_socket: A socket instance, used for client/server interactions.
        frame_loc: A string representing the frame location to compute and
        send size from.

    Returns:
        None
    """

    filesize = os.path.getsize(frame_loc)
    client_socket.send(str(filesize).encode('ascii'))


def send_frame(client_socket, frame_loc):
    """Send frame to client.

    Send one frame to the client, but wait for sleep seconds before sending
    it. Sleep parameter is useful when a lot of frames are sent in a row,
    in order to avoid broken pipe with the server, when the other end
    cannot keep up the rythm.

    Args:
        client_socket: A socket instance, used for client/server interactions.
        frame_loc: A string representing the frame location.
        sleep: Optional float representing the number of second to wait
        before sending.

    Returns:
        None
    """

    with open(frame_loc, 'rb') as filedesc:
        buf = filedesc.readline(1024)
        while buf:
            client_socket.send(buf)
            buf = filedesc.readline(1024)
        filedesc.close()


def receive_frame(client_sock, frame_size, save_loc):
    """Receive and save one frame.

    Main function responsible for storing and saving exactly one frame from
    a remote client. In order to properly delimitate a frame from a stream,
    the function also takes the frame size as a parameter and compute the
    necessary incoming byte number to expect.

    Args:
        client_sock: A socket instance representing a client connection.
        frame: An int representing the frame number to receive.
        frame_size: An int representing the frame size to expect.
        img_loc: A string representing the destination where to save the
        frame

    Returns:
        None
    """
    img_size = 0
    filename = save_loc + ".jpg"
    with open(filename, 'wb') as img:
        while img_size < frame_size:
            remain = frame_size - img_size
            if remain < 1024:
                data = client_sock.recv(remain)
            else:
                data = client_sock.recv(1024)
            img.write(data)
            img_size += len(data)


def waiting_for_ack(client_socket, exptype='FRAME'):
    """Wait for a particular frame/message to be acked by server.

    Client expects a message of the form 'OK FRAME X' from the server,
    where X is the frame number waiting to be ack'ed.

    Args:
        client_socket: A socket instance, used for client/server interactions.
        frame: An int representing the current frame number waiting to be
        ack'ed.

    Returns:
        None
    """

    msg = client_socket.recv(1024).decode('UTF-8')
    while msg != 'OK ' + exptype:
        msg = client_socket.recv(1024).decode('UTF-8')


def send_msg(client_sock, msg):
    """Send ACK for the frame to the client.

    Client expects a message of the form 'OK FRAME X' from the server,
    where X is the frame number wainting to be ack'ed.

    Args:
        client_sock: A socket instance representing the client connection.
        frame: An int representing the frame number to ack.

    Returns:
        None
    """

    client_sock.send((str(msg)).encode('ascii'))
