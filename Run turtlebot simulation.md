# Install turtlebot
- sudo apt-get install ros-melodic-turtlebot*

# Launch gazebo
- roslaunch turtlebot_gazebo turtlebot_world.launch

# Control turtlebot using keyboard
- roslaunch kobuki_keyop keyop.launch

# Build mapping
- roslaunch turtlebot_gazebo gmapping_demo.launch

# RVIZ
- roslaunch turtlebot_rviz_launchers view_navigation.launch

# SAVE FILE MAPPING
- rosrun map_server map_saver -f **_<NAME_FILE>_**

# Autonomous
### Close control and gmapping first
- roslaunch turtlebot_gazebo amcl_demo.launch map_file:=/home/**_<YOUR_USER_NAME>_**/**_<NAME_FILE>_**.yaml
