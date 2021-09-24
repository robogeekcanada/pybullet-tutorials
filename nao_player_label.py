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

#Get body unique id, draw a line aabb for each link
cid = p.getBodyUniqueId(robot.robot_model)
#print(f'\nbody unique id is {cid}')

#Head is link 2, draw line to show aabb and display P1
head_aabb = p.getAABB(cid, 2)
p.addUserDebugLine(head_aabb[0], head_aabb[1], [0,1,0], 3, 0)
p.addUserDebugText('P1', head_aabb[1], [0,0,1], 3.5)
