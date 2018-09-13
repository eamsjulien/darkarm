# Test servo with Maestro 

import time
from dynamixel_sdk import *                    # Uses Dynamixel SDK library
import numpy
import math

print("yo yo what's up")

####################################################### Set Servo Configuration #############################################################
# Control table address
ADDR_PRO_TORQUE_ENABLE      = 64               # Control table address is different in Dynamixel model
ADDR_PRO_GOAL_POSITION      = 116
ADDR_PRO_PRESENT_POSITION   = 132

ADDR_PRO_CURRENT_LIMIT      = 38
ADDR_PRO_GOAL_CURRENT       = 102
ADDR_PRO_PRESENT_CURRENT    = 126 

ADDR_PRO_OPERATING_MODE     = 11

ADDR_PRO_GOAL_VELOCITY      = 104

ADDR_PRO_ACCELERATION_LIMIT = 40
ADDR_PRO_VELOCITY_LIMIT     = 44
ADDR_PRO_PROFILE_ACCELERATION  = 108
ADDR_PRO_PROFILE_VELOCITY   = 112

ADDR_PRO_POSITION_D_GAIN    = 80
ADDR_PRO_POSITION_I_GAIN    = 82
ADDR_PRO_POSITION_P_GAIN    = 84
ADDR_PRO_FEEDFORWARD_2nd_GAIN = 88
ADDR_PRO_FEEDFORWARD_1st_GAIN = 90

ADDR_PRO_MOVING             = 122
ADDR_PRO_MOVING_STATUS       = 123

CURRENT_CONTROL                     = 0
POSITION_CONTROL                    = 3 # Default
CURRENT_BASED_POSITION_CONTROL      = 5
# Protocol version
PROTOCOL_VERSION            = 2.0               # See which protocol version is used in the Dynamixel

# Default setting
DXL1_ID                      = 1                             # Dynamixel ID: 1
DXL2_ID                      = 2                             # Dynamixel ID: 2
DXL3_ID                      = 3                             # Dynamixel ID: 3
DXL4_ID                      = 4
DXL5_ID                      = 5
DXL6_ID                      = 6
DXL7_ID                      = 7

BAUDRATE                    = 57600             # Dynamixel default baudrate : 57600
DEVICENAME                  = '/dev/ttyUSB0'    # Check which port is being used on your controller
                                                # ex) Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*"
TORQUE_ENABLE               = 1                 # Value for enabling the torque
TORQUE_DISABLE              = 0                 # Value for disabling the torque

# Initialize PortHandler instance
# Set the port path
# Get methods and members of PortHandlerLinux or PortHandlerWindows
portHandler = PortHandler(DEVICENAME)

# Initialize PacketHandler instance
# Set the protocol version
# Get methods and members of Protocol1PacketHandler or Protocol2PacketHandler
packetHandler = PacketHandler(PROTOCOL_VERSION)

# Open port
if portHandler.openPort():
    print("Succeeded to open the port")
else:
    print("Failed to open the port")
    print("Press any key to terminate...")
    getch()
    quit()


# Set port baudrate
if portHandler.setBaudRate(BAUDRATE):
    print("Succeeded to change the baudrate")
else:
    print("Failed to change the baudrate")
    print("Press any key to terminate...")
    getch()
    quit()


# When need to change mode just remove block comment out
# Disable Dynamixel Torque 1
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 1 has been successfully connected")
# Disable Dynamixel Torque 2   
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 2 has been successfully connected")
# Disable Dynamixel Torque 3
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 3 has been successfully connected")
# Disable Dynamixel Torque 4
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 4 has been successfully connected")
# Disable Dynamixel Torque 5   
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 5 has been successfully connected")
# Disable Dynamixel Torque 6
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Dynamixel 6 has been successfully connected")

    # Check Operating Mode
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_OPERATING_MODE, POSITION_CONTROL)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_OPERATING_MODE, CURRENT_BASED_POSITION_CONTROL)


present_mode, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_OPERATING_MODE)
if present_mode == 0:
    # Current (Torque) Control Mode
    print("Now Operating Mode is Torque Control")
elif present_mode == 3:
    # Position Control Mode
    print("Now Operating Mode is Position Control")
elif present_mode == 5:
    # Current-based Position Control Mode
    print("Now Operating Mode is Current-based Position Control")
else:
    print("In other Mode that didn't set!")

'''
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)

if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Torque is enable")
'''
######################### Set Velocity / Acceleration Profile  ##############################
set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
set_V_Limit = 350       # 350 Default                  [0.229RPM]

set_A_PRFL = 15      # between 0 ~ set_A_limit      [214.577 rev/min^2]
set_V_PRFL = 30      # between 0 ~ set_V_Limit      [0.229RPM]

set_A_PRFL_Gripper = 70      # between 0 ~ set_A_limit      [214.577 rev/min^2]
set_V_PRFL_Gripper = 120      # between 0 ~ set_V_Limit      [0.229RPM]

dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL_Gripper))
dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL_Gripper))

acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_ACCELERATION_LIMIT)
velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_VELOCITY_LIMIT)
#print("Initial Position: %f" %start_pos)
#print("Final Position: %f" %final_pos)
#print("Travel time: %d" %t3)
print("V PRFL: %f" %set_V_PRFL)
print("A PRFL: %f" %set_A_PRFL)
print("Acceleration Limited: %d" %acceleration_limit)
print("Velocity Limited: %d" %velocity_limit)
print("--------------------------------")

######################### Set PID Gain Position Loop  ##############################
set_P_Gain = 1000    #800 default
set_I_Gain = 20     #0 default
set_D_Gain = 1000   #4700 default

set_P_Gain_Gripper = 1000
set_I_Gain_Gripper = 30
set_D_Gain_Gripper = 2000

dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_P_GAIN, set_P_Gain_Gripper)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_I_GAIN, set_I_Gain_Gripper)
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_D_GAIN, set_D_Gain_Gripper)
print("PID's Gain are set")

position_D_gain, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_D_GAIN)
position_I_gain, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_I_GAIN)
position_P_gain, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_POSITION_P_GAIN)

position_D_gain_Gripper, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_D_GAIN)
position_I_gain_Gripper, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_I_GAIN)
position_P_gain_Gripper, dxl_comm_result, dxl_error = packetHandler.read2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_POSITION_P_GAIN)

