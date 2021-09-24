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

link_parameters = list()

count = 0
for name, link in robot.link_dict.items():
    print(f'{count} {name}')
    count +=1

time.sleep(2)


#Get body unique id, draw a line aabb for each link
cid = p.getBodyUniqueId(robot.robot_model)
print(f'\nbody unique id is {cid}')

for count, link in enumerate(robot.link_dict.items()):
    aabb = p.getAABB(cid, count)
    print(f'\n{count} aabb {aabb}')
    p.addUserDebugLine(aabb[0], aabb[1], [0,1,0])
