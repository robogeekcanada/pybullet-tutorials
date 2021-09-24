import pybullet as p
import pybullet_data
import time
import os

from qibullet import NaoVirtual

cwd = os.getcwd()
os.chdir(cwd)

client = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.loadURDF("plane.urdf")

p.setRealTimeSimulation(1)
p.setGravity(0, 0, -10)

robot1 = NaoVirtual()
robot1.description_file = "nao_blue.urdf"
robot1.loadRobot([0,0,0], [0,0,0,1])


robot2 = NaoVirtual()
robot2.description_file = "nao_red.urdf"
robot2.loadRobot([-1,-1,0], [0,0,0,1])

time.sleep(20)

p.disconnect()
