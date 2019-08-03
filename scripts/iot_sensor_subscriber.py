#!/usr/bin/env python
import rospy
from iot_sensor.msg import IoTSensor
import random


def callback(message):
    rospy.loginfo(message)


def subscriber():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('iot_sensor_subscriber', anonymous=True)

    rospy.Subscriber("iot_sensor_topic", IoTSensor, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    subscriber()
