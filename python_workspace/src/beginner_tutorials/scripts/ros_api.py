#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from fastapi import FastAPI
import threading
import uvicorn
import signal
import sys


app = FastAPI()


state = None


def signal_handler(signal, frame):
    print('Terminating node...')
    rospy.signal_shutdown("Node terminated")
    sys.exit(0)


@app.get("/")
def read_root():
    return state


def run_fastapi_app():
    uvicorn.run(app, host="0.0.0.0", port=8000)


def callback(data):
    global state
    state = data.data
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)


def main():
    rospy.init_node('api_node')
    rate = rospy.Rate(100)  # Hz

    # Register signal handlers
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi_app)
    
    rospy.Subscriber('chatter', String, callback)

    fastapi_thread.start()
    
    # spin() simply keeps python from exiting until this node is stopped
    rospy.loginfo('API is running...')
    rospy.spin()
    fastapi_thread.join()

    while not rospy.is_shutdown():
        # Your ROS node logic here
        rate.sleep()

    # Stop FastAPI when the ROS node is shut down
    rospy.signal_shutdown("Node terminated")


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass