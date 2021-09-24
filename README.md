<img src="https://github.com/robogeekcanada/noetic_robots/blob/main/images/RG-logo.jpg" alt="alt text" width=100 height=150>

[@robogeekcanada](https://robo-geek.ca/)

# Pybullet Tutorials

A collection of PyBullet tutorials using Qibullet's NAO robot.

## Installation

1. Clone the repo: 
```
git clone https://github.com/robogeekcanada/pybullet-tutorials.git
```

2. Conda install the environment: `pybullet_env.yml` or refer to list of dependencies required in **.yml** file.

```
conda env create --file pybullet_env.yml
conda activate pybullet_env
```

If it's the first time running QiBullet, make sure to accept the agreement in your computer, otherwise you won't be able to load NAO robots in PyBullet.
More info: https://github.com/softbankrobotics-research/qibullet

## Instructions

1. Complete installation, preferably in conda.Tested in Windows, Ubuntu and OS
2. Unzip `meshes.zip` file into the working directory.
3. Test 
```
python nao_color_suits.py
```

![image](https://github.com/robogeekcanada/pybullet-tutorials/blob/main/images/nao_color_suits.PNG)

## How to use

The objective of this tutorial is to learn how to access NAO's hardware to use in more advanced simulations.

`nao_cameras.py`         shows how to access both NAO's cameras
`nao_color_suits.py`     shows how to load a blue and red NAO. Noticed that meshes were updated. Easy to figure out but make sure to read QiBullet agreement
`nao_get_link_names.py`  shows how to access individual links
`nao_joints_control.py`  shows how to access individual joints. 
`nao_joints_control2.py` same but using a different technique to access the hardware.
`nao_motions.py`         shows how to read motion files. Hacking: https://github.com/cyberbotics/webots/tree/master/projects/robots/softbank/nao/motions
`nao_player_label.py`    shows how to add a player number
`nao_soccer_field.py`    shows how to add a soccer field and a soccer ball
`nao_teleportation.py`   shows how to move to different positions by "teleporting"


