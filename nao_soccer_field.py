import pybullet as p
import pybullet_data
import time
import math

from qibullet import NaoVirtual

client = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.loadURDF("plane.urdf")

field = p.loadURDF('/home/osilva/soccer_project/field/soccerfield.urdf', physicsClientId=client)

ball = p.loadURDF("soccerball.urdf",basePosition=[0, 0, 0.36], globalScaling=0.2, physicsClientId=client)

p.changeDynamics(ball,-1,linearDamping=0, angularDamping=0, rollingFriction=0.001, spinningFriction=0.001)
p.changeVisualShape(ball,-1,rgbaColor=[0.8,0.8,0.8,1])


p.setRealTimeSimulation(1)
p.setGravity(0, 0, -10)

robot1 = NaoVirtual()
robot1.description_file = '/home/osilva/soccer_project/nao_blue.urdf'
robot1.loadRobot([0.8,0,0], [0,0,3.4,1])  #math.pi = 180 degrees


robot2 = NaoVirtual()
robot2.description_file = '/home/osilva/soccer_project/nao_red.urdf'
robot2.loadRobot([-1,-1,0], [0,0,0,1])

#time.sleep(20)
#p.disconnect()