print("Robot PID Parameters")
print("Position P Gain: %d" %position_P_gain)
print("Position I Gain: %d" %position_I_gain)
print("Position D Gain: %d" %position_D_gain)
print("--------------------------------")
print("Gripper PID Parameters")
print("Gripper P Gain: %d" %position_P_gain_Gripper)
print("Gripper I Gain: %d" %position_I_gain_Gripper)
print("Gripper D Gain: %d" %position_D_gain_Gripper)
print("--------------------------------")
######################### Set Goal Current  ##############################
SetCur = 60
dxl_comm_result, dxl_error = packetHandler.write2ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_GOAL_CURRENT, SetCur)
if dxl_comm_result != COMM_SUCCESS:
    print("%s" % packetHandler.getTxRxResult(dxl_comm_result))
elif dxl_error != 0:
    print("%s" % packetHandler.getRxPacketError(dxl_error))
else:
    print("Goal Current is set")
print("--------------------------------")

print("Ready to go....")
time.sleep(2)

def rc_map(x,in_min,in_max,out_min,out_max):
    result = (x - in_min)*(out_max - out_min) / (in_max - in_min) + out_min
    return result

def map(val, in_min, in_max, out_min, out_max):

    return (val - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def RobotArmINV(qx,qy,qz,x6_rot,y6_rot,z6_rot):

    rad2deg = 180/math.pi
    deg2rad = math.pi/180
    pi = math.pi
    ########################## parameters ################################
    a1 = 0
    d1 = 0
    alp1 = pi/2

    a2 = 216
    d2 = 0
    alp2 = 0

    a3 = 74
    d3 = 0
    alp3 = pi/2

    a4 = 0
    d4 = 142
    alp4 = -pi/2

    a5 = 0
    d5 = 0
    alp5 = pi/2

    a6 = 0
    d6 = 200
    alp6 = 0

    '''
    qx = 200
    qy = 300
    qz = 150

    x6_rot = 0
    y6_rot = 0
    z6_rot = 0
    '''

    rr = x6_rot*deg2rad
    pp = y6_rot*deg2rad
    yy = z6_rot*deg2rad

    E11 = math.cos(yy)*math.cos(pp)
    E12 = math.cos(yy)*math.sin(pp)*math.sin(rr)-math.cos(rr)*math.sin(yy)
    E13 = math.sin(rr)*math.sin(yy)+math.cos(rr)*math.cos(yy)*math.sin(pp)

    E21 = math.cos(pp)*math.sin(yy)
    E22 = math.cos(rr)*math.cos(yy) + math.sin(rr)*math.sin(yy)*math.sin(pp)
    E23 = math.cos(rr)*math.sin(yy)*math.sin(pp)-math.cos(yy)*math.sin(rr)

    E31 = -math.sin(pp)
    E32 = math.cos(pp)*math.sin(rr)
    E33 = math.cos(rr)*math.cos(pp)

    TCP = numpy.matrix([[E11,E12,E13],[E21,E22,E23],[E31,E32,E33]])

    r = 180*deg2rad
    p = -90*deg2rad
    y = 90*deg2rad

    psi = y
    theta = p
    phi = r

    F11 = math.cos(psi)*math.cos(theta)
    F12 = math.cos(psi)*math.sin(phi)*math.sin(theta)-math.cos(phi)*math.sin(psi)
    F13 = math.sin(phi)*math.sin(psi)+math.cos(phi)*math.cos(psi)*math.sin(theta)

    F21 = math.cos(theta)*math.sin(psi)
    F22 = math.cos(phi)*math.cos(psi) + math.sin(phi)*math.sin(psi)*math.sin(theta)
    F23 = math.cos(phi)*math.sin(psi)*math.sin(theta)-math.cos(psi)*math.sin(phi)

    F31 = -math.sin(theta)
    F32 = math.cos(theta)*math.sin(phi)
    F33 = math.cos(phi)*math.cos(theta)

    RPY = numpy.matrix([[F11,F12,F13],[F21,F22,F23],[F31,F32,F33]])

    RPY_TCP = RPY*TCP

    ux = RPY_TCP[0,0]
    uy = RPY_TCP[1,0]
    uz = RPY_TCP[2,0]

    vx = RPY_TCP[0,1]
    vy = RPY_TCP[1,1]
    vz = RPY_TCP[2,1]

    wx = RPY_TCP[0,2]
    wy = RPY_TCP[1,2]
    wz = RPY_TCP[2,2]

    px = qx - d6*wx
    py = qy - d6*wy
    pz = qz - d6*wz


    ################################ Find q1 #####################################
    q1 = math.atan(py/px)

    if ((q1 <= pi) and (q1 >= 0)):
        q1_1 = q1
        q1_2 = q1 + pi
    else:
        q1_1 = q1 + pi
        q1_2 = q1
        q1 = q1 + pi
    '''
    if q1_1 < 0.000001:
        q1_2 = 0

    if q1_2 < 0.000001:
        q1_2 = 0
    '''
    deg1 = [None]*2
    deg1 = numpy.array([q1_1, q1_2])*rad2deg



    #print(q1)

    ################################ Find q3 #####################################
    k1 = 2*a2*d4
    k2 = 2*a2*a3
    k3 = px**2 + py**2 + pz**2 - 2*px*a1*math.cos(q1) - 2*py*a1*math.sin(q1) + a1**2 - a2**2 - a3**2 - d4**2
 
    q3_1 = 2*math.atan( (k1+ math.sqrt(k1**2 + k2**2 - k3**2)) / (k3+k2) )
    q3_2 = 2*math.atan( (k1- math.sqrt(k1**2 + k2**2 - k3**2)) / (k3+k2) )

    '''
    if q3_1 < 0.000001:
        q3_1 = 0
    if q3_2 < 0.000001:
        q3_2 = 0
    '''
    q3 = [None]*2
    q3 = numpy.array([q3_1,q3_2])


    #print(q3)
    deg3 = [None]*2
    deg3 = numpy.array([q3[0],q3[1]])*rad2deg

    ################################ Find q2 #####################################

    #print("----------------")

    uu1_0 = a2 + a3*math.cos(q3[0])+d4*math.sin(q3[0])
    vv1_0 = -a3*math.sin(q3[0]) + d4*math.cos(q3[0])
    yy1_0 = px*math.cos(q1) + py*math.sin(q1) - a1
    uu2_0 = a3*math.sin(q3[0]) - d4*math.cos(q3[0])
    vv2_0 = a2 + a3*math.cos(q3[0]) + d4*math.sin(q3[0])
    yy2_0 = pz

    uu1_1 = a2 + a3*math.cos(q3[1])+d4*math.sin(q3[1])
    vv1_1 = -a3*math.sin(q3[1]) + d4*math.cos(q3[1])
    yy1_1 = px*math.cos(q1) + py*math.sin(q1) - a1
    uu2_1 = a3*math.sin(q3[1]) - d4*math.cos(q3[1])
    vv2_1 = a2 + a3*math.cos(q3[1]) + d4*math.sin(q3[1])
    yy2_1 = pz


    A0 = numpy.array([[uu1_0,vv1_0],[uu2_0,vv2_0]])
    B0 = numpy.array([yy1_0,yy2_0])
    X0 = numpy.linalg.solve(A0,B0)

    A1 = numpy.array([[uu1_1,vv1_1], [uu2_1,vv2_1]])
    B1 = numpy.array([yy1_1,yy2_1])
    X1 = numpy.linalg.solve(A1,B1)

    cq2_1 = X0[0]
    sq2_1 = X0[1]
    cq2_2 = X1[0]
    sq2_2 = X1[1]

    q2 = [None]*2
    q2[0] = math.atan2(sq2_1,cq2_1)
    q2[1] = math.atan2(sq2_2,cq2_2)
    '''
    if q2[0] < 0.000001:
        q2[0] = 0
    if q2[1] < 0.000001:
        q2[1] = 0
    '''
    deg2 = [None]*2
    deg2 = numpy.array([q2[0],q2[1]])*rad2deg

    #print(q2)
    #print(deg2)

    ################################ Find q5 #####################################

    r33 = [None]*2
    r33[0] = wx*math.cos(q1)*math.sin(q2[0]+q3[0]) + wy*math.sin(q1)*math.sin(q2[0]+q3[0]) - wz*math.cos(q2[0]+q3[0])
    r33[1] = wx*math.cos(q1)*math.sin(q2[1]+q3[1]) + wy*math.sin(q1)*math.sin(q2[1]+q3[1]) - wz*math.cos(q2[1]+q3[1])
    #print(r33)
    q5 = [None]*2
    q5[0] = math.acos(r33[0])
    q5[1] = math.acos(r33[1])
    '''
    if q5[0] < 0.000001:
        q5[0] = 0
    if q5[1] < 0.000001:
        q5[1] = 0
    '''
    deg5 = [None]*2
    deg5 = numpy.array([q5[0],q5[1]])*rad2deg

    #print("----------------")
    #print(q5)
    #print(deg5)

    ################################ Find q4 #####################################
    cq4 = [None]*2
    sq4 = [None]*2
    q4 = [None]*2
    deg4 = [None]*2

    if (abs(r33[1]) < 1):
        # Normal Condition
        cq4[0] = (  wx*math.cos(q1)*math.cos(q2[0]+q3[0]) + wy*math.sin(q1)*math.cos(q2[0]+q3[0]) + wz*math.sin(q2[0]+q3[0]) ) / math.sin(q5[0])
        cq4[1] = (  wx*math.cos(q1)*math.cos(q2[1]+q3[1]) + wy*math.sin(q1)*math.cos(q2[1]+q3[1]) + wz*math.sin(q2[1]+q3[1]) ) / math.sin(q5[1])
        sq4[0] = ( wx*math.sin(q1) - wy*math.cos(q1) )/ math.sin(q5[0])
        sq4[1] = ( wx*math.sin(q1) - wy*math.cos(q1) )/ math.sin(q5[1])

        q4[0] = math.atan2(sq4[0],cq4[0])
        q4[1] = math.atan2(sq4[1],cq4[1])
    elif abs(r33[1]) == 1:
        # When q5 = 0
        q4[0] = 0
        q4[1] = 0

    else:
        print("|r33| > 1 : cannotr physically arise")
    '''
    if q4[0] < 0.000001:
        q4[0] = 0
    if q4[1] < 0.000001:
        q4[1] = 0
    '''
    deg4 = numpy.array([q4[0],q4[1]])*rad2deg
    #print("-----------------")
    #print(q4)
    #print(deg4)

    ################################ Find q6 #####################################
    cq6 = [None]*2
    sq6 = [None]*2
    q6 = [None]*2
    deg6 = [None]*2

    if (abs(r33[1]) < 1):
        # Normal Condition
        cq6[0] = -(ux*math.cos(q1)*math.sin(q2[0]+q3[0]) + uy*math.sin(q1)*math.sin(q2[0]+q3[0]) - uz*math.cos(q2[0]+q3[0]) ) / math.sin(q5[0])
        cq6[1] = -(ux*math.cos(q1)*math.sin(q2[1]+q3[1]) + uy*math.sin(q1)*math.sin(q2[1]+q3[1]) - uz*math.cos(q2[1]+q3[1]) ) / math.sin(q5[1])
        sq6[0] = (vx*math.cos(q1)*math.sin(q2[0]+q3[0]) + vy*math.sin(q1)*math.sin(q2[0]+q3[0]) - vz*math.cos(q2[0]+q3[0]) ) / math.sin(q5[0])
        sq6[1] = (vx*math.cos(q1)*math.sin(q2[1]+q3[1]) + vy*math.sin(q1)*math.sin(q2[1]+q3[1]) - vz*math.cos(q2[1]+q3[1]) ) / math.sin(q5[1])

        q6[0] = math.atan2(sq6[0],cq6[0])
        q6[1] = math.atan2(sq6[1],cq6[1])
    elif abs(r33[1]) == 1:
        # When q5 = 0
        q6[0] = 0
        q6[1] = 0
    else:
        print("|r33| > 1 : cannotr physically arise")
    '''
    if q6[0] < 0.000001:
        q6[0] = 0
    if q6[1] < 0.000001:
        q6[1] = 0
    '''
    deg6 = numpy.array([q6[0],q6[1]])*rad2deg
    #print("-----------------")
    #print(q6)
    #print(deg6)

    DEG_INV = [None]*6
    DEG_INV = numpy.array([deg1[0],deg2[1],deg3[1],deg4[1],deg5[1],deg6[1]])
    ServoAng1 = DEG_INV[0]+90
    ServoAng2 = DEG_INV[1]+90
    ServoAng3 = DEG_INV[2]+180
    ServoAng4 = DEG_INV[3]+180
    ServoAng5 = DEG_INV[4]+180
    ServoAng6 = DEG_INV[5]+180
    ServoANG = [None]*6
    ServoANG = numpy.array([ServoAng1,ServoAng2,ServoAng3,ServoAng4,ServoAng5,ServoAng6])

    return ServoANG

def DeltaPos(pre_pos,goal_pos):
    if pre_pos > 360 or goal_pos > 360:
        print("Input position is over than 360!")
        return 0
    else:
        pre_pos_pul = map(pre_pos,0.0,360.0,0.0,4095.0)
        pre_pos_pul = int(pre_pos_pul)
        goal_pos_pul = map(goal_pos,0.0,360.0,0.0,4095.0)
        goal_pos_pul = int(goal_pos_pul)

        delta_pos = abs(goal_pos_pul - pre_pos_pul)

        return delta_pos

def TrajectoryGeneration3(Vstd,Astd,DelPos1,DelPos2,DelPos3,DelPos4,DelPos5,DelPos6):
    DelPos = [DelPos1, DelPos2, DelPos3, DelPos4, DelPos5, DelPos6]
    MIN = min(DelPos)
    MAX = max(DelPos)

    V_Lim = 150
    A_Lim = 80

    ## If no travel distance for every servos, return a slow speed profile
    if DelPos1 <= 1 and DelPos2 <= 1 and DelPos3 <= 1 and DelPos4 <= 1 and DelPos5 <= 1 and DelPos6 <= 1:
        V1 = 20
        A1 = 5
        V2 = 20
        A2 = 5
        V3 = 20
        A3 = 5
        V4 = 20
        A4 = 5
        V5 = 20
        A5 = 5
        V6 = 20
        A6 = 5
        print("Low travel distance...")
        return V1, A1, V2, A2, V3, A3, V4, A4, V5, A5, V6, A6
    ## If V and A input are over the limit
    if Vstd >= V_Lim or Astd >= A_Lim:
        
        Vstd = V_Lim
        Astd = A_Lim
        
        print("Standard Velocity is over the limit!")
    
    if DelPos1 == MAX:
        V1 = Vstd
        A1 = Astd
        print("Servo1 is the standard")
        t3_1 = 64.0*V1/A1 + 64.0*DelPos1/V1
        t2_1 = 64.0*DelPos1/V1
        t3_std = t3_1
        t2_std = t2_1
        t3_2 = t3_std
        t3_3 = t3_std
        t3_4 = t3_std
        t3_5 = t3_std
        t3_6 = t3_std

        t2_2 = t2_std
        t2_3 = t2_std
        t2_4 = t2_std
        t2_5 = t2_std
        t2_6 = t2_std
        den_std = (t3_std - t2_std)

        V2 = 64.0*DelPos2/t2_2
        V3 = 64.0*DelPos3/t2_3
        V4 = 64.0*DelPos4/t2_4
        V5 = 64.0*DelPos5/t2_5
        V6 = 64.0*DelPos6/t2_6
        A2 = 64*V2 / den_std
        A3 = 64*V3 / den_std
        A4 = 64*V4 / den_std
        A5 = 64*V5 / den_std
        A6 = 64*V6 / den_std
        
    elif DelPos2 == MAX:
        V2 = Vstd
        A2 = Astd
        print("Servo2 is the standard")
        t3_2 = 64.0*V2/A2 + 64.0*DelPos2/V2
        t2_2 = 64.0*DelPos2/V2
        t3_std = t3_2
        t2_std = t2_2
        t3_1 = t3_std
        t3_3 = t3_std
        t3_4 = t3_std
        t3_5 = t3_std
        t3_6 = t3_std
        
        t2_1 = t2_std
        t2_3 = t2_std
        t2_4 = t2_std
        t2_5 = t2_std
        t2_6 = t2_std
        den_std = (t3_std - t2_std)
        V1 = 64.0*DelPos1/t2_1
        V3 = 64.0*DelPos3/t2_3
        V4 = 64.0*DelPos4/t2_4
        V5 = 64.0*DelPos5/t2_5
        V6 = 64.0*DelPos6/t2_6
        A1 = 64*V1 / den_std
        A3 = 64*V3 / den_std
        A4 = 64*V4 / den_std
        A5 = 64*V5 / den_std
        A6 = 64*V6 / den_std
        
    elif DelPos3 == MAX:
        V3 = Vstd
        A3 = Astd
        print("Servo3 is the standard")
        t3_3 = 64.0*V3/A3 + 64.0*DelPos3/V3
        t2_3 = 64.0*DelPos3/V3
        t3_std = t3_3
        t2_std = t2_3
        t3_1 = t3_std
        t3_2 = t3_std
        t3_4 = t3_std
        t3_5 = t3_std
        t3_6 = t3_std
        
        t2_1 = t2_std
        t2_2 = t2_std
        t2_4 = t2_std
        t2_5 = t2_std
        t2_6 = t2_std
        den_std = (t3_std - t2_std)

        V1 = 64.0*DelPos1/t2_1
        V2 = 64.0*DelPos2/t2_2
        V4 = 64.0*DelPos4/t2_4
        V5 = 64.0*DelPos5/t2_5
        V6 = 64.0*DelPos6/t2_6
        A1 = 64*V1 / den_std
        A2 = 64*V2 / den_std
        A4 = 64*V4 / den_std
        A5 = 64*V5 / den_std
        A6 = 64*V6 / den_std
        
    elif DelPos4 == MAX:
        V4 = Vstd
        A4 = Astd
        print("Servo4 is the standard")
        t3_4 = 64.0*V4/A4 + 64.0*DelPos4/V4
        t2_4 = 64.0*DelPos4/V4
        t3_std = t3_4
        t2_std = t2_4
        t3_1 = t3_std
        t3_2 = t3_std
        t3_3 = t3_std
        t3_5 = t3_std
        t3_6 = t3_std

        t2_1 = t2_std
        t2_2 = t2_std
        t2_3 = t2_std
        t2_5 = t2_std
        t2_6 = t2_std
        den_std = (t3_std - t2_std)

        V1 = 64.0*DelPos1/t2_1
        V2 = 64.0*DelPos2/t2_2
        V3 = 64.0*DelPos3/t2_3
        V5 = 64.0*DelPos5/t2_5
        V6 = 64.0*DelPos6/t2_6
        A1 = 64*V1 / den_std
        A2 = 64*V2 / den_std
        A3 = 64*V3 / den_std
        A5 = 64*V5 / den_std
        A6 = 64*V6 / den_std

    elif DelPos5 == MAX:
        V5 = Vstd
        A5 = Astd
        print("Servo5 is the standard")
        t3_5 = 64.0*V5/A5 + 64.0*DelPos5/V5
        t2_5 = 64.0*DelPos5/V5
        t3_std = t3_5
        t2_std = t2_5
        t3_1 = t3_std
        t3_2 = t3_std
        t3_3 = t3_std
        t3_4 = t3_std
        t3_6 = t3_std

        t2_1 = t2_std
        t2_2 = t2_std
        t2_3 = t2_std
        t2_4 = t2_std
        t2_6 = t2_std
        den_std = (t3_std - t2_std)

        V1 = 64.0*DelPos1/t2_1
        V2 = 64.0*DelPos2/t2_2
        V3 = 64.0*DelPos3/t2_3
        V4 = 64.0*DelPos4/t2_4
        V6 = 64.0*DelPos6/t2_6
        A1 = 64*V1 / den_std
        A2 = 64*V2 / den_std
        A3 = 64*V3 / den_std
        A4 = 64*V4 / den_std
        A6 = 64*V6 / den_std
        
    elif DelPos6 == MAX:
        V6 = Vstd
        A6 = Astd
        print("Servo6 is the standard")
        t3_6 = 64.0*V6/A6 + 64.0*DelPos6/V6
        t2_6 = 64.0*DelPos6/V6
        t3_std = t3_6
        t2_std = t2_6
        t3_1 = t3_std
        t3_2 = t3_std
        t3_3 = t3_std
        t3_4 = t3_std
        t3_5 = t3_std

        t2_1 = t2_std
        t2_2 = t2_std
        t2_3 = t2_std
        t2_4 = t2_std
        t2_5 = t2_std
        den_std = (t3_std - t2_std)

        V1 = 64.0*DelPos1/t2_1
        V2 = 64.0*DelPos2/t2_2
        V3 = 64.0*DelPos3/t2_3
        V4 = 64.0*DelPos4/t2_4
        V5 = 64.0*DelPos5/t2_5
        A1 = 64*V1 / den_std
        A2 = 64*V2 / den_std
        A3 = 64*V3 / den_std
        A4 = 64*V4 / den_std
        A5 = 64*V5 / den_std

    return V1, A1, V2, A2, V3, A3, V4, A4, V5, A5, V6, A6

def SetProfile1(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 1: %d" %set_V_PRFL)
    print("A PRFL 1: %d" %set_A_PRFL)
    print("--------------------------------")

def SetProfile2(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 2: %d" %set_V_PRFL)
    print("A PRFL 2: %d" %set_A_PRFL)
    print("--------------------------------") 

def SetProfile3(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 3: %d" %set_V_PRFL)
    print("A PRFL 3: %d" %set_A_PRFL)
    print("--------------------------------")    

def SetProfile4(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 4: %d" %set_V_PRFL)
    print("A PRFL 4: %d" %set_A_PRFL)
    print("--------------------------------")

def SetProfile5(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 5: %d" %set_V_PRFL)
    print("A PRFL 5: %d" %set_A_PRFL)
    print("--------------------------------")    

def SetProfile6(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 6: %d" %set_V_PRFL)
    print("A PRFL 6: %d" %set_A_PRFL)
    print("--------------------------------")

def SetProfile7(set_V_PRFL,set_A_PRFL):
    ######################### Set Velocity / Acceleration Profile  ##############################
    set_A_Limit = 32767     # 32767 default                [214.577 rev/min^2]
    set_V_Limit = 500       # 350 Default                  [0.229RPM]

    #set_A_PRFL = 30      # between 0 ~ set_A_limit      [214.577 rev/min^2]
    #set_V_PRFL = 200      # between 0 ~ set_V_Limit      [0.229RPM]

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_ACCELERATION_LIMIT, set_A_Limit)
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_VELOCITY_LIMIT, set_V_Limit)

    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_PROFILE_ACCELERATION, int(set_A_PRFL))
    dxl_comm_result, dxl_error = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_PROFILE_VELOCITY, int(set_V_PRFL))

    acceleration_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_ACCELERATION_LIMIT)
    velocity_limit, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_VELOCITY_LIMIT)

    print("V PRFL 7: %d" %set_V_PRFL)
    print("A PRFL 7: %d" %set_A_PRFL)
    print("--------------------------------")     

def IsMoving1():
    Moving1, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_MOVING)
    return Moving1

