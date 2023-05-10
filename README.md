
# ROBOT FOOTBALL TRACKING IN ROS
The football tracking robot is a robot system that uses ROS2 (Robot Operating System 2) to follow the movement of a football on a playing field. 
The robot is outfitted with sensors and cameras that record photos of the football, which are then analysed using computer vision algorithms to track its 
position and movement. The robot may be programmed to follow the football or to travel to certain spots on the pitch to record different viewpoints of the game. 
This technology may be used for a variety of purposes, including analysing player performance, recording highlights for broadcasting, and supplying data for 
sports analytics.

## Introduction

The Neuron bot is a robotic device developed to follow a football's movement on a football pitch. The Neuron bot detects and tracks the football's movement using object detection algorithms based on RGB and HSV information. The robot is created in Gazebo, a virtual football world, and is designed to track the football and capture its motions from multiple perspectives.

## Prerequisites
## For Cloning Neuron Bot
- https://github.com/Adlink-ROS/neuronbot2
- Execute steps 2, 3, 4 and 6 from the terminal.
- Go to src/neuronbot2/neuronbot_gazebo directory. Then, open the spawn_nb2.launch file and change the 3 timeout values from ‘300’ to ‘5’ (otherwise you may have to wait 300 seconds for the laser to start up after spawning the robot)
- ros2 launch neuronbot2_gazebo neuronbot2_world.launch.py world_model:=mememan_world.model
- If the robot does not spawn, go to the Insert tab on the left side. You will see 3 neuronbot models. Although they have the same name, they are actually different models: 1. NeuronBot with laser scanner 2. NeuronBot with laser scanner and camera on the front 3. NeuronBot with laser scanner and camera on the top
- Go to src/neuronbot2/neuronbot2_gazebo/models/ neuronbot2_w_front_camera directory. Open the models.sdf file and find the tag. Underneath it, you will find the , and tags. Edit their values to 36 samples, -0.7 min_angle and 0.7 max_angle. Save the file and rerun the simulation with the NeuronBot model (front camera version). Now the robot will have the modified laser.)

## Set Up

In this section, provide instructions on how to set up your project. This may include things like:

- How to clone the repository
- How to install dependencies
- How to configure the project
- Any other steps required to get your project up and running

## Simulation

In this section, describe how to run the simulation. You may include information such as:

- Command-line arguments or flags
- Configuration options
- Examples of how to run the simulation

You may also include any other information that you think would be helpful for users, such as troubleshooting tips or known issues.

## Conclusion

Wrap up your README with a conclusion that includes any acknowledgments or credits. You may include things like:

- Acknowledgments for any external libraries or resources used in your project
- Credits for any contributors or collaborators who helped with the project
- Contact information or links to your personal website or social media profiles
