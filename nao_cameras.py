import time
import pybullet as p
import pybullet_data

from qibullet import NaoVirtual
from qibullet import Camera

import cv2

client = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

p.setRealTimeSimulation(1)
p.setGravity(0, 0, -10)

robot = NaoVirtual()
robot.loadRobot([0,0,0], [0,0,0,1])

time.sleep(2)

joint_parameters = list()

for name, joint in robot.joint_dict.items():
    if "Finger" not in name and "Thumb" not in name:
        joint_parameters.append((p.addUserDebugParameter(name, joint.getLowerLimit(),
                                                         joint.getUpperLimit(),
                                                         robot.getAnglesPosition(name)), name))


handle_top = robot.subscribeCamera(NaoVirtual.ID_CAMERA_TOP, resolution=Camera.K_VGA, fps=15.0)
handle_bottom = robot.subscribeCamera(NaoVirtual.ID_CAMERA_BOTTOM, resolution=Camera.K_VGA, fps=15.0)

while True:
   
    for joint_parameter in joint_parameters:
        robot.setAngles(joint_parameter[1], p.readUserDebugParameter(joint_parameter[0]), 1.0)

    #If image wants to be retrieved, it can be copied to cv2
        
    #img_top = robot.getCameraFrame(handle_top)
    #cv2.imshow('top camera', img_top)
    #cv2.waitKey(1)