def IsMoving2():
    Moving2, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_MOVING)
    return Moving2

def IsMoving3():
    Moving3, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_MOVING)
    return Moving3

def IsMoving4():
    Moving4, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_MOVING)
    return Moving4

def IsMoving5():
    Moving5, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_MOVING)
    return Moving5

def IsMoving6():
    Moving6, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_MOVING)
    return Moving6

def MoveRobot(xval,yval):
    Mem_X = [None]*20
    Mem_Y = [None]*20
    Mem_Z = [None]*20
    Yconst = 250
    Zconst = 150
    X6_ROT = 0
    Y6_ROT = 0
    Z6_ROT = 0
    Mem_X[0] = 250
    Mem_Y[0] = Yconst
    Mem_Z[0] = Zconst
    throttle = 1000
    PreAng = ReadAngle()
    PreAng1 = PreAng[0]
    PreAng2 = PreAng[1]
    PreAng3 = PreAng[2]
    PreAng4 = PreAng[3]
    PreAng5 = PreAng[4]
    PreAng6 = PreAng[5]
    #Mem_ANG = mymath.RobotArmINV(int(data['yaw']),int(data['throttle']),Mem_Z[K],X6_ROT,Y6_ROT,Z6_ROT)
    Mem_ANG = RobotArmINV(xval,250,Mem_Z[0],X6_ROT,Y6_ROT,Z6_ROT)
    GoalPos1 = Mem_ANG[0]
    GoalPos2 = Mem_ANG[1]
    GoalPos3 = Mem_ANG[2]
    GoalPos4 = Mem_ANG[3]
    GoalPos5 = Mem_ANG[4]
    GoalPos6 = Mem_ANG[5]
    DelPos1 = DeltaPos(PreAng1,GoalPos1)
    DelPos2 = DeltaPos(PreAng2,GoalPos2)
    DelPos3 = DeltaPos(PreAng3,GoalPos3)
    DelPos4 = DeltaPos(PreAng4,GoalPos4)
    DelPos5 = DeltaPos(PreAng5,GoalPos5)
    DelPos6 = DeltaPos(PreAng6,GoalPos6)
    VSTD = 100
    ASTD = 15
    TRAJ = TrajectoryGeneration3(VSTD,ASTD,DelPos1,DelPos2,DelPos3,DelPos4,DelPos5,DelPos6)
    V1 = TRAJ[0]
    A1 = TRAJ[1]
    V2 = TRAJ[2]
    A2 = TRAJ[3]
    V3 = TRAJ[4]
    A3 = TRAJ[5]
    V4 = TRAJ[6]
    A4 = TRAJ[7]
    V5 = TRAJ[8]
    A5 = TRAJ[9]
    V6 = TRAJ[10]
    A6 = TRAJ[11]

    SetProfile1(V1,A1)
    SetProfile2(V2,A2)
    SetProfile3(V3,A3)
    SetProfile4(V4,A4)
    SetProfile5(V5,A5)
    SetProfile6(V6,A6)

    RunServo(GoalPos1,GoalPos2,GoalPos3,GoalPos4,GoalPos5,GoalPos6)
    MoveType1 = MovingStatus1()
    MoveType2 = MovingStatus2()
    MoveType3 = MovingStatus3()
    MoveType4 = MovingStatus4()
    MoveType5 = MovingStatus5()
    MoveType6 = MovingStatus6()
    
    MovingFlag = True
    Block1 = True
    Block2 = True
    Block3 = True
    Block4 = True
    Block5 = True
    Block6 = True
    '''
    while MovingFlag:
        Move1 = IsMoving1()
        Move2 = IsMoving2()
        Move3 = IsMoving3()
        Move4 = IsMoving4()
        Move5 = IsMoving5()
        Move6 = IsMoving6()

        if Move1 == 0 and Block1 == True:
            endTime1 = time.time()
            period1 = endTime1 - startTime
            Block1 = False
        if Move2 == 0 and Block2 == True:
            endTime2 = time.time()
            period2 = endTime2 - startTime 
            Block2 = False 
        if Move3 == 0 and Block3 == True:
            endTime3 = time.time()
            period3 = endTime3 - startTime
            Block3 = False
        if Move4 == 0 and Block4 == True:
            endTime4 = time.time()
            period4 = endTime4 - startTime
            Block4 = False
        if Move5 == 0 and Block5 == True:
            endTime5 = time.time()
            period5 = endTime5 - startTime 
            Block5 = False 
        if Move6 == 0 and Block6 == True:
            endTime6 = time.time()
            period6 = endTime6 - startTime
            Block6 = False

        if Move1 == 0 and Move2 == 0 and Move3 == 0 and Move4 == 0 and Move5 == 0 and Move6 == 0:
            MovingFlag = False
            print("Period1: %f" %period1)
            print("Period2: %f" %period2) 
            print("Period3: %f" %period3)
            print("Period4: %f" %period4)
            print("Period5: %f" %period5) 
            print("Period6: %f" %period6)
            print("Finished point %d" %K)
            print("--------------------------------------------------")
            print("--------------------------------------------------")
    '''
    
    PreAng1 = GoalPos1
    PreAng2 = GoalPos2
    PreAng3 = GoalPos3
    PreAng4 = GoalPos4
    PreAng5 = GoalPos5
    PreAng6 = GoalPos6

