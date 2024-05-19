#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from fastapi import FastAPI
import threading
import uvicorn

app = FastAPI()


state = None


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
    rospy.init_node('fastapi_node')
    rate = rospy.Rate(10)  # 10 Hz

    # Start FastAPI in a separate thread
    fastapi_thread = threading.Thread(target=run_fastapi_app)
    fastapi_thread.start()

    while not rospy.is_shutdown():
        # Your ROS node logic here
        rate.sleep()

    # Stop FastAPI when the ROS node is shut down
    rospy.signal_shutdown("Node terminated")
    fastapi_thread.join()
    
    rospy.Subscriber('chatter', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass