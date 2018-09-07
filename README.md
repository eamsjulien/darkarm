# DarkArm

Simple OpenCV / Darknet project to remotely move a robotic arm based on label detection thanks to [darknet](https://github.com/pjreddie/darknet).

DarkArm consists of two parts: the client and the server. Both parts are also divided in two distinct components. Client part includes camera and socket component and server part includes label detection and socket component as well.

With the client part, one user can send an arbitrary number of frames (hence a video) to the server. The client does not need a public IP, only internet connectivity is enough. The robotic arm (client) has a jetson installed with it, with Intel Realsense as a webcam for depth detection.

With the server part, a host, typically a cloud instance such as AWS, can receive incoming frames from a client and perform some simple label detection on them. A modified version of darknet, available [here](https://github.com/julienstark/darknet) is needed to get this one working. After the detection is made, vector coordinates are sent to the robotic arm (client) so it can moves and eventually grep the detected label.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Implementation also requires the modified [darknet](https://github.com/julienstark/darknet) project to be installed on the server and in the same directory as the darkarm one.

### Prerequisites

What things you need to install the software and how to install them. Python3 libraries are in requirements.txt for easy installation with pip.

#### Client Prerequisites

- Linux >= 4.17.11
- Bash >= 4.4.23
- Python >= 3.7.0
- Numpy >= 1.15.0
- opencv-python >= 3.4.2.17
- pyrealsense2

Earlier program/package versions might work too but haven't been tested. Numpy/opencv-python are required dependencies for the current implementation but minimal changes should be required to adapt the videocapture to a more lightweight backend.

#### Server Prerequisites

- Linux >= 4.14.59
- Bash >= 4.2.46
- Python >= 3.7.0
- Numpy >= 1.15.0
- opencv-python >= 3.4.2.17
- [modified darknet](https://github.com/julienstark/darknet)

### Installing

A step by step series of examples that tell you how to get a development env running.

#### Client Installation

Simply clone the repository.

```bash
git clone https://github.com/julienstark/darkarm.git
```

And that's it !

#### Server Installation

Clone the repository.

```bash
git clone https://github.com/julienstark/darkarm.git
```

Get and compile the modified [modified darknet](https://github.com/julienstark/darknet) in the same directory as the darkarm one.
And good to go !

### Running

This section will introduce a quick way to get the client and server running and to receive/process frames.  
- On the server, in the darkarm folder:

```bash
./launch.sh --mode server --label "label-to-detect"
```

Replace "label-to-detect" by the label you wish to detect. Available labels are in the darknet folder > cfg/coco.names.

- On the client, in the darkarm folder:

```bash
./launch.sh --mode client --address "pub-ip-address-of-your-server"
```

Replace the address by your server IP address.