def MovingStatus1():
    MovingStat1, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat1 > 48:
        print("Motor1 is in Trapezodal Profile")
    elif MovingStat1 < 35 and MovingStat1 > 20:
        print("Motor1 is in Triangular Profile")
    elif MovingStat1 < 20 and MovingStat1 > 3:
        print("Motor1 is in Rectangular Profile")
    elif MovingStat1 < 3:
        print("Motor1 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat1

def MovingStatus2():
    MovingStat2, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat2 > 48:
        print("Motor2 is in Trapezodal Profile")
    elif MovingStat2 < 35 and MovingStat2 > 20:
        print("Motor2 is in Triangular Profile")
    elif MovingStat2 < 20 and MovingStat2 > 3:
        print("Motor2 is in Rectangular Profile")
    elif MovingStat2 < 3:
        print("Motor2 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat2

def MovingStatus3():
    MovingStat3, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat3 > 48:
        print("Motor3 is in Trapezodal Profile")
    elif MovingStat3 < 35 and MovingStat3 > 20:
        print("Motor3 is in Triangular Profile")
    elif MovingStat3 < 20 and MovingStat3 > 3:
        print("Motor3 is in Rectangular Profile")
    elif MovingStat3 < 3:
        print("Motor3 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat3 

def MovingStatus4():
    MovingStat4, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat4 > 48:
        print("Motor4 is in Trapezodal Profile")
    elif MovingStat4 < 35 and MovingStat4 > 20:
        print("Motor4 is in Triangular Profile")
    elif MovingStat4 < 20 and MovingStat4 > 3:
        print("Motor4 is in Rectangular Profile")
    elif MovingStat4 < 3:
        print("Motor4 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat4

def MovingStatus5():
    MovingStat5, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat5 > 48:
        print("Motor5 is in Trapezodal Profile")
    elif MovingStat5 < 35 and MovingStat5 > 20:
        print("Motor5 is in Triangular Profile")
    elif MovingStat5 < 20 and MovingStat5 > 3:
        print("Motor5 is in Rectangular Profile")
    elif MovingStat5 < 3:
        print("Motor5 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat5

def MovingStatus6():
    MovingStat6, dxl_comm_result, dxl_error = packetHandler.read1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_MOVING_STATUS)
    
    if MovingStat6 > 48:
        print("Motor6 is in Trapezodal Profile")
    elif MovingStat6 < 35 and MovingStat6 > 20:
        print("Motor6 is in Triangular Profile")
    elif MovingStat6 < 20 and MovingStat6 > 3:
        print("Motor6 is in Rectangular Profile")
    elif MovingStat6 < 3:
        print("Motor6 is in Step Mode (No Profile)")
    else:
        print("UNKNOWN Profile...")

    return MovingStat6

def RunServo(inputDeg1,inputDeg2,inputDeg3,inputDeg4,inputDeg5,inputDeg6):

    pos1 = inputDeg1
    pos2 = inputDeg2
    pos3 = inputDeg3
    pos4 = inputDeg4
    pos5 = inputDeg5
    pos6 = inputDeg6

    servo_com1 = map(pos1,0.0,360.0,0.0,4095.0)
    servo_com2 = map(pos2,0.0,360.0,0.0,4095.0)
    servo_com3 = map(pos3,0.0,360.0,0.0,4095.0)
    servo_com4 = map(pos4,0.0,360.0,0.0,4095.0)
    servo_com5 = map(pos5,0.0,360.0,0.0,4095.0)
    servo_com6 = map(pos6,0.0,360.0,0.0,4095.0)

    dxl1_goal_position = int(servo_com1)
    dxl2_goal_position = int(servo_com2)
    dxl3_goal_position = int(servo_com3)
    dxl4_goal_position = int(servo_com4)
    dxl5_goal_position = int(servo_com5)
    dxl6_goal_position = int(servo_com6)

    dxl_comm_result1, dxl_error1 = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_GOAL_POSITION, dxl1_goal_position)
    if dxl_comm_result1 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result1))
    elif dxl_error1 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error1))

    dxl_comm_result2, dxl_error2 = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_GOAL_POSITION, dxl2_goal_position)
    if dxl_comm_result2 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result2))
    elif dxl_error2 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error2))

    dxl_comm_result3, dxl_error3 = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_GOAL_POSITION, dxl3_goal_position)
    if dxl_comm_result3 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result3))
    elif dxl_error3 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error3))

    dxl_comm_result4, dxl_error4 = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_GOAL_POSITION, dxl4_goal_position)
    if dxl_comm_result4 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result4))
    elif dxl_error4 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error4))

    dxl_comm_result5, dxl_error5 = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_GOAL_POSITION, dxl5_goal_position)
    if dxl_comm_result5 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result5))
    elif dxl_error5 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error5))

    dxl_comm_result6, dxl_error6 = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_GOAL_POSITION, dxl6_goal_position)
    if dxl_comm_result6 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result6))
    elif dxl_error6 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error6))

