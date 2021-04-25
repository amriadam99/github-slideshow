# Intallation Info
 - Link: http://wiki.ros.org/Installation/Ubuntu
 - Ubuntu Version: 18.04 lte
 - Ros Version: Melodic
#
# Setup your sources.list
- sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

# Set up your keys
- sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
- sudo apt update

# Desktop-Full Install: (Recommended) : ROS, rqt, rviz, robot-generic libraries, 2D/3D simulators and 2D/3D perception
- sudo apt install ros-melodic-desktop-full

# Environment setup
- echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
- source ~/.bashrc
# Dependencies for building packages
- sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

# Initialize rosdep
- sudo apt install python-rosdep
- sudo rosdep init
- rosdep update
