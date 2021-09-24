import time
import pybullet as p
import pybullet_data

from qibullet import NaoVirtual


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

while True:
    for joint_parameter in joint_parameters:
        robot.setAngles(joint_parameter[1], p.readUserDebugParameter(joint_parameter[0]), 1.0)