def ReadAngle():
    dxl_present_position1, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_PRESENT_POSITION)
    dxl_present_position2, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_PRESENT_POSITION)
    dxl_present_position3, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_PRESENT_POSITION)
    dxl_present_position4, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_PRESENT_POSITION)
    dxl_present_position5, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_PRESENT_POSITION)
    dxl_present_position6, dxl_comm_result, dxl_error = packetHandler.read4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_PRESENT_POSITION)

    pre_pos1 = map(dxl_present_position1, 0.0, 4095.0, 0.0, 360.0)
    pre_pos2 = map(dxl_present_position2, 0.0, 4095.0, 0.0, 360.0)
    pre_pos3 = map(dxl_present_position3, 0.0, 4095.0, 0.0, 360.0)
    pre_pos4 = map(dxl_present_position4, 0.0, 4095.0, 0.0, 360.0)
    pre_pos5 = map(dxl_present_position5, 0.0, 4095.0, 0.0, 360.0)
    pre_pos6 = map(dxl_present_position6, 0.0, 4095.0, 0.0, 360.0)

    return pre_pos1,pre_pos2,pre_pos3,pre_pos4,pre_pos5,pre_pos6

def RunServo1(inputDeg1):
    pos1 = inputDeg1
    servo_com1 = map(pos1,0.0,360.0,0.0,4095.0)
    dxl1_goal_position = int(servo_com1)
    dxl_comm_result1, dxl_error1 = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_GOAL_POSITION, dxl1_goal_position)
    if dxl_comm_result1 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result1))
    elif dxl_error1 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error1))

