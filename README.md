
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

## For Teleoperation
- ros2 run teleop_twist_keyboard teleop_twist_keyboard
- ros2 run turtlesim turtlesim_node 
- ros2 run turtlesim turtle_teleop_key

## For Setting the linear and angular velocities
- ros2 topic pub --once turtle1/cmd_vel geometry_msgs/msg/Twist "linear: x: 0.0 y: 0.0 z: 0.0 angular: x: 0.0 y: 0.0 z: 0.0"


## Set Up
- For all commands, replace "user"  with your ubuntu username
- If your system contains folder gazebo_11 instead of gazebo, replace gazebo with gazebo_11 in following commands
- Download this github respository using the terminal command git clone https://github.com/gbale20142018/Robot-Football-Tracking-ROS2.git

## Create Package "soccer"
- mkdir –p myWorkspace/src
- cd src
- ros2 pkg create --build-type ament_python soccer --dependencies rclpy std_msgs --node-name myNode

## Set Up Soccer World
- Copy the folder deepsoccer_gazebo from the downloaded repository and place the folder inside /home/user/.gazebo/models or /home/user/.gazebo_11/models depending on your system
- Type command gedit .bashrc and add the following at the bottom, after adding run the command source .bashrc
- export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:/home/user/.gazebo/models or 
- export GAZEBO_RESOURCE_PATH=/home/user/.gazebo/models
- Run the command ros2launch soccerr football_world.launch to observe the soccer world


## Simulation

## Dummy Code
- ### TURN CODE STARTS HERE ### import rclpy from rclpy.node import Node from std_msgs.msg import Int32 from geometry_msgs.msg import Twist class VelocityPublisher(Node): def __init__(self): super().__init__('turn') self.publisher_=self.create_publisher(Twist, 'cmd_vel', 10) timer_period = 0.5 self.timer= self.create_timer(timer_period, self.timer_callback) def timer_callback(self): msg = Twist() msg.angular.z =1.0 self.publisher_.publish(msg) def main (args=None): rclpy.init(args=args) vel_publish = VelocityPublisher() rclpy.spin(vel_publish) vel_publish.destroy_node() rclpy.shutdown() EE-381 – Robotics if __name__== '__main__': main()


- cp -r /home/user/deepsoccer_gazebo/ /home/user/.gazebo/models
- /usr/share/gazebo-11/models
- sudo cp -r  /home/user/deepsoccer_gazebo/Soccer/models/football /usr/share/gazebo-11/models
- cd neuronbot2_ws/Soccer
- colcon build
- . install/setup.bash
-  sudo cp -a /home/user/deepsoccer_gazebo/models/. /usr/share/gazebo-11/models/
- just change the world file a bit
- then first launch the football world then the neuronbot world and then the ball tracker node
