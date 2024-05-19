# ROS1 Noetic Playground

ON a RPi 5 Rasbian bookworm.

# Python Node Exercise

1. Create a catkin package [link](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)
2. Write a publisher node [link](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)
3. Run the two together [link](http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber)


# Basic Run Workflow

1. Compile the package by running the following command in the root of the **workspace**
```bash
catkin_make
``` 

2. Source the workspace
```bash
source devel/setup.bash
```

3. Start ROS core node
```bash
roscore
```

4. Run the publisher node
```bash
rosrun beginner_tutorials talker.py
```

5. Run the subscriber node
```bash
rosrun beginner_tutorials listener.py 
```

6. Run the api node
```bash
rosrun beginner_tutorials listener.py 
```

7. Ru
```bash