def RunServo2(inputDeg2):
    pos2 = inputDeg2
    servo_com2 = map(pos2,0.0,360.0,0.0,4095.0)
    dxl2_goal_position = int(servo_com2)
    dxl_comm_result2, dxl_error2 = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_GOAL_POSITION, dxl2_goal_position)
    if dxl_comm_result2 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result2))
    elif dxl_error2 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error2))

def RunServo3(inputDeg3):
    pos3 = inputDeg3
    servo_com3 = map(pos3,0.0,360.0,0.0,4095.0)
    dxl3_goal_position = int(servo_com3)
    dxl_comm_result3, dxl_error3 = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_GOAL_POSITION, dxl3_goal_position)
    if dxl_comm_result3 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result3))
    elif dxl_error3 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error3))

def RunServo4(inputDeg4):
    pos4 = inputDeg4
    servo_com4 = map(pos4,0.0,360.0,0.0,4095.0)
    dxl4_goal_position = int(servo_com4)
    dxl_comm_result4, dxl_error4 = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_GOAL_POSITION, dxl4_goal_position)
    if dxl_comm_result4 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result4))
    elif dxl_error4 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error4))

def RunServo5(inputDeg5):
    pos5 = inputDeg5
    servo_com5 = map(pos5,0.0,360.0,0.0,4095.0)
    dxl5_goal_position = int(servo_com5)
    dxl_comm_result5, dxl_error5 = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_GOAL_POSITION, dxl5_goal_position)
    if dxl_comm_result5 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result5))
    elif dxl_error5 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error5))

