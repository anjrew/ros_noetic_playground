#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import sys
from streamlit import cli as stcli
import streamlit as st
import threading

def run_streamlit_app():
    st.set_option('server.port', 8501)  # Set the desired port number
    st.title("My Streamlit App")
    st.write("Hello from ROS!")
    # Add more Streamlit components 


def main():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('gui', anonymous=True)
    rate = rospy.Rate(100)  # hz
    
    # Start Streamlit in a separate thread
    streamlit_thread = threading.Thread(target=run_streamlit_app)
    streamlit_thread.start()

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        # Run your Streamlit app here
        st.title("My Streamlit App")
        st.write("Hello from ROS!")
        rate.sleep()


if __name__ == '__main__':
    try:
        if st._is_running_with_streamlit:
            main()
        else:
            sys.argv = ["streamlit", "run", sys.argv[0]]
            sys.exit(stcli.main())
    except rospy.ROSInterruptException:
        pass
