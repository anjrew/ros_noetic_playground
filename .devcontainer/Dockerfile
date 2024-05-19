FROM ros:noetic

# Add vscode user with same UID and GID as your host system
# (copied from https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#\_creating-a-nonroot-user)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME
RUN useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME

RUN apt-get update
RUN apt-get install -y sudo

RUN echo "$USERNAME ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/$USERNAME
RUN chmod 0440 /etc/sudoers.d/$USERNAME

# Set up workspace directory and grant permissions to vscode user
RUN mkdir -p /workspace
RUN chown -R $USERNAME:$USERNAME /workspace

# Switch from root to user
USER $USERNAME

# Add user to video group to allow access to webcam
RUN sudo usermod --append --groups video $USERNAME

# Update all packages
RUN sudo apt update && sudo apt upgrade -y

# Install Git
RUN sudo apt install -y git

# Source the ROS setup file
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> ~/.bashrc

# Update apt package list
RUN sudo apt update

# Install dependencies
RUN sudo apt install -y python3-rosdep

# Initialize rosdep
# RUN sudo rosdep init
RUN rosdep update


RUN echo "source /ldlidar_ros_ws/devel/setup.bash" >> ~/.bashrc