def RunServo6(inputDeg6):
    pos6 = inputDeg6
    servo_com6 = map(pos6,0.0,360.0,0.0,4095.0)
    dxl6_goal_position = int(servo_com6)
    dxl_comm_result6, dxl_error6 = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_GOAL_POSITION, dxl6_goal_position)
    if dxl_comm_result6 != COMM_SUCCESS:
        print("%s" % packetHandler.getTxRxResult(dxl_comm_result6))
    elif dxl_error6 != 0:
        print("%s" % packetHandler.getRxPacketError(dxl_error6))

def TorqueOn():
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_ENABLE)
    print("torque is on bitch")

def TorqueOff():
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)
    dxl_comm_result, dxl_error = packetHandler.write1ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_TORQUE_ENABLE, TORQUE_DISABLE)

def GripOpen():
    dxl7_goal_position = 1700
    dxl_comm_result7, dxl_error7 = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_GOAL_POSITION, dxl7_goal_position)

def GripClose():
    dxl7_goal_position = 2780
    dxl_comm_result7, dxl_error7 = packetHandler.write4ByteTxRx(portHandler, DXL7_ID, ADDR_PRO_GOAL_POSITION, dxl7_goal_position)


def StandByPos():
    pos1 = 180
    pos2 = 180
    pos3 = 180
    pos4 = 180
    pos5 = 180
    pos6 = 180

    servo_com1 = map(pos1,0.0,360.0,0.0,4095.0)
    servo_com2 = map(pos2,0.0,360.0,0.0,4095.0)
    servo_com3 = map(pos3,0.0,360.0,0.0,4095.0)
    servo_com4 = map(pos4,0.0,360.0,0.0,4095.0)
    servo_com5 = map(pos5,0.0,360.0,0.0,4095.0)
    servo_com6 = map(pos6,0.0,360.0,0.0,4095.0)

    dxl1_goal_position = int(servo_com1)
    dxl2_goal_position = int(servo_com2)
    dxl3_goal_position = int(servo_com3)
    dxl4_goal_position = int(servo_com4)
    dxl5_goal_position = int(servo_com5)
    dxl6_goal_position = int(servo_com6)

    dxl_comm_result1, dxl_error1 = packetHandler.write4ByteTxRx(portHandler, DXL1_ID, ADDR_PRO_GOAL_POSITION, dxl1_goal_position)
    dxl_comm_result2, dxl_error2 = packetHandler.write4ByteTxRx(portHandler, DXL2_ID, ADDR_PRO_GOAL_POSITION, dxl2_goal_position)
    dxl_comm_result3, dxl_error3 = packetHandler.write4ByteTxRx(portHandler, DXL3_ID, ADDR_PRO_GOAL_POSITION, dxl3_goal_position)
    dxl_comm_result4, dxl_error4 = packetHandler.write4ByteTxRx(portHandler, DXL4_ID, ADDR_PRO_GOAL_POSITION, dxl4_goal_position)
    dxl_comm_result5, dxl_error5 = packetHandler.write4ByteTxRx(portHandler, DXL5_ID, ADDR_PRO_GOAL_POSITION, dxl5_goal_position)
    dxl_comm_result6, dxl_error6 = packetHandler.write4ByteTxRx(portHandler, DXL6_ID, ADDR_PRO_GOAL_POSITION, dxl6_goal_position)

