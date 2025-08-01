# DWA Planner for ROS2 Humble

A custom Dynamic Window Approach local planner for TurtleBot3.
Samples velocity commands, predicts & scores trajectories,
and publishes safe /cmd_vel commands while avoiding obstacles.

## Build & Run

```bash
cd ~/dwa_ws
colcon build --packages-select dwa_planner
source install/setup.bash
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 run dwa_planner dwa_planner
```

Visualize `/visual_paths` in RViz (Marker display).
