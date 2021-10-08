import numpy as np
import os
from pathlib import Path
import time
#import matplotlib.pyplot as plt
import pybullet as p
from time import sleep
import pybullet_data
import time
from datetime import datetime
import cv2

from qibullet import SimulationManager
from qibullet import NaoVirtual
from qibullet import Camera

import numpy as np
import pandas as pd

'''
ID_CAMERA_TOP = 0
ID_CAMERA_BOTTOM = 1
FRAME_WORLD = 1
FRAME_ROBOT = 2
URDF_FILE = "/nao.urdf"
P_STAND = NaoPosture("Stand")
P_STAND_INIT = NaoPosture("StandInit")
P_STAND_ZERO = NaoPosture("StandZero")
P_CROUCH = NaoPosture("Crouch")
P_SIT = NaoPosture("Sit")
P_SIT_RELAX = NaoPosture("SitRelax")
P_LYING_BELLY = NaoPosture("LyingBelly")
P_LYING_BACK = NaoPosture("LyingBack")
'''

cwd = os.getcwd()

data_folder = Path(cwd)
motions_folder = data_folder/"motions"     #/motions" 


def read_csv(filename):

    #Read csv file for HandWave.csv
    df = pd.read_csv(filename)

    num_poses = df.count()[0]
    cols = df.columns
    num_cols = len(cols)

    #Determine number of joints
    num_joints = num_cols - 2

    joint_names = cols[2:]

    return num_poses, num_joints, joint_names, df

def animate(num_poses, num_joints, joint_names, df, robot, delay =0.05):

    for pose in range(num_poses):
        for j in range(num_joints):
            name = joint_names[j]
            angle = float(df[name][pose])
            robot.setAngles(name, angle, 1.0)

        if delay != 0.0:
            sleep(delay)
    

def main():

    print('Simulation starting...')
    simulation_manager = SimulationManager()
    client = simulation_manager.launchSimulation(gui=True, auto_step=True)   
    robot = simulation_manager.spawnNao(client, quaternion =[0.0,0.0,0.0, 1.2], spawn_ground_plane=True)

    #Wave hand
    print('\nWaving hand...')
    
    filename = motions_folder/'HandWave.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot)

    sleep(4.0)

    #Walking forward
    print('\nWalk Forward a couple small steps...')
    filename = motions_folder/'Forwards.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.01)

    sleep(2.0)

    #Walking forward 50
    print('\nWalk Forward 50 test...')
    filename = motions_folder/'Forwards50.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.01)

    sleep(4.0)

    #Backwards
    print('\nBackwards...')
    filename = motions_folder/'Backwards.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.01)

    sleep(4.0)

    #Shoot
    print('\nShoot test...')
    filename = motions_folder/'Shoot.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.01)

    sleep(3.0)

    #Side Step Left
    print('\nSide Step left...')
    filename = motions_folder/'SideStepLeft.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.0)

    sleep(3.0)

    #Side Step Right
    print('\nSide Step right...')
    filename = motions_folder/'SideStepRight.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.0)

    sleep(2.0)

    #Lying Back
    print('\nLying back pose...')
    robot.goToPosture('LyingBack', 1.0)

    sleep(3.0)

    #Stand up from Front
    print('\nStand up from front...')
    filename = 'motions\\StandUpfromFront.csv'
    num_poses, num_joints, joint_names, df = read_csv(filename)
    animate(num_poses, num_joints, joint_names, df, robot, delay=0.03)
  
    sleep(5.0)

    #Crouch
    print('\nCrouch pose...')
    robot.goToPosture('Crouch', 1.0)

    sleep(2.0)

    #Stand pose
    print('\nStand pose...')
    robot.goToPosture('StandInit', 1.0)

    sleep(2.0)

    #Sit Position
    print('\nSitting pose...')
    robot.goToPosture('Sit', 1.0)

    sleep(2.0)

    #Lying Belly
    print('\nLying belly pose...')
    robot.goToPosture('LyingBelly', 1.0)

    sleep(2.0)
    #Get position
    print('\nNao position:', robot.getPosition())

    pos_orientation = p.getBasePositionAndOrientation(1)

       
main()