def RobotArmGoHome():
    GripOpen()
    #### Point 0 ####
    Mem_Ang1 = 271.296703
    Mem_Ang2 = 194.021978
    Mem_Ang3 = 157.714286
    Mem_Ang4 = 182.769231
    Mem_Ang5 = 176.000000
    Mem_Ang6 = 181.186813
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

    #### Point 1 ####
    Mem_Ang1 = 278.417582
    Mem_Ang2 = 203.956044
    Mem_Ang3 = 157.978022
    Mem_Ang4 = 181.714286
    Mem_Ang5 = 123.164835
    Mem_Ang6 = 184.263736
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

    #### Point 2 ####
    Mem_Ang1 = 278.593407
    Mem_Ang2 = 220.131868
    Mem_Ang3 = 149.714286
    Mem_Ang4 = 182.857143
    Mem_Ang5 = 102.769231
    Mem_Ang6 = 183.560440
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

    #### Point 3 ####
    Mem_Ang1 = 283.956044
    Mem_Ang2 = 207.472527
    Mem_Ang3 = 116.307692
    Mem_Ang4 = 188.307692
    Mem_Ang5 = 132.747253
    Mem_Ang6 = 187.516484
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

    #### Point 4 ####
    Mem_Ang1 = 282.285714
    Mem_Ang2 = 188.483516
    Mem_Ang3 = 107.164835
    Mem_Ang4 = 194.021978
    Mem_Ang5 = 148.043956
    Mem_Ang6 = 184.087912
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

    #### Point 5 ####
    Mem_Ang1 = 282.637363
    Mem_Ang2 = 185.846154
    Mem_Ang3 = 106.109890
    Mem_Ang4 = 197.186813
    Mem_Ang5 = 152.879121
    Mem_Ang6 = 184.087912
    RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
    time.sleep(1)

def RobotArmAwake():
    # Last Home Position #
    Last_Ang1 = 282.637363
    Last_Ang2 = 185.846154
    Last_Ang3 = 106.109890
    Last_Ang4 = 197.186813
    Last_Ang5 = 152.879121
    Last_Ang6 = 184.087912
    InitAng = ReadAngle()
    Deg1 = InitAng[0]
    Deg2 = InitAng[1]
    Deg3 = InitAng[2]
    Deg4 = InitAng[3]
    Deg5 = InitAng[4]
    Deg6 = InitAng[5]
    DelAng1 = abs(Deg1 - Last_Ang1)
    DelAng2 = abs(Deg2 - Last_Ang2)
    DelAng3 = abs(Deg3 - Last_Ang3)
    DelAng4 = abs(Deg4 - Last_Ang4)
    DelAng5 = abs(Deg5 - Last_Ang5)
    DelAng6 = abs(Deg6 - Last_Ang6)
    if (DelAng1 < 60) and (DelAng2 < 60) and (DelAng3 < 60) and (DelAng4 < 60) and (DelAng5 < 60) and (DelAng6 < 60):
        print("Robot is in sleep position")
        time.sleep(1)
        AwakenOK = True
        TorqueOn()
        GripOpen()
        #### Point 0 ####
        Mem_Ang1 = 277.802198
        Mem_Ang2 = 194.021978
        Mem_Ang3 = 110.329670
        Mem_Ang4 = 190.593407
        Mem_Ang5 = 142.593407
        Mem_Ang6 = 177.934066
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 1 ####
        Mem_Ang1 = 273.670330
        Mem_Ang2 = 199.384615
        Mem_Ang3 = 125.802198
        Mem_Ang4 = 186.901099
        Mem_Ang5 = 119.912088
        Mem_Ang6 = 177.934066
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 2 ####
        Mem_Ang1 = 271.560440
        Mem_Ang2 = 201.670330
        Mem_Ang3 = 152.351648
        Mem_Ang4 = 184.967033
        Mem_Ang5 = 96.351648
        Mem_Ang6 = 175.296703
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 3 ####
        Mem_Ang1 = 270.505495
        Mem_Ang2 = 213.890110
        Mem_Ang3 = 169.934066
        Mem_Ang4 = 184.439560
        Mem_Ang5 = 86.681319
        Mem_Ang6 = 174.153846
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 4 ####
        Mem_Ang1 = 272.175824
        Mem_Ang2 = 219.164835
        Mem_Ang3 = 155.604396
        Mem_Ang4 = 182.593407
        Mem_Ang5 = 180.219780
        Mem_Ang6 = 183.120879
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 5 ####
        Mem_Ang1 = 224.351648
        Mem_Ang2 = 175.560440
        Mem_Ang3 = 224.967033
        Mem_Ang4 = 173.450549
        Mem_Ang5 = 233.318681
        Mem_Ang6 = 181.098901
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 6 ####
        Mem_Ang1 = 180.659341
        Mem_Ang2 = 182.153846
        Mem_Ang3 = 186.373626
        Mem_Ang4 = 171.164835
        Mem_Ang5 = 222.857143
        Mem_Ang6 = 177.230769
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(0.5)

        #### Point 7 ####
        Mem_Ang1 = 177.494505
        Mem_Ang2 = 207.120879
        Mem_Ang3 = 111.208791
        Mem_Ang4 = 174.065934
        Mem_Ang5 = 222.857143
        Mem_Ang6 = 185.582418
        RunServo(Mem_Ang1,Mem_Ang2,Mem_Ang3,Mem_Ang4,Mem_Ang5,Mem_Ang6)
        time.sleep(2)
    
    else:
        print("WARNING!: Robot is not in sleep position")
        AwakenOK = False
        print("Delta Deg1: %f" %DelAng1)
        print("Delta Deg2: %f" %DelAng2)
        print("Delta Deg3: %f" %DelAng3)
        print("Delta Deg4: %f" %DelAng4)
        print("Delta Deg5: %f" %DelAng5)
        print("Delta Deg6: %f" %DelAng6)

        TorqueOff()

    

    return AwakenOK



if __name__ == '__main__':


    print("yo yo what's up")