DWA Planner ROS 2

A custom Dynamic Window Approach local planner for TurtleBot3 in Gazebo using ROS 2 Humble.

## Structure

- `src/dwa_planner/`  
  - `dwa_planner.py` — the main node  
- `README.md` (this file)  `

## Setup

```bash
1. Clone
git clone https://github.com/Tushar10987/dwa_planner_ros2.git
cd dwa_planner_ros2

2. Create a ROS2 workspace
mkdir -p ~/dwa_ws/src
ln -s $PWD ~/dwa_ws/src/dwa_planner

3. Build & source
cd ~/dwa_ws
colcon build --packages-select dwa_planner
source install/setup.bash

4. Run in Gazebo
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py

5. Launch your planner
ros2 run dwa_planner dwa_planner

🎯 Choosing Goals
Pick any (X, Y) inside a 1 m radius of the start (0,0) to avoid collisions with the ring of pillars.
Example goals: ( 0.5,  0.5), ( 0.5,  0.0), ( 0.0,  0.5), ( 0.7,  0.7), (-0.5, -0.5)
## The sample goals should satisfy √(x² + y²) > 1.0 m